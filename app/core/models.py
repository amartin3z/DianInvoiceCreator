# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core import signing
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from .storage import satfile_storage, logo_storage, pdf_storage, xml_storage
from django.conf import settings
from django.contrib.postgres.fields import JSONField, ArrayField
from django.contrib.auth.models import User
from app.core.utils import get_client_ip
from django.utils import timezone
import os
import re
from datetime import datetime

SATFILE_STATUS = (
  ('A', 'Active'),
  ('S', 'Suspended'),
  ('C', 'Cancelled'),
  ('R', 'Revoked'),
)

FISCAL_REGIME = (
  ('601',	u'General de Ley Personas Morales'),
  ('603',	u'Personas Morales con Fines no Lucrativos'),
  ('605',	u'Sueldos y Salarios e Ingresos Asimilados a Salarios'),
  ('606',	u'Arrendamiento'),
  ('608',	u'Demás ingresos'),
  ('609',	u'Consolidación'),
  ('610',	u'Residentes en el Extranjero sin Establecimiento Permanente en México'),
  ('611',	u'Ingresos por Dividendos (socios y accionistas)'),
  ('612',	u'Personas Físicas con Actividades Empresariales y Profesionales'),
  ('614',	u'Ingresos por intereses'),
  ('616',	u'Sin obligaciones fiscales'),
  ('620',	u'Sociedades Cooperativas de Producción que optan por diferir sus ingresos'),
  ('621',	u'Incorporación Fiscal'),
  ('622',	u'Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras'),
  ('623',	u'Opcional para Grupos de Sociedades'),
  ('624',	u'Coordinados'),
  ('628',	u'Hidrocarburos'),
  ('607',	u'Régimen de Enajenación o Adquisición de Bienes'),
  ('629',	u'De los Regímenes Fiscales Preferentes y de las Empresas Multinacionales'),
  ('630',	u'Enajenación de acciones en bolsa de valores'),
  ('615',	u'Régimen de los ingresos por obtención de premios'),
)

BUSINESS_STATUS =(
  ('A', 'Activated'),
  ('D', 'Deleted'),
  ('S', 'Suspended'),
  ('P', 'PendingOfFillWizard'),
)

COUNTRY = (
  ('MEX', u'México'),
  ('USA', 'Estados Unidos'),
  ('MA', 'Morocco')
)

CSD_TYPE = (
  ('F', 'Fiel'),
  ('C', 'CSD'),
)


class OverrideFileSystemStorage(FileSystemStorage):

  def __init__(self, location=settings.STORAGE_PATH, *args, **kwargs):
    self._location = location
    super(OverrideFileSystemStorage, self).__init__(location, *args, **kwargs)

  def get_available_name(self, name, max_length=None):
    if self.exists(name) and not settings.DEBUG:
      os.remove(os.path.join(self._location, name))
    else:
      name = super(OverrideFileSystemStorage, self).get_available_name(name, max_length)
    return name


