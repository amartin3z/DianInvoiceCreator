from .utils import get_summer_dates, get_original_string, generate_uuid
from app.sat.utils.validate import Catalogos
from app.sat.models import LCO, LRFC
from app.cfdi.models import Invoice

from datetime import datetime, timedelta
from pdb import set_trace
from lxml import etree
from django.conf import settings
from django.utils import timezone

import base64
import M2Crypto
import pytz



def validacion_fecha(date_str, zipcode=None):
  result = False
  tz_dict = {
      '5':     'America/Cancun',
      '7':     'America/Hermosillo',
      '5-6':   'America/Mexico_City',
      '6-7':   'America/Mazatlan',
      '7-8':   'America/Tijuana',
    }
  date_regx = '%Y-%m-%dT%H:%M:%S'  
  minutes = 5
  hours = 72 
  try:
    invoice_date = datetime.strptime(date_str, date_regx)
    now = pytz.timezone('America/Mexico_City').localize(timezone.now())
    catalogos_obj = Catalogos(invoice_date.date())
    tz_key, tz_name = catalogos_obj.obtener('CodigoPostal', zipcode)
    summer_dates = get_summer_dates(now.year)
    tzinfo_cp = pytz.timezone(tz_dict[tz_key])
    invoice_date_tz = tzinfo_cp.localize(invoice_date)
    if tz_key in ('5-6', '6-7', '7-8') and 'Frontera' in tz_name:
      if (invoice_date >= summer_dates['march'] and invoice_date <= summer_dates['april']) or (invoice_date >= summer_dates['october'] and invoice_date <= summer_dates['november']):
        hours = 71
        if tz_key in ('5-6', '6-7'):
          minutes = 65
    delta_72hrs = timedelta(hours=hours)
    delta_5mins = timedelta(minutes=minutes)
    date_range_before = now - delta_72hrs
    date_range_after = now + delta_5mins
    result = invoice_date_tz >= date_range_before and invoice_date_tz <= date_range_after
  except Exception as e:
    print(f'Exception validacion_fecha => {e}')
  return result


def validacion_fiel(x509_cert):
  result = False
  try:
    subject = x509_cert.get_subject().__str__()
    if "OU=" in subject:
      result = True
  except Exception as e:
    print(f"Exception valdiacion_fiel => {e}")
  return result


def validacion_lco(x509_cert, taxpayer_id):
  result = False
  try:
    serial_number = hex(x509_cert.get_serial_number())[3::2]
    lco_obj = LCO.objects.get(rfc=taxpayer_id, serial=serial_number)
    result = True
  except Exception as e:
    print(f"Exception validacion_lco => {e}")
  return result


def validacion_lcocsd(x509_cert, taxpayer_id):
  result = False
  try:
    serial_number = hex(x509_cert.get_serial_number())[3::2]
    lco_obj = LCO.objects.get(rfc=taxpayer_id, serial=serial_number, estatus='A', validez__in=('1', '2'))
    result = True
  except Exception as e:
    print(f"Exception validacion_lcocsd => {e}")
  return result


def validacion_lrfc(taxpayer_id):
  result = False
  try:
    inc_dict = LRFC.objects.filter(rfc=taxpayer_id).values('sncf', 'subcontratacion')[0]
    result = True
  except Exception as e:
    print(f"Exception validacion_lrfc => {e}")
  return result


def validacion_sello(seal, x509_cert, xml_string):
  result = False
  try:
    #decoded_seal = base64.decodestring(seal)
    decoded_seal = base64.b64decode(seal)
    original_string = get_original_string(xml_string)
    rsa = x509_cert.get_pubkey().get_rsa()
    pubkey = M2Crypto.EVP.PKey()
    pubkey.assign_rsa(rsa)
    pubkey.reset_context(md='sha256')
    pubkey.verify_init()
    pubkey.verify_update(original_string)
    result = bool(pubkey.verify_final(decoded_seal))
  except Exception as e:
    print(f"Exception validacion_sello => {e}")
  return result


