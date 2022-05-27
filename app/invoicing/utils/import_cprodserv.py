# -*- encoding: UTF-8 -*-
import os
import json
import xlrd
import codecs
import urllib2

worksheets_to_work = ('c_ClaveProdServ', 'c_ClaveUnidad')

catalogos_tmpl = u'''
# -*- encoding: utf-8 -*-

PRODSERV = {prodserv}

CLAVEUNIDAD = {claveunidad}
'''


c_unidad = {}
c_prodserv = {}

CAT_CFDI = os.path.join(os.path.dirname(__file__), 'catCFDI.xsl')
DESTINATION_FILE = os.path.join(os.path.dirname(__file__), 'catalogos.py')
URL_CATALOGOS = 'http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls'


def download():
  filedata = urllib2.urlopen('http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls')
  datatowrite = filedata.read()
  with open(CAT_CFDI, 'wb') as f:
    f.write(datatowrite)


def process_prodserv():
  workbook = xlrd.open_workbook(CAT_CFDI, encoding_override='latin-1', on_demand=True)
  worksheet = workbook.sheet_by_name('c_ClaveProdServ')
  for row in range(4, worksheet.nrows):
    code, desc = worksheet.cell_value(row, 0), worksheet.cell_value(row, 1)
    try:
      code = "{}".format(code).split('.')[0]
    except:
      pass
    try: 
      desc = desc.encode('utf-8')
    except Exception, e: 
      print str(e)
    c_prodserv.update({
      code: desc
    })

def process_cunidad():
  workbook = xlrd.open_workbook(CAT_CFDI, encoding_override='latin-1', on_demand=True)
  worksheet = workbook.sheet_by_name('c_ClaveUnidad')
  for row in range(6, worksheet.nrows):
    code, desc = worksheet.cell_value(row, 0), worksheet.cell_value(row, 1)
    try:
      if isinstance(code, float):
        code = str(int(code))
    except:
      pass
    try: 
      desc = desc.encode('utf-8')
    except Exception, e: 
      print str(e)
    c_unidad.update({
      code: desc
    })
  
def save_catalog():
  catalogos_str = catalogos_tmpl.format(
    prodserv=c_prodserv,
    claveunidad=c_unidad
  )
  prod = codecs.open(DESTINATION_FILE, 'w', encoding='UTF-8')
  prod.write(catalogos_str)
  prod.close()


download()
process_prodserv()
process_cunidad()
save_catalog()

if os.path.exists(CAT_CFDI):
  os.remove(CAT_CFDI)
