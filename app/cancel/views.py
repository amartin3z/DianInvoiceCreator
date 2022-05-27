# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app.core.models import Business
from app.core.models import SatFile
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from .models import Request as CancelRequest
from .models import Cancellation
from .models import PendingCancellation
from .models import Cancellation
from .decorators import get_query_list_cancellation_request
from django.core.cache import cache
from django.contrib.auth.models import User
from pdb import set_trace
from app.core.decorators import get_default_business
from app.users.decorators import has_group, has_groups
#from app.providers.utils.utils import SatValidator
#from app.download.models import Invoice as DownloadInvoice
from app.core.models import Log
from .utils import value_progressbar

ANSWER = {
  'A': u'Aceptacion',
  'R': u'Rechazo',
  'U': u'Desconocida',
} 

INVOICE_STATUS = {
  'V': u'<button title="Vigente" class="btn btn-success btn-xs" ><strong>Vigente</strong></button>',
  'C': u'<button title="Cancelado" class="btn btn-danger btn-xs" ><strong>Cancelado</strong></button>',
}

INVOICE_TYPE = {
  '' : '',
  'I': u'<button title="Ingreso" class="btn btn-success btn-xs"><strong>Ingreso</strong></button>',
  'E': u'<button title="Egreso" class="btn btn-primary btn-xs"><strong>Egreso</strong></button>',
  'T': u'<button title="Traslado" class="btn btn-default btn-xs"><strong>Traslado</strong></button>',
  'N': u'<button title="Nomina" class="btn btn-info btn-xs"><strong>Nomina</strong></button>',
  'P': u'<button title="Pago" class="btn btn-warning btn-xs"><strong>Pago</strong></button>',
}

ANSWER_TYPE = {
  'A': u'<button title="Aceptación" class="btn btn-success btn-xs" ><strong>Aceptación</strong></button>',
  'R': u'<button title="Rechazo" class="btn btn-warning btn-xs"><strong>Rechazo</strong></button>',
  'U': u'<button title="Desconida" class="btn btn-danger btn-xs"><strong>Desconocida</strong></button>',
}

ESTATUSCANCELACION = {
  '': u'',
  'A': u'<button class="btn btn-danger btn-xs" title="Error"><strong>Error</strong></button>',
  'C': u'<button class="btn btn-info btn-xs" title="Cancelado con aceptación"><strong>Cancelado con aceptación</strong></button>',
  'D': u'<button class="btn btn-warning btn-xs" title="Plazo Vencido"><strong>Plazo Vencido</strong></button>', 
  'E': u'<button class="btn btn-danger btn-xs" title="En proceso"><strong>En proceso</strong></button>', 
  'W': u'<button class="btn btn-success btn-xs" title="Cancelado sin aceptación"><strong>Cancelado sin aceptación</strong></button>',
  'U': u'<button class="btn btn-default btn-xs" title="Desconocido"><strong>Desconocido</strong></button>',
}

STATUS_TYPE = {
  '1000': u'<button class="btn btn-success btn-xs" title="1000"><strong>1000</strong></button>',
  '1001': u'<button class="btn btn-warning btn-xs" title="1001"><strong>1001</strong></button>',
  '1002': u'<button class="btn btn-warning btn-xs" title="1002"><strong>1002</strong></button>',
  '1003': u'<button class="btn btn-warning btn-xs" title="1003"><strong>1003</strong></button>',
  '1004': u'<button class="btn btn-warning btn-xs" title="1004"><strong>1004</strong></button>',
  '1005': u'<button class="btn btn-warning btn-xs" title="1005"><strong>1005</strong></button>',
  '1006': u'<button class="btn btn-warning btn-xs" title="1006"><strong>1006</strong></button>',
  '996':  u'<button class="btn btn-danger btn-xs" title="Solicitud rechazada"><strong>Solicitud rechazada</strong></button>',
  '997':  u'<button class="btn btn-danger btn-xs" title="Plazo Vencido"><strong>Plazo Vencido</strong></button>',
  '998':  u'<button class="btn btn-danger btn-xs" title="Desconocido"><strong>Desconocido</strong></button>',
  '999':  u'<button class="btn btn-danger btn-xs" title="Error"><strong>Error</strong></button>',
}

