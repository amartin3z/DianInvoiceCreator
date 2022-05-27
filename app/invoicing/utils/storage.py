# -*- encoding: UTF-8 -*-
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os
from uuid import uuid4
from datetime import datetime

class OverrideFileSystemStorage(FileSystemStorage):

  def __init__(self, location=settings.STORAGE_PATH, *args, **kwargs):
    self._location = location
    super(OverrideFileSystemStorage, self).__init__(location, *args, **kwargs)

  def get_available_name(self, name, max_length=None):
    if self.exists(name):
      os.remove(os.path.join(self._location, name))
    return name


def invoice_storage(instance, filename):
  emission_date = instance.emission_date
  if isinstance(emission_date, str):
    #emission_date = datetime.strptime(emission_date, '%Y-%m-%dT%H:%M:%S')
    emission_date = datetime.strptime(emission_date, '%Y-%m-%d')
  if not instance.uuid:
    uuid = uuid4().__str__().upper()
  else:
    uuid = instance.uuid
  upload_to = os.path.join('invoicing', 'invoice', instance.taxpayer_id, emission_date.strftime('%Y'), emission_date.strftime('%m'), emission_date.strftime('%d'), uuid[0:2], uuid[2:4], uuid[4:6], uuid[6:8])
  return os.path.join(upload_to, filename)

def cancel_storage(instance, filename):
  cancellation_date = instance.date
  if isinstance(cancellation_date, str):
    cancellation_date = datetime.strptime(cancellation_date, '%Y-%m-%dT%H:%M:%S')
  uuid = instance.uuid
  upload_to = os.path.join('invoicing', 'cancellation', instance.taxpayer_id, cancellation_date.strftime('%Y'), cancellation_date.strftime('%m'), cancellation_date.strftime('%d'), uuid[0:2], uuid[2:4], uuid[4:6], uuid[6:8])
  return os.path.join(upload_to, filename)