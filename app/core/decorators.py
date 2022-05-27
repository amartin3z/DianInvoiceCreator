# -*- coding: UTF-8 -*-

from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .models import Business
from app.core.models import Log
from app.core.models import SatFile
from app.invoicing.models import Receiver, ProdServ
from datetime import datetime
#import locale
from pdb import set_trace
from psycopg2  import sql

def get_default_business(function):
  def wrap(request, *args, **kwargs):
    #set_trace()
    user = request.user
    business = None
    try:
      if not user.is_anonymous:
        if user.profile.role not in ('A', 'G'):
          if user.business_set.exists():
            business_id = request.session.get('business_id', None)
            if business_id is not None:
              business = Business.objects.get(id=business_id)
            else:
              business = user.business_set.last()
            request.session['business_id'] = business.id
      kwargs['business'] = business
      # raise Exception('E')
    except Exception as e:
      print(f'Exception on get_default_business {e}')
      if not user.is_anonymous:
        if user.profile.role == 'C':
          return redirect('profile')
    return function(request, *args, **kwargs)
  return wrap


def able_to_invoice(function):
  def wrap(request, *args, **kwargs):
    # set_trace()
    business = kwargs.get('business', None)
    try:
      try:
        kwargs['sat_file'] = SatFile.objects.get(business=business, status='A', certificate_type='C', default=True)
      except SatFile.DoesNotExist:
        kwargs['sat_file'] = SatFile.objects.filter(business=business, certificate_type='C', status='A').last()
        assert kwargs['sat_file'], 'No tiene configurados CSD'
    except Exception as e:
      return redirect('profile')

    #try:
    #  assert Receiver.objects.filter(business=business).exists(), 'No tiene clientes registrados'
    #except Exception as e:
    #  return redirect('list-receivers')

    #try:
    #  assert ProdServ.objects.filter(business=business).exists(), 'No tiene productos registrados'
    #except:
    #  return redirect('list-prodservs')
    
    try:
      assert business.address.zipcode, 'No cuenta con un codigo postal'
    except:
      return redirect('profile')
    
    return function(request, *args, **kwargs)
  return wrap

def get_query_branch(function):
  @get_default_business
  def wrap(request, *args, **kwargs):
    try:
      query = Q()
      if request.method == 'POST' and request.is_ajax():
        #set_trace()
        business = kwargs['business']
        query = query.__and__(Q(business_id=business.id))
        search = request.POST.get('search[value]')
        if 'search[value]' in request.POST and request.POST.get('search[value]') != '':
          query = query.__and__(Q(name__icontains=search) | Q(state__icontains=search) | Q(municipality__icontains=search) | Q(neighborhood__icontains=search) | Q(zipcode__icontains=search))
        if 'branch_filter' in request.POST and request.POST.get('branch_filter') != '':
          query = query.__and__(Q(name__icontains=request.POST.get('branch_filter')))
        if 'state_filter' in request.POST and request.POST.get('state_filter') != '':
          query = query.__and__(Q(state__icontains=request.POST.get('state_filter')))
        if 'zipcode_filter' in request.POST and request.POST.get('zipcode_filter') != '':
          query = query.__and__(Q(zipcode__icontains=request.POST.get('zipcode_filter'))) 
        return function(request, query)
      else:
        template = 'business/branch.html'
        context = {
        }
        return TemplateResponse(request, template, context)  
    except Exception as e:
      print("Exception get_query_branch() | {}".format(e))
  return wrap

def get_query_branch_location(function):
  @get_default_business
  def wrap(request, *args, **kwargs):
    try:
      query = Q()
      if request.method == 'POST' and request.is_ajax():
        business = kwargs['business']
        query = query.__and__(Q(business_id=business.id)) 
        return function(request, query)
      else:
        template = 'business/branch.html'
        context = {
        }
        return TemplateResponse(request, template, context)  
    except Exception as e:
      print("Exception get_query_branch() | {}".format(e))
  return wrap  

