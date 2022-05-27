from app.providers.models import Invoice
from lxml import etree
from django.core.exceptions import MultipleObjectsReturned
from pdb import set_trace

parser = etree.XMLParser(remove_blank_text=True, recover=True, remove_comments=True, ns_clean=True)
nsmap = {
  'cfdi': 'http://www.sat.gob.mx/cfd/3', 
  'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital', 
  'pago10': 'http://www.sat.gob.mx/Pagos'
}

ranges = [
  ['2019-04-01','2019-05-01'],
  ['2019-01-01','2019-02-01'],
  ['2019-02-01','2019-03-01'],
  ['2019-03-01','2019-04-01'],
  ['2019-05-01','2019-06-01'],
  ['2019-06-01','2019-07-01'],
  ['2019-07-01','2019-08-01'],
  ['2019-08-01','2019-09-01'],
  ['2019-09-01','2019-10-01'],
]

#pinvoices = Invoice.objects.all()
#pinvoices = Invoice.objects.filter(uuid='8CC0A4B3-2884-11E9-8FA8-00155D014009')
#pinvoices = Invoice.objects.filter(uuid='A2D336D8-4F05-48AE-AF46-BD2F5492ECD3')

for ra in ranges:
  #pinvoices = Invoice.objects.all()
  #pinvoices = Invoice.objects.filter(uuid='A2D336D8-4F05-48AE-AF46-BD2F5492ECD3')
  #pinvoices = Invoice.objects.filter(emission_date__range=['2019-08-01','2019-10-01'])
  pinvoices = Invoice.objects.filter(emission_date__range=ra)
  total = pinvoices.count()
  counter = 0
  for invoice in pinvoices:
    counter += 1
    try:
      xml_string = invoice.xml  
      xml_string = xml_string.replace('xmlns:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd"', '').replace("xmlns:schemaLocation", "xsi:schemaLocation")      
      xml_etree = etree.fromstring(xml_string, parser=parser)
      total_ret = xml_etree.xpath('sum(//cfdi:Impuestos/@TotalImpuestosRetenidos)', namespaces=nsmap)
      total_trans = xml_etree.xpath('sum(//cfdi:Impuestos/@TotalImpuestosTrasladados)', namespaces=nsmap)
      taxes = {'tra': {}, 'ret': {}}
      for t in xml_etree.xpath('//cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado', namespaces=nsmap):
        tasaocuota = t.get('TasaOCuota', None)
        importe = t.get('Importe')
        impuesto = t.get('Impuesto')
        if impuesto not in taxes['tra']:
          taxes['tra'][impuesto] = {}
        if tasaocuota is not None:
          taxes['tra'][impuesto][tasaocuota] = {
            'Importe': importe,
            'Base': xml_etree.xpath('sum(//cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@TasaOCuota=%s and @Impuesto=%s]/@Base)' % (tasaocuota, impuesto), namespaces=nsmap)
          }
        else:
          taxes['tra'][impuesto]['exento'] = {
            'Importe': importe,
            'Base': xml_etree.xpath('sum(//cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@TipoFactor="Exento" and @Impuesto=%s]/@Base)' % (impuesto), namespaces=nsmap)
          }    
      for r in xml_etree.xpath('//cfdi:Impuestos/cfdi:Retenciones/cfdi:Retencion', namespaces=nsmap):
        taxes['ret'][r.get('Impuesto')] = r.get('Importe')
      invoice.taxes = taxes
      invoice.save()
      print "%s/%s %s %s DONE" % (counter, total, invoice.uuid, ra[0])
    except Exception, e:
      print "%s/%s %s %s EXCEPTION => %s" % (counter, total, invoice.uuid, ra[0], str(e))
