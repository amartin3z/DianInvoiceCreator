from django.conf import settings
from datetime import datetime


def validacion_ieeh10(xml_etree):

  print('INGRESOSHIDROCARBUROS10') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  namespaces = {'namespaces': {'ieeh': 'http://www.sat.gob.mx/IngresosHidrocarburos10'}}
  complement_ieeh = xml_etree.xpath('//ieeh:IngresosHidrocarburos', **namespaces)
  if complement_ieeh:
    namespaces = {'namespaces': xml_etree.nsmap}
    try:                
      if len(complement_ieeh) == 1:
        ieeh = complement_ieeh[0]

        version_de_comprobante = xml_etree.get('Version')
        if version_de_comprobante != '3.3':
          return False, 'IEEH101'

        tipo_de_comprobante = xml_etree.get('TipoDeComprobante')
        if tipo_de_comprobante != 'I':
          return False, 'IEEH102'
        
        total_de_comprobante = float(xml_etree.get('Total'))
        total_ieeh = float(ieeh.get('ContraprestacionPagadaOperador'))
        if total_ieeh != total_de_comprobante:
          return False, 'IEEH105'
        
        porcentaje_ieeh = float(ieeh.get('Porcentaje'))
        if porcentaje_ieeh <= 0 or porcentaje_ieeh > 100:
          return False, 'IEEH104'

        complement_DocumentoRelacionados = xml_etree.xpath('//ieeh:DocumentoRelacionado', **namespaces)
        for documentorelacionado in complement_DocumentoRelacionados:
          fecha_documentorelacionado = documentorelacionado.get('FechaFolioFiscalVinculado')
          fecha_documentorelacionado = datetime.strptime(fecha_documentorelacionado, "%Y-%m-%d")
          mes_documentorelacionado = int(documentorelacionado.get('Mes'))
          
          allowed_date = fecha_documentorelacionado - relativedelta(months=1)
          if mes_documentorelacionado not in (fecha_documentorelacionado.month, allowed_date.month):
            return False, 'IEEH103'
      else:
        return False, 'IEEH999'
    except Exception as e:
      print(f"Exception ieeh validacion_ieeh10 => {e}")
      return False, 'IEEH999'

  return True, None