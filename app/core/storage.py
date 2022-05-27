# -*- coding: utf-8 -*-
import os
from datetime import datetime

def satfile_storage(instance, filename):
  upload_to = os.path.join('satfiles', instance.business.taxpayer_id)
  return os.path.join(upload_to, filename)

def logo_storage(instance, filename):
  upload_to = instance.taxpayer_id
  extension = filename.split('.')[-1]
  filename = '{}.{}'.format(instance.taxpayer_id, extension)
  return os.path.join(upload_to, filename)

def xml_storage(instance, filename):
  date = datetime.now().strftime('%Y/%m/%d')
  upload_to = os.path.join('xml_signed', date)
  return os.path.join(upload_to, filename)

def pdf_storage(instance, filename):
  date = datetime.now().strftime('%Y/%m/%d')
  upload_to = os.path.join('pdf_signed', date)
  return os.path.join(upload_to, filename)