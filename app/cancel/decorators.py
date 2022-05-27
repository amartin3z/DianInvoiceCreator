# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from django.template.response import TemplateResponse
from django.db.models import Q
from datetime import datetime
import locale
from pdb import set_trace


def get_query_list_cancellation_request(function):
  def wrap(request, **kwargs):
    try:
      if request.method == 'POST' and request.is_ajax():
        query = Q()
        if request.POST.get('oper') == 'list-cancel-emisor':
          if 'uuid' in request.POST:
            uuid = request.POST.get('uuid')
            query = query.__and__(Q(uuid=uuid))
          if 'date_from' in request.POST and 'date_to' in request.POST:
            date_from = request.POST.get('date_from')
            date_from = datetime.strptime(date_from, '%d %B %Y').strftime('%Y-%m-%d') if date_from else None
            date_to = request.POST.get('date_to')
            date_to = datetime.strptime(date_to, '%d %B %Y').strftime('%Y-%m-%d') if date_to else None
            if date_to and date_from:
              query = query.__and__(Q(date__range=[date_from, date_to]))
          if 'estado_sat' in request.POST:
            estado_sat = request.POST.get('estado_sat')
            query = query.__and__(Q(status_sat=estado_sat))
          if 'estatus_cancelacion' in request.POST:
            estatus_cancelacion = request.POST.get('estatus_cancelacion')
            query = query.__and__(Q(status=estatus_cancelacion))
          if 'taxpayer_id' in request.POST:
            taxpayer_id = request.POST.get('taxpayer_id')
            query = query.__and__(Q(taxpayer_id=taxpayer_id))
          if 'rtaxpayer_id' in request.POST:
            rtaxpayer_id = request.POST.get('rtaxpayer_id')
            query = query.__and__(Q(rtaxpayer_id=rtaxpayer_id))
          if 'invoice_type' in request.POST:
            invoice_type = request.POST.get('invoice_type')
            query = query.__and__(Q(invoice_type=invoice_type))
          if 'business' in kwargs:
            taxpayer_id = kwargs['business'].taxpayer_id
            query = query.__and__(Q(taxpayer_id=taxpayer_id))

        elif request.POST.get('oper') == 'list-cancel-receiver-pending':
          if 'uuid' in request.POST:
            uuid = request.POST.get('uuid')
            query = query.__and__(Q(uuid=uuid))
          if 'date_from' in request.POST and 'date_to' in request.POST:
            date_from = request.POST.get('date_from')
            date_from = datetime.strptime(date_from, '%d %B %Y').strftime('%Y-%m-%d') if date_from else None
            date_to = request.POST.get('date_to')
            date_to = datetime.strptime(date_to, '%d %B %Y').strftime('%Y-%m-%d') if date_to else None
            if date_to and date_from:
              query = query.__and__(Q(date__range=[date_from, date_to]))
          if 'taxpayer_id' in request.POST:
            taxpayer_id = request.POST.get('taxpayer_id')
            query = query.__and__(Q(taxpayer_id=taxpayer_id))
          if 'invoice_type' in request.POST:
            invoice_type = request.POST.get('invoice_type')
            query = query.__and__(Q(invoice_type=invoice_type))


        elif request.POST.get('oper') == 'list-cancel-receiver-finished':
          if 'uuid' in request.POST:
            uuid = request.POST.get('uuid')
            query = query.__and__(Q(uuid=uuid))
          if 'date_from' in request.POST and 'date_to' in request.POST:
            date_from = request.POST.get('date_from')
            date_from = datetime.strptime(date_from, '%d %B %Y').strftime('%Y-%m-%d') if date_from else None
            date_to = request.POST.get('date_to')
            date_to = datetime.strptime(date_to, '%d %B %Y').strftime('%Y-%m-%d') if date_to else None
            if date_to and date_from:
              query = query.__and__(Q(date__range=[date_from, date_to]))
          if 'answer' in request.POST:
            answer = request.POST.get('answer')
            query = query.__and__(Q(response=answer))
          if 'estado_sat' in request.POST:
            estado_sat = request.POST.get('estado_sat')
            if estado_sat == 'V':
              query = query.__and__((Q(last=True) & Q(response__in = ['R','U'])))
            elif estado_sat == 'C':
              query = query.__and__((Q(status='1000') & Q(response='A')))
          if 'business' in kwargs:
            taxpayer_id = kwargs['business'].taxpayer_id
            query = query.__and__(Q(rtaxpayer_id=taxpayer_id))

        elif request.POST.get('oper') == 'list-cancel-provider':
          #set_trace()
          if 'uuid' in request.POST:
            uuid = request.POST.get('uuid')
            query = query.__and__(Q(invoice__uuid=uuid))
          if 'date_from' in request.POST and 'date_to' in request.POST:
            date_from = request.POST.get('date_from')
            date_from = datetime.strptime(date_from, '%d %B %Y').strftime('%Y-%m-%d') if date_from else None
            date_to = request.POST.get('date_to')
            date_to = datetime.strptime(date_to, '%d %B %Y').strftime('%Y-%m-%d') if date_to else None
            if date_to and date_from:
              query = query.__and__(Q(date__range=[date_from, date_to]))
          if 'estatus_cancelacion' in request.POST:
            estatus_cancelacion = request.POST.get('estatus_cancelacion')
            query = query.__and__(Q(status=estatus_cancelacion))
          if 'taxpayer_id' in request.POST:
            taxpayer_id = request.POST.get('taxpayer_id')
            query = query.__and__(Q(invoice__taxpayer_id=taxpayer_id))
          if 'invoice_type' in request.POST:
            invoice_type = request.POST.get('invoice_type')
            query = query.__and__(Q(invoice__type=invoice_type))
          if 'business' in kwargs:
            taxpayer_id = kwargs['business'].taxpayer_id
            query = query.__and__(Q(invoice__rtaxpayer_id=taxpayer_id))

        return function(request, query, **kwargs)

      else:
        parameters = {
          'tab': kwargs['tab'] if 'tab' in kwargs.keys() else 'P'
        }
        template = 'cancel/cancellation_requests.html'
        return TemplateResponse(request, template, parameters)  
    except Exception as e:
      print('Exception get_query_list_cancellation_request() | %s' % str(e))
  return wrap