STATUS = {
  '1000': u'Se recibió la respuesta de la petición de forma exitosa',
  '1001': u'No existen peticiones de cancelación en espera de respuesta para el uuid',
  '1002': u'Ya se recibió una respuesta para la petición de cancelación del uuid',
  '1003': u'Sello No Corresponde al RFC Receptor',
  '1004': u'Existen más de una petición de cancelación para el mismo uuid',
  '1005': u'El uuid es nulo no posee el formato correcto',
  '1006': u'Se rebaso el número máximo de solicitudes permitidas',
  '996':  u'Solicitud rechazada',
  '997':  u'Cancelado por Plazo Vencido',
  '998':  u'Aceptación o Rechazo no realizado en el super portal',
  '999':  u'Ocurrio un error durante el proceso de aceptacion rechazo',
  '300':  u'Usuario No Válido',
  '301':  u'XML Mal Formado',
  '302':  u'Sello Mal Formado',
  '304':  u'Certificado Revocado o Caduco',
  '305':  u'Certificado Inválido',
  '309':  u'Patrón de Folio inválido',
} 


@login_required(login_url='/')
@has_groups(['admins', 'cancelacion', 'clients'], False)
@get_default_business
@get_query_list_cancellation_request
def list_cancellation_request(request, query, **kwargs):
  try:
    if request.method == 'POST' and request.is_ajax():      
      if request.POST.get('oper') == 'list-cancel-emisor':
        list_result = []
        total = 0
        start = int(request.POST.get('iDisplayStart'))
        length = int(request.POST.get('iDisplayLength'))
        list_cancel = Cancellation.objects.filter(query).order_by('-date')
        total = list_cancel.count()
        list_cancel = list_cancel[start:start+length]
        for cancel in list_cancel.iterator():
          options = ''
          if cancel.status_sat == 'V' and cancel.status == 'E':
            options = '<button type="button" total="{}" class="btn btn-info get_sat_status btn-xs" title="Consultar estatus"><i class="fa fa-eye"></i></button>'.format(cancel.total)
          list_result.append([
            '<span class="label label-emails" title="">{}</span>'.format(cancel.user.email),
            cancel.uuid,
            cancel.date.strftime("%Y-%m-%dT%H:%M:%S"),
            INVOICE_STATUS[cancel.status_sat],
            ESTATUSCANCELACION[cancel.status],
            cancel.taxpayer_id,
            cancel.rtaxpayer_id,
            INVOICE_TYPE[cancel.invoice_type],
            cancel.total,
            options,
          ])
        result = {
          'aaData': list_result,
          'iTotalRecords': total,
          'iTotalDisplayRecords': total,
        }
        Log.objects.log_action(request, 5, 'R', u'Se listaron las cancelaciones del emisor', 'A', '')
        return JsonResponse(result)        
      elif request.POST.get('oper') == 'list-cancel-receiver-pending':
        business_id = request.session.get('business_id', None)
        business = Business.objects.get(id=business_id)
        rtaxpayer_id = business.taxpayer_id
        cont = 1
        list_result = []
        total = 0
        start = int(request.POST.get('iDisplayStart'))
        length = int(request.POST.get('iDisplayLength'))
        list_pending_cacellation = PendingCancellation.objects.filter(rtaxpayer_id=rtaxpayer_id).filter(query).order_by('date')
        total = list_pending_cacellation.count()
        list_pending_cacellation = list_pending_cacellation[start:start+length]
        for invoice in list_pending_cacellation.iterator():
          taxpayer_id, invoice_type, invoice_total = '', '', ''
          if invoice.taxpayer_id:
            taxpayer_id = invoice.taxpayer_id
          if invoice.invoice_type: 
            invoice_type = invoice.invoice_type 
          if invoice.total:
            invoice_total = invoice.total
          value = value_progressbar(invoice.date)
          answer = render_to_string('strings/accept_reject_options.html', {'cont': cont}, request)
          progressbar = render_to_string('strings/progres_bar_pending_cancellation.html', {'value': value}, request)
          options = render_to_string('strings/get_pending_options.html', {'uuid': invoice.uuid}, request)
          list_result.append([
            invoice.date.strftime("%Y-%m-%dT%H:%M:%S"),
            progressbar,
            invoice.uuid,
            taxpayer_id,
            INVOICE_TYPE[invoice_type],
            invoice_total,
            answer,
            options,
          ])
          cont+=1
        result = {
          'aaData': list_result,
          'iTotalRecords': total,
          'iTotalDisplayRecords': total,
        }
        Log.objects.log_action(request, 5, 'R', u'Se listarón las cancelaciones pendientes del receptor', 'A', '')
        return JsonResponse(result)
      elif request.POST.get('oper') == 'list-cancel-receiver-finished':  
        list_result = []
        total = 0
        start = int(request.POST.get('iDisplayStart'))
        length = int(request.POST.get('iDisplayLength'))
        list_cancel = CancelRequest.objects.filter(last=True).filter(query).order_by('-date')
        total = list_cancel.count()
        list_cancel = list_cancel[start:start+length]
        for cancel_request in list_cancel.iterator():
          options = render_to_string('strings/history_options.html', {'uuid': cancel_request.uuid, 'status':cancel_request.status}, request)
          status = render_to_string('strings/status_options.html', {'status': cancel_request.status, 'answer':cancel_request.response}, request)
          list_result.append([
            '<span class="label label-emails" title="">{}</span>'.format(cancel_request.user.email),
            cancel_request.uuid,
            cancel_request.date.strftime("%Y-%m-%dT%H:%M:%S"),
            ANSWER_TYPE[cancel_request.response],
            status,
            options,
          ])
        result = {
          'aaData': list_result,
          'iTotalRecords': total,
          'iTotalDisplayRecords': total,
        }
        Log.objects.log_action(request, 5, 'R', u'Se listarón las cancelaciones finalizadas del receptor con un total de {}'.format(total), 'A', '')
        return JsonResponse(result)
    else:
      parameters = {
        'tab': 'P'
      }
      template = 'cancel/cancellation_requests.html'
      return TemplateResponse(request, template, parameters) 
  except Exception as e:    
    Log.objects.log_action(request, 2, 'R', u'Ocurrio una excepción al listar las peticiones de cancelacion', 'A', 'Exception list_cancellation_request => {}'.format(e))
    raise Exception('Exception list_cancellation_request() | {}'.format(e))

