# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import list_cancellation_request
from .views import accept_reject
from .views import history_cancellation
from .views import consult_status

app_name = 'cancel'

urlpatterns = [
  url(u'^$', list_cancellation_request, name='cancelrequests'),
  url(u'^(?P<tab>[P|H|C|X])+$', list_cancellation_request, name='cancelrequests'),
  url(u'^answer/$', accept_reject, name='answer'),
  url(u'^history/$', history_cancellation, name='history_cancellation'),
  url(u'^consult_status/$', consult_status, name='consult_status'),
]