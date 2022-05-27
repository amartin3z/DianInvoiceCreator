#from app.download.models import Package, Search
#from app.providers.models import Invoice as PInvoice
#from app.download.utils.downloadFK import DOWNLOADFK
from app.cancel.models import Cancellation, ProviderCancellation
from django.conf import settings
import os
import zipfile
import codecs
import shutil
from datetime import datetime, timedelta



date_ranges_sent = []
date_ranges_received = []
last_requested = datetime.now() - timedelta(days=3)
last_emission = datetime.now() - timedelta(days=6)
searches = Search.objects.filter(status='2', requested__lte=last_requested).order_by('date_from')
for search in searches:
  print '-----'*5
  print 'Pending Search => %s => %s' % (search.id, search.search_id)
  print 'FROM DATE => %s' % search.date_from
  print 'TO DATE => %s' % search.date_to
  print 'TYPE => %s' % search.type
  print 'TYPE DATA => %s' % search.type_data
  print '-----'*5
  if search.type == 'S':
    date_ranges_sent.append([search.date_from, search.date_to])
  else:
    date_ranges_received.append([search.date_from, search.date_to])


pinvoices = PInvoice.objects.filter(_xml='', emission_date__lte=last_emission)
for date_range  in date_ranges_received:
  pinvoices = pinvoices.exclude(emission_date__range=date_range)
print '-----'*5
print pinvoices.query
print 'Received Pending Invoices => %s' % pinvoices.count()
print '-----'*5

# sinvoices = SInvoice.objects.filter(_xml='', emission_date__lte=last_emission)
# for date_range  in date_ranges_sent:
#   sinvoices = sinvoices.exclude(emission_date__range=date_range)
# print '-----'*5
# print sinvoices.query
# print 'Sent Pending Invoices => %s' % sinvoices.count()
# print '-----'*5