@login_required(login_url='/')
@has_groups(['admins', 'cancelacion'], False)
def accept_reject(request):
  try:
    if request.method == 'POST' and request.is_ajax():
      success = False
      message = u'Error en el proceso, intentar mas tarde.'
      status = '1000'
      notes = None
      business_id = request.session.get('business_id', None)
      business = Business.objects.get(id=business_id)
      rtaxpayer_id = business.taxpayer_id
      answer_pos = request.POST.get('answer')
      answer = ANSWER[answer_pos]
      uuid = request.POST.get('uuid')
      csd = business.get_csd()
      cer = csd['cer'].encode('base64')
      key = csd['key'].encode('base64')
      result =FINKOKWS.accept_rejects(uuid, rtaxpayer_id, answer, cer, key)
      try:
        try:
          if result.rechazo is not None:
            status = result.rechazo.Rechaza[0].status
            notes = STATUS[status]
            if status in ('300', '301', '302', '304', '305', '309'):
              status = '999'
          elif result.aceptacion is not None:
            status = result.aceptacion.Acepta[0].status
            notes = STATUS[status]
            if status in ('300', '301', '302', '304', '305', '309'):
              status = '999'
          else:
            status = '999'
            notes = STATUS[status]
        except:
          status = '999'
          notes = result.error
        try:
          invoices = CancelRequest.objects.filter(uuid=uuid)
          invoices.update(last=False)
        except:
          print('Exception update to false in CancelRequest')
        cacel_request = CancelRequest(
          user = request.user,
          uuid = uuid,
          date = datetime.now(),
          rtaxpayer_id = rtaxpayer_id,
          response = answer_pos,
          status = status,
          notes = notes,
        )
        cacel_request.save()
        if status == '1000':
          success = True
          message = '[{}] solicitud de {} exitosa'.format(uuid, answer)
          PendingCancellation.objects.get(uuid=uuid).delete()
          Log.objects.log_action(request, 5, 'R', message, 'I', '')
        else:
          message = notes
      except Exception as e:
        print('Exception save db Cancel-Request ==> {}'.format(e))
        Log.objects.log_action(request, 2, 'C', u'Ocurrio una excepción al guardar la peticion de cancelacion {} en la BD'.format(uuid), 'A', 'Exception save db Cancel-Request ==> {}'.format(e))
      Log.objects.log_action(request, '5', 'U', '{} del uuid => {}'.format(answer, uuid), 'A', '')
  except Exception as e:
    print('Exception accept_reject() | {}'.format(str(e)))
    Log.objects.log_action(request, 2, 'R', u'Ocurrio una excepcion en el metodo accept_reject', 'A', 'Exception accept_reject() => {}'.format(str(e)))
  data = {'success' : success, 'message' : message}
  return JsonResponse(data)

