# -*- coding: UTF-8 -*-

from django.conf import settings
#from django.db import transaction
from django.db.models import F, Q
from django.core.cache import cache
from django.db import IntegrityError
from django.urls import resolve, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from django.views.decorators.http import require_POST, require_http_methods

from .decorators import get_query_invoicing
from .models import ProdServ, Receiver, Invoice, Buyer

from .utils.cfdi33 import CFDI
from .utils.moneda import numero_a_letras
from .utils.catalogos import PRODSERV, CLAVEUNIDAD
from .utils.pdf import CreatePDF
from app.peppol.utils.utils import CreatePDF as CreatePDF_
from .utils.handler import get_context, post_invoice

#from app.providers.utils.utils import SatValidator
#from app.providers.utils.controller import CreatePDF

from app.sat.tasks import consultar_sat, cancelar_sat

from app.core.models import FISCAL_REGIME, Log, Business
from app.core.catalogs import INVOICE_STATUS
from app.core.decorators import get_default_business, able_to_invoice

from app.sat.models.cfdi import UsoCFDI, ClaveUnidad, ClaveProdServ
from app.sat.models.lco import LRFC

from django.contrib.auth.models import User
from app.sat.models.cfdi import RegimenFiscal 

from app.users.decorators import has_group, has_groups
from app.core.logs import MESSAGES_LOGS

from app.invoicing.forms import (
  InvoiceForm, 
  ProdServForm, 
  ReceiverForm
)

from os import urandom
from pdb import set_trace
from decimal import Decimal
from datetime import datetime
from dateutil.relativedelta import relativedelta
#from celery.task.control import revoke
from ublinvoice.celery import app
from app.core.catalogs import USE_CFDI

import unidecode

from app.sat.utils.connector import SATConnector

from .utils.catalogos import COUNTRY_CODE, UNIT_CODE, CURRENCY_ID, LIST_ID, TAX_CATEGORY_CODE, STANDARD_ITEM_SCHEME
from django.utils.translation import ugettext as _
from app.peppol.models import *
from app.core.models import SatFile

RECEIVER_STATUS = {
  True: '<span class="label label-success">Activo</span>',
  False: '<span class="label label-danger">Suspendido</span>',
}

INVOICE_TYPE = {
  'I': '<span class="label label-success">Ingreso</span>',
  'E': '<span class="label label-warning">Egreso</span>',
  'P': '<span class="label label-default">Pago</span>',
  'T': '<span class="label label-danger">Traslado</span>',
  'N': u'<span class="label label-info">Nómina</span>',
}

def get_celery_status():
  apply_async = False
  try:
    celery_control = app.control
    inspect = celery_control.inspect()
    stats = inspect.stats()
    if stats:
      apply_async = True
  except IOError as e:
    from errno import errorcode
    msg = "Error connecting to the backend: " + str(e)
    if len(e.args) > 0 and errorcode.get(e.args[0]) == 'ECONNREFUSED':
      msg += ' Check that the RabbitMQ/Redis server is running.'
    apply_async = False
  return apply_async and settings.APPLY_ASYNC


@require_http_methods(['GET', 'POST'])
@login_required(login_url='/')
@has_groups(['clients', 'billing'], False)
@get_default_business
# @able_to_invoice
def new_invoice(request, *args, **kwargs):
  template = 'invoicing/new-invoice.html'
  context = {}
  business = kwargs['business']
  certificate = kwargs.get('sat_file', None)
  sat_file = SatFile.objects.filter(business_id=business.id, default=True).last()
  has_certificate = True if sat_file else False
  if request.method == 'POST':
    context = post_invoice(request, business)
    return JsonResponse(
      context
    )
  elif request.method == 'GET':
    context = get_context(request, business, certificate)
  context['has_certificate'] = has_certificate
  print("Context")
  print(context)
  return TemplateResponse(request, template, context) 

@require_http_methods(['GET', 'POST'])
@login_required(login_url='/')
@has_groups(['clients', 'billing'], False)
@get_default_business
@able_to_invoice
def new_payment(request, *args, **kwargs):
  #set_trace()
  template = 'invoicing/new-invoice.html'
  context = {}
  business = kwargs['business']
  certificate = kwargs.get('sat_file', None)
  if request.method == 'POST':
    context = post_invoice(request, business, _type='payment')
    return JsonResponse(context)
  elif request.method == 'GET':
    context = get_context(request, business, certificate, _type='payment')
  return TemplateResponse(request, template, context)


