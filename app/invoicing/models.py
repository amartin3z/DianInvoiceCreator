# -*- encoding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core import signing
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField, JSONField

from app.invoicing.utils.storage import OverrideFileSystemStorage, invoice_storage, cancel_storage

from app.core.catalogs import INVOICE_STATUS, INVOICE_STATUS_SAT, INVOICE_TYPE, PAYMENT_WAY, PAYMENT_METHOD, REGIMEN_TYPE, OTHERPAYMENT_TYPE, INABILITY_TYPE, RISK_TYPE, WORKING_TYPE, PERIODICITY_TYPE, CONTRACT_TYPE, STATES, USE_CFDI, PAYROLL_TYPE, PERCEPTION_TYPE, DEDUCTION_TYPE, CURRENCIES

from app.core.models import Business
from app.core.catalogs import USE_CFDI
from app.sat.models.cfdi import UsoCFDI
from django.utils.timezone import now

import os
from uuid import uuid4

INVOICE_TYPE = (
  ('I', 'Ingreso'),
  ('E', 'Egreso'),
  ('T', 'Traslado'),
  ('N', 'Nomina'),
  ('P', 'Pago'),
)

class CFDI(models.Model):
  version =  models.CharField(max_length=5, default='3.3')
  taxpayer_id = models.CharField(max_length=25, null=True)
  name = models.CharField(max_length=250, null=True)
  certificate_number = models.CharField(max_length=30, null=True)  
  uuid = models.CharField(max_length=40, null=True)
  serial = models.CharField(max_length=30, null=True)
  folio = models.CharField(max_length=50, null=True)
  emission_date = models.DateTimeField(null=True)
  stamping_date = models.DateTimeField(null=True)
  subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
  tax = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
  discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
  total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
  status = models.CharField(choices=INVOICE_STATUS, default='E', max_length=1)
  status_sat = models.CharField(max_length=1, choices=INVOICE_STATUS_SAT, default='V')
  payment_way = models.CharField(choices=PAYMENT_WAY, default='01', max_length=2, null=True)
  payment_method = models.CharField(choices=PAYMENT_METHOD, default='PUE', max_length=3, null=True)
  type = models.CharField(choices=INVOICE_TYPE, default='I', max_length=1)
  cancellation_date = models.DateTimeField(null=True, blank=True)
  cfdi_use = models.CharField(max_length=255,  choices=USE_CFDI, default='P01')
  pac_taxpayer_id = models.CharField(max_length=14)
  branch = models.ForeignKey('core.Branch', null=True, related_name='+', on_delete=models.CASCADE)

  class Meta:
    abstract = True

  def __str__(self):
    return self.uuid

  def __unicode__(self):
    return unicode(self.uuid)

  def get_payment_way(self):
    payment_way = 'No Aplica'
    try:
      payment_way = dict(PAYMENT_WAY)[self.payment_way]
    except:
      pass
    return payment_way

  def get_payment_method(self):
    payment_method = 'No Aplica'
    try:
      payment_method = dict(PAYMENT_METHOD)[self.payment_method]
    except:
      pass
    return payment_method

# use_cfdi = UsoCFDI.objects.all()
# dict_use_cfdi = dict()
# for u_cfdi in use_cfdi:
#   dict_use_cfdi[u_cfdi.clave] = u_cfdi.descripcion

# USE_CFDI_TUPLE = tuple(dict_use_cfdi.items())

class ProdServ(models.Model):
  business = models.ForeignKey(Business, null=True, blank=True, verbose_name='Negocio', on_delete=models.CASCADE)
  name = models.CharField('Name', max_length=100, null=False)
  description = models.TextField()
  origin_country = models.CharField('Origin Country', max_length=5, blank=False, null=False)
  unit_code = models.CharField('Unit Code', max_length=3, null=False, blank=False)
  list_id = models.CharField('List ID', max_length=3, null=False, blank=False)
  unit_price = models.FloatField()
  item_classification_code = models.CharField('Item Classification Code', max_length=10, null=False, blank=False)
  tax_category_code = models.CharField('Tax Category Code', max_length=3, default='', blank=True, null=True) #Opcional
  tax_percent = models.FloatField(blank=True, null=True) #Opcional
  tax_scheme = models.CharField('Tax Scheme', max_length=5, default='VAT', blank=True, null=True)
  standard_item_identifier = models.CharField(max_length=15, default='', blank=True, null=True)
  standard_item_scheme = models.CharField(max_length=5, default='', blank=True, null=True)
  creation_date = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = (
      ('business', 'item_classification_code'),
    )
    verbose_name = 'Producto o Servicio'
    verbose_name_plural = 'Productos y Servicios'
  
  def __str__(self):
    return u'{} - {}'.format(self.unit_code, self.name)
  
  @property
  def encrypt(self):
    return signing.dumps({'id': self.id}, compress=True)
  
  @staticmethod
  def decrypt_id(value):
    return int(signing.loads(value)['id'])

