from django.core.management.base import (
	BaseCommand,
	CommandError
)
from django.conf import settings
from datetime import datetime
from app.peppol.utils.run import Peppol
import re
import os
import sys

class Command(BaseCommand):
	help = "Get Peppol Information to create Models and Fixture"

	LIST_CHOICES = {
		1: 'ICD',
		2: 'EAS',
		3: '3166',
		4: '4217',
		5: 'Recommendation 20',
		6: 'Recommendation 21',
		7: 'Duty',
		8: 'Item',
		9: 'Invoice',
		10: 'Credit',
		11: 'Invoiced',
		12: 'UNCL2005',
		13: 'UNCL4461',
		14: 'UNCL5189',
		15: 'UNCL7161',
		16: 'IANA',
		17: 'SEPA',
		18: 'VATEX',
	}

	def add_arguments(self, parser):
		parser.add_argument(
			'-l',
			'--list',
			dest = 'list',
			type = int,
			default = list(self.LIST_CHOICES),
			help = '(Opcional) Importa una lista de Peppol. Si no es especificada el nombre, se tomaran todas',
		)
		parser.add_argument(
			'-o',
			'--only-import',
			dest = 'onlyimport',
			action = 'store_true',
			help = '(Opcional) Importa solamente la lista, sin descargar (IMPORTANTE: El archivo a importar debe existir)'
		)
		parser.add_argument(
			'-ni',
			'--no-import',
			dest = 'noimport',
			action = 'store_true',
			help = '(Opcional) No importa las listas a la Base de Datos'
		)
		parser.add_argument(
			'-nf',
			'--no-file',
			dest = 'nofile',
			action = 'store_true',
			help = '(Opcional) Crea solo CSV de las listas especificadas sin crear el modelo',
		)
		parser.add_argument(
			'-nm',
			'--no-model',
			dest = 'nomodel',
			action ='store_true',
			help = '(Opcional) Crea solo el modelo de las listas especificadas sin crear CSV (IMPORTANTE: El archivo CSV debe existir)',
		)
		parser.add_argument(
			'-m',
			'--no-migrate',
			dest = 'migrate',
			action = 'store_true',
			help = '(Opcional) Impide la migracion de los modelos descargados'
		)

	def handle(self, *args, **options):
		self.list = options['list']
		self.onlyimport = options['onlyimport']
		self.nofile = options['nofile']
		self.nomodel = options['nomodel']
		self.noimport = options['noimport']
		self.migrate = options['migrate']
		self.sett = options['settings']
		self.peppol = Peppol()

		if type(self.list) is int and self.list not in self.LIST_CHOICES:
			return CommandError('La lista a importar no se encuentra dentro de las opciones. {}'.format(self.LIST_CHOICES.keys().__str__()))
		if type(self.list) is int:
			self.list_name = [self.LIST_CHOICES[self.list]]
		else:
			self.list_name = []
			for i in self.list:
				self.list_name.append(self.LIST_CHOICES[i])
		self.log(init=True, message='Import process started ({})...'.format(self.list_name))

		if self.onlyimport:
			self.log(message='Importing to database')
			#self.import_csv(self.list_name)
			self.import_json()
		else:
			if not self.nofile:
				self.create_csv()
			if not self.nomodel:
				self.create_model()
			if not self.migrate:
				self.migrate_model()
			if not self.noimport:
				self.import_json()
				#fixed_files = self.fix_csv()
				#self.import_csv()

	def create_csv(self):
		for list_name in self.list_name:
			try:
				self.log(message='Creating CSV list {}'.format(list_name))
				self.peppol.create_csv(list_name)
			except Exception as e:
				message = 'Failed create CSV: {} => {}'.format(list_name, e)
				self.log(message=message, exception=True)
	
	def create_model(self):
		for list_name in self.list_name:
			try:
				self.log(message='Creating model list {}'.format(list_name))
				self.peppol.create_model(list_name)
			except Exception as e:
				message = 'Failed create model: {} => {}'.format(list_name, e)
				self.log(message=message, exception=True)

	def fix_csv(self):
		fixed_csv = []
		for list_name in self.list_name:
			try:
				self.log('Fixing CSV FILE {}'.format(list_name))
				fixed_csv.append(self.peppol.fix_csv(list_name))
			except Exception as e:
				message = 'Failed fix csv: {} => {}'.format(list_name, e)
				self.log(message=message, exception=True)
		return fixed_csv

	def import_csv(self):
		for file in self.list_name:
			list_name = file.split('/')[-1].split('.')[0]
			try:
				self.log('Importing {} CSV File to DataBase'.format(list_name))
				self.peppol.import_to_database(list_name)
			except Exception as e:
				message = 'Failed import csv: {} => {}'.format(list_name, e)
				self.log(message=message, exception=True)

	def import_json(self):
		for list_name in self.list_name:
			try:
				self.log('Importing Json to {}'.format(list_name))
				self.peppol.csv_to_json(list_name, self.sett)
			except Exception as e:
				message = 'Failed import json: {} => {}'.format(list_name, e)
				self.log(message=message, exception=True)

	def migrate_model(self):
		try:
			self.log('Migrating Models')
			self.peppol.migrate_model(self.sett)
		except Exception as e:
			message = 'Failed migrations: {} => {}'.format(e)
			self.log(message=message, exception=True)

	def log(self, message='', init=False, exception=False, _exit=False):
		date_log = datetime.now().replace(microsecond=0).isoformat()
		message = '[{}]  {}'.format(date_log, message)
		
		self.peppol.print_to_log(message)

		if init:
			self.stdout.write('=='*50, ending='\n')
			self.stdout.write(message, ending='\n')
		elif exception:
			self.stderr.write(message, ending='\n')
		else:
			self.stdout.write(message, ending='\n')


