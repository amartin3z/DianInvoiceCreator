# -*- encoding: UTF-8 -*-

from celery.decorators import task
from ublinvoice.celery import app
from .models import Cancellation
from .models import PendingCancellation
from .models import Request as CancelRequest
from .views import STATUS 

from app.core.models import Business 
from django.conf import settings
from pdb import set_trace
from lxml import etree as ET
from django.contrib.auth.models import User
from datetime import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string
if settings.DEBUG:
  from pdb import set_trace

#@app.task(queue=settings.CELERY_QUEUE_NAME)
def import_cancellation(xml_string=None, xml_path=None, xml_etree=None):
  try:

    error = 'Error: en la funcion import_cancellation' 
    namespaces = {'cfdi': 'http://www.sat.gob.mx/cfd/3', 'tfd':'http://www.sat.gob.mx/TimbreFiscalDigital'}
    cancellation_obj = None

    # Make sure we have an xml_etree object, so we can get all the needed information
    if xml_etree is None:
      if xml_string is not None:
        xml_etree = ET.fromstring(xml_string)
      elif xml_path is not None:
        xml_string =  open(xml_path, 'r').read()
        xml_etree = ET.fromstring(xml_string)
  
    try:
      tfd = xml_etree.xpath('.//cfdi:Complemento/tfd:TimbreFiscalDigital', namespaces=namespaces)[0]
      uuid = tfd.get('UUID').upper()
    except:
      error = 'Error en import_cancellation: al obtener el UUID del comprobante'
      return None, error 

    ## Verify if the Cancellation object already exists
    cancellation_exits = Cancellation.objects.filter(uuid=uuid).exists()
    if not cancellation_exits:
      try:
        invoice_type = xml_etree.get('TipoDeComprobante')
      except:
        error = "Error en import_cancellation: al obtener el Tipo De Comprobante"
        return None, error
      try:
        issuing = xml_etree.xpath('.//cfdi:Emisor', namespaces=namespaces)[0]
        taxpayer_id = issuing.get('Rfc')
      except:
        error = 'Error en import_cancellation: al obtener el RFC emisor del comprobante'
        return None, error
      try:
        receiver = xml_etree.xpath('.//cfdi:Receptor', namespaces=namespaces)[0]
        rtaxpayer_id = receiver.get('Rfc')
      except:
        error = 'Error en import_cancellation: al obtener el RFC receptor del comprobante'
        return None, error
      try:
        total =  xml_etree.get('Total')
      except:
        error = 'Error en import_cancellation: al obtener el total del comprobante'
        return None, error
      try:
        date = xml_etree.get('Fecha')
      except:
        error = 'Error en import_cancellation: al obtener la Fecha del comprobante' 
        return None, error

      user = User.objects.get(id=1)
      cancellation_obj = Cancellation(uuid=uuid)
      cancellation_obj.user = user
      cancellation_obj.date = date
      cancellation_obj.total = total
      cancellation_obj.invoice_type = invoice_type
      cancellation_obj.taxpayer_id = taxpayer_id
      cancellation_obj.rtaxpayer_id = rtaxpayer_id
      cancellation_obj.status = 'U'
      cancellation_obj.status_sat = 'C'
      cancellation_obj.notes = 'import_cancellation'
      cancellation_obj.save()
      error = 'Imported import_cancellation Successfull'
    else:
      error = "Objeto cancellation existente UUID => {}".format(uuid)
      cancellation_obj = True
          
    return cancellation_obj, error

  except Exception as e:
    error = str(e) 
    print('Exception in import_cancellation ==> {}'.format(error))

  return None, error