@login_required(login_url='/')
@require_POST
@has_groups(['admins', 'clients', 'billings'], False)
@get_default_business
def stuffs(request, *args, **kwargs):
  from pdb import set_trace
  from app.sat.utils.validate import Catalogos
  from app.cfdi.utils.validate.adicionales import trunc, normal_round
  #set_trace()
  context = {}
  # set_trace()
  oper = request.POST.get('oper')
  prodserv = request.POST.get('prodserv', None)
  keyunit = request.POST.get('keyunit', None)
  identifier = request.POST.get('identifier', None)
  peppolkey = request.POST.get('peppolkey', None)
  quantity = 0.0
  
  if request.POST.get('quantity'):
    quantity = float(request.POST.get('quantity', 1.0))
  amount = Decimal(0.0)
  if request.POST.get('amount'):
    amount = Decimal(request.POST.get('amount', 1.0))
  feeorfee = Decimal(0.0)
  if request.POST.get('feeorfee'):
    feeorfee = Decimal(request.POST.get('feeorfee', 1.0))
  if request.POST.get('discount'):
    discount = Decimal(request.POST.get('discount'))
  try:
    business = kwargs['business']   
    if request.is_ajax():
      if oper == 'get-business-identifier':
        # Error caused in business "Variable declared before assigment"
        query = Q(business=business)
        if prodserv or identifier:
          if prodserv is not None:
            query = query.__and__(Q(item_classification_code__icontains=prodserv))
          elif identifier is not None:
            query = query.__and__(Q(standard_item_identifier__icontains=identifier))      
          context = list(ProdServ.objects.filter(query).values(
            code=F('item_classification_code'), 
            des=F('description'), 
            su=F('unit_code'), 
            iden=F('standard_item_identifier'), 
            price=F('unit_price')
          )[:10])
      elif oper == 'get-amount':
        try:
          amount = 0
          if identifier:
            unit_price = cache.get(identifier)
            prodserv_obj = ProdServ.objects.filter(business=business)
            if unit_price is None:
              if identifier:
                prodserv_obj = prodserv_obj.filter(standard_item_identifier__icontains=identifier).first()
              if prodserv:
                prodserv_obj = prodserv_obj.filter(item_classification_code__icontains=prodserv).first()
              unit_price = prodserv_obj.unit_price
              cache.set(identifier, unit_price)
            amount = trunc((quantity * unit_price), 6, False)
            Log.objects.log_action(request, 5, 'R', u'La cantidad obtenida es: {}'.format(str(amount)), 'I', "")
        except Exception as e:
          print(f'exception {e}')
        context = {'amount': amount}
      elif oper == 'get-receiver':
        taxpayer_id = request.POST.get('taxpayer_id', None)
        if taxpayer_id is not None:
          try:
            #receiver = Receiver.objects.filter(business=business, taxpayer_id__icontains=taxpayer_id, status=True)[:10]          
            receiver = Buyer.objects.filter(business=business, tax_idenfier_number__icontains=taxpayer_id)[:10]          
            context = list(receiver.values('tax_idenfier_number', 'company_name', 'organization_id', 'country'))
          except Exception as e:
            print(str(e))
      elif oper == 'get-prodserv':
        context = []
        if len(prodserv) >= 4:
          for code, description in PRODSERV.items():
            if prodserv is not None and prodserv in code:
              context.append({
                'code': code, 
                'des': '{} - {}'.format(code, description)
              })
        Log.objects.log_action(request, 5, 'R', MESSAGES_LOGS.get('mensaje27').get(settings.DEFAULT_LANGUAGE_CODE).format(str(ProdServ.objects.all().count())), 'I', '')
      elif oper == 'get-keyunit':
        context = []
        if len(keyunit) >= 2:
          for code, description in CLAVEUNIDAD.items():
            if keyunit is not None and keyunit in code:
              context.append({
                'code': code, 
                'des': '{} - {}'.format(code, description)
              })
      elif oper == 'get-tax':
        total_tax = Decimal(0.0)
        #if feeorfee > Decimal(0.0):
        #  total_tax = trunc((amount * feeorfee), 6, False)
        #context = {'total_tax': total_tax}
        # if feeorfee > Decimal(0.0) and discount <= Decimal(0.0):
        #   total_tax = trunc(((feeorfee * amount)/100), 6, False)
        if feeorfee > Decimal(0.0):
          amount_wd = Decimal(trunc((amount-discount), 6, False))
          total_tax = trunc(((feeorfee * amount_wd)/100), 6, False)
          print("amount "+str(amount))
          print("discount "+str(discount))
          print("feeorfee "+str(feeorfee))
          print("amount_wd "+str(amount_wd))
          print("total_tax "+str(total_tax))
        context = {'total_tax': trunc(total_tax, 6, False)}
      elif oper == 'get-country':
        clave = request.POST.get('clave', None)
        from app.sat.models.cfdi import Pais
        countries = Pais.objects.filter(clave__icontains=clave)
        context = list(countries.values('clave', 'descripcion', 'rit'))
      elif oper == 'get-currency':
        from app.sat.models.cfdi import Moneda
        clave = request.POST.get('clave', None)
        currencies = Moneda.objects.filter(clave__icontains=clave).filter(inicio__lte=datetime.now()).filter(Q(fin__gte=datetime.now()) | Q(fin=None))
        context = list(currencies.values('clave', 'descripcion', 'tipo_cambio'))
      elif oper == 'get-payment-name':
        from app.peppol.models import UNCL4461
        code = request.POST.get('code', None)
        payment_names = UNCL4461.objects.filter(code__icontains=code)
        context = list(payment_names.values('code', 'name'))
      elif oper == 'get-cp':
        from app.sat.models.cfdi import CodigoPostal
        clave = request.POST.get('clave', None)
        cp = CodigoPostal.objects.filter(clave__icontains=clave).filter(inicio__lte=datetime.now()).filter(Q(fin__gte=datetime.now()) | Q(fin=None))[:5]
        context = list(cp.values('clave', 'estado'))
      elif oper == 'get-serial':
        from .models import InvoicingSerial
        from sequences import get_last_value
        serial = request.POST.get('serial', None)
        serials = InvoicingSerial.objects.filter(business=business, is_active=True, sequence__name__icontains=f'{business.taxpayer_id}-{serial}')
        serials_list = []
        for serial in serials:
          serials_list.append({
            'serial': serial.sequence.name.replace(f'{business.taxpayer_id}-', ''),
            'folio': get_last_value(serial.sequence.name)
          })
        context = serials_list
      elif oper == 'get-peppol-catalogue':
        CATALOGUES = {'ISO3166': ISO3166, 'UNECEREC20': UNECEREC20, 'ISO4217': ISO4217, 'UNCL7143': UNCL7143, 'ICD': ICD, 'UNCL5305': UNCL5305}
        modelo = CATALOGUES[request.POST.get('catalogue')]

        context = []
        if len(peppolkey) >= 1:
          values = modelo.objects.filter(code__icontains=peppolkey)
          for value in values:
            context.append({
              'id': value.code,
              'text': '{}-{}'.format(value.code, value.name)
            })
      elif oper == 'get-uuid':
        import uuid
        context = []
        uuid_ = str(uuid.uuid4()).upper() 
        context.append({
          'uuid': uuid_
        })
  except Exception as ex:
    print("Exception in stuffs => " + str(ex))
    #MESSAGES_LOGS.get('mensaje11').get(settings.DEFAULT_LANGUAGE_CODE)
    Log.objects.log_action(request, 2, 'R', MESSAGES_LOGS.get('mensaje28').get(settings.DEFAULT_LANGUAGE_CODE), 'I', "Exception in stuffs => " + str(ex))
  return JsonResponse(
    context, safe=False
  )


@login_required(login_url='/')
@require_POST
@has_groups(['admins', 'clients', 'billings'], False)
def calculate_amounts(request, *args, **kwargs):
  context = [{}]
  subtotal = Decimal(0.0)
  oper = request.POST.get('oper')
  from app.sat.utils.validate import Catalogos
  from app.cfdi.utils.validate.adicionales import trunc, normal_round
  if request.is_ajax():
    if oper == 'get-subtotal':
      #from pdb import set_trace
      # set_trace()
      subtotal_amounts = list(filter(None, request.POST.getlist('amounts[]', [])))
      subtotal_discounts = list(filter(None, request.POST.getlist('discounts[]', [])))
      subtotal_tras = list(filter(None, request.POST.getlist('taxes[tax][Traslado][]', [])))
      subtotal_ret = list(filter(None, request.POST.getlist('taxes[tax][Retencion][]', [])))
      subtotal_taxes = list(filter(None, request.POST.getlist('taxes[tax][undefined][]', [])))
      currency = request.POST.get('currency', 'MXN')
      catalogos_obj = Catalogos(datetime.now())
      currency_obj = catalogos_obj.obtener('Moneda', currency)
      decimales = currency_obj.decimales

      discount_trunc = Decimal(0.0)
      subtotal_trunc = Decimal(0.0)
      subtotal_ret_trunc = Decimal(0.0)
      subtotal_tras_trunc = Decimal(0.0)
      subtotal_taxes_trunc = Decimal(0.0)
      
      if subtotal_amounts:
        subtotal_cal = sum(map(Decimal, subtotal_amounts))
        subtotal_trunc = normal_round(subtotal_cal, decimales)
      if subtotal_discounts:
        discount_cal = sum(map(Decimal, subtotal_discounts))
        discount_trunc = trunc(discount_cal, decimales)
      if subtotal_tras:
        subtotal_tras_cal = sum(map(Decimal, subtotal_tras))
        subtotal_tras_trunc = trunc(subtotal_tras_cal, decimales, True)
      if subtotal_ret:
        subtotal_ret_cal = sum(map(Decimal, subtotal_ret))
        subtotal_ret_trunc = trunc(subtotal_ret_cal, decimales, True)
      if subtotal_taxes:
        subtotal_taxes = sum(map(Decimal, subtotal_taxes))
        subtotal_taxes_trunc = trunc(subtotal_taxes, decimales, True)

      context = {
        'discount': discount_trunc,
        'subtotal': subtotal_trunc,
        'ret': subtotal_ret_trunc,
        'tras': subtotal_tras_trunc,
        'ret_display': subtotal_ret_trunc,
        'subtotal_taxes_trunc': subtotal_taxes_trunc,
        'tras_display': subtotal_tras_trunc,
        'discount_display': discount_trunc,
        'subtotal_display': subtotal_trunc,
      }
    elif oper == 'get-total':

      currency = request.POST.get('currency', 'MXN')

      catalogos_obj = Catalogos(datetime.now())
      currency_obj = catalogos_obj.obtener('Moneda', currency)

      decimales = currency_obj.decimales

      zero = Decimal(0.0)
      
      amounts = request.POST.get('amounts', zero)
      discounts = request.POST.get('discounts', zero)
      total_ret = request.POST.get('totalRet', zero)
      total_tras = request.POST.get('totalTras', zero)
      
      total_calc = Decimal(amounts)
      if discounts:
        total_calc -= Decimal(discounts)
      if total_tras:
        total_calc += Decimal(total_tras)
      if total_ret:
        total_calc -= Decimal(total_ret)
      
      total_trunc = trunc(total_calc, decimales)
      total_letter = numero_a_letras(total_trunc)

      context = {
        'total': total_trunc,
        'total_display': total_trunc,
        'total_letter': total_letter,
      }
  return JsonResponse(
    context, safe=False
  )


