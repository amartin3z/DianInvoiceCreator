from lxml import etree
import glob, os
from app.providers.tasks import import_provider
#from app.download.models import Package


namespaces_dict = {
  'cfdi': 'http://www.sat.gob.mx/cfd/3',
  'nomina': 'http://www.sat.gob.mx/nomina',
  'nomina12': 'http://www.sat.gob.mx/nomina12',
  'pago10': 'http://www.sat.gob.mx/Pagos',
  'tfd':'http://www.sat.gob.mx/TimbreFiscalDigital',
}

errors_path = '/data/soriana/ERRORS'
for xml_error in glob.glob('{}/*.xml'.format(errors_path)):
  try:  
    uuid = None
    import_result = None
    import_name = 'None import'
    message = 'There was no import'
    status = 'V'
    with open(xml_error) as xml_file:
      xml_string = xml_file.read()
      if not 'Elektra' in xml_string:
        xml_string = xml_string.replace('xmlns:schemaLocation', 'xsi:schemaLocation').replace(' http://www.sat.gob.mx/Pagos', 'http://www.sat.gob.mx/Pagos')
      else:
        xml_string = xml_string.replace('xmlns:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd" ', '')
      xml_parser = etree.XMLParser(remove_blank_text=True, recover=True, remove_comments=True, ns_clean=True)
      try:
        try:
          xml_encoded = xml_string.encode('utf-8')
        except:
          xml_encoded = xml_string.decode('utf-8')
        xml_etree = etree.XML(xml_encoded.encode('utf-8'), parser=xml_parser)
      except:
        xml_etree = etree.XML(xml_string, parser=xml_parser)
      comp_node = xml_etree.xpath('//cfdi:Comprobante', namespaces=namespaces_dict)[0]
      version = comp_node.get('Version', '3.3')
      nominas = xml_etree.xpath('//cfdi:Complemento/nomina:Nomina', namespaces=namespaces_dict)
      nominas12 = xml_etree.xpath('//cfdi:Complemento/nomina12:Nomina', namespaces=namespaces_dict)
      is_payroll = bool(nominas or nominas12)    
      uuid = xml_etree.xpath('//tfd:TimbreFiscalDigital/@UUID', namespaces=namespaces_dict)[0].upper()                  
      if version == '3.2':
        taxpayer_id = xml_etree.xpath('//cfdi:Comprobante/cfdi:Emisor/@rfc', namespaces=namespaces_dict)[0]
        rtaxpayer_id = xml_etree.xpath('//cfdi:Comprobante/cfdi:Receptor/@rfc', namespaces=namespaces_dict)[0]
        emission_date = xml_etree.xpath('//cfdi:Comprobante/@fecha', namespaces=namespaces_dict)[0]
        invoice_type = comp_node.get('tipoDeComprobante')
        if taxpayer_id == 'CCF121101KQ4':          
          if invoice_type == 'egreso' and is_payroll:
            try:
              status = Payroll.objects.get(uuid=uuid).values_list('status_sat', flat=True)
              package = Payroll.objects.get(uuid=uuid).package_xml
            except:
              package = Package.objects.filter(search__type='S', search__type_data='X', search__date_from__lte=emission_date, search__date_to__gte=emission_date).first()
            import_result, message = import_payroll_32(xml_etree=xml_etree, status=status, package=package)
            import_type = 'import_payroll_32'
          else:
            try:
              status = Invoice.objects.get(uuid=uuid).values_list('status_sat', flat=True)
              package = Invoice.objects.get(uuid=uuid).package_xml
            except:
              package = Package.objects.filter(search__type='S', search__type_data='X', search__date_from__lte=emission_date, search__date_to__gte=emission_date).first()
            import_result, message = import_emission_32(xml_etree=xml_etree, status=status, package=package)
            import_type = 'import_emission_32'            
        elif rtaxpayer_id == 'CCF121101KQ4':
          try:
            status = PInvoice.objects.get(uuid=uuid).values_list('status_sat', flat=True)
            package = PInvoice.objects.get(uuid=uuid).package_xml
          except:
            package = Package.objects.filter(search__type='R', search__type_data='X', search__date_from__lte=emission_date, search__date_to__gte=emission_date).first()
          import_result, message = import_provider(xml_etree=xml_etree, status=status, package=package)
          import_type = 'import_provider'
      elif version == '3.3':
        taxpayer_id = xml_etree.xpath('//cfdi:Comprobante/cfdi:Emisor/@Rfc', namespaces=namespaces_dict)[0]
        rtaxpayer_id = xml_etree.xpath('//cfdi:Comprobante/cfdi:Receptor/@Rfc', namespaces=namespaces_dict)[0]
        emission_date = xml_etree.xpath('//cfdi:Comprobante/@Fecha', namespaces=namespaces_dict)[0]
        invoice_type = comp_node.get('TipoDeComprobante')
        if taxpayer_id == 'CCF121101KQ4':          
          if invoice_type == 'N':
            try:
              status = Payroll.objects.get(uuid=uuid).values_list('status_sat', flat=True)
              package = Payroll.objects.get(uuid=uuid).package_xml
            except:
              package = Package.objects.filter(search__type='S', search__type_data='X', search__date_from__lte=emission_date, search__date_to__gte=emission_date).first()
            import_result, message = import_payroll(xml_etree=xml_etree, status=status, package=package)
            import_type = 'import_payroll'
          else:
            try:
              status = Invoice.objects.get(uuid=uuid).values_list('status_sat', flat=True)
              package = Invoice.objects.get(uuid=uuid).package_xml
            except:
              package = Package.objects.filter(search__type='S', search__type_data='X', search__date_from__lte=emission_date, search__date_to__gte=emission_date).first()
            import_result, message = import_emission(xml_etree=xml_etree, status=status, package=package)
            import_type = 'import_emission'
        elif rtaxpayer_id == 'CCF121101KQ4':
          try:
            status = PInvoice.objects.get(uuid=uuid).values_list('status_sat', flat=True)
            package = PInvoice.objects.get(uuid=uuid).package_xml
          except:
            package = Package.objects.filter(search__type='R', search__type_data='X', search__date_from__lte=emission_date, search__date_to__gte=emission_date).first()
          import_result, message = import_provider(xml_etree=xml_etree, status=status, package=package)
          import_type = 'import_provider'
      print '-'*60
      print xml_error
      if import_result:
        print 'Success => %s' % uuid
        try:
          os.remove(xml_error)
          print 'Removed...'
        except Exception as e:
          pass            
      else:
        print 'Error => %s' % uuid
        print 'Failed {} => {}'.format(import_type, message)        
      print '-'*60
  except Exception, e:      
    print '-'*60
    print xml_error
    print 'Exception fix_errors | {} | {} '.format(str(uuid), str(e))
    print '-'*60
