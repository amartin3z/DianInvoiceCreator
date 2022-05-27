# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .views import list_tickets, tickets_options


urlpatterns = [
  url(r'', include('helpdesk.urls')),
  url(u'^list-tickets/$', list_tickets, name='tickets'),
  url(u'^tickets_options$', tickets_options, name='tickets_options'),
]