class Business(models.Model):
  taxpayer_id = models.CharField('R.F.C.', max_length=14, null=True, unique=True)
  fiscal_regime = models.CharField(u'Régimen Fiscal',max_length=3, choices=FISCAL_REGIME, default='601', blank=True)
  name = models.CharField(u'Razón Social', max_length=256, null=True, blank=True)
  address = models.ForeignKey('Address', verbose_name=u'Dirección', null=True, blank=True, on_delete=models.CASCADE)
  logo = models.FileField('Logo', storage=OverrideFileSystemStorage(location=settings.LOGOS_PATH.__str__()), upload_to=logo_storage, null=True, max_length=200, blank=True)
  # email = models.EmailField(u'Correo electrónico', max_length=254, null=True, blank=True)
  email = ArrayField(models.EmailField(max_length=254, null=True), null=True, default=list)
  status = models.CharField('Estatus',max_length=1, choices=BUSINESS_STATUS, default='P')
  has_fiel = models.BooleanField(default=False)
  default = models.BooleanField(default=False)
  users = models.ManyToManyField(User, blank=True)
  is_staff = models.BooleanField(default=False)
  fk_access = JSONField(null=True, blank=True)
  contract = models.BooleanField(default=False)
  privacy = models.BooleanField(default=False)
  schemeid = models.CharField(max_length=4, null=True, blank=True)
  organization_id = models.CharField(max_length=100, null=True, blank=True)
  # legal_organization_id = models.CharField(max_length=100, null=True, blank=True, default='') # Este valor pertenece al numero de identificacion fiscal
  seller_elect_address = models.CharField(max_length=100, null=True, blank=True)

  def get_email(self):
    str_email = ", ".join(self.email).rstrip(',')
    if str_email and str_email != "":
      email = str_email.split(',')[0] 
    else:
      email = str_email  
    return email
  
  def __unicode__(self):
    return '{} - {}'.format(self.taxpayer_id, self.name)

  def __str__(self):
    return '{} - {}'.format(self.taxpayer_id, self.name)
  
  @property
  def encrypt(self):
    return signing.dumps({'id': self.id})
  
  def decrypt_id(self, value):
    return signing.loads(value)

  def get_csd(self, serial=None):
    #import pdb; pdb.set_trace()
    satfile = None
    result = {'cer': None, 'key': None, 'serial': serial}
    try:
      satfile = self.satfile_set.filter(status='A', certificate_type='C')
      if satfile.exists():
        if serial is not None:
          satfile = satfile.filter(serial=serial)
        elif satfile.filter(default=True).exists():
          satfile = satfile.filter(default=True)

        satfile = satfile.first()
        result['cer'] = satfile.cer
        result['key'] = satfile.key
        result['serial'] = satfile.serial
        result['satfile'] = satfile
    except Exception as e:
      print(f"get_csd Exception => {e}")

    return result

  def is_completed(self):
    success = False
    if self.taxpayer_id and self.status != 'P' and self.contract and self.privacy:
      success = True
    return success

  def get_logo(self):
    logo_path = ''
    try:
      if hasattr(self, 'logo') and self.logo:
        logo_path = self.logo.url
    except Exception as e:
      print(f'Exception on get_logo {e}')
    return logo_path
  
  def save2(self, *args, **kwargs):
    self.is_staff = False
    if self.taxpayer_id and self.taxpayer_id in settings.BUSINESS:
      self.is_staff = True
      self.user = None
    super(Business, self).save(*args, **kwargs)
    
  def profile_logo(self):
    logo = '/static/img/logos/default_avatar_male.jpg'
    if bool(self.logo):
        logo = '/media/logo/' + self.logo.name
      # logo = self.logo.url
    return logo


class SatFile(models.Model):
  business = models.ForeignKey('Business', on_delete=models.CASCADE)
  serial = models.CharField(max_length=60, db_index=True)
  _cer = models.FileField(storage=OverrideFileSystemStorage(), db_column='cer', upload_to=satfile_storage, null=False, max_length=200)
  _key = models.FileField(storage=OverrideFileSystemStorage(), db_column='key', upload_to=satfile_storage, null=False, max_length=200)
  passphrase = models.CharField(max_length=256, null=True)
  certificate_type = models.CharField(max_length=1, choices=CSD_TYPE, default='C')
  status = models.CharField(max_length=1, choices=SATFILE_STATUS, default='A')
  expedition_date = models.DateTimeField(null=True)
  expiration_date = models.DateTimeField(null=True)
  default = models.BooleanField(default=False)

  class Meta:
    unique_together = ('business', 'serial')

  @property
  def cer(self):
    self._cer.open()
    cer = self._cer.read()
    self._cer.close()
    return cer

  @cer.setter
  def cer(self, value):
    name = '{}.cer.pem'.format(self.serial)
    content_file = ContentFile(value, name=name)
    self._cer.save(content_file.name, content_file, save=True)

  @property
  def key(self):
    self._key.open()
    key = self._key.read()
    self._key.close()
    return key

  @key.setter
  def key(self, value):
    name = '{}.key.pem'.format(self.serial)
    content_file = ContentFile(value, name=name)
    self._key.save(content_file.name, content_file, save=True)

  def get_cer_b64(self):
    cer_str = None
    cer_exp = re.compile(b'-----BEGIN CERTIFICATE-----\n(.*)\n-----END CERTIFICATE-----', re.S)
    try:
      cer_str = cer_exp.findall(self.cer)[0]
      cer_str = "".join(cer_exp.findall(self.cer)[0].decode().split())
    except:
      pass
    return cer_str


