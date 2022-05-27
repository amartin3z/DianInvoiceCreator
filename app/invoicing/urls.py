# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import (
  # new_invoice, 
  # new_payment,
  stuffs, 
  invoices,
  # prodservs,
  # receivers,
  calculate_amounts,
  download
)

app_name = 'invoicing'

urlpatterns = [

  url(u'^$', invoices, name='list-invoices'),
  url(r'^download_xml/(?P<uuid>[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})+/$', invoices, name='download_xml'),
  url(r'^download_pdf/(?P<uuid>[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})+/$', invoices, name='download_pdf'),

  url(r'download/', download, name='download_file'),

  url(r'^stuffs/$', stuffs, name='get-stuffs'),
  url(r'^calculate/$', calculate_amounts, name='get-amounts'),
]