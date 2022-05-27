#from app.download.models import Package
from app.providers.models import Invoice as PInvoice
from app.cancel.models import Cancellation, ProviderCancellation
from django.conf import settings
import os
import zipfile
import codecs
import shutil


downloadfk = DOWNLOADFK()
packages =  Package.objects.filter(search__type_data='M')
for package in packages:
  print package.search.date_from
  metadata_lst = []
  zip_path = package._file.path
  filename = os.path.basename(zip_path)
  dirname = os.path.dirname(zip_path)
  dirname_tmp = os.path.join('/tmp', dirname.replace('/data/', ''))
  if os.path.exists(dirname_tmp):
    shutil.rmtree(dirname_tmp)
  else:
    os.makedirs(dirname_tmp)
  zf = zipfile.ZipFile(zip_path, "r")
  zf.extractall(dirname_tmp)
  decompressed_files = os.listdir(dirname_tmp)
  for d_file in decompressed_files:
    txt = codecs.open(os.path.join(dirname_tmp, d_file), 'r', 'utf-8')
    record = ''
    separator = 0
    for line in txt.readlines():
      try:
        line = line.strip().encode('utf-8')
      except:
        line = line.strip().decode('utf-8')
      if 'Uuid' in line:
        continue
      if (line.count('~') + separator) < 11:
        #set_trace()
        record = '{} {}'.format(record, line)
        separator = separator + line.count('~')
      if (line.count('~') + separator) == 11:
        record = '{} {}'.format(record, line)
        invoice_lst = record.strip().split('~')
        invoice_dict = dict(zip(settings.METADATA_KEYS, invoice_lst))
        for k, v in invoice_dict.iteritems():
          invoice_dict[k] = v[:250]
        metadata_lst.append(invoice_dict)
        record = ''
        separator = 0
      if (line.count('~') + separator) > 11:
        raise Exception('Error, un registro contiene mas de 11 columnas:\n\r{}'.format(line))
    txt.close()
    print len(metadata_lst)
    for invoice in metadata_lst:
      uuid = invoice.pop('uuid')
      status = invoice.pop('status')
      c_date = invoice.pop('cancellation_date')
      if package.search.type == 'S':
        if status == '0':
          print "S", uuid
          try:
            cancellation_obj = Cancellation.objects.filter(uuid=uuid).order_by('-id')[0]
          except:
            invoice_obj = SInvoice.objects.get(uuid=uuid)
            cancellation_obj = Cancellation(uuid=uuid)
            cancellation_obj.user_id = 1
            cancellation_obj.total = invoice_obj.total
            cancellation_obj.invoice_type = invoice_obj.type
            cancellation_obj.taxpayer_id = invoice_obj.taxpayer_id
            cancellation_obj.rtaxpayer_id = invoice_obj.rtaxpayer_id
            cancellation_obj.status_sat = 'C'
            cancellation_obj.status = 'U'
            cancellation_obj.notes = ''
          cancellation_obj.date = c_date
          cancellation_obj.save()
      elif package.search.type == 'R':          
        if status == '0':
          print "R", uuid
          try:
            cancellation_obj = ProviderCancellation.objects.filter(invoice_provider__uuid=uuid).order_by('-id')[0]
          except:
            invoice_obj = PInvoice.objects.get(uuid=uuid)
            cancellation_obj = ProviderCancellation(invoice_provider=invoice_obj)
            cancellation_obj.status = 'U'
            cancellation_obj.notes = ''
          cancellation_obj.date = c_date
          cancellation_obj.save()
