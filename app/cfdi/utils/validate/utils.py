# -*- encoding: UTF-8 -*-

from datetime import datetime, timedelta
from pdb import set_trace
from django.conf import settings
from lxml import etree
import uuid


def get_summer_dates(year):
  #set_trace()
  march_1st = datetime(year, 3, 1)
  april_1st = datetime(year, 4, 1)
  november_1st = datetime(year, 11, 1)

  ## March
  sunday_offset = 7 - march_1st.isoweekday()
  march_1st_sunday = march_1st + timedelta(days=sunday_offset)
  march_2nd_sunday = march_1st_sunday + timedelta(days=7)
  
  ## April
  sunday_offset = 7 - april_1st.isoweekday()
  april_1st_sunday = april_1st + timedelta(days=sunday_offset)
  
  ## October
  sunday_offset = november_1st.isoweekday() % 7
  # Sometimes november_1st could be sunday, so the offset would be 0, need to subtrac 7 instead of 0
  october_last_sunday = november_1st - timedelta(days=sunday_offset if sunday_offset > 0 else 7) 
  
  ## November
  sunday_offset = 7 - november_1st.isoweekday()
  november_1st_sunday = november_1st + timedelta(days=sunday_offset)
  
  # print "Segundo Domingo Marzo => %s" % march_2nd_sunday
  # print "Primer Domingo Abril => %s" % april_1st_sunday
  # print "Ultimo Domingo Octubre => %s" % october_last_sunday
  # print "Primer Domingo Noviembre => %s" % november_1st_sunday

  result = {
    'march': march_2nd_sunday,
    'april': april_1st_sunday,
    'october': october_last_sunday,
    'november': november_1st_sunday
  }

  return result


def get_original_string(xml_string):
  original_string = ''
  try:
    if isinstance(xml_string, bytes):
      xml_etree = etree.fromstring(xml_string)
    else:
      xml_etree = etree.fromstring(bytes(bytearray(xml_string, encoding='utf-8')))
    #parser = etree.XMLParser()
    #parser.resolvers.add(FileResolver())
    #xslt_root = etree.XML(settings.XSLT_STR, parser)
    #transform = etree.XSLT(xslt_root)
    transform = settings.XSLT_TRANSFORM
    result = transform(xml_etree)
    original_string = str(result).encode("utf-8")
    """
    result = result.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
    result = result.replace('\n','')
    result = result.replace('&quot;', '"')
    result = result.replace('&lt;', '<')
    result = result.replace('&gt;', '>')
    result = result.replace('&amp;', '&')
    result = result.strip()
    """
  except Exception as e:
    print(f"Exception get_original_string => {e}")
  return original_string


def generate_uuid(sello):
  sello = "".join(sello.split())
  namespace = '{}/{}'.format(settings.UUID_NAMESPACE, sello)
  result = str(uuid.uuid5(uuid.NAMESPACE_DNS, namespace)).upper()
  return result

class FileResolver(etree.Resolver):
  def resolve(self, filename, id, context):
    print ('Resolving url %s ' % filename)
    return self.resolve_filename(filename, context)