@task(queue=settings.CELERY_QUEUE_NAME)
def consult_pending_cancellation():
  try:
    list_result = []
    if settings.DEBUG:
      businesses = Business.objects.filter(is_staff=True).values_list('taxpayer_id', flat=True)
    else:
      businesses = Business.objects.filter(is_staff=True).exclude(taxpayer_id='TCM970625MB1').values_list('taxpayer_id', flat=True)
    user = User.objects.get(id=1)
    for business in businesses:
      result = {'success':True, 'business':business, 'message': 'Proceso exitoso', 'requests_new': [], 'requests_expired': []}
      uuids_pendingcancellation = list(PendingCancellation.objects.filter(rtaxpayer_id=business).values_list('uuid', flat=True))
      success, uuids_get_pendig = FINKOKWS.get_pending(business)
      if success: 
        list_get_pendig = list(set(uuids_get_pendig)-set(uuids_pendingcancellation)) #uuids que no se encuentran en PendingCancellation
        list_pendingcancellation = list(set(uuids_pendingcancellation)-set(uuids_get_pendig)) #uuids que no se encuentran en get_pending
        if len(list_get_pendig):
          result['requests_new'] = list_get_pendig
        if len(list_pendingcancellation):
          result['requests_expired'] = list_pendingcancellation
        for uuid in list_get_pendig:
          # modificar???
          # try:
          #   invoice = DownloadInvoice.objects.get(uuid=uuid)
          #   taxpayer_id = invoice.taxpayer_id
          #   invoice_type = invoice.type
          #   invoice_total = invoice.total
          # except:
          #   taxpayer_id, invoice_type, invoice_total = None, None, None
          try:
            pending_cancellation = PendingCancellation(
              uuid = uuid,
              taxpayer_id = taxpayer_id,
              rtaxpayer_id = business,
              invoice_type = invoice_type,
              total = invoice_total
            )
            pending_cancellation.save()
          except Exception as e:
            print('Exception: save database in consult_cancellation_pending ==> {}'.format(str(e)))
        
        for uuid in list_pendingcancellation:
          try:
            status = '998'
            response = 'U'
            try:
              invoices = CancelRequest.objects.filter(uuid=uuid)
              invoices.update(last=False)
            except:
              print('Exception update to false in CancelRequest')
            PendingCancellation.objects.get(uuid=uuid).delete()
            cancel_request = CancelRequest(
              user = user,
              uuid = uuid,
              date = datetime.now(),
              rtaxpayer_id = business,
              response = response,
              status = status,
              notes = STATUS[status]
            )
            cancel_request.save()
          except Exception as e:
            print('Exception: in save database in consult_cancellation_pending ==> {}'.format(str(e)))
      else:
        result = {'success':False, 'business':business, 'message': uuids_get_pendig[0], 'requests_new': [], 'requests_expired': []}
      list_result.append(result)
    html_message = render_to_string('strings/mail.html', {'module': 'Cancel', 'rows': list_result, 'option':'pending'})
    send_mail('Portal Soriana | Cancel', '', settings.SMTP_FROM_EMAIL, [settings.SMTP_TO_EMAIL], fail_silently=True, html_message=html_message)
  except Exception as e:
    print('Exception: in consult_cancellation_pending ==> {}'.format(str(e)))


@task(queue=settings.CELERY_QUEUE_NAME)
def verify_status(uuid):
  try:
    register = False
    user = User.objects.get(id=1)
    template = '?re=%s&rr=%s&tt=%s&id=%s'
    status = '998'
    response = 'U'
    invoice = DownloadInvoice.objects.get(uuid=uuid)
    taxpayer_id = invoice.taxpayer_id
    rtaxpayer_id = invoice.rtaxpayer_id
    invoice_total = '%017f'%invoice.total
    query = template % (taxpayer_id, rtaxpayer_id, invoice_total, uuid)
    sat_obj = SatValidator(query)
    response_sat_obj = sat_obj.is_valid()
    if response_sat_obj['success']:
      if response_sat_obj['status'] == 'C':
        register = True
        estatus_cancelacion = response_sat_obj['notes']
        if 'Cancelado con acept' in estatus_cancelacion:
          status = '1000'
          response = 'A'
        elif 'Plazo vencido' in estatus_cancelacion:
          status = '997'
      elif response_sat_obj['status'] == 'V' and 'Solicitud rechazada' in response_sat_obj['notes']:
        response = 'R'
        status='996'
        register = True
      try:
        if register:
          try:
            invoices_request = CancelRequest.objects.filter(uuid=uuid)
            invoices_request.update(last=False)
          except:
            pass
          cancel_request = CancelRequest(
            user = user,
            uuid = uuid,
            date = datetime.now(),
            rtaxpayer_id = rtaxpayer_id,
            response = response,
            status = status,
            notes = STATUS[status]
          )
          cancel_request.save()
          print('Register {} update success'.format(uuid))
          try:
            invoice.status_sat = 'C'
            invoice.status = 'C'
            invoice.save()
          except:
            print('Exception: to the update invoice_download status C uuid ==> {}'.format(uuid))
      except Exception as e:
        print('Exception: in save database in consult_cancellation_pending ==> {}'.format(str(e)))
  except Exception as e:
    print('Exception in the function verify_status => {}'.format(str(e)))


@task(queue=settings.CELERY_QUEUE_NAME)
def consult_status():
  try:
    list_result = []
    if settings.DEBUG:
      businesses = Business.objects.filter(is_staff=True).values_list('taxpayer_id', flat=True)
    else:
      businesses = Business.objects.filter(is_staff=True).exclude(taxpayer_id='TCM970625MB1').values_list('taxpayer_id', flat=True)
    for business in businesses:
      result = {'success':True, 'business':business, 'message': u'Actualización de estatus exitosa.'}
      invoices = CancelRequest.objects.filter(last=True, rtaxpayer_id=business, response='U', status='998')
      for invoice_ in invoices:
        try:
          verify_status.apply_async((invoice_.uuid,),)
        except:
          pass
      list_result.append(result)
    html_message = render_to_string('strings/mail.html', {'module': 'Cancel', 'rows': list_result, 'option':'status'})
  except Exception as e:
    message = 'Error en el proceso de consultar estatus de CFDI ==> {}'.format(str(e))
    result['success'], result['message'] = False, str(e)
  send_mail('Portal Soriana | Cancel', '', settings.SMTP_FROM_EMAIL, [settings.SMTP_TO_EMAIL], fail_silently=True, html_message=html_message)