@login_required(login_url='/')
@has_groups(['admins', 'cancelacion'], False)
def consult_status(request):
  try:
    if request.method == 'POST' and request.is_ajax():
      success = False
      message = ''
      uuid = request.POST.get('uuid')
      template = '?re=%s&rr=%s&tt=%s&id=%s'
      if request.POST.get('option') == 'receiver':
        try:
          business_id = request.session.get('business_id', None)
          business = Business.objects.get(id=business_id)
          rtaxpayer_id = business.taxpayer_id
          invoice = ProviderInvoice.objects.get(uuid=uuid)
          taxpayer_id = invoice.taxpayer_id
          total = '%017f'%invoice.total
          try:
            #response_get_sat_status, client  = FINKOKWS.get_sat_status(uuid, taxpayer_id, rtaxpayer_id, total)
            query = template % (taxpayer_id, rtaxpayer_id, total, uuid)
            sat_obj = SatValidator(query)
            response_sat_obj = sat_obj.is_valid()
            if response_sat_obj['success']:
              if response_sat_obj['status'] == 'C':
                estatus_cancelacion = response_sat_obj['notes']
                if 'Cancelado con acept' in estatus_cancelacion:
                  status = '1000'
                  response = 'A'
                elif 'Plazo vencido' in estatus_cancelacion:
                  status = '997'
                  response = 'U'
                elif 'En proceso'in estatus_cancelacion:
                  return JsonResponse({'success':True, 'message':u'Cancelación en proceso'})
                try:
                  try:
                    invoices = CancelRequest.objects.filter(uuid=uuid)
                    invoices.update(last=False)
                  except:
                    print('Exception update to false in CancelRequest')
                  user = User.objects.get(id=1)
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
                  message = 'Actualización exitosa, comprobante cancelado'
                  success = True
                except Exception as e:
                  message = u'Contactar a Soporte Técnico.'
                  print('Exception: in save database in consult_cancellation_pending ==> {}'.format(str(e)))
                  Log.objects.log_action(request, 2, 'R', u'Ocurrio una excepcion al momento de guardar en la BD la consulta de cancelacion pendiente con uuid {}'.format(uuid), 'A', 'Exception: in save database in consult_cancellation_pending => {}'.format(str(e)))
              elif response_sat_obj['status'] == 'V':
                message = u'Comprobante Vigente'
                success = True
                Log.objects.log_action(request, 5, 'R','{} {}'.format(message, uuid), 'A', '')
              elif response_sat_obj['status'] == 'N':
                success = True
                message = 'No encontrado en el SAT'
                Log.objects.log_action(request, 5, 'R','{} {}'.format(message, uuid), 'A', '')
              else:
                message = u'Contactar a Soporte Técnico.'
            else:
              message = u'Error con el SAT, Intente mas tarde.'
              Log.objects.log_action(request, 5, 'R','{} {}'.format(message, uuid), 'A', '')
          except Exception as e:
            message = u'Contactar a Soporte Técnico.'
            print('Exception: in consult status ==> {}'.format(str(e)) )
        except:
          message = 'Aceptación o Rechazo no realizada en el super portal'
          print('Exception: Invoice not exist in Download')
          Log.objects.log_action(request, 2, 'R', u'Aceptación o rechazo no realizada en el portal {}'.format(uuid), 'A', 'Exception: Invoice not exist in Download')
        Log.objects.log_action(request, 5, 'R', u'{}'.format(message), "A", '')
      elif request.POST.get('option') == 'emisor':
        taxpayer_id = request.POST.get('taxpayer_id')
        rtaxpayer_id = request.POST.get('rtaxpayer_id')
        total = '%017f'%request.POST.get('total')
        #response, client = FINKOKWS.get_sat_status(uuid, taxpayer_id, rtaxpayer_id, total)
        query = template % (taxpayer_id, rtaxpayer_id, total, uuid)
        sat_obj = SatValidator(query)
        response_sat_obj = sat_obj.is_valid()
        try:
          if response_sat_obj['success']:
            estatus_cancelacion = response_sat_obj['notes']
            if response_sat_obj['status'] == 'C':
              success = True
              status_sat = 'C'
              status = 'D'
              if 'Cancelado sin' in estatus_cancelacion:
                status = 'W'
              elif 'Cancelado con' in estatus_cancelacion:
                status = 'C'
              try:
                invoice = Cancellation.objects.filter(uuid=uuid).latest('date')
                invoice.status_sat = status_sat
                invoice.status = status
                invoice.save()
                stamping_invoice_obj = stamping_invoice.objects.get(uuid=uuid)
                stamping_invoice_obj.status = status_sat
                stamping_invoice_obj.save()
                success = True
                message = 'Actualización exitosa'
                Log.objects.log_action(request, 5, 'R','{} {}'.format(message, uuid), 'A', '')
              except Exception as e:
                print('Exception save db Cancel-Cancellation ==> {}'.format(e))
                Log.objects.log_action(request, 2, 'R',u'Ocurrio un inconveniente al guardar la cancelacion en la BD', 'A', 'Exception save db Cancel-Cancellation ==> {}'.format(e))
            elif response_sat_obj['status'] == 'V':
              message = u'Comprobante Vigente'
              success = True
              if 'En proceso'in estatus_cancelacion:
                success = True
                message = u'Cancelación en proceso'
                Log.objects.log_action(request, 5, 'R','{} {}'.format(message, uuid), 'A', '')
            elif response_sat_obj['status'] == 'N':
              success = True
              message = 'No encontrado en el SAT'
              Log.objects.log_action(request, 5, 'R','{} {}'.format(message, uuid), 'A', '')
            else:
              message = u'Contactar a Soporte Técnico.'
          else:
            message = u'Error con el SAT, Intente mas tarde.'
        except Exception as e:
          message = u'Contactar a Soporte Técnico.'
          print('Exception in get_sat_status ==> {}'.format(str(e)))
          Log.objects.log_action(request, 2, 'R', u'Ocurrio una excepción al momento de consultar el estatus de la cancelacion', 'A', 'Exception in get_sat_status ==> {}'.format(str(e)))
        Log.objects.log_action(request, 5, 'R', u'{}'.format(message), "A", '')
      data = {
        'success' : success,
        'message' : message
      }
      return JsonResponse(data)
  except Exception as e:
    raise Exception('Exception get_sat_status() | {}'.format(e)) 