'''class Address(models.Model):
  country = models.CharField(max_length=3, choices=COUNTRY, default='MEX')
  zipcode = models.CharField(max_length=10, default='58000')
  state = models.CharField(max_length=128, blank=True, null=True)
  municipality = models.CharField(max_length=128, blank=True, null=True)
  locality = models.CharField(max_length=128, blank=True, null=True)
  neighborhood = models.CharField(max_length=128, blank=True, null=True)
  street = models.CharField(max_length=128, blank=True, null=True)
  external_number = models.CharField(max_length=10, blank=True, null=True)
  internal_number = models.CharField(max_length=10, blank=True, null=True)
  phone = models.CharField(max_length=15, blank=True, null=True)
  street_aditional = models.CharField(max_length=128, blank=True, null=True)
  address_line = models.TextField(blank=True, null=True)


  def user_address(self):
    context = {
      "country": self.country if self.country else 'MEX', 
      "zipcode": self.zipcode if self.zipcode and self.zipcode != 'None' else '', 
      "state": self.state if self.state and self.state != 'None' else '', 
      "municipality": self.municipality if self.municipality else '', 
      "locality": self.locality if self.locality and self.locality != 'None' else '', 
      "neighborhood": self.neighborhood if self.neighborhood and self.neighborhood != 'None' else '', 
      "street": self.street if self.street and self.street != 'None' else '', 
      "external_number": self.external_number if self.external_number and self.external_number != 'None' else '', 
      "internal_number": self.internal_number if self.internal_number and self.internal_number != 'None' else '', 
      "phone": self.phone if self.phone and self.phone != '--' else '', 
      "street_aditional": self.street_aditional if self.street_aditional else '', 
      "address_line": self.address_line if self.address_line else '', 
    }
    return context

  def __unicode__(self):
    return (
      u'%s %s %s, %s, %s, %s, %s, %s' %
      (self.street, self.external_number, self.internal_number,
      self.neighborhood, self.zipcode, self.municipality, self.state,
      self.country)
    )

  def get_single_address(self):
    return (
      u'%s #%s %s, Col. %s' %
        (self.street, self.external_number, self.internal_number,
        self.neighborhood)
      )
'''
class Address(models.Model):
  country = models.CharField(max_length=3, choices=COUNTRY, default='MEX')
  state = models.CharField(max_length=128, blank=True, null=True)
  city = models.CharField(max_length=128, blank=True, null=True)
  zipcode = models.CharField(max_length=10, default='58000')
  external_number = models.CharField(max_length=10, blank=True, null=True)
  internal_number = models.CharField(max_length=10, blank=True, null=True)
  phone = models.CharField(max_length=15, blank=True, null=True)
  street = models.CharField(max_length=128, blank=True, null=True)

  def user_address(self):
    return {
      "country": self.country if self.country else 'MEX', 
      "zipcode": self.zipcode if self.zipcode and self.zipcode != 'None' else '', 
      "state": self.state if self.state and self.state != 'None' else '', 
      "city": self.city if self.city and self.city != 'None' else '', 
      "street": self.street if self.street and self.street != 'None' else '', 
      "external_number": self.external_number if self.external_number and self.external_number != 'None' else '', 
      "internal_number": self.internal_number if self.internal_number and self.internal_number != 'None' else '', 
      "phone": self.phone if self.phone and self.phone != '--' else '', 
    }
  
  
  def get_addressline(self):
      return '{} {} {}'.format(self.street if self.street else '', self.external_number if self.external_number else '')     