@require_http_methods(['GET', 'POST'])
@login_required(login_url='/')
@has_groups(['admins', 'clients', 'billings'], False)
@get_default_business
@get_query_invoicing
def invoices(request, *args, **kwargs):
  context = {}
  user = request.user
  business = kwargs.get('business', None)
  template = 'invoicing/invoices.html'

  datatable = {
    'aaData' : [],
    'iTotalRecords': 0,
    'iTotalDisplayRecords': 0,
  }

  oper = request.POST.get('oper')
  log_message = ''
  if request.method == 'POST':
    if request.is_ajax():
      if oper == 'list-invoices':
        invoices_list = []
        invoices_append = invoices_list.append

        role = request.user.profile.role

        query = kwargs['query']
        start = int(request.POST.get('iDisplayStart'))
        length = int(request.POST.get('iDisplayLength'))
        #set_trace()
        invoices = Invoice.objects.filter(query).order_by('-id')
        total = invoices.count()
        invoices = invoices[start:start+length]
        invoice_status = dict(INVOICE_STATUS)
        for invoice in invoices:
          status = render_to_string(
            'invoicing/strings/invoice-status.html', {
            'status': invoice.status,
            'error_messages': invoice.error_messages,
            }
          )

          options = render_to_string(
            'invoicing/strings/invoice-options.html', {
              'id': invoice.encrypt,
              'status': invoice.status,
              'uuid': invoice.uuid,
              'role': role,
            }
          )
          
          invoices_append([
            '',
            invoice.taxpayer_id,
            #invoice.name,
            invoice.rtaxpayer_id,
            invoice.rname,
            invoice.uuid,
            # INVOICE_TYPE[invoice.type],
            invoice.total,
            invoice.emission_date,
            # status,
            options
          ])
        if role != 'A':
            for i in invoices_list:
              del i[1]
        
        datatable.update(
          aaData=invoices_list,
          iTotalRecords=total,
          iTotalDisplayRecords=total,
        )
        #log_message= MESSAGES_LOGS.get('mensaje29').get(settings.DEFAULT_LANGUAGE_CODE)
        Log.objects.log_action(request, 5, 'R', MESSAGES_LOGS.get('mensaje29').get(settings.DEFAULT_LANGUAGE_CODE) , 'I', '')
        return JsonResponse(datatable)
      # if oper == 'restamp-invoice':
      #   try:
      #     invoice_obj = None
      #     enc_invoice_id = request.POST.get('invoice', None)
      #     if enc_invoice_id:
      #       invoice_id = Invoice.decrypt_id(enc_invoice_id)
      #       invoice_obj = Invoice.objects.get(id=invoice_id, taxpayer_id=business.taxpayer_id)
      #       if invoice_obj:
      #         last_day_to_stamp = invoice_obj.emission_date + relativedelta(days=+3)
      #         today = datetime.now()
      #         if today > last_day_to_stamp:
      #           invoice_obj.status = 'E'
      #           invoice_obj.error_messages = {
      #             'error': '402',
      #             'incident': u'Fecha y hora de generación fuera de rango.',
      #             'extra_info': u'El comprobante no se timbro durante los 3 primeros dias de su generación.'
      #           }
      #           Log.objects.log_action(request, 5, 'C', u'Fecha y hora de generación fuera de rango.', 'I')
      #           invoice_obj.save()

      #           context.update({
      #             'success': False,
      #             'message': invoice_obj.error_messages['extra_info']
      #           })

      #         # Si factura no esta en E. Error, P. Processed, F. Finished o C Cancelled
      #         # la factura se reporcesara
      #         elif invoice_obj.status not in ('E', 'F', 'C'):
      #           apply_async = get_celery_status()
      #           #if False and settings.APPLY_ASYNC:
      #           if apply_async:
      #             task_id = stamp_process.apply_async(args=(invoice_obj.xml, invoice_obj.id))
      #             invoice_obj.task_id = task_id
      #             invoice_obj.save()
      #           else:
      #             stamp_process(invoice_obj.xml, invoice_obj.id)
      #           context.update({
      #             'success': True,
      #             'message': u'Se realizó la solicitud con éxito, por favor espere.'
      #           })
      #           Log.objects.log_action(request, 5, 'C', u'{}'.format(context['message']), 'I')
      #       else:
      #         context.update({
      #           'success': False,
      #           'message': u'No se pudo obtener información de la factura a re-timbrar.'
      #         })
      #     else:
      #       context.update({
      #         'success': False,
      #         'message': u'No hay suficiente información para procesar el re-timbrado.'
      #       })

      #     Log.objects.log_action(request, 5, 'C',"{}".format(context['message']), 'I')
      #   except Exception as e:
      #     folio = urandom(6).encode('base64').strip().replace('=', '')
      #     print('{}: Exception on restamp-invoice method => {}'.format(folio, e))
      #     context.update({
      #       'success': False,
      #       'message': u'{}: Hubo un error procesando su petición.'.format(folio)
      #     })
      
      if oper == 'cancel-invoice':
        try:
          enc_invoice_id = request.POST.get('invoice', None)
          notes = request.POST.get('notes', None)
          if enc_invoice_id:
            taxpayer_id = business.taxpayer_id
            csd = business.get_csd()
            if csd['serial'] is not None:
              serial = csd['serial']
              invoice_id = Invoice.decrypt_id(enc_invoice_id)
              invoice_obj = Invoice.objects.get(id = invoice_id, taxpayer_id = taxpayer_id)
              uuid = invoice_obj.uuid
              result = cancelar_sat([uuid], taxpayer_id, csd['cer'], csd['key'])
              if result[0]['success']:
                invoice_obj.status = 'P'
                invoice_obj.status_sat = 'C'
                invoice_obj.save()
                context.update({
                  'success': True,
                  'message': _('Cancellation request made successfully.')
                })
                Log.objects.log_action(request, 5, 'U',MESSAGES_LOGS.get('mensaje30').get(settings.DEFAULT_LANGUAGE_CODE).format(uuid), 'I', '')
              else:
                context.update({
                  'success': False,
                  'message': _('There was an error in the request, please try again later.')
                })
                Log.objects.log_action(request, 5, 'U',"{}".format(context['message']), 'I', '')
            else:
              context.update({
                'success': False,
                'message': _('The issuer does not have active certificates to perform the cancellation.')
              })
              Log.objects.log_action(request, 5, 'U',"{}-{}".format(context['message'], taxpayer_id), 'I', '')
          else:
            context.update({
              'success': False,
              'message': _('There is not enough information to process the cancellation.')
            })
          Log.objects.log_action(request, 5, 'U',"{}".format(context['message']), 'I', '')
        except Exception as e:
          import base64
          folio =  base64.encodestring(bytes(bytearray(urandom(6)))).strip().replace(b'=', b'').decode()
          print('{}: Exception on cancel-invoice method => {}'.format(folio, e))
          context.update({
            'success': False,
            'message': u'{}: Hubo un error procesando su petición.'.format(folio)
          })
          Log.objects.log_action(request, 5, 'U',"{}".format(context['message']), 'I', '{}: Exception on cancel-invoice method => {}'.format(folio, e))
      if oper == 'update-status':
        invoice_obj = None
        enc_invoice_id = request.POST.get('invoice', None)
        if enc_invoice_id:
          invoice_id = Invoice.decrypt_id(enc_invoice_id)
          invoice_obj = Invoice.objects.get(id=invoice_id, taxpayer_id=business.taxpayer_id)
          sat_query = invoice_obj.get_sat_query(as_dict=True)
          if invoice_obj and sat_query:            
            result = consultar_sat(**sat_query)
            if result['success']:
              invoice_status = 'F' if result['estado'] == 'Vigente' else 'C' if result['estado'] == 'Cancelado' else None
              if invoice_status is not None:
                invoice_obj.status = invoice_status
                invoice_obj.save()
                context.update({
                  'success': True,
                  'message': _('The invoice voucher status was updated successfully.')
                })
              else:
                context.update({
                  'success': False,
                  'message': _('Your invoice was not found, please try again.')
                })
            else:
              context.update({
                'success': False,
                'message': _('It is not possible to obtain the invoice status, please try again later.')
              })
          else:
            context.update({
              'success': False,
              'message': _('Invoice not found.')
            })
        else:
          context.update({
            'success': False,
            'message': _('There is not enough information to obtain the status of the invoice.')
           })
        Log.objects.log_action(request, 5, 'U',"{}-{}-invoice_id: {}".format(context['message'], invoice_obj.taxpayer_id, invoice_id), 'I', '')
      if oper == 'stop-cancellation':
        invoice_obj = None
        enc_invoice_id = request.POST.get('invoice', None)
        if enc_invoice_id:
          invoice_id = Invoice.decrypt_id(enc_invoice_id)
          invoice_obj = Invoice.objects.get(id=invoice_id, taxpayer_id=business.taxpayer_id)
          task_id = invoice_obj.task_id
          if invoice_obj and task_id:
            celery_control = app.control
            celery_control.revoke(task_id, terminate=True)
            invoice_obj.status = 'A'
            invoice_obj.save()
            context.update({
              'success': True,
              'message': _('You have been asked to stop the cancellation, the process may not stop.')
            })
          else:
            context.update({
              'success': False,
              'message': _('The cancellation process cannot be denied.')
            })  
        else:
          context.update({
            'success': False,
            'message': _('There is not enough information to obtain the status of the invoice.')
           })
        Log.objects.log_action(request, 5, 'U',"{} invoice id {}".format(context['message'], invoice_id), 'I', '')
      if oper == 'send-invoice-email':
        from django.core.mail import EmailMessage
        emails = request.POST.get('emails').split(',')
        is_pdf = True if request.POST.get('pdf_check') else False
        is_xml = True if request.POST.get('xml_check') else False
        uuid = request.POST.get('invoice')

        invoice = Invoice.objects.get(uuid=uuid)
        sender = Business.objects.filter(users=request.user).last()
        
        success = False
        message = ''
        if is_pdf or is_xml:
          try:
            subject = 'Envío de CFDI'
            email_message = render_to_string('invoicing/strings/send-invoice-email.html', {
              'sender': sender.name if sender else request.user.username,
              'uuid': invoice.uuid,
            })
            msg = EmailMessage(
              subject,
              email_message,
              to=emails
            )
            msg.content_subtype = 'html'
            if is_xml:
              msg.attach_file(invoice._xml.path)
            if is_pdf:
              filename = '{}.pdf'.format(invoice.uuid)
              creator = CreatePDF_(invoice.xml, filename)
              if creator.success:
                msg.attach_file(creator.pdf_path)
            msg.send()
            success = True
            message = _('Invoice sent to the selected emails.')
          except Exception as e:
            print(str(e))
            message = _('Error sending invoice')
        else:
          message = _('You must select a format')  
        context = {'success': success, 'message': message}
    return JsonResponse(context)
  elif request.method == 'GET':
    oper = resolve(request.path_info).url_name
    if oper == 'download_xml':
      uuid = kwargs['uuid']
      if True or (request.user.has_group('emision') or request.user.has_group('admins')): 
        invoice = Invoice.objects.get(uuid=uuid)
      else:
        return HttpResponseForbidden()
      filename = '{}.xml'.format(invoice.uuid)
      xml = invoice.xml
      response = HttpResponse(xml, content_type='application/xml text/xml')
      response['Content-Disposition'] = 'attachment; filename=%s' % filename
      Log.objects.log_action(request, 5, 'R',MESSAGES_LOGS.get('mensaje31').get(settings.DEFAULT_LANGUAGE_CODE).format(filename), 'D', '')
      return response
    if oper == 'download_pdf':
      uuid = kwargs['uuid']
      notes = ''
      iva_pdf = 0.00
      subtotal_precalculated = 0.00
      if True or(request.user.has_group('emision') or request.user.has_group('admins')):
        invoice = Invoice.objects.get(uuid=uuid)
      else:
        return HttpResponseForbidden()
      xml = invoice.xml
      iva_pdf = invoice.total_tra
      subtotal_precalculated = invoice.subtotal
      filename = '{}.pdf'.format(invoice.uuid)
      creator = CreatePDF_(xml, filename)
      #pdf_obj = CreatePDF(xml, filename, invoice.status,  invoice.internal_notes)
      if creator.success:
        pdf_content = open(creator.pdf_path, 'rb')
        if pdf_content is not None:
          response = HttpResponse(pdf_content, content_type='application/pdf')
          response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
          Log.objects.log_action(request, 5, 'R', MESSAGES_LOGS.get('mensaje32').get(settings.DEFAULT_LANGUAGE_CODE).format(filename), 'D', '')
          return response
    template_base = 'base_providers.html' if request.user.profile.role in ('P', ) else 'base.html'
    context.update({
      'template_base': template_base
    })
  return TemplateResponse(request, template, context) 