def validacion_satcsd(x509_cert):
  result_ca = False
  result_issuer = False
  sat_name = 'SERVICIO DE ADMINISTRACION TRIBUTARIA'
  sat_rfc = 'SAT970701NN3'
  try:
    issuer = x509_cert.get_issuer().as_text(flags=(M2Crypto.m2.XN_FLAG_RFC2253 | M2Crypto.m2.ASN1_STRFLGS_UTF8_CONVERT))
    try:
      issuer = issuer.decode('utf8', 'ignore')
    except:
      pass
    if (sat_rfc in issuer or sat_name in issuer):
      result_issuer = True
    for root_cert in settings.SAT_ROOT_CERTS:
      if bool(x509_cert.verify(root_cert)):
        result_ca = True
        break
  except Exception as e:
    print(f"Exception validacion_satcsd => {e}")
  return result_ca and result_issuer


def validacion_timbreexistente(sello):
  namespaces = {'cfdi': 'http://www.sat.gob.mx/cfd/3','tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'}
  result, stamped_response = False, {}
  try:
    uuid = generate_uuid(sello)
    try:
      invoice_obj = Invoice.objects.get(uuid=uuid)
      xml_string = invoice_obj.xml.read()
      xml_etree = etree.fromstring(xml_string)
      sello_sat = xml_etree.xpath('string(.//cfdi:Complemento/tfd:TimbreFiscalDigital/@SelloSAT)', namespaces=namespaces)
      stamped_response = {
        "Codigo": "201",
        "Mensaje": "Timbre Previo",
        "Fecha": invoice_obj.date.replace(microsecond=0).isoformat('T'),
        "UUID": invoice_obj.uuid,
        "RFCPac": settings.SAT_RFCPROVCERTIF,
        "Xml": xml_string.decode(),
        "SelloSAT":sello_sat,
      }
    except Exception as e:
      result = True
  except Exception as e:
    print(f"Exception validacion_timbreexistente e => {e}")
  return result, stamped_response


def validacion_subjectdn(taxpayer_id, x509_cert):
  result = False
  try:
    subject = x509_cert.get_subject().as_text().replace('\\xD1', '\xD1')
    if taxpayer_id in subject:
      result = True
  except Exception as e:
    print(f"Exception validacion_subjectdn => {e}")
  return result


def validacion_csd_expiracion(x509_cert, date_str, zipcode):
  result = False
  date_regx = '%Y-%m-%dT%H:%M:%S'
  tz_dict = {
      '5':     'America/Cancun',
      '7':     'America/Hermosillo',
      '5-6':   'America/Mexico_City',
      '6-7':   'America/Mazatlan',
      '7-8':   'America/Tijuana',
  }
  try:
    date_after = x509_cert.get_not_after().get_datetime()
    date_before = x509_cert.get_not_before().get_datetime()
    invoice_date = datetime.strptime(date_str, date_regx)
    catalogos_obj = Catalogos(invoice_date.date())
    tz_key, tz_name = catalogos_obj.obtener('CodigoPostal', zipcode)
    tzinfo_cp = pytz.timezone(tz_dict[tz_key])
    invoice_date_tz = tzinfo_cp.localize(invoice_date)
    if invoice_date_tz >= date_before and invoice_date_tz <= date_after:
      result = True
  except Exception as e:
    print(f"Exception validacion_csd_expiration => {e}")
  return result


def validacion_fecha_403(date_str):
  result = False
  date_regx = '%Y-%m-%dT%H:%M:%S'    
  invoice_date = datetime.strptime(date_str, date_regx)
  if invoice_date > datetime(2018, 1, 1):
    result = True
  return result


def validacion_estructura(xml_string):
  result =  False
  try:
    root = etree.fromstring(xml_string, settings.XSD_PARSER)    
    result = True
  except Exception as e:
    print(f"Exception validacion_xml => {e}")
  return result

def validacion_usuario(user , rfc_em):
  result, error = False, 703
  if user.is_active:
    if user.business_set.last().taxpayer_id == rfc_em:
      result = True
    else:
      error = 702
  return result, error