# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import soap_application

app_name = 'cfdi'

urlpatterns = [
  url(u'^sat/$', soap_application),
]
