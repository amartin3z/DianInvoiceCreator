from celery.decorators import task
from django.conf import settings
from app.cfdi.models import Invoice
#from app.invoicing.models import Invoice as FreeInvoice
#from app.invoicing.models import ProdServ
from app.sat.models import Receipt, Cancellation, ServiceLevel, ServiceLevelDetail
from pdb import set_trace
from datetime import datetime
from html import escape
from .utils.connector import SATConnector
from django.core.files.base import ContentFile
from django.db.models import F
import re
import json


@task(ignore_result=True, soft_time_limit=100, time_limit=100, default_retry_delay=50, max_retries=6)
def enviar_sat(uuid):
  #set_trace()
  from app.invoicing.models import Invoice as FreeInvoice
  try:
    now = datetime.now()
    print(f"[{now}] {uuid}")

    if settings.SAT_RECEPCION:

      sat_obj = SATConnector()
      invoice = Invoice.objects.get(uuid=uuid, status='S')

      metadatos = {
        'uuid': uuid,
        'rfc': invoice.taxpayer_id,
        'fecha': invoice.date.replace(microsecond=0).isoformat(),
        'no_certificado': settings.SAT_NO_CERTIFICADO, 
        'version': invoice.version,
      }
      xml_str = invoice.xml.read().decode().replace('''<?xml version='1.0' encoding='utf8'?>''','').replace('\n','')
      result_dict, incident_lst, acuse_xml = sat_obj.enviar(metadatos, xml_str)

      year = int(result_dict['Fecha'][:4])
      month = int(result_dict['Fecha'][5:7])

      if 'CodEstatus' in result_dict:
        cod_estatus = result_dict['CodEstatus']
        if re.match('.*recibido.*', cod_estatus):
          invoice.status = 'F'
          invoice.save()
          if re.match(".*incidencia.*", cod_estatus):
            registrar_incidencia('incidents', year, month, uuid, invoice.taxpayer_id, incident_lst, acuse_xml)
          if re.match(".*extemp.*", cod_estatus):
            registrar_incidencia('extemporaneous', year, month, uuid, invoice.taxpayer_id, incident_lst, acuse_xml)
          if re.match(".*satisfactoriamente.*", cod_estatus):
            registrar_incidencia('satisfied', year, month, uuid, invoice.taxpayer_id, incident_lst, acuse_xml)
          print(f'{uuid} => {cod_estatus}')
        elif re.match('.*rechazado.*', cod_estatus):
          invoice.status = "R"
          invoice.save()
          if invoice.type == 'F' and settings.APPLY_ASYNC:
            f_invoice = FreeInvoice.objects.get(uuid=uuid)
            f_invoice.status = 'R'
            f_invoice.save()
          codigoerror = incident_lst[0]['CodigoError']
          mensaje = incident_lst[0]['MensajeIncidencia']
          registrar_incidencia('rejected', year, month, uuid, invoice.taxpayer_id, incident_lst, acuse_xml)
          print(f'{uuid} => {cod_estatus} => {codigoerror} => {mensaje}')
        receipt = Receipt(
          uuid=uuid,
          cod_status=cod_estatus,
          date=result_dict['Fecha'],
          incidents=json.dumps(incident_lst),
          taxpayer_id=invoice.taxpayer_id,
        )
        receipt.xml = ContentFile(acuse_xml, '{}.xml'.format(uuid)) 
        receipt.save()
      elif 'faultcode' in result_dict:
        invoice.status = 'E'
        invoice.save()
        if invoice.type == 'F':
          f_invoice = FreeInvoice.objects.get(uuid=uuid)
          f_invoice.status = 'E'
          f_invoice.save()
        print(f"{result_dict['UUID']} => FAULTCODE => {result_dict['faultcode']} => {result_dict['faultstring']}")
  except Exception as e:
    print(f"Exception tasks enviar_sat => {e}")
    if settings.APPLY_ASYNC:
      enviar_sat.retry(args=[uuid])


def registrar_incidencia(_type, year, month, uuid, taxpayer_id, incident_lst, acuse_xml):
  service_level, created = ServiceLevel.objects.get_or_create(year=year, month=month)
  if _type == 'satisfied':
    service_level.satisfied = F('satisfied') + 1
  else:
    if _type == 'extemporaneous':
      service_level.extemporaneous = F('extemporaneous') + 1
    elif _type == 'incidents':
      service_level.incidents = F('incidents') + 1
    elif _type == 'rejected':
      service_level.rejected = F('rejected') + 1
    detail = ServiceLevelDetail(service=service_level, uuid=uuid, taxpayer_id=taxpayer_id, incidents=incident_lst, detail=acuse_xml)
    detail.save()
  service_level.save()



@task(ignore_result=True, soft_time_limit=100, time_limit=100, default_retry_delay=50, max_retries=6)
def cancelar_sat(uuid_lst, rfc, cer, key):
  success = True
  result = {}
  folios_lst = []
  response = ""
  error1 = ""
  error2 = ""
  try:    
    now = datetime.now()
    print(f"[{now}] cancelar_sat {uuid_lst} {rfc}")
    if settings.SAT_CANCELACION:
      sat_obj = SATConnector()
      result, folios_lst, response, error1, error2 = sat_obj.cancelar(uuid_lst, rfc, cer, key)
            
      if 'CodEstatus' not in result or (error1 == "" and error2 == ""):
        for folio in folios_lst:
          uuid_success = False
          uuid = folio['UUID']
          estatus = folio['EstatusUUID']        
          cancel = Cancellation(
            taxpayer_id = rfc,
            cod_status = None,
            date = result['Fecha'],
            uuid = uuid, 
            uuid_status = estatus,
            faultcode = error1,
            faultstring = error2,
          )
          cancel.xml = ContentFile(response, '{}.xml'.format(uuid))
          cancel.save()
          if estatus in ('201', '202'):
            uuid_success = True
            invoice = Invoice.objects.get(uuid=uuid)
            invoice.status = 'C'
            invoice.save()
          else:
            uuid_success = False

          success = success and uuid_success
  except Exception as e:
    print(f"Exception tasks cancelar_sat => {e}")
    success = False

  result['success'] = success

  return result, folios_lst, response, error1, error2 


@task(ignore_result=True, soft_time_limit=100, time_limit=100, default_retry_delay=50, max_retries=6)
def consultar_sat(re, rr, tt, id):
  result = {'success': False}
  sat_obj = SATConnector()
  try:
    result = sat_obj.consultar(re, rr, tt, id)
  except Exception as e:
    print(f"Exception tasks consultar_sat => {e}")
  return result