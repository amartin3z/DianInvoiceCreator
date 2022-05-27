
from django.utils.translation import ugettext as _

from app.core.models import SatFile
from app.sat.models.lco import LCO

from datetime import timedelta, datetime
from M2Crypto import X509
from M2Crypto import EVP

import tempfile
import os
import re

def email_validator(email):
  resquest, message = False, None
  try:
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email.lower()):
      message = ''
      resquest = True
    else:
      message = 'Formato de correo electrónico incorrecto.'
  except Exception as e:
    print ('Exception in email_validator ==> {}'.format(str(e)))
    message = 'Error en la validacion datos datos corrompidos'

  return resquest, message

def imgext_val(img):
  try:
    success = False
    ext = ['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG']
    valid_ext = img.split('.').pop()
    if valid_ext in ext:
      success = True
  except Exception as e:
     print ('Exception in imgext_val => {}'.format(str(e)))

  return success

def validate_csd(file_key, file_cer, pass_csd, user):
  success, message, obj_csd, is_active, default = True, '', {}, False, True
  try:
    tmp_private_key = tempfile.NamedTemporaryFile(delete=False)
    tmp_private_key.write(file_key.read())
    tmp_private_key.close()
    tmp_pem_key = tempfile.NamedTemporaryFile(delete=False)
    tmp_pem_key.close()
    command_key = 'openssl pkcs8 -inform DER -in %s -out %s -passin pass:\'%s\'' % (tmp_private_key.name, tmp_pem_key.name, pass_csd)
    is_valid_key = os.system(command_key)
    
    if is_valid_key != 0:
      return False, u'La contraseñá de la llave no es válida', obj_csd
    tmp_public_cer = tempfile.NamedTemporaryFile(delete=False)
    tmp_public_cer.write(file_cer.read())
    tmp_public_cer.close()
    tmp_pem_cer = tempfile.NamedTemporaryFile(delete=False)
    tmp_pem_cer.close()
    command_cer = 'openssl x509 -inform DER -in %s -pubkey -out %s' % (tmp_public_cer.name, tmp_pem_cer.name)
    is_valid_cer = os.system(command_cer)

    if is_valid_cer != 0:
      return False, u'Certificado dañado', obj_csd

    cert = X509.load_cert(tmp_pem_cer.name)
    evp = EVP.load_key(tmp_pem_key.name)
    serial2 = hex(cert.get_serial_number())
    # serial = hex(cert.get_serial_number())[3::2]
    serial = hex(cert.get_serial_number())[3::2]
    expiration_date = cert.get_not_after().get_datetime().replace(tzinfo=None)
    expedition_date = cert.get_not_before().get_datetime().replace(tzinfo=None)
    subject = cert.get_subject().as_text().replace('\\xD1', '\xD1')
    rfc_user = user.taxpayer_id
    # print(rfc_user)
    # print(subject)
    # print(serial)
    #No borrar solo se comento para pruebas
    if rfc_user not in subject:
      return False, u'El certificado no corresponde con el RFC', obj_csd

    #LCO 
    csd_lco = LCO.objects.filter(serial=serial, rfc=rfc_user)
    #if not csd_lco.exists():
    #  return False, u'El certificado no se encuentra registrado en la LCO', obj_csd
    #elif csd_lco.filter(estatus = 'C').exists():
    #  return False, u'El certificado se encuentra cancelado', obj_csd
    #elif csd_lco.filter(estatus = 'R').exists():
    #  return False, u'El certificado se encuentra revocado', obj_csd

    certificate_type = 'C' if "OU" in subject else 'F'
    
    # if not certificate_type == 'C':
    #   return False, u'No es posible cargar FIEL', obj_csd

    cer_modulus = cert.get_pubkey().get_modulus()
    key_modulus = evp.get_modulus()

    if cer_modulus != key_modulus:
      return False, u'El certificado y la llave no corresponden.', obj_csd

    query_csd = SatFile.objects.filter(business_id = user.id)
    
    if query_csd.filter(serial=serial).exists():
     return False, u'Certificado registrado anteriormente.', obj_csd

    if query_csd.filter(default=True).exists():
      default = False

    date_now = datetime.now()
    
    is_active = 'R'

    if date_now < expiration_date:
      is_active = 'A'
      
    obj_csd = {
      'cer_num': serial,
      'start_date': expedition_date,
      'end_date': expiration_date,
      'is_active': is_active,
      'default': default,
      'type_cert': certificate_type,
      'temp_cer': tmp_pem_cer.name,
      'tem_key':tmp_pem_key.name
    }

  except Exception as e:
    print('Exception in validate_csd ==> {}').format(str(e))

  return success, message, obj_csd

def validate_pass(password, password2):
  try:
    message, success = u'La contraseñas estan vacias ó no son iguales.', False
    print ('PASSWORD {} PASSWORD2 {}'.format(password, password2))
    if (password and password2) and (password2 == password):
      message, rex = u'La  contraseña no debe tener espacio.', re.compile('\s')
      if not rex.search(password):#espacios
        message, rex = 'La contraseña no es segura: debe contar con los parametros requeridos.', re.compile('[.$@#!%*?&_/()^{}¿="]')
        if rex.search(password):
          mayus, minus, num = False, False, False
          if len(password) > 8:
            for x in password:
              if x.isupper():#mayusculas
                mayus = True
              if x.islower():# minusculas
                minus = True
              if x.isdigit():# Numeros
                num = True
          if mayus and minus and num: 
            message, success = '', True
  except Exception as e:
    print ('Exception in validate_pass => {}'.format(str(e)))
  return success, message 

def validate_pass_one(password):
  try:
    message, rex, success = u'La  contraseña no debe tener espacio.', re.compile('\s'), False
    print ('PASSWORD ONE {}'.format(password))
    if not rex.search(password):#espacios
      message, rex = 'La contraseña no es segura: debe contar con los parametros requeridos.', re.compile('[.$@#!%*?&_/()^{}¿="]')
      if rex.search(password):
        mayus, minus, num = False, False, False
        if len(password) > 8:
          for x in password:
            if x.isupper():#mayusculas
              mayus = True
            if x.islower():# minusculas
              minus = True
            if x.isdigit():# Numeros
              num = True
        if mayus and minus and num: 
          message, success = '', True
  except Exception as e:
    print ('Exception in validate_pass => {}'.format(str(e)))
  return success, message 

def datos_series(folio, serie):
  message, success = _('Serie and folio are to long.'), False
  if len(serie) <= 25 and folio.isdigit() and len(folio) <= 40:
    success, message = True, ''
  return success, message

def not_only_numbers(data):
  try:
    for item in data:
      success = False if (data[item].isdigit() and data[item]) else  True
  except Exception as e:
    print ('Exception in not_only_numbers => {}'.format(str(e)))
  return success
