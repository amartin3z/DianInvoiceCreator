# -*- coding: utf-8 -*-
#!/usr/bin/python
from datetime import datetime, timedelta

def value_progressbar(date=None):
  try:
    percentage = 0 
    date_now = datetime.now()
    date_now = (date_now - date)
    date_number =  date_now.total_seconds() / timedelta (days=1).total_seconds()
    percentage = date_number / 0.03
    if percentage > 100:
      percentage = 100 
  except:
    pass
  return percentage


  