@login_required(login_url='/')
@has_groups(['admins', 'cancelacion', 'clients'], False)
def history_cancellation(request):
  try:
    if request.method == 'POST' and request.is_ajax():
      list_result = []
      total = 0
      try:
        uuid = request.POST.get('uuid')
        list_cancel =  CancelRequest.objects.filter(uuid=uuid).order_by('-date')
        total = list_cancel.count()
        for cancel in list_cancel.iterator():
          list_result.append([
            '<span class="label label-emails" title="">{}</span>'.format(cancel.user.email),
            cancel.date.strftime("%Y-%m-%d %H:%M"),
            ANSWER_TYPE[cancel.response],
            STATUS_TYPE[cancel.status],
            cancel.notes if cancel.notes is not None else STATUS[cancel.status],
          ])
      except ObjectDoesNotExist as ex:
        Log.objects.log_action(request, 2, 'R', u'No existe la cancelacion', 'A', str(ex))
      result = {
        'aaData': list_result,
        'iTotalRecords': total,
        'iTotalDisplayRecords': total,
      }
      return JsonResponse(result)
  except Exception as e:
    raise Exception('Exception history_cancellation() | {}'.format(e))
    Log.objects.log_action(request, 2, 'R', u'Ocurrio una excepcion en historial de cancelacion', 'A', 'Exception history_cancellation() => {}'.format(e))