@require_http_methods(['GET', 'POST'])
@login_required(login_url='/')
@has_groups(['admins', 'clients', 'billing'], False)
@get_default_business
@get_query_invoicing
def receivers(request, *args, **kwargs):
  context = {}
  user = request.user
  business = kwargs.get('business', None)
  template = 'invoicing/receivers.html'

  datatable = {
    'aaData' : [],
    'iTotalRecords': 0,
    'iTotalDisplayRecords': 0,
  }
  # list_use_cfdi = list(USE_CFDI)
  # print(list_use_cfdi[0][0])
  context.update({
    'list_use_cfdi': list(UsoCFDI.objects.all().values('clave', 'descripcion'))
    })

  #set_trace()
  print(template)
  if request.method == 'POST':
    if request.is_ajax():
      oper = request.POST.get('oper')
      if oper == 'list-receivers':
        receiver_list = []
        receiver_append = receiver_list.append
        role = request.user.profile.role
        query = kwargs['query']
        start = int(request.POST.get('iDisplayStart', 1))
        length = int(request.POST.get('iDisplayLength', 10))
        #receivers = Receiver.objects.filter(query).order_by('-id')
        receivers = Buyer.objects.filter(query).order_by('-id')
        total = receivers.count()
        receivers = receivers[start:start+length]
        
        for receiver in receivers:
          #emails = render_to_string('invoicing/strings/receiver-emails.html', {'emails': receiver.emails}, request)
          emails = render_to_string('invoicing/strings/receiver-emails.html', {'emails': receiver.email_contact}, request)
          #options = render_to_string('invoicing/strings/receiver-options.html', {'receiver': receiver, 'role': role}, request)
          options = render_to_string('invoicing/strings/receiver-options.html', {'receiver': receiver, 'role': role}, request)
          owner = receiver.business.users.last()
          receiver_append([
            '',
            #receiver.taxpayer_id,
            receiver.tax_idenfier_number,
            #receiver.name,
            receiver.company_name,
            '<button title="Detalles del Propietario" owner="%s" class="btn btn-xs btn-warning btn-details-owner"><b>%s</b></button>' % (owner.id, owner.username),
            #'<span class="label label-default"> %s </span>' % receiver.use_cfdi,
            emails,
            #RECEIVER_STATUS[receiver.status],
            #receiver.organization_id,
            options
          ])
        if role != 'A':
            for i in receiver_list:
              del i[3]
        datatable.update(
          aaData=receiver_list,
          iTotalRecords=total,
          iTotalDisplayRecords=total,
        )
        Log.objects.log_action(request, 5, 'R', MESSAGES_LOGS.get('mensaje33').get(settings.DEFAULT_LANGUAGE_CODE), 'I', '')
        return JsonResponse(datatable)
      elif oper == 'add-receiver':
        
        addreceiverform = ReceiverForm(request.POST)
        if addreceiverform.is_valid():
          try:
            use_cfdi_exists = UsoCFDI.objects.filter(clave=request.POST.get('use_cfdi')).exists()
            if not use_cfdi_exists:
              return JsonResponse({'success': False, 'errors': { 'error': [u'La clave de Uso CFDI es inválida'] }})
            receiver = addreceiverform.save(commit=False)
            receiver.business = business
            
            general_rfc = ['XEXX010101000', 'XAXX010101000']
            taxpayer_exists = LRFC.objects.filter(rfc=receiver.taxpayer_id)
            try:
              if taxpayer_exists.count() > 0 or receiver.taxpayer_id in general_rfc:
                context.update({
                  'success': True,
                  'message': _('Business added correctly')
                })
                Log.objects.log_action(request, 2, 'C',"{} - {}".format(context['message'], receiver.name), 'I', '')
                receiver.save()
              else:
                context.update({
                  'success': False,
                  'errors': {
                    'error': ['No se puede registrar el Receptor, el RFC {} no se encuentra en la BD, por favor agregue un RFC valido'.format(receiver.taxpayer_id)]
                  }
                })
                Log.objects.log_action(request, 2, 'C', MESSAGES_LOGS.get('mensaje34').get(settings.DEFAULT_LANGUAGE_CODE).format(receiver.taxpayer_id), 'I', '')
            except Exception as e:
               context.update({
                  'success': False,
                  'errors': {
                    'error': ['No es posible agregar el receptor, el RFC ya cuenta con un registro previo'.format(e)]
                  }
                })
               Log.objects.log_action(request, 2, 'C',"{}".format(context['errors']['error']), 'I', context['errors']['error'])
            # Log.objects.log_action(request, 2, 'C',"{}".format(context['message']), 'I', '')
          except IntegrityError as e:
            context.update({
              'success': False,
              'message': 'Producto/Servicio duplicado'
            })
          except Exception as e:
            context.update({
              'success': False,
              'message': _(u'Registration is not possible, please try again later.')
            })
            Log.objects.log_action(request, 2, 'C',"{}".format(context['message']), 'I', u'Exception in add-receiver => {}'.format(str(e)))
          # Log.objects.log_action(request, 5, 'C',"{}".format(context['message']), 'I', '')
        else:
          context.update({
            'success': False,
            'errors': addreceiverform.errors
          })
      elif oper == 'add-buyer':
        #import pdb; pdb.set_trace()
        #addreceiverform = ReceiverForm(request.POST)
        #if addreceiverform.is_valid():
        try:
          identifier_number = request.POST.get('identifier_number')
          organizacion_id = request.POST.get('organizacion_id')
          custom_name = request.POST.get('custom_name')
          address_name = request.POST.get('address_name')
          city_name = request.POST.get('city_name')
          id_province = request.POST.get('id_province')
          postal_zone = request.POST.get('postal_zone')
          # id_country = request.POST.get('id_country')
          id_language = request.POST.get('id_language')
          id_currency = request.POST.get('id_currency')
          id_full_name = request.POST.get('id_full_name')
          id_department = request.POST.get('id_department')
          id_email = request.POST.get('id_email')
          id_telephone = request.POST.get('id_telephone')
          id_web = request.POST.get('id_web')
          id_category = request.POST.get('id_category')
          id_method = request.POST.get('id_method')
          payment_method = request.POST.get('payment_method')
          term = request.POST.get('term')

          buyer_obj, created = Buyer.objects.get_or_create(business= business, 
            tax_idenfier_number = identifier_number, 
            organization_id = organizacion_id,
            company_name=custom_name, 
            address_name=address_name, 
            city_name=city_name, 
            province = id_province,
            postal_zone=postal_zone, 
            # country=id_country,
            language=id_language, 
            currency=id_currency, 
            full_name=id_full_name, 
            department=id_department,
            email_contact=id_email,  
            telephone_contact=id_telephone, 
            web=id_web,
            category=id_category,
            method_category=id_method,
            payment_method=payment_method,
            term=term)

          buyer_obj.save()
          context.update({
            'success': True,
            'message': _('Registered buyer correctly')
          })
          #if not use_cfdi_exists:
          #  return JsonResponse({'success': False, 'errors': { 'error': [u'La clave de Uso CFDI es inválida'] }})
          #receiver = addreceiverform.save(commit=False)
          #receiver.business = business
          #
          #general_rfc = ['XEXX010101000', 'XAXX010101000']
          #taxpayer_exists = LRFC.objects.filter(rfc=receiver.taxpayer_id)
          #try:
          #  if taxpayer_exists.count() > 0 or receiver.taxpayer_id in general_rfc:
          #    context.update({
          #      'success': True,
          #      'message': 'Receptor agregado correctamente'
          #    })
          #    Log.objects.log_action(request, 2, 'C',"{} - {}".format(context['message'], receiver.name), 'I', '')
          #    receiver.save()
          #  else:
          #    context.update({
          #      'success': False,
          #      'errors': {
          #        'error': ['No se puede registrar el Receptor, el RFC {} no se encuentra en la BD, por favor agregue un RFC valido'.format(receiver.taxpayer_id)]
          #      }
          #    })
          #    Log.objects.log_action(request, 2, 'C','No se puede registrar el Receptor, el RFC {} no se encuentra en la BD, por favor agregue un RFC valido'.format(receiver.taxpayer_id), 'I', '')
          #except Exception as e:
          #  context.update({
          #    'success': False,
          #    'errors': {
          #      'error': ['No es posible agregar el receptor, el RFC ya cuenta con un registro previo'.format(e)]
          #    }
          #  })
          #  Log.objects.log_action(request, 2, 'C',"{}".format(context['errors']['error']), 'I', context['errors']['error'])
          # Log.objects.log_action(request, 2, 'C',"{}".format(context['message']), 'I', '')
        except IntegrityError as e:
          context.update({
            'success': False,
            'message': 'Producto/Servicio duplicado'
          })
        except Exception as e:
          context.update({
            'success': False,
            'message': _('Registration is not possible, please try again later.')
          })
          Log.objects.log_action(request, 2, 'C',"{}".format(context['message']), 'I', u'Exception in add-receiver => {}'.format(str(e)))
        # Log.objects.log_action(request, 5, 'C',"{}".format(context['message']), 'I', '')
        #else:
        #  context.update({
        #    'success': False,
        #    'errors': addreceiverform.errors
        #  })
      elif oper == 'edit-buyer':
        #import pdb; pdb.set_trace()
        #addreceiverform = ReceiverForm(request.POST)
        #if addreceiverform.is_valid():
        try:
          buyer_id = request.POST.get('receiver_id')
          buyer_name_edit = request.POST.get('buyer_name_edit')
          identifier_number_edit = request.POST.get('identifier_number_edit')
          organizacion_id_edit = request.POST.get('organizacion_id_edit')
          buyer_emails_edit = request.POST.get('buyer_emails_edit')
          buyer_telephone_edit = request.POST.get('buyer_telephone_edit')
          buyer_address_name_edit = request.POST.get('buyer_address_name_edit')
          buyer_city_name_edit = request.POST.get('buyer_city_name_edit')
          # buyer_country_edit = request.POST.get('buyer_country_edit')
          
          buyer_edit_obj = Buyer.objects.get(id=buyer_id)

          buyer_edit_obj.company_name = buyer_name_edit
          buyer_edit_obj.tax_idenfier_number = identifier_number_edit
          buyer_edit_obj.organization_id = organizacion_id_edit
          buyer_edit_obj.email_contact = buyer_emails_edit
          buyer_edit_obj.telephone_contact = buyer_telephone_edit
          buyer_edit_obj.address_name = buyer_address_name_edit
          buyer_edit_obj.city_name = buyer_city_name_edit
          # buyer_edit_obj.country = buyer_country_edit

          buyer_edit_obj.save()
          context.update({
            'success': True,
            'message': _('Buyer successfully edited')
          })
          #if not use_cfdi_exists:
          #  return JsonResponse({'success': False, 'errors': { 'error': [u'La clave de Uso CFDI es inválida'] }})
          #receiver = addreceiverform.save(commit=False)
          #receiver.business = business
          #
          #general_rfc = ['XEXX010101000', 'XAXX010101000']
          #taxpayer_exists = LRFC.objects.filter(rfc=receiver.taxpayer_id)
          #try:
          #  if taxpayer_exists.count() > 0 or receiver.taxpayer_id in general_rfc:
          #    context.update({
          #      'success': True,
          #      'message': 'Receptor agregado correctamente'
          #    })
          #    Log.objects.log_action(request, 2, 'C',"{} - {}".format(context['message'], receiver.name), 'I', '')
          #    receiver.save()
          #  else:
          #    context.update({
          #      'success': False,
          #      'errors': {
          #        'error': ['No se puede registrar el Receptor, el RFC {} no se encuentra en la BD, por favor agregue un RFC valido'.format(receiver.taxpayer_id)]
          #      }
          #    })
          #    Log.objects.log_action(request, 2, 'C','No se puede registrar el Receptor, el RFC {} no se encuentra en la BD, por favor agregue un RFC valido'.format(receiver.taxpayer_id), 'I', '')
          #except Exception as e:
          #  context.update({
          #    'success': False,
          #    'errors': {
          #      'error': ['No es posible agregar el receptor, el RFC ya cuenta con un registro previo'.format(e)]
          #    }
          #  })
          #  Log.objects.log_action(request, 2, 'C',"{}".format(context['errors']['error']), 'I', context['errors']['error'])
          # Log.objects.log_action(request, 2, 'C',"{}".format(context['message']), 'I', '')
        except IntegrityError as e:
          context.update({
            'success': False,
            'message': 'Producto/Servicio duplicado'
          })
        except Exception as e:
          context.update({
            'success': False,
            'message': _('Registration is not possible, please try again later.')
          })
          Log.objects.log_action(request, 2, 'C',"{}".format(context['message']), 'I', u'Exception in add-receiver => {}'.format(str(e)))
        # Log.objects.log_action(request, 5, 'C',"{}".format(context['message']), 'I', '')
        #else:
        #  context.update({
        #    'success': False,
        #    'errors': addreceiverform.errors
        #  })
      elif oper == 'activate-receiver':
        receiver_encr = request.POST.get('receiver') 
        receiver_obj = Receiver.objects.get_encrypted(receiver_encr)
        if receiver_obj:
          receiver_obj.status = (not receiver_obj.status)
          receiver_obj.save()
          message = ('activo', '') if receiver_obj.status else ('suspendio', u'¡Importante!, es posible que no pueda emitir factura a este Receptor.')
          context.update({
            'success': True,
            'message': u'Se {} correctamente. {}'.format(*message)
          })
          Log.objects.log_action(request, 5, 'C',"{} {}".format(context['message'], receiver_obj.name), 'I', '')
        else:
          context.update({
            'success': False,
            'message': u'No se pudo obtener información del receptor.'
          })
          Log.objects.log_action(request, 5, 'C',"{} {}".format(context['message'], receiver_obj.name), 'I', '')
      elif oper == 'get-info-edit':
        receiver_encr = request.POST.get('receiver')
        #receiver_obj = Receiver.objects.get_encrypted(receiver_encr)
        receiver_obj = Buyer.objects.get_encrypted(receiver_encr)
        if receiver_obj:
          context.update({
            'success': True,
            'receivers-info':{
              'buyer_name': receiver_obj.company_name,
              'identifier_number': receiver_obj.tax_idenfier_number,
              'organizacion_id': receiver_obj.organization_id,
              'buyer_emails': receiver_obj.email_contact,
              'id_telephone': receiver_obj.telephone_contact,
              'address_name': receiver_obj.address_name,
              'city_name': receiver_obj.city_name,
              # 'id_country': receiver_obj.country,
              'receiver_last_modified': receiver_obj.modified.strftime('%Y-%m-%d %H:%M:%S'),
              'receiver_id': receiver_obj.id,
              #'use_cfdi_values': list(uses_cfdi),
              #'receiver_use_cfdi_val': receiver_obj.use_cfdi
            }
            })
        else:
          context.update({
            'success':False,
            'message': _('It was not possible to obtain the information of this buyer.')
            })
      elif oper == 'get-info-details':
        #set_trace()
        receiver_encr = request.POST.get('receiver')
        receiver_obj = Buyer.objects.get_encrypted(receiver_encr)
        if receiver_obj:
          context.update({
            'success': True,
            'receivers-info':{
              'identifier_number': receiver_obj.tax_idenfier_number,
              'organizacion_id': receiver_obj.organization_id,
              'custom_name': receiver_obj.company_name,
              'address_name': receiver_obj.address_name,
              'city_name': receiver_obj.city_name,
              'id_province': receiver_obj.province,
              'postal_zone': receiver_obj.postal_zone,
              # 'id_country': receiver_obj.country,
              'id_language': receiver_obj.language,
              'id_currency': receiver_obj.currency,
              'id_full_name': receiver_obj.full_name,
              'id_department': receiver_obj.department,
              'id_email': receiver_obj.email_contact,
              'id_telephone': receiver_obj.telephone_contact,
              'id_web': receiver_obj.web,
              'id_category': receiver_obj.category,
              'id_method': receiver_obj.method_category,
              'payment_method': receiver_obj.payment_method,
              'term': receiver_obj.term,
            }
            })
        else:
          context.update({
            'success':False,
            'message': _('It was not possible to obtain the information of this buyer.')
            })
      #elif oper == 'get-info-details':
      #  receiver_encr = request.POST.get('receiver')
      #  receiver_obj = Receiver.objects.get_encrypted(receiver_encr)
      #  if receiver_obj:
      #    uses_cfdi = UsoCFDI.objects.all().values('clave', 'descripcion')
      #    receiver_use_cfdi = UsoCFDI.objects.get(clave=receiver_obj.use_cfdi)
      #    status = {True:'Activo', False:'Suspendido'}
      #    context.update({
      #      'success': True,
      #      'receivers-info':{
      #        'receiver_name': receiver_obj.name,
      #        'receiver_taxpayer_id': receiver_obj.taxpayer_id,
      #        'receiver_use_cfdi': "{} - {}".format(receiver_obj.use_cfdi,receiver_use_cfdi.descripcion),
      #        'receiver_emails': receiver_obj.emails,
      #        'receiver_status': status[receiver_obj.status],
      #        'receiver_last_modified': receiver_obj.modified.strftime('%Y-%m-%d %H:%M:%S'),
      #        'receiver_id': receiver_obj.id,
      #        'use_cfdi_values': list(uses_cfdi),
      #        'receiver_use_cfdi_val': receiver_obj.use_cfdi
      #      }
      #      })
      #  else:
      #    context.update({
      #      'success':False,
      #      'message':u'No fue posible obtener la informacion de este receptor'
      #      })
          #Log.objects.log_action(request, 5, 'C',"{} {}".format(context['message'], receiver.taxpayer_id), 'I', '')
      elif oper == 'edit-receiver':
        try:          
          id_object = int(request.POST.get('receiver_id_val'))
          receiver_obj = Receiver.objects.get(id=id_object)
          use_cfdi = request.POST.get('receiver_use_cfdi');
          receiver_status = request.POST.get('receiver_status')
          status = {"Suspendido":False, "Activo":True}
          status_undefined = True if receiver_status == "undefined" else False
          use_cfdi_not_undefined = True if use_cfdi != "undefined" else False

          if receiver_obj:
            receiver_obj.name = request.POST.get('receiver_name_val')
            receiver_obj.emails = list(request.POST.get('receiver_emails_val').split(','))
            if not status_undefined:
              receiver_obj.status = status[receiver_status]
            if use_cfdi_not_undefined:
              receiver_obj.use_cfdi = use_cfdi
            # receiver_obj.use_cfdi = use_cfdi
            receiver_obj.save()
            context.update({
              'success': True,
              'message': u'Informacion del receptor actualizada correctamente!'
              })
            Log.objects.log_action(request, 5, "U", "{} - {}".format(context['message'], receiver_obj.taxpayer_id), 'I', '')
          else:
            context.update({
              'success': False,
              'message': u'No fue posible actualizar la informacion del receptor, intente mas tarde!'
              })
            Log.objects.log_action(request, 5, "U", "{} - {}".format(context['message'], receiver_obj.taxpayer_id), 'I', '')
        except Exception as ex:
          print("Exception in edit receiver => {}".format(str(ex)))
          Log.objects.log_action(request, 2, 'U', u'Ocurrió una excepcion al momento de editar la información del receptor', 'I', "Exception in edit receiver => {}".format(str(ex)))
      elif oper == 'get-usecfdi':
        context = []
        use_cfdi = request.POST.get('usecfdi', '')
        taxpayer_id = request.POST.get('taxpayer_id', '')

        data_use_cfdi = UsoCFDI.objects.none()

        if len(taxpayer_id) == 13:
          data_use_cfdi = UsoCFDI.objects.filter(fisica__in=['Sí', 'Si'], clave__icontains=use_cfdi)
        elif len(taxpayer_id) == 12:
          data_use_cfdi = UsoCFDI.objects.filter(moral__in=['Sí', 'Si'], clave__icontains=use_cfdi)
        elif 'select' in request.POST and request.POST.get('select') == 'filter':
          data_use_cfdi = UsoCFDI.objects.filter(clave__icontains=use_cfdi)

        if len(use_cfdi) >= 1:
          for duc in data_use_cfdi:
            descripcion = unidecode.unidecode(duc.descripcion)
            context.append({
              'code': duc.clave, 
              'desc': '{} - {}'.format(duc.clave, descripcion)
            })
        return JsonResponse({'data': context})
      elif oper == 'get-owner-details':
        try:
          owner = request.POST.get('owner')
          data_owner = []
          info_owner = User.objects.get(id=owner)
          #from pdb import set_trace; set_trace();
          business = Business.objects.get(users=info_owner)
          reg_fiscal = RegimenFiscal.objects.get(clave=business.fiscal_regime)
          data_owner.append({ 'taxpayer_id': business.taxpayer_id, 'email': info_owner.username, 'name': '%s %s' % (info_owner.first_name, info_owner.last_name), 'reg_fiscal': '{} - {}'.format(reg_fiscal.clave, reg_fiscal.descripcion), 'status': RECEIVER_STATUS[info_owner.is_active]})
          context.update({ 'success': True, 'values': data_owner})
        except Exception as e:
          print(str(e))
          context.update({'Error al extraer los datos del propietario'})
    return JsonResponse(context)
  elif request.method == 'GET':
    template_base = 'base_providers.html' if request.user.profile.role in ('P', ) else 'base.html'
    addreceiverform = ReceiverForm()
    print(kwargs)
    context.update({
      'addreceiverform': addreceiverform,
      'template_base': template_base,
      'total_business': Business.objects.all().count()
    })
  return TemplateResponse(request, template, context)


