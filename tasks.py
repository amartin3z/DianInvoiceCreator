# -*- encoding: UTF-8 -*-
from datetime import datetime
import os

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
  os.environ['DJANGO_SETTINGS_MODULE'] = 'ublinvoice.settings.demo'
import django
django.setup()

from celery import Celery

app = Celery('soriana_tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

@app.task(soft_time_limit=3600)
def process_stampfk(xml_path):
  try:
    result = STAMPFK(xml_path)
  except Exception, e:
    print "task proccess_stampfk Exception => " + str(e)
