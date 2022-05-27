# -*- coding: utf-8 -*-
import os

def invoice_storage(instance, filename):
  upload_to = os.path.join('xml', instance.uuid[0:2], instance.uuid[2:4], instance.uuid[4:6], instance.uuid[6:8])
  return os.path.join(upload_to, filename)
