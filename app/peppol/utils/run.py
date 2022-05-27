'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import os
from django.conf import settings

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.lists = [
			'ICD', 'EAS', '3166', 
			 '4217', 'Recommendation 20', 'Recommendation 21', 
			 'Duty', 'Item', 'Invoice', 
			 'Credit', 'Invoiced', 'UNCL2005', 
			 'UNCL4461', 'UNCL5189', 'UNCL7161',
			 'IANA', 'SEPA', 'VATEX']
		self.types = { 
			str: 'CharField', 
			int: 'IntegerField',
			bool: 'BooleanField'
		}
		#self.PATH_MODELS = '/tmp/peppol/'
		#if not os.path.exists(self.PATH_MODELS):
		#	os.makedirs('/tmp/peppol/')
		self.PATH_MODELS = settings.PEPPOL_DIR
		self.fields = ['code', 'name', 'description']
		self.file_models = open(self.PATH_MODELS + 'models.py', 'w')

	def test_search_in_peppol(self):
		driver = self.driver
		driver.get('https://docs.peppol.eu/poacc/billing/3.0/codelist/')

		file_models = self.file_models
		file_models.write('from django.db import models\n\n')


		for element in self.lists:
			csv_models_data = open(self.PATH_MODELS + '/csv/' + 'CSV_MODELS_DATA-{}.csv'.format(element.upper()), 'w') #open('/tmp/csv_models_data.csv', 'w')
			file_models = self.file_models
			csv_columns_names = []
			csv_columns_values = []
			identifier = element
			comments = ''

			try:
				driver.find_element_by_partial_link_text(element).click()
				dd_len = len(driver.find_elements_by_xpath('//dl[@class="dl-horizontal"]/dd'))

				try:
					print(f'************ CREATING COMMENTS ************')
					identifier = driver.find_element_by_xpath('//dl[@class="dl-horizontal"]/dd[1]').text
					agency = driver.find_element_by_xpath('//dl[@class="dl-horizontal"]/dd[2]').text
					version = driver.find_element_by_xpath('//dl[@class="dl-horizontal"]/dd[3]').text
					usage = driver.find_element_by_xpath('//dl[@class="dl-horizontal"]/dd[{}]'.format(dd_len - 1)).text.replace('\n', '\n\t\t\t\t\t') if dd_len > 4 else ''

					comments = f''
	Identifier \t\t{identifier}
	Agency \t\t\t{agency}
	Version \t\t{version}
	Usage \t\t\t{usage}
	'
				except Exception as e:
					print(f'************ EXCEPTION CREATING COMMENTS ************')
					print(f'{e}')


				dd = driver.find_element_by_xpath('//dl[@class="dl-horizontal"]/dd[{}]'.format(dd_len))
				list_divs = dd.find_elements_by_xpath('div')

				print(f'************ CREATING MODEL {identifier.upper()} ************')
				file_models.write('class {}(models.Model):\n'.format(identifier.upper().replace('-', '')))
				file_models.write(f"\t'{comments}\n")
				
				i = 0
				for text in list_divs[0].text.split('\n'):
					field_name = self.fields[i]
					field_type = self.types[type(text)]
					field_len = 10 if len(text) <= 10 else (150 if len(text) <= 150 else 255)

					if type(text) == str:
						file_models.write(f'\t{field_name} = models.{field_type}(max_length={field_len}, null=True, blank=True)\n')
					elif type(text) == int:
						file_models.write(f'\t{field_name} = models.{field_type}()\n')
					elif type(text) == bool:
						file_models.write(f'\t{field_name} = models.{field_type}(default=False)\n')
					else:
						file_models.write(f'\t{field_name} = models.{field_type}() ## PENDIENTE\n')
					csv_columns_names.append(field_name)

					i += 1
				
				print(f'************ MODEL {identifier.upper()} CREATED SUCCESSFULLY ************')
				print(f'************ CREATING CSV FOR MODEL {identifier.upper()} ************')

				for values in list_divs:
					temp_row = []
					for text in values.text.split('\n'):
						temp_row.append(text)
					if len(temp_row) > i:
						#i += 1
						field_name = self.fields[i]
						field_type = self.types[type(text)]
						field_len = len(text) if len(text) < 4 else (25 if len(text) <= 25 else 255)

						if type(text) == str:
							file_models.write(f'\t{field_name} = models.{field_type}(max_length={field_len}, null=True, blank=True)\n')
						elif type(text) == int:
							file_models.write(f'\t{field_name} = models.{field_type}()\n')
						elif type(text) == bool:
							file_models.write(f'\t{field_name} = models.{field_type}(default=False)\n')
						else:
							file_models.write(f'\t{field_name} = models.{field_type}() ## PENDIENTE\n')
						csv_columns_names.append(field_name)
						i += 1
					csv_columns_values.append(temp_row)
				
				try:
					with csv_models_data:
						writer = csv.writer(csv_models_data)
						for row in [csv_columns_names]:
							writer.writerow(row)
						for row in csv_columns_values:
							writer.writerow(row)
					print(f'************ CSV {identifier.upper()} CREATED SUCCESSFULLY ************\n\n')
					csv_models_data.close()
				except Exception as e:
					print(f'************ EXCEPTION CREATING CSV ************')
					print(f'{e}')


				file_models.write('\n')


				driver.back()
			except Exception as e:
				print(f'************ EXCEPTION IN MODEL {identifier.upper()} ************')
				print(f'{e}\n\n')


		file_models.close()

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
'''

from django.db import connection, transaction
from django.conf import settings
import csv
import os
import re
import sys
import codecs
import socket
import urllib
import datetime
import simplejson
from dateutil.relativedelta import relativedelta
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

TABLES_NAME = {
	'ICD': 'ICD',
	'EAS': 'EAS',
	'3166': 'ISO3166',
	'4217': 'ISO4217',
	'Recommendation 20': 'UNECEREC20',
	'Recommendation 21': 'UNECEREC21',
	'Duty': 'UNCL5305',
	'Item': 'UNCL7143',
	'Invoice': 'UNCL1001INV',
	'Credit': 'UNCL1001CN',
	'Invoiced': 'UNCL1153',
	'UNCL2005': 'UNCL2005',
	'UNCL4461': 'UNCL4461',
	'UNCL5189': 'UNCL5189',
	'UNCL7161': 'UNCL7161',
	'IANA': 'MIMECODE',
	'SEPA': 'SEPA',
	'VATEX': 'VATEX',
}

TRUNCATE_QUERY = {
	'ICD': 'TRUNCATE ICD RESTART IDENTITY',
	'EAS': 'TRUNCATE EAS RESTART IDENTITY',
	'3166': 'TRUNCATE ISO3166 RESTART IDENTITY',
	'4217': 'TRUNCATE ISO4217 RESTART IDENTITY',
	'Recommendation 20': 'TRUNCATE UNECEREC20 RESTART IDENTITY',
	'Recommendation 21': 'TRUNCATE UNECEREC21 RESTART IDENTITY',
	'Duty': 'TRUNCATE UNCL5305 RESTART IDENTITY',
	'Item': 'TRUNCATE UNCL7143 RESTART IDENTITY',
	'Invoice': 'TRUNCATE UNCL1001INV RESTART IDENTITY',
	'Credit': 'TRUNCATE UNCL1001CN RESTART IDENTITY',
	'Invoiced': 'TRUNCATE UNCL1153 RESTART IDENTITY',
	'UNCL2005': 'TRUNCATE UNCL2005 RESTART IDENTITY',
	'UNCL4461': 'TRUNCATE UNCL4461 RESTART IDENTITY',
	'UNCL5189': 'TRUNCATE UNCL5189 RESTART IDENTITY',
	'UNCL7161': 'TRUNCATE UNCL7161 RESTART IDENTITY',
	'IANA': 'TRUNCATE MIMECODE RESTART IDENTITY',
	'SEPA': 'TRUNCATE SEPA RESTART IDENTITY',
	'VATEX': 'TRUNCATE VATEX RESTART IDENTITY',
}

COLUMNS = {
	'2': (
		'code',
		'name',
	),
	'3': (
		'code',
		'name',
		'description',
	)
}

REINDEX_QUERY = {
	'ICD': 'REINDEX TABLE ICD',
	'EAS': 'REINDEX TABLE EAS',
	'3166': 'REINDEX TABLE ISO3166',
	'4217': 'REINDEX TABLE ISO4217',
	'Recommendation 20': 'REINDEX TABLE UNECEREC20',
	'Recommendation 21': 'REINDEX TABLE UNECEREC21',
	'Duty': 'REINDEX TABLE UNCL5305',
	'Item': 'REINDEX TABLE UNCL7143',
	'Invoice': 'REINDEX TABLE UNCL1001INV',
	'Credit': 'REINDEX TABLE UNCL1001CN',
	'Invoiced': 'REINDEX TABLE UNCL1153',
	'UNCL2005': 'REINDEX TABLE UNCL2005',
	'UNCL4461': 'REINDEX TABLE UNCL4461',
	'UNCL5189': 'REINDEX TABLE UNCL5189',
	'UNCL7161': 'REINDEX TABLE UNCL7161',
	'IANA': 'REINDEX TABLE MIMECODE',
	'SEPA': 'REINDEX TABLE SEPA',
	'VATEX': 'TRUNCATE VATEX',
}

class Peppol():
	def __init__(self):
		self.downloaded_file = []
		self.fields = ['code', 'name', 'description']
		self.types = { 
			str: 'CharField', 
			int: 'IntegerField',
			bool: 'BooleanField'
		}
		#self.driver = webdriver.Chrome()
		self.columns_names = []
		self.columns_values = []
		if not os.path.exists(settings.PEPPOL_DIR + '/csv/'):
			os.makedirs(settings.PEPPOL_DIR + '/csv/')

	def create_model(self, list_name):
		try:
			self.print_to_log('CREATING MODEL {}: SUCCESS'.format(list_name))
			try:
				driver = webdriver.Chrome()
			except Exception as e:
				print('No se encontro el navegador Chrome')
			try:
				driver = webdriver.Firefox()
			except Exception as e:
				print('No se encontro el navegador Firefox')
			try:
				driver = webdriver.Opera()
			except Exception as e:
				print('No se encontro el navegador Opera')
				raise Exception('No se encontro ningun navegador necesario para esta tarea')

			driver.get('https://docs.peppol.eu/poacc/billing/3.0/codelist/')
			driver.find_element_by_partial_link_text(list_name).click()

			iterator = 0
			file_models = open(settings.PEPPOL_DIR + '/models.py', 'a+')
			columns_names = []

			dd_len = len(driver.find_elements_by_xpath('//dl[@class="dl-horizontal"]/dd'))
			dd = driver.find_element_by_xpath('//dl[@class="dl-horizontal"]/dd[{}]'.format(dd_len))

			identifier = driver.find_element_by_xpath('//dl[@class="dl-horizontal"]/dd[1]').text
			agency = driver.find_element_by_xpath('//dl[@class="dl-horizontal"]/dd[2]').text
			version = driver.find_element_by_xpath('//dl[@class="dl-horizontal"]/dd[3]').text
			usage = driver.find_element_by_xpath('//dl[@class="dl-horizontal"]/dd[{}]'.format(dd_len - 1)).text.replace('\n', '\n\t\t\t\t\t') if dd_len > 4 else ''

			comments = f'''\n\tIdentifier \t\t{identifier}\n\tAgency \t\t\t{agency}\n\tVersion \t\t{version}\n\tUsage \t\t\t{usage}\n\t'''

			file_models.write('\n')
			file_models.write('class {}(models.Model):\n'.format(identifier.upper().replace('-', '')))
			file_models.write(f"\t'''{comments}'''\n")

			list_divs = dd.find_elements_by_xpath('div')

			with open(settings.PEPPOL_DIR + '/csv/{}.csv'.format(list_name), newline='') as csvfile:
				reader = csv.reader(csvfile, delimiter=',')
				for row in reader:
					columns_names = row
					break

			for text in columns_names:
				field_name = self.fields[iterator]
				field_type = self.types[type(text)]
				field_len = 80 if iterator < 1 else (200 if iterator < 2 else 1500)

				if type(text) == str:
					file_models.write(f'\t{field_name} = models.{field_type}(max_length={field_len}, null=True, blank=True)\n')
				else:
					file_models.write(f'\t{field_name} = models.{field_type}() ## PENDING\n')

				iterator += 1
			file_models.write('\n')
			file_models.close()
			driver.close()

		except Exception as e:
			self.print_to_log('FAILED CREATING MODEL {} => {}'.format(table_name, e))
			#print(f'Exception in create_model => {e}')

	def create_csv(self, list_name):
		try:
			self.print_to_log('CREATING CSV {}: SUCCESS'.format(list_name))
			try:
				driver = webdriver.Chrome()
			except Exception as e:
				print('No se encontro el navegador Chrome')
			try:
				driver = webdriver.Firefox()
			except Exception as e:
				print('No se encontro el navegador Firefox')
			try:
				driver = webdriver.Opera()
			except Exception as e:
				print('No se encontro el navegador Opera')
				raise Exception('No se encontro ningun navegador necesario para esta tarea')
			driver.get('https://docs.peppol.eu/poacc/billing/3.0/codelist/')
			driver.find_element_by_partial_link_text(list_name).click()

			csv_models = open(settings.PEPPOL_DIR + '/csv/' + '{}.csv'.format(list_name), 'w')
			dd_len = len(driver.find_elements_by_xpath('//dl[@class="dl-horizontal"]/dd'))
			dd = driver.find_element_by_xpath('//dl[@class="dl-horizontal"]/dd[{}]'.format(dd_len))
			list_divs = dd.find_elements_by_xpath('div')
			iterator = 0
			columns_values = []

			for values in list_divs:
				temp_row = []
				for text in values.text.split('\n'):
					temp_row.append(text)
				columns_values.append(temp_row)
			try:
				total_columns = 0
				diference = False
				with csv_models:
					writer = csv.writer(csv_models)
					writer.writerow(['code', 'name'])
					for row in columns_values:
						writer.writerow(row)
						if len(row) != 2:
							diference = True
				csv_models.close()
				
				if diference:
					with open(settings.PEPPOL_DIR + '/csv/{}.csv'.format(list_name)) as inf:
						reader = csv.reader(inf.readlines())

					with open(settings.PEPPOL_DIR + '/csv/{}.csv'.format(list_name), 'w') as outf:
						writer = csv.writer(outf)
						for line in reader:
							writer.writerow(['code', 'name', 'description'])
							break
						writer.writerows(reader)

			except Exception as e:
				print(f'{e}')
			driver.close()
		except Exception as e:
			self.print_to_log('FAILED CSV {} => {}'.format(table_name, e))
			#print(f'Exception in create_csv => {e}')

	def fix_csv(self, table_name):
		try:
			fixed_rows = []
			file_path = settings.PEPPOL_DIR + '/csv/{}.csv'.format(table_name)
			file_path_fixed = file_path.replace('.csv', '_fixed.csv')
			try:
				with codecs.open(file_path, 'rb', encoding='utf-8') as csvfile:
					fix_reader = csv.reader(csvfile)
					for row in fix_reader:
						fixed_rows.append(row) 

				with codecs.open(file_path_fixed, 'wb', encoding='utf-8') as csvfile:
					fixed_writer = csv.writer(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE, escapechar='\\')
					fixed_writer.writerows(fixed_rows)
			except Exception as e:
				print_to_log('FAILED FIX CSV {}: {}'.format(table_name, e))
			return file_path_fixed
		except Exception as e:
			print_to_log('FAILED FIX CSV {} => {}'.format(table_name, e))

	def migrate_model(self, sett):
		try:
			self.print_to_log('MIGRATING MODEL')
			command1 = 'python manage.py makemigrations peppol --settings={}'.format(sett)
			command2 = 'python manage.py migrate peppol --settings={}'.format(sett)
			os.system(command1)
			os.system(command2)
		except Exception as e:
			self.print_to_log('FAILED MIGRATION => {}'.format(e))

	def import_to_database(self, table_name):
		cursor = connection.cursor()
		self.truncate_table(cursor, table_name)
		self.import_csv(cursor, table_name)
		self.reindex_table(cursor, table_name)

	def reindex_table(self, cursor, table_name):
		try:
			cursor.execute(REINDEX_QUERY[table_name])
			self.print_to_log('REINDEXING TABLE {}: SUCCESS'.format(table_name))
		except Exception as e:
			self.print_to_log('REINDEXING TABLE {}: FAILED => {}'.format(table_name, e))

	def truncate_table(self, cursor, table_name):
		try:
			cursor.execute(TRUNCATE_QUERY[table_name])
			self.print_to_log('TRUNCATE TABLE {}: SUCCESS'.format(table_name))
		except Exception as e:
			self.print_to_log('TRUNCATE TABLE {}: FAILED => {}'.format(table_name, e))

	def import_csv(self, cursor, table_name):
		self.print_to_log('IMPORTING CSV {}'.format(table_name))
		try:
			csv_file = settings.PEPPOL_DIR + '/csv/' + '{}.csv'.format(table_name)#), 'r')
			columns_names = []

			with open(csv_file, newline='') as csvfile:
				reader = csv.reader(csvfile, delimiter=',')
				for row in reader:
					columns_names = row
					break

			encoding = 'utf-8'
			with codecs.open(csv_file, 'rb', encoding=encoding) as csv_code_obj:
				cursor.copy_from(csv_code_obj, 'peppol_{}'.format(table_name.split('_')[0]), columns=COLUMNS[str(len(columns_names))])
			self.print_to_log('COPY {}: SUCCESS'.format(csv_file))
		except Exception as e:
			self.print_to_log('COPY {}: FAILED => {}'.format(csv_file, e))
			sys.exit()

	def csv_to_json(self, table_name, sett):
		cursor = connection.cursor()
		self.truncate_table(cursor, table_name)
		self.print_to_log('PARSING CSV TO JSON {}'.format(table_name))
		try:
			header_row = []#'code', 'name', 'description']
			entries = []
			pk = 1
			model = 'peppol.{}'.format(TABLES_NAME[table_name])

			csv_file = open(settings.PEPPOL_DIR + '/csv/{}.csv'.format(table_name), 'r')
			fixtures_path = settings.BASE_DIR + '/fixtures/peppol/'
			if not os.path.exists(fixtures_path):
				os.makedirs(fixtures_path)
			fixture = open(fixtures_path + '{}.json'.format(table_name.replace(' ', '')), 'w')

			reader = csv.reader(csv_file)

			for row in reader:
				fields = {}
				if not header_row:
					header_row = row
					continue
				for i in range(len(row)):
					active_field = row[i]
					fields[header_row[i]] = active_field.strip()
				row_dict = {}
				row_dict['pk'] = pk
				row_dict['model'] = model
				row_dict['fields'] = fields
				entries.append(row_dict)
				pk += 1

			fixture.write('{}'.format(simplejson.dumps(entries, indent=4)))
			fixture.close()
			csv_file.close()
			self.print_to_log('PARSE {}: SUCCESS'.format(table_name))

			self.import_json(table_name, sett)
			self.reindex_table(cursor, table_name)

		except Exception as e:
			self.print_to_log('PARSE {}: FAILED => {}'.format(table_name, e))

	def import_json(self, table_name, sett):
		try:
			self.print_to_log('IMPORTING JSON TO TABLE {}'.format(table_name))
			command = 'python manage.py loaddata fixtures/peppol/{}.json --settings={}'.format(table_name.replace(' ', ''), sett)
			os.system(command)
		except Exception as e:
			self.print_to_log('FAILED IMPORT JSON TABLE {} => {}'.format(table_name, e))

	def print_to_log(self, log):
		try:
			log_file = open('/tmp/log_peppol.txt', 'a+')
			time = datetime.strftime(datetime.now(), '%H:%M:%S')
			log_file.write('[{}] {}\n'.format(time, log))
			log_file.close()
		except IOError:
			print('Error: Cannot open log file')