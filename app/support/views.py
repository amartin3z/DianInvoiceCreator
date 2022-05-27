# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.http import JsonResponse, Http404

from helpdesk.models import Queue, Ticket, FollowUp, Attachment

from app.core.decorators import get_default_business
from app.users.decorators import has_group, has_groups
from .decorators import get_query_list_tickets
from .strings import TICKET_ID, QUEUE
from app.core.models import Log
from app.core.logs import MESSAGES_LOGS

import os
from django.utils.translation import ugettext_lazy as _


# Create your views here.

@login_required(login_url='/')
@has_group('clients')
@get_query_list_tickets
@get_default_business
def list_tickets(request, query, *args, **kwargs):
  try:
    template, context = "list_tickets.html", {}
    if request.method == "POST" and request.is_ajax():
      Log.objects.log_action(request, 5, 'R', MESSAGES_LOGS.get('mensaje41').get(settings.DEFAULT_LANGUAGE_CODE), 'S', '')
      list_result, total = [], 0
      start, length = int(request.POST.get('iDisplayStart')), int(request.POST.get('iDisplayLength'))
      tickets = Ticket.objects.filter(query).order_by('-modified')
      total = tickets.count()
      tickets = tickets[start:start+length]
      for ticket in tickets.iterator():
        options =  render_to_string('strings/options.html', {"ticket":ticket}, request)
        status =  render_to_string('strings/status.html', {"ticket":ticket}, request)
        priority =  render_to_string('strings/priority.html', {"ticket":ticket}, request)
        list_result.append([
          TICKET_ID.format(ticket.id),
          status,
          ticket.title,
          ticket.created,
          ticket.modified,
          QUEUE.format(ticket.queue.title),
          priority,
          options,
        ])
       
      result = {
        'aaData': list_result,
        'iTotalRecords': total,
        'iTotalDisplayRecords': total,
      }
      return JsonResponse(result)
    else:
      queues = Queue.objects.filter().order_by('id')
      queues_val = [{'title': _('Billing'), 'id': 1}, {'title': _('Questions'), 'id': 2}, {'title': _('Doubts'), 'id': 3}, {'title': _('Low'), 'id': 4}]
      context.update({"queues":queues_val, 'total_tickets': Ticket.objects.filter(submitter_email=request.user.username).count()})
  except Exception as e:
    print("Exception in list_tickets => {}".format(str(e)))
    
    Log.objects.log_action(request, 3, 'R', MESSAGES_LOGS.get('mensaje42').get(settings.DEFAULT_LANGUAGE_CODE), 'S', "Exception in list_tickets => {}".format(str(e)))
  return TemplateResponse(request, template, context)

@login_required(login_url='/')
@has_group('clients')
@get_default_business
def tickets_options(request, *args, **kwargs):
  try:
    success, message = False, "Error, please try again later ..."
    if request.method == "POST" and request.is_ajax():
      user = request.user
      option = request.POST.get("option", None)
      if option is not None:
        if option == "get_queues":
          list_queues = []
          queues = Queue.objects.filter().order_by('id')
          for queue in queues: 
            list_queues.append({'code':queue.id,'des':queue.title})
          success, message = True, list_queues
        elif option == "add_ticket":
          subject = request.POST.get("subject")
          description = request.POST.get("description")
          queue = request.POST.get("queue")
          priorty = request.POST.get("priorty")
          ticket_obj = Ticket.objects.create(
            title = subject,
            submitter_email = user.username,
            status = 1,
            description = description,
            priority = priorty,
            assigned_to_id = user.id,
            queue_id = queue,
          )
          followup_obj = FollowUp.objects.create(
            title = subject,
            comment = description,
            ticket_id = ticket_obj.id,
            user_id = user.id,
          )
          if 'file' in request.FILES:
            file = request.FILES.get("file")
            attachment_obj = Attachment.objects.create(
              filename = file.name,
              mime_type = file.content_type,
              size = file.size,
              followup_id = followup_obj.id
            )
            attachment_obj.file = file
            attachment_obj.save()
          success, message = True, _('Ticket created successfully')
          Log.objects.log_action(request, 5, 'C', MESSAGES_LOGS.get('mensaje43').get(settings.DEFAULT_LANGUAGE_CODE), 'S', '')
        elif option == "update_ticket":
          data_id = int(request.POST.get("data-id"))
          comment = request.POST.get("description")
          user_id = user.id
          try:
            ticket = Ticket.objects.get(id=data_id, submitter_email=user.username)
            followup_obj = FollowUp.objects.create(
              title = ticket.title,
              comment = comment,
              ticket_id = ticket.id,
              user_id = user_id,
            )
            if 'file' in request.FILES:
              file = request.FILES.get("file")
              attachment_obj = Attachment.objects.create(
                filename = file.name,
                mime_type = file.content_type,
                size = file.size,
                followup_id = followup_obj.id
              )
              attachment_obj.file = file
              attachment_obj.save()
            success, message = True, _("Answer Sent successfully")
            #MESSAGES_LOGS.get('mensaje42').get(settings.DEFAULT_LANGUAGE_CODE)
            Log.objects.log_action(request, 5, 'U', message, 'S', '')
            #Log.objects.log_action(request, 5, 'U', u'Answer Sent successfully', 'S', '')
          except:
            message = _("Permission denied for this Ticket")
            #Log.objects.log_action(request, 2, 'U', u'Permission denied for this Ticket', 'S', '')
            Log.objects.log_action(request, 2, 'U', message, 'S', '')
        elif option == "solved_ticket":
          data_id = int(request.POST.get("data-id"))
          comment = request.POST.get("description")
          user_id = user.id
          try:
            ticket = Ticket.objects.get(id=data_id, submitter_email=user.username)
            followup_obj = FollowUp.objects.create(
              title = ticket.title,
              comment = comment,
              ticket_id = ticket.id,
              user_id = user_id,
            )
            ticket.status= 3
            ticket.save()
            success, message = True, _("Ticket Solved")
            Log.objects.log_action(request, 5, 'U', message, 'S', '')
            #Log.objects.log_action(request, 5, 'U', u'Ticket status updated to Resolved', 'S', '')
          except:
            message = "Permission denied for this Ticket"
            #Log.objects.log_action(request, 2, 'U', u'Permission denied for this Ticket', 'S', '')
            Log.objects.log_action(request, 2, 'U', message, 'S', '')
        elif option == "followup_ticket":
          id_ = request.POST.get("data-id")
          user_id, list_followup  = user.id, []
          followups = FollowUp.objects.filter(ticket_id=id_).order_by('date')
          for followup in followups:
            attachment = None
            attachment = Attachment.objects.filter(followup_id=followup.id)
            if attachment.exists():
              attachment = attachment[0]
            if followup.user_id  == user_id:
              username = kwargs['business'].name 
              logo = kwargs['business'].get_logo()
              list_followup.append(render_to_string('strings/followup_cliente.html', {"followup":followup, "username":username, "logo":logo, "attachment":attachment}, request))
            else: 
              list_followup.append(render_to_string('strings/followup_support.html', {"followup":followup, "attachment":attachment}, request))
          success, message = True, list_followup
      else:
        message = _("Option not valid")
  except Exception as e:
    print("Exception in list_tickets => {}".format(str(e)))
    Log.objects.log_action(request, 3, 'R', MESSAGES_LOGS.get('mensaje44').get(settings.DEFAULT_LANGUAGE_CODE), 'S', "Exception in list_tickets => {}".format(str(e)))
  result = {"success":success,"message":message}
  if settings.DEBUG:
    print (result)
  return JsonResponse(result)

