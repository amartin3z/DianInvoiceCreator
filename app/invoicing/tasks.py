# -*- encoding: UTF-8 -*-
from django.conf import settings
from django.contrib.auth.models import User

from .models import Invoice
from app.cancel.models import Cancellation
from app.cfdi.utils.controller import CFDIValidator

from ublinvoice.celery import app

import os
from lxml import etree
from celery.decorators import task


#@task(name='app.invoicing.tasks.add', default_retry_delay=60, max_retries=3, ignore_result=True, queue=settings.CELERY_QUEUE_NAME)
def add(x, y):
  return x + y

#@task(name='app.invoicing.tasks.stamp', ignore_result=True, queue=settings.CELERY_QUEUE_NAME)
from base64 import b64encode
def stamp_process_old(xml_string, invoice_id):
  try:
    count_incidents = 0
    incidents_response = {'error': []}
    incidents_append = incidents_response['error'].append
    invoice_obj = Invoice.objects.get(id=invoice_id)
    response, client = FINKOKWS.sign_stamp(xml_string, taxpayer_id=invoice_obj.taxpayer_id)
    #raise Exception('Error hasnt controlated')
    if hasattr(response, 'CodEstatus') and response.CodEstatus in ('Comprobante timbrado satisfactoriamente', 'Comprobante timbrado previamente'):
      invoice_obj.uuid = response.UUID
      invoice_obj.stamping_date = response.Fecha
      tfd_seal = response.SatSeal
      invoice_obj.status = 'F'
      try:
        stamped_xml = response.xml
        try:
          stamped_xml = stamped_xml.encode('utf-8')
        except:
          pass
        xml_etree = etree.fromstring(stamped_xml)
        invoice_obj.xml = response.xml
        invoice_obj.seal = xml_etree.get('Sello')
      except Exception as e:
        print('Could not get XML from stamping response => {}'.format(e))
      #invoice_obj.save()
    elif hasattr(response, 'Incidencias') and response.Incidencias:
      incidents = response.Incidencias.Incidencia
      if invoice_obj.error_messages:
        incidents_response = invoice_obj.error_messages
        incidents_append = incidents_response['error'].append
      for incident in incidents:
        code_error = 'undefined'
        if hasattr(incident, 'CodigoError') and not incident.CodigoError in incidents_response:
          code_error = incident.CodigoError
          incident_message = incident.MensajeIncidencia
          try:
            incident_message = incident_message.encode('utf-8')
          except:
            pass
          extra_info = incident.ExtraInfo
        incidents_append({
          'error': code_error,
          'incident': incident_message.__str__(),
          'extra_info': extra_info
        })
      invoice_obj.status = 'E'
      invoice_obj.error_messages = incidents_response
    invoice_obj.save()
  except Exception as e:
    folio = b64encode(os.urandom(6)).strip().replace(b'=', b'').__str__()
    print('{}: Exception on stamp_process method => {}'.format(folio, e))
    if invoice_obj and invoice_obj.error_messages:
      #set_trace()
      incidents_response = invoice_obj.error_messages
      incidents_append = incidents_response['error'].append
      count_incidents = len(incidents_response['error'])
    try:  
      incidents_append({
        'error': 'Folio: {}'.format(folio),
        'incident': 'Hubo un error, re intente el timbrado, si el problema persiste proporcioné el folio a desarrollo@finkok.com para más información.'
      })
      status_error = 'U'
      if count_incidents > 2:
        status_error = 'E'
      invoice_obj.status = status_error
      invoice_obj.error_messages = incidents_response
      invoice_obj.save()
    except Exception as e:
      print('{}: Exception stamp_process on save invoice_obj => {}'.format(folio, e))



#@task(name='app.invoicing.task.cancel', queue=settings.CELERY_QUEUE_NAME)
def cancel_process(uuid, taxpayer_id, invoice_id, serial, notes=None, user_id=None):
  try:
    status_sat = 'V'
    status_invoice = 'F'
    status_cancellation = 'D'

    message = ''
    status_uuid = None
    
    incidents_response = {'error': []}
    incidents_append = incidents_response['error'].append
    user = User.objects.get(id=user_id)
    invoice_obj = Invoice.objects.get(id=invoice_id)
    response, client = FINKOKWS.sign_cancel(uuid, taxpayer_id, serial)
    print(response)
    if hasattr(response, 'Folios'):
      for folio in response.Folios[0]:
        uuid = folio.UUID
        status_uuid = folio.EstatusUUID
        status_cancel = folio.EstatusCancelacion
        if status_uuid in ('201', '202'):
          if status_cancel in (u'Cancelado sin aceptación', u'Cancelado con aceptación', u'Plazo vencido'):
            status_invoice = 'C'
            status_sat = 'C'
            if 'con' in status_cancel:
              status_cancellation = 'C'
            if 'sin' in status_cancel:
              status_cancellation = 'W'
          elif status_cancel == 'En proceso':
            status_invoice = 'R'
            status_cancellation = 'E'
          elif status_cancel == 'No cancelable':
            message = 'Factura no cancelable'
          if status_invoice != 'F':
            cancellation_obj = Cancellation(
              user = user,
              uuid = uuid,
              total = invoice_obj.total,
              invoice_type = invoice_obj.type,
              taxpayer_id = invoice_obj.taxpayer_id,
              rtaxpayer_id = invoice_obj.rtaxpayer_id,
              status = status_cancellation,
              status_sat = status_sat,
              notes=u'{} => {}'.format(status_cancellation, notes),
            )
            cancellation_obj.save()
        elif status_uuid == '708':
          try:
            raise Exception('708')
          except Exception as e:
            print('708 could not connect with SAT, retrying => {}'.format(e))
            cancel_process.retry(args=[uuid, taxpayer_id, invoice_id, serial, user, notes], countdown=300)
      invoice_obj.status = status_invoice
      invoice_obj.save()
  except Exception as e: 
    folio = os.urandom(6).encode('base64').strip().replace('=', '')
    print('{}: Exception on cancel_process => {}'.format(folio, e))
    try:
      invoice_obj.status = 'S'
      invoice_obj.task_id = ''
      invoice_obj.save()
    except Exception as e:
      print('{}: Exception cancel_process on save invoice_obj => {}'.format(folio, e))