@require_http_methods(['GET', 'POST'])
@login_required(login_url='/')
@has_groups(['admins', 'clients', 'billing'], False)
@get_default_business
@get_query_invoicing
def prodservs(request, *args, **kwargs):
  user = request.user
  business = kwargs.get('business', None)
  template = 'invoicing/prodservs.html'
  import re
  re_description = re.compile('[^|]{1,1000}')
  re_unit = re.compile('[^|]{1,20}')
  re_no_identification = re.compile('[^|]{1,100}')

  context = {}
  datatable = {
    'aaData' : [],
    'iTotalRecords': 0,
    'iTotalDisplayRecords': 0,
  }

  if request.method == 'POST':
    if request.is_ajax():
      oper = request.POST.get('oper', None)
      if oper == 'list-prodserv':
        prodserv_list = []
        prodserv_append = prodserv_list.append
        #set_trace()
        query = kwargs['query']
        start = int(request.POST.get('iDisplayStart'))
        length = int(request.POST.get('iDisplayLength'))
        
        prodservs = ProdServ.objects.filter(query).order_by('-id')
        total = prodservs.count()
        prodservs = prodservs[start:start+length]
        for prodserv in prodservs:
          identifier = render_to_string(
            'invoicing/strings/prodserv-label.html', 
            {'ltype': 'success', 'description': prodserv.item_classification_code}
          
          )
          unit_code = render_to_string(
            'invoicing/strings/prodserv-label.html',
            {'ltype': 'info', 'description': prodserv.unit_code, 'title': UNECEREC20.objects.get(code=prodserv.unit_code).name}
            )
          pprodserv = render_to_string(
            'invoicing/strings/prodserv-label.html', 
            {'ltype': 'info', 'description': prodserv.name}
          
          )
          options = render_to_string(
            'invoicing/strings/prodserv-options.html', 
            {'id': prodserv.encrypt}
          
          )

          len_decimales = len(str(prodserv.unit_price).rstrip('0').split('.')[1])

          if len_decimales > 1:
            new_unit_price = prodserv.unit_price 
          else:
            new_unit_price = str(prodserv.unit_price) + '0'
          
          prodserv_append([
            '',
            identifier,
            pprodserv,
            unit_code,
            prodserv.description,
            new_unit_price,
            options
          ])
        datatable.update(
          aaData = prodserv_list,
          iTotalRecords = total,
          iTotalDisplayRecords = total,
        )
        #
        log_message = MESSAGES_LOGS.get('mensaje35').get(settings.DEFAULT_LANGUAGE_CODE)
        Log.objects.log_action(request, 5, 'R', log_message, 'I', '')
        return JsonResponse(datatable)
      elif oper == 'add-prodserv':
        success, message = True, ''

        item_name = request.POST.get('item_name')
        pryce_item = float(request.POST.get('pryce_item'))
        unit_code = request.POST.get('unit_code')
        item_classification_code = request.POST.get('item_classification_code')
        list_id = request.POST.get('list_id')
        prodserv_description = request.POST.get('prodserv_description')
        tax_category_code = request.POST.get('tax_category_code')
        try:
          tax_percent = float(request.POST.get('tax_percent'))
        except:
          tax_percent = None
        standard_item_identifier = request.POST.get('standard_item_identifier')
        standard_item_scheme = request.POST.get('standard_item_scheme')
        
        try:
          prodserv = ProdServ(
            business=business,
            name=item_name,
            description=prodserv_description,
            unit_code=unit_code,
            list_id=list_id,
            unit_price=pryce_item,
            item_classification_code=item_classification_code,
            standard_item_identifier=standard_item_identifier,
            standard_item_scheme=standard_item_scheme,
          )
          if (tax_percent is not None and tax_category_code in ['Z', 'E', 'AE', 'K', 'G']
           and tax_category_code != ''):
            if tax_category_code in ['Z', 'E', 'AE', 'K', 'G'] and tax_percent == 0 and tax_percent is not None:
              prodserv.tax_category_code = tax_category_code
              prodserv.tax_percent = tax_percent
              prodserv.save()

              success = True
              message = _(u'Product/Service successfully registered')

            elif tax_category_code in ['Z', 'E', 'AE', 'K', 'G'] and tax_percent > 0 and tax_percent is not None:
              error = 'BR-{}-05'.format(tax_category_code)
              success = False
              message = _('When the category code is equal to Z, E, AE, K or G, the rate of the article must be equal to 0')
          else:
            if tax_category_code in ['L', 'M'] and tax_percent is not None:
              prodserv.tax_category_code = tax_category_code
              prodserv.tax_percent = tax_percent
              prodserv.save()

              success = True
              message = _(u'Product/Service successfully registered')
            
            elif tax_category_code in ['L', 'M'] and tax_percent is None:
              success = False
              message = _('When the category code is equal to L or M, the VAT rate of the invoiced item will be 0 (zero) or greater than zero.')
            else:
              prodserv.save()

              success = True
              message = MESSAGES_LOGS.get('mensaje36').get(settings.DEFAULT_LANGUAGE_CODE)
              #message = _(u'Product/Service successfully registered')
              Log.objects.log_action(request, 5, 'U', message, 'I', '')

          translate_message = message
          context.update({
            'success': success,
            'message': translate_message
          })
          Log.objects.log_action(request, 5, 'C', "{} - id: {}".format(context['message'], prodserv.id), 'I', '')
        except IntegrityError as ie:
          print(ie)
          message = MESSAGES_LOGS.get('mensaje37').get(settings.DEFAULT_LANGUAGE_CODE)
          #message = _('Duplicate Product/Service')
          context.update({
            'success': False,
            'message': message
          })
          Log.objects.log_action(request, 2, 'C', message, 'I', 'Exception in Product/Service => {}'.format(ie))
        except Exception as e:
          print('Exception in add-prodserv | {}'.format(e))
          log_message = MESSAGES_LOGS.get('mensaje38').get(settings.DEFAULT_LANGUAGE_CODE)
          #log_message = _('An exception occurred when registering the product/service')
          Log.objects.log_action(request, 2, 'C', log_message, 'I', u'Exception in add-prodserv => {}'.format(str(e)))
          context.update({
            'success': False,
            'message': 'The Product/Service could not be registered, please try again later.'
          })
        Log.objects.log_action(request, 5, 'C', message, 'I', '')
      elif oper == 'get-prodserv':
        product_enc = request.POST.get('product', None)
        product_id = ProdServ.decrypt_id(product_enc)
        if product_id:
          product_obj = ProdServ.objects.get(id=product_id)
          standard_item_scheme = {}
          tax_category_code = {'id': '', 'full_name': ''}

          unit_code = {
            'id': product_obj.unit_code,
            'full_name': '{}-{}'.format(product_obj.unit_code, UNECEREC20.objects.get(code=product_obj.unit_code).name)
          }
          list_id = {
            'id': product_obj.list_id,
            'full_name': '{}-{}'.format(product_obj.list_id, UNCL7143.objects.get(code=product_obj.list_id).name)
          }
          if product_obj.tax_category_code != '':
            tax_category_code = {
              'id': product_obj.tax_category_code,
              'full_name': '{}-{}'.format(product_obj.tax_category_code, UNCL5305.objects.get(code=product_obj.tax_category_code).name)
            }
          # set_trace()
          if product_obj.standard_item_scheme != "":
            standard_item_scheme = {
              'id': product_obj.standard_item_scheme,
              'full_name': '{}-{}'.format(product_obj.standard_item_scheme, ICD.objects.get(code=product_obj.standard_item_scheme).name)
            }

          context.update({
            'success': True,
            'unit_code': unit_code,
            'list_id': list_id,
            'tax_category_code': tax_category_code,
            'standard_item_scheme': standard_item_scheme,
            'info':{
              'item_name': product_obj.name,
              'prodserv_description': product_obj.description,
              'pryce_item': product_obj.unit_price,
              'item_classification_code': product_obj.item_classification_code,
              'tax_percent': product_obj.tax_percent,
              'standard_item_identifier': product_obj.standard_item_identifier
            }
          })
      elif oper == 'edit-prodserv':
        #set_trace()
        item_classification_code = request.POST.get('item_classification_code')
        prodserv_obj = ProdServ.objects.get(business=business, 
        item_classification_code=item_classification_code)
        success, txt_message = True, ''

        if prodserv_obj:
          description = request.POST.get('prodserv_description')
          unit_code = request.POST.get('unit_code')

          prodserv_obj.name = request.POST.get('item_name')
          prodserv_obj.description = description
          prodserv_obj.unit_code = unit_code
          
          origin_country = request.POST.get('origin_country')
          tax_category_code = request.POST.get('tax_category_code')
          try:
            tax_percent = float(request.POST.get('tax_percent'))
          except:
            tax_percent = None

          prodserv_obj.unit_price = request.POST.get('pryce_item')
          prodserv_obj.list_id = request.POST.get('list_id')
          prodserv_obj.standard_item_identifier = request.POST.get('standard_item_identifier')
          prodserv_obj.standard_item_scheme = request.POST.get('standard_item_scheme')
          # prodserv_obj.origin_country = origin_country
          
          if (tax_percent is not None and tax_category_code in ['Z', 'E', 'AE', 'K', 'G']
           and tax_category_code != ''):
            if tax_category_code in ['Z', 'E', 'AE', 'K', 'G'] and tax_percent == 0:
              prodserv_obj.tax_category_code = tax_category_code
              prodserv_obj.tax_percent = tax_percent
              prodserv_obj.save()
              success = True
              message = _(u'Product/Service successfully edited')
            elif tax_category_code in ['Z', 'E', 'AE', 'K', 'G'] and tax_percent > 0:
              error = 'BR-{}-05'.format(tax_category_code)
              success = False
              message = _('When the category code is equal to Z, E, AE, K or G, the rate of the article must be equal to 0')
          else:
            if tax_category_code in ['L', 'M'] and tax_percent is not None:
              prodserv_obj.tax_category_code = tax_category_code
              prodserv_obj.tax_percent = tax_percent
              prodserv_obj.save()

              success = True
              message = MESSAGES_LOGS.get('mensaje39').get(settings.DEFAULT_LANGUAGE_CODE)
              #message = _(u'Product/Service successfully edited')
              Log.objects.log_action(request, 5, 'U', message, 'I', '')
            elif tax_category_code in ['L', 'M'] and tax_percent is None:
              success = False
              message = _('When the category code is equal to L or M, the VAT rate of the invoiced item will be 0 (zero) or greater than zero.')
            else:
              prodserv_obj.save()
              success = True
              message = _(u'Product/Service successfully edited')
          #prodserv_obj.save()
          context.update({
                'success': success,
                'message': message
              })
        else:
          message = MESSAGES_LOGS.get('mensaje40').get(settings.DEFAULT_LANGUAGE_CODE)
          #message = _('Could not get product or service information.')
          context.update({
            'success': False,
            'message': message
          })
          Log.objects.log_action(request, 5, 'R', message, 'I', '')
    return JsonResponse(context)
  elif request.method == 'GET':
    addprodservform = ProdServForm()
    template_base = 'base_providers.html' if request.user.profile.role in ('P', ) else 'base.html'
    business_id = kwargs.get('business', None).id
    total_prodserv = ProdServ.objects.filter(business_id=business_id).count()
    context.update({
      'addprodservform': addprodservform,
      'template_base': template_base,
      'total_prodserv': total_prodserv
    })
  return TemplateResponse(request, template, context) 