class Invoice(CFDI):
  #business = models.ForeignKey(Business, verbose_name="Negocio", null=True)
  uuid = models.CharField(max_length=40, null=True)
  rtaxpayer_id = models.CharField(max_length=25)
  rname = models.CharField(max_length=255, null=True)
  uuid_rel = models.CharField(max_length=36, null=True)
  expedition_place = models.CharField(max_length=250)
  total_tra = models.DecimalField(max_digits=18, decimal_places=6, default=0.0)
  total_ret = models.DecimalField(max_digits=18, decimal_places=6, default=0.0)
  seal = models.TextField()
  _xml = models.FileField(storage=OverrideFileSystemStorage(), upload_to=invoice_storage, null=True, db_column='xml')
  internal_notes = models.TextField(null=True)
  error_messages = JSONField(null=True, verbose_name='Mensajes de error')
  snapshot = JSONField(null=True)
  task_id = models.CharField(max_length=40, null=True)
  #stamp_task = models.CharField(max_length=40, null=True)

  class Meta:
    verbose_name = 'Factura'
    verbose_name_plural = u'Facturas (Modulo facturación manual)'
    indexes = [
      #models.Index(fields=['uuid']),
      models.Index(fields=['rtaxpayer_id']),
    ]
    unique_together = (
      ('seal'),
      ('uuid')
    )

  @property
  def xml(self):
    xml_string = self._xml.read()
    try:
      xml_string = xml_string.encode('utf-8')
    except:
      pass
    finally:
      self._xml.seek(0)
    return xml_string
  
  @xml.setter
  def xml(self, value):
    if self._xml.name is not None:
      os.remove(self._xml.path)
    name = self.uuid
    if not name:
      name = uuid4().__str__().upper()
    content_file = ContentFile(value, name='%s.xml' % name)
    self._xml.save(content_file.name, content_file, save = False)

  @property
  def encrypt(self):
    return signing.dumps({'id': self.id}, compress=True)

  @staticmethod
  def decrypt_id(value):
    return int(signing.loads(value)['id'])
  
  def __str__(self):
    return '{}.- {} - {}'.format(self.id, self.uuid, self.taxpayer_id)
  
  def get_sat_query(self, as_dict=False):
    sat_query = None
    try:
      if self.uuid:
        if as_dict:
          sat_query = {'re': self.taxpayer_id, 'rr': self.rtaxpayer_id, 'tt': self.total, 'id': self.uuid}
        else:
          sat_query = '?re={taxpayer_id}&rr={rtaxpayer_id}&tt={total}&id={uuid}'.format(**self.__dict__)
    except Exception as e:
      print(f'Exception on get_sat_query {e}')
    return sat_query

  
taxpayer_validator = RegexValidator(
  r'[A-Z&Ñ]{3,4}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A]', 
  #u'El RFC debe corresponder al patrón. ([A-Z&Ñ]{3,4}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A])'
  u'El RFC no cumple con el patrón requerido. Estructura inválida.'
)

class ReceiverManager(models.Manager):

  def get_encrypted(self, encrypted_id):
    receiver = None
    try:
      receiver_id = int(signing.loads(encrypted_id)['id'])
      receiver = self.get(id=receiver_id)
    except Exception as e:
      print('Exception on get_encrypted manager => {e}')
    return receiver

class Receiver(models.Model):
  business = models.ForeignKey(Business, null=True, blank=True, verbose_name='Negocio', on_delete=models.CASCADE)
  name = models.CharField(u'Razón Social/Nombre', max_length=125, null=True, blank=True)
  use_cfdi = models.CharField('Uso CFDI', max_length=3, choices=USE_CFDI, default='601')
  taxpayer_id = models.CharField('R.F.C.', max_length=20, validators=[taxpayer_validator])
  status = models.BooleanField('Estatus', default=True)
  emails = ArrayField(models.EmailField(null=True), null=True, verbose_name='Correos')
  modified = models.DateTimeField(null=True, auto_now=True)

  objects = ReceiverManager()

  class Meta:
    verbose_name = 'Receptor'
    verbose_name_plural = u'Receptores (Modulo facturación manual)'
    unique_together = (
      ('business', 'taxpayer_id'),
    )

  def __str__(self):
    return u'{} - {}'.format(self.taxpayer_id, self.name)

  @property
  def encrypt(self):
    return signing.dumps({'id': self.id}, compress=True)