def get_query_logs(function):
  #locale.setlocale(locale.LC_ALL, 'es_MX.utf8')
  
  @get_default_business
  def wrap(request, *args, **kwargs):
    template = 'core/logs.html'
    context = {}

    try:
      if request.method == 'POST' and request.is_ajax():
        business = kwargs.get('business', None)
        oper = request.POST.get('oper')
        query = Q(user__is_superuser=False)
        if request.is_ajax() and oper == 'list-logs':
          if 'log_admin' in request.POST and request.user.is_superuser:
            #query = Q(user__is_superuser=False, business=business)
            #query = Q(user__is_superuser=False)
            query = Q()
          if 'exception-logs' in request.POST:
            query = query.__and__(~Q(err_exception=""))
            Log.objects.log_action(request, 5, 'R', u'Se filtraron los registros de la bitácora mediante el filtro "Excepción"', 'L', "")
          if 'date_from' in request.POST and 'date_to' in request.POST:
            date_from = request.POST.get('date_from')
            date_from = datetime.strptime(date_from, '%d-%m-%Y').strftime('%Y-%m-%d') if date_from else None
            date_to = request.POST.get('date_to')
            date_to = datetime.strptime(date_to, '%d-%m-%Y').strftime('%Y-%m-%d') if date_to else None              
            query = query.__and__(Q(timestamp__range=[date_from, date_to]))
            Log.objects.log_action(request, 5, 'R', u'Se filtraron los registros de la bitácora mediante los filtros de fecha de creación', 'L', '')  
          else:
            date_to = datetime.now()
            date_from = datetime(date_to.year, date_to.month, 1)
            query = query.__and__(Q(timestamp__range=[date_from, date_to]))
          if 'user' in request.POST:
            user = request.POST.get('user')
            query = query.__and__(Q(user__username__icontains=user))
            Log.objects.log_action(request, 5, 'R', u'Se filtraron los registros de la bitácora mediante el filtro "Usuario"', 'L', '')
          if 'action' in request.POST:
            action = request.POST.get('action')
            query = query.__and__(Q(action=action))
            Log.objects.log_action(request, 5, 'R', u'Se filtraron los registros de la bitácora mediante el filtro "Acción"', 'L', '')
          if 'module' in request.POST:
            module = request.POST.get('module')
            query = query.__and__(Q(module=module))
            Log.objects.log_action(request, 5, 'R', u'Se filtraron los registros de la bitácora mediante el filtro "Módulo"', 'L', '')
        return function(request, query, *args, **kwargs)
      else:
        return TemplateResponse(request, template, context)
    except Exception as e:
      print("Exception get_query_logs | {}".format(e))

  return wrap

def get_query_conciliacion(function):
  @get_default_business
  def wrap(request, *args, **kwargs):
    #set_trace()
    try:
      query = Q()
      if request.method == 'POST' and request.is_ajax():
        business = kwargs['business']
        
        if 'date_from' in request.POST and 'date_to' in request.POST:
          date_from = request.POST.get('date_from')
          date_from = datetime.strptime(date_from, '%d %B %Y').strftime('%Y-%m-%d') if date_from else None
          date_to = request.POST.get('date_to')
          date_to = datetime.strptime(date_to, '%d %B %Y').strftime('%Y-%m-%d') if date_to else None              
          query = query.__and__(Q(emission_date__range=[date_from, date_to]))
        if 'uuid' in request.POST:
          query = query.__and__(Q(uuid=request.POST.get('uuid')))
        return function(request, query)
      else:
        template = 'core/conciliacion.html'
        return TemplateResponse(request, template)
    except Exception as e:
      print("Exception get_query_conciliacion() | {}".format(e))
  return wrap

from dateutil.relativedelta import relativedelta