@require_http_methods(['POST'])
@login_required(login_url='/')
@has_groups(['admins', 'clients', 'billings'], False)
@get_default_business
def download(request, *args, **kwargs):
  import zipfile
  from io import BytesIO
  user = request.user
  invoice = request.POST.get('invoice')
  business = kwargs['business']
  #set_trace()
  try:
    invoice_id = Invoice.decrypt_id(invoice)
    invoice_obj = Invoice.objects.get(id=invoice_id, taxpayer_id=business.taxpayer_id)
    if invoice_obj:
      xml = invoice_obj.xml
      uuid = invoice_obj.uuid
      byteszip = BytesIO()
      # response = HttpResponse(xml, content_type='application/octet-stream', status=201)
      # response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
      # Log.objects.log_action(request, 5, 'R', "Respuesta {} en descarga de archivo".format(response), 'I', '')
      #   response = HttpResponse(pdf_content, content_type='application/octet-stream', status=201)
      #   response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
      # else:
      #   response = HttpResponse(u'No se pudo procesar su petición (PDF).', status=403) 
      zf = zipfile.ZipFile(byteszip, mode='a', compression=zipfile.ZIP_DEFLATED)
      filename_xml = '{}.xml'.format(uuid)
      zf.writestr(filename_xml, xml)
        
      notes = ''
      iva_pdf = invoice_obj.total_tra
      filename_pdf = '{}.pdf'.format(uuid)
      subtotal_precalculated = invoice_obj.subtotal
      
      filename = '{}.pdf'.format(invoice_obj.uuid)
      creator = CreatePDF_(invoice_obj.xml, filename)
      if creator.success:
        test2 = open(creator.pdf_path, 'rb')
        test2.seek(0)
        pdf_content = test2.read()
        print(creator.pdf_path)
        if pdf_content is not None:
          zf.writestr(filename_pdf, pdf_content)

      for _file in zf.filelist:
        _file.create_system = 0
        
      # with open('/tmp/test.zip', 'wb') as writer:
      #   writer.write(byteszip.getvalue())
      zf.close()
      byteszip.seek(0)
      response = HttpResponse(content_type='application/zip', status=201)
      response['Content-Disposition'] = 'attachment; filename={}.zip'.format(uuid)
      response['Content-Type'] = 'application/zip'
      response['Download-Filename'] = '{}.zip'.format(uuid)
      response.write(byteszip.read())
          # Log.objects.log_action(request, 5, 'R', u'No se pudo obtener el archivo PDF', 'I')
      # Log.objects.log_action(request, 5, 'R', "Respuesta {} en descarga de archivo".format(response), 'I')
    else:
      response = HttpResponse('Su comprobante no puede ser procesado en este momento, intente más tarde.', status=403)
  except Exception as e:
    response = HttpResponse('Hubo un error al procesar la solicitud, contacte a soporte.', status=403)
    # Log.objects.log_action(request, 2, 'R', u'Hubo un error al procesar la solicitud', 'I', u'Exception in invoicing-download => {}'.format(str(e)))
  
  return response

