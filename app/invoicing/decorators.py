# -*- encoding: UTF-8 -*-
from django.db.models import Q
from app.core.decorators import get_default_business
from app.core.models import Log

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from pdb import set_trace

def get_query_invoicing(function):
  @get_default_business
  def wrap(request, *args, **kwargs):
    # set_trace()
    query = Q()
    if request.method == 'POST':
      if request.is_ajax():
        oper = request.POST.get('oper')
        now = datetime.now().replace(day=1).date()
        if oper == 'list-invoices':
          now = datetime.now().replace(day=1).date()
          if request.user.profile.role == 'C':
            if 'business' in kwargs and kwargs['business']:
              query = Q(
                taxpayer_id=kwargs['business'].taxpayer_id
              )
            else:
              from django.http import HttpResponseForbidden
              return HttpResponseForbidden()
          if 'uuid' in request.POST:
            query = query.__and__(
              Q(uuid=request.POST.get('uuid'))
            )
          if 'date_from' in request.POST and 'date_to' in request.POST:
            date_from = request.POST.get('date_from')
            date_from = datetime.strptime(date_from, '%d-%m-%Y').strftime('%Y-%m-%d') if date_from else None
            date_to = request.POST.get('date_to')
            date_to = datetime.strptime(date_to, '%d-%m-%Y').strftime('%Y-%m-%d') if date_to else None
            if date_to and date_from:
              query = query.__and__(Q(emission_date__gte=date_from) & Q(emission_date__lte=date_to))
            elif date_from:
              query = query.__and__(Q(emission_date__gte=date_from))
            elif date_to:
              query = query.__and__(Q(emission_date__lte=date_to))
          else:
            current_month = Q(emission_date__gte=now) &  Q(emission_date__lte=(now + relativedelta(months=1)))
            query = query.__and__(current_month)
          if 'receiver' in request.POST:
            query = query.__and__(Q(rtaxpayer_id__icontains=request.POST.get('receiver')) | Q(taxpayer_id__icontains=request.POST.get('receiver')))
          #if 'owner' in request.POST:
          #  query = query.__and__(Q(taxpayer_id__icontains=request.POST.get('owner')))
          #if 'status' in request.POST:
          #  #query = query.__and__(Q(status_sat=request.POST.get('status')) | Q(status=request.POST.get('status')))
          #  query = query.__and__(Q(status_sat=request.POST.get('status')))
          if 'legal_schemeID' in request.POST:
            query = query.__and__(Q(legal_schemeID=request.POST.get('legal_schemeID')))
          if request.POST.get('type') is not '':
            query = query.__and__(Q(type=request.POST.get('type')))
        elif oper == 'list-receivers':
          #set_trace()
          if request.user.profile.role == 'C':
            if 'business' in kwargs and kwargs['business']:
              query = Q(business= kwargs.get('business', None))
            #else:
            #  from django.http import HttpResponseForbidden
            #  return HttpResponseForbidden()
          elif request.user.profile.role not in ('A', 'S', 'B'):
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden()
          elif request.user.profile.role == 'A':
            query = Q()
          if 'taxpayer_id' in request.POST:
            query = query.__and__(Q(taxpayer_id__contains=str(request.POST.get('taxpayer_id')).upper()))
          if 'owner_filter' in request.POST:
            query = query.__and__(Q(business__users__username__icontains=request.POST.get('owner_filter')))
          #if 'status' in request.POST:
          #  query = query.__and__(Q(status=bool(eval(request.POST.get('status')))))
          if 'identifier_number' in request.POST:
            query = query.__and__(Q(tax_idenfier_number__icontains=request.POST.get('identifier_number')))
          if 'organizacion_id' in request.POST:
            query = query.__and__(Q(organization_id=request.POST.get('organizacion_id')))
          if 'emails' in request.POST:
            query = query.__and__(Q(email_contact__icontains=request.POST.get('emails')) | Q(business__users__username__icontains=request.POST.get('emails')))
          if 'name' in request.POST:
            query = query.__and__(Q(company_name__istartswith=request.POST.get('name')) | Q(company_name__icontains=request.POST.get('name')))
          if 'date-from' in request.POST and 'date-to' in request.POST:
            date_from = request.POST.get('date-from')
            date_from = datetime.strptime(date_from, '%d %B %Y').strftime('%Y-%m-%d') if date_from else None
            date_to = request.POST.get('date-to')
            date_to = datetime.strptime(date_to, '%d %B %Y') + timedelta(days=1)
            date_to = date_to.strftime('%Y-%m-%d') if date_to else None
            if date_from and date_to:
              query = query.__and__(Q(modified__gte=date_from) & Q(modified__lte=date_to))
            elif date_from:
              query = query.__and__(Q(modified__gte=date_from))
            elif date_to:
              query = query.__and__(Q(modified__lte=date_to))
            else:
              current_month = Q(modified__gte=now) &  Q(modified__lte=(now + relativedelta(months=1)))
              query = query.__and__(current_month)
        elif oper == 'list-prodserv':
          if request.user.profile.role == 'C':
            if 'business' in kwargs and kwargs['business']:
              query = Q(
                business=kwargs['business'].id
              )
            else:
              from django.http import HttpResponseForbidden
              return HttpResponseForbidden()
          languaje = request.POST.get('language')
          if 'prodserv' in request.POST:
            query = query.__and__(Q(name__startswith=request.POST.get('prodserv')))
          if 'clasification_code_filter' in request.POST:
            query = query.__and__(Q(item_classification_code__icontains=request.POST.get('clasification_code_filter')))
          if 'description' in request.POST:
            query = query.__and__(Q(description__istartswith=request.POST.get('description')) | Q(description__icontains=request.POST.get('description')))
          if 'unit_code' in request.POST:
            query = query.__and__(Q(unit_code__contains=str(request.POST.get('unit_code')).upper()))
          if 'date-from' in request.POST and 'date-to' in request.POST:
            #from pdb import set_trace; set_trace()
            date_from = request.POST.get('date-from')
            date_to = request.POST.get('date-to')
            # if languaje == 'es':
            date_from = datetime.strptime(date_from, '%d-%m-%Y').strftime('%Y-%m-%d') if date_from else None
            date_to = datetime.strptime(date_to, '%d-%m-%Y').strftime('%Y-%m-%d') if date_to else None
            # elif languaje == 'en':
            #   date_from = datetime.strptime(date_from, '%d %b %Y').strftime('%Y-%m-%d') if date_from else None
            #   date_to = datetime.strptime(date_to, '%d %b %Y') + timedelta(days=1)
            # date_to = date_to.strftime('%Y-%m-%d') if date_to else None
            if date_from and date_to:
              query = query.__and__(Q(creation_date__gte=date_from) & Q(creation_date__lte=date_to))
            elif date_from:
              query = query.__and__(Q(creation_date__gte=date_from))
            elif date_to:
              query = query.__and__(Q(creation_date__lte=date_to))
            else:
              current_month = Q(creation_date__gte=now) &  Q(creation_Date__lte=(now + relativedelta(months=1)))
              query = query.__and__(current_month)   
    kwargs.update({'query': query})
    return function(request, *args, **kwargs)
  return wrap