class Buyer(models.Model):
  business = models.ForeignKey(Business, null=True, blank=True, verbose_name='Negocio', on_delete=models.CASCADE)
  tax_idenfier_number = models.CharField(u'Tax Identifier Number', max_length=125, null=True, blank=True)
  company_name = models.CharField(u'Company Name', max_length=125, null=True, blank=True)
  organization_id = models.CharField(u'Organization ID', max_length=125, null=True, blank=True) # choices='DUNS,GLN,REID,IBAN'
  address_name = models.CharField(u'Address name', max_length=125, null=True, blank=True)
  city_name = models.CharField(u'City', max_length=125, null=True, blank=True)
  postal_zone = models.CharField(u'Postal Zone', max_length=125, null=True, blank=True)
  country = models.CharField(u'Country', max_length=125, null=True, blank=True)
  province = models.CharField(u'Province', max_length=125, null=True, blank=True)
  language = models.CharField(u'Language', max_length=125, null=True, blank=True)
  currency = models.CharField(u'Currency', max_length=125, null=True, blank=True)
  full_name = models.CharField(u'Full name', max_length=125, null=True, blank=True)
  department = models.CharField(u'Department', max_length=125, null=True, blank=True)
  web = models.CharField(u'Web', max_length=125, null=True, blank=True)
  email_contact = models.CharField(u'Email', max_length=125, null=True, blank=True)
  telephone_contact = models.CharField(u'Phone', max_length=125, null=True, blank=True)
  category = models.CharField(u'Category', max_length=125, null=True, blank=True)
  method_category = models.CharField(u'Method', max_length=125, null=True, blank=True)
  payment_method = models.CharField(u'Payment method', max_length=125, null=True, blank=True)
  term = models.CharField(u'Term', max_length=125, null=True, blank=True)

  modified = models.DateTimeField(null=True, auto_now=True)

  objects = ReceiverManager()

  class Meta:
    verbose_name = 'Buyer'
    verbose_name_plural = u'Compradores (Modulo facturación manual)'
    #unique_together = (
    #  ('business', 'taxpayer_id'),
    #)

  def __str__(self):
    return u'{} - {}'.format(self.tax_idenfier_number, self.company_name)

  @property
  def encrypt(self):
    return signing.dumps({'id': self.id}, compress=True)

# class InvoicingSerial(models.Model):
#   business = models.ForeignKey(Business, verbose_name="Negocio", on_delete=models.CASCADE, blank=True, null=True)
#   serie = models.CharField("Serie", max_length=80, default="A")
#   sequence = models.ForeignKey("sequences.Sequence", verbose_name="Serie y Folio", on_delete=models.CASCADE, blank=True, null=True)
#   #Sequence must be many to many????
#   is_active = models.BooleanField("Serie activa", default=True)

#   class Meta:
#     verbose_name = 'Serie y Folio'
#     verbose_name_plural = u'Serie y Folios (Modulo facturación manual)'

#   def __str__(self):
#     return f'{self.business.taxpayer_id} - {self.sequence.name} {self.sequence.last}'

#   def save(self):
#     from sequences.models import Sequence
#     sequence_exists  = hasattr(self, 'sequence')
#     if not sequence_exists:
#       sequence = Sequence.objects.create(
#         last = 0,
#         name = self.business.taxpayer_id
#       )
#       self.sequence = sequence
#     super(InvoicingSerial, self).save()

class InvoicingSerial(models.Model):
  business = models.ForeignKey(Business, verbose_name="Negocio", on_delete=models.CASCADE, blank=True, null=True)
  serie = models.CharField("Serie", max_length=80, default="F")
  sequence = models.ForeignKey("sequences.Sequence", verbose_name="Serie y Folio", on_delete=models.CASCADE, blank=True, null=True)
  status = models.BooleanField('Estatus', default=True)
  #Sequence must be many to many????
  is_active = models.BooleanField("Serie activa", default=True)

  class Meta:
    verbose_name = 'Serie y Folio'
    verbose_name_plural = u'Serie y Folios (Modulo facturación manual)'

  def __str__(self):
    return f'{self.business.taxpayer_id} - {self.sequence.name} {self.sequence.last}'

  def save(self):
    from sequences.models import Sequence
    sequence_exists  = hasattr(self, 'sequence')
    if not sequence_exists:
      sequence = Sequence.objects.create(
        last = 0,
        name = f"{self.business.taxpayer_id}-{self.serie}"
      )
      self.sequence = sequence
    super(InvoicingSerial, self).save()
