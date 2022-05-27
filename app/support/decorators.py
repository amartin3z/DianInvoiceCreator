# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from django.template.response import TemplateResponse
from django.db.models import Q
from datetime import datetime
from pdb import set_trace

def get_query_list_tickets(function):
  def wrap(request, *args, **kwargs):
    try:
      template, context = "list_tickets.html", {}
      if request.method == "POST" and request.is_ajax():
        query= Q(submitter_email=request.user.username)
        if "ticket_id" in request.POST:
          ticket_id = int(request.POST.get("ticket_id"))
          query = query.__and__(Q(id=ticket_id)) 
        if "ticket_subject" in request.POST:
          query = query.__and__(Q(title__icontains=request.POST.get("ticket_subject")))
        if "ticket_status" in request.POST:
          query = query.__and__(Q(status=request.POST.get("ticket_status"))) 
        if "ticket_category" in request.POST:
          queue_id = int(request.POST.get("ticket_category"))
          query = query.__and__(Q(queue_id=queue_id))
        if "ticket_priority" in request.POST:
          priority = int(request.POST.get("ticket_priority"))
          query = query.__and__(Q(priority=priority))
        return function(request, query, *args, **kwargs)
    except Exception as e:
      print("Exception in get_query_list_tickets => {}".format(str(e)))
    return function(request, None, *args, **kwargs)
  return wrap