LOG_LEVEL = (
    (0, 'Action must be taken immediately'),
    (1, 'Critical conditions'),
    (2, 'Error conditions'),
    (3, 'Warning conditions'),
    (4, 'Normal but significant conditions'),
    (5, 'Informational'),
    (6, 'Debug-level messages'),
)
LOG_ACTIONS = (
    ('C', 'Create'),
    ('R', 'Read'),
    ('U', 'Update'),
    ('D', 'Delete'),
)
LOG_MODULES = (
    ('C', 'Clients'),
    ('I', 'Invoicing'),
    ('U', 'Users'),
    ('A', 'Cancelation'),
    ('L', 'Logs'),
    ('S', 'Support'),
    ('T', 'SAT'),
    ('M', 'Admin'),
    ('B', 'Billing'),
    ('O', 'Others'),
)

#from django.utils.functional import SimpleLazyObject

class LogManager(models.Manager):

  def log_action(self, request, level, action, data, module, err_exception, user=None):

    new_data = {}
    if request is not None:
      if hasattr(request.user, 'id') and request.user.id is not None:
        user = request.user
      
      if not isinstance(data, dict):      
        new_data['message'] = data
      else:
        new_data = data

      if 'ip' not in new_data:
        new_data['ip'] = get_client_ip(request)
      if 'username' not in new_data:
        new_data['username'] = request.user.username
      if 'app' not in new_data:
        new_data['app'] = request.resolver_match.app_name
      if 'view' not in new_data:
        new_data['view'] = request.resolver_match.url_name
      if 'path' not in new_data:
        new_data['path'] = request.get_full_path()

    try:
      self.create(user=user, level=level, action=action, data=new_data, module=module, err_exception=err_exception).save()
    except:
      pass

    
class Log(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  level = models.SmallIntegerField(choices=LOG_LEVEL)
  action = models.CharField(max_length=1, choices=LOG_ACTIONS)
  data = JSONField(null=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  module = models.CharField(max_length=2, choices=LOG_MODULES)
  err_exception = models.TextField(null=True)

  objects = LogManager()

  class Meta:
    ordering = ('-timestamp',)

  def unicode(self):
    return u'{} - {} - {}'.format(self.user, self.action, self.module)

class BadInvoice(models.Model):
  uuid = models.CharField(max_length=50)
  error = JSONField(null=True)
  
  class Meta:
    indexes = [
      models.Index(fields=['uuid'], name='uuid_idx'),
    ]

class Branch(models.Model):
  business = models.ForeignKey(Business, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  zipcode = models.CharField(max_length=5)
  street = models.CharField(max_length=255, null=True, blank=True)
  number = models.CharField(max_length=45, null=True, blank=True)
  neighborhood = models.CharField(max_length=45, null=True, blank=True)
  locality = models.CharField(max_length=45, null=True, blank=True)
  municipality = models.CharField(max_length=45, null=True, blank=True)
  state = models.CharField(max_length=45, null=True, blank=True)
  latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
  longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)


class PasswordHistory(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  last_rotation_date = models.DateTimeField(null=True)
  old = models.CharField(('password'), max_length=128, null=True)
  older = models.CharField(('password'), max_length=128, null=True)
  oldest = models.CharField(('password'), max_length=128, null=True)

  def rotate(self, new_encode_password):
    self.oldest = self.older
    self.older = self.old
    self.old = new_encode_password
    self.last_rotation_date = timezone.now()
    self.save()

class SatFaq(models.Model):
  question = models.CharField("Pregunta", max_length=500)
  anwser = models.TextField("Respuesta")
  can_show = models.BooleanField("Mostrar ")
  added = models.DateField("Fecha adición ", auto_now_add=True)

  def __str__(self):
    return f"{self.id} - {self.question}"


class Manifest(models.Model):
  business = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)
  signed = models.BooleanField(default=False)
  signed_contract_xml = models.FileField(storage=OverrideFileSystemStorage(location=settings.MANIFEST_STORAGE.__str__()), upload_to=xml_storage, null=False, blank=False, default=None)
  signed_contract_pdf = models.FileField(storage=OverrideFileSystemStorage(location=settings.MANIFEST_STORAGE.__str__()), upload_to=pdf_storage, null=False, blank=False, default=None)
  date_signed = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return f'{self.business} - {self.signed} - {self.date_signed}'
  
