from __future__ import absolute_import


from django.conf import settings

import os
from celery import Celery
from celery.schedules import crontab

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ublinvoice.settings.local')


app = Celery('ublinvoice')

app.config_from_object('django.conf.settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


#@app.task(bind=True)
#def debug_tas(self):
#  print('Rquest: ({0!r}'.format(self.request))