def get_query_invoicing_sat(function):
  @get_default_business
  def wrap(request, *args, **kwargs):
    query = Q()
    #set_trace()
    if request.method == 'POST':
      if request.is_ajax():
        oper = request.POST.get('oper')
        if oper == 'list-invoices':

          now = datetime.now().replace(day=1).date()
          if 'uuid' in request.POST:
            query = query.__and__(
              Q(uuid=request.POST.get('uuid'))
            )
          if 'date-from' in request.POST and 'date-to':
            date_from = request.POST.get('date-from')
            date_from = datetime.strptime(date_from, '%d %B %Y').strftime('%Y-%m-%d 00:00:00') if date_from else None
            date_to = request.POST.get('date-to')
            date_to = datetime.strptime(date_to, '%d %B %Y').strftime('%Y-%m-%d 11:59:59') if date_to else None
            if date_to and date_from:
              query = query.__and__(Q(emission_date__gte=date_from) & Q(emission_date__lte=date_to))
            #if date_from:
            #  query = query.__and__(Q(emission_date__gte=date_from))
            #elif date_to:
            #  query = query.__and__(Q(emission_date__lte=date_to))
          else:
            current_month = Q(emission_date__gte=now) &  Q(emission_date__lte=(now + relativedelta(months=1)))
            query = query.__and__(current_month)
          if 'taxpayer_id' in request.POST:
            query = query.__and__(Q(rtaxpayer_id__icontains=request.POST.get('taxpayer_id')) | Q(taxpayer_id__icontains=request.POST.get('taxpayer_id')))
          if 'type_invoice' in  request.POST:
            query = query.__and__(Q(type=request.POST.get('type_invoice')))
          #if 'rtaxpayer_id' in request.POST:
          #  query = query.__and__(Q(rtaxpayer_id=request.POST.get('rtaxpayer_id')))
        elif oper == 'list-receivers':
          if 'identifier_number' in request.POST:
            query = query.__and__(Q(tax_idenfier_number=request.POST.get('identifier_number')))
          if 'organizacion_id' in request.POST:
            query = query.__and__(Q(organization_id=request.POST.get('organizacion_id')))
          if 'emails' in request.POST:
            query = query.__and__(Q(email_contact__icontains=request.POST.get('emails')) | Q(business__users__username__icontains=request.POST.get('emails')))
          if 'name' in request.POST:
            query = query.__and__(Q(company_name__istartswith=request.POST.get('name')) | Q(company_name__icontains=request.POST.get('name')))          
    kwargs.update({'query': query})
    return function(request, *args, **kwargs)
  return wrap



def get_report_sat(function):
  #@get_default_business
  def wrap(request, *args, **kwargs):
    #set_trace()
    if request.method == 'POST':
      if request.is_ajax():
        try:
          if eval(request.POST.get('get_report_sat', 'False')):
            where = []
            values = {}

            if 'uuid' in request.POST:
              uuid = request.POST.get('uuid')
              #where.append('status = {}'.format(sql.Identifier(str(status))))
              where.append(
                sql.SQL('{} = {}').format(
                  sql.Identifier('uuid'),
                  sql.Placeholder('uuid')
                )
              )
              values.update({
                'uuid': uuid,
              })
            if 'taxpayer_id' in request.POST:
              emisor = request.POST.get('taxpayer_id')
              #where.append('status = {}'.format(sql.Identifier(str(status))))
              where.append(
                sql.SQL('{} = {}').format(
                  sql.Identifier('taxpayer_id'),
                  sql.Placeholder('taxpayer_id')
                )
              )
              values.update({
                'taxpayer_id': emisor,
              })
            if 'rtaxpayer_id' in request.POST:
              receiver = request.POST.get('rtaxpayer_id')
              #where.append('status = {}'.format(sql.Identifier(str(status))))
              where.append(
                sql.SQL('{} = {}').format(
                  sql.Identifier('rtaxpayer_id'),
                  sql.Placeholder('rtaxpayer_id')
                )
              )
              values.update({
                'rtaxpayer_id': receiver,
              })
            if 'emission_date' in request.POST:
              emission_date = request.POST.get('emission_date')
              emission_date = datetime.strptime(emission_date,  '%d %B %Y').strftime('%Y-%m-%d')

              print (emission_date)
              #where.append('status = {}'.format(sql.Identifier(str(status))))
              where.append(
                sql.SQL('{}::varchar LIKE{}').format(sql.Identifier('emission_date'),sql.Placeholder('emission_date'))
              )
              values.update({
                'emission_date': emission_date + '%',
              })
            #print where
            query = sql.SQL("{}").format(
              sql.SQL(' AND ').join(where)
            )
            
            return function(request, query, values, *args, **kwargs)
        except Exception as e:
          print('An exception was occurred in get_report_sat function => {}'.format(str(e)))

        return HttpResponseForbidden()
  return wrap