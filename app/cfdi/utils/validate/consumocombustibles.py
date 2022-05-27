from django.conf import settings
from app.sat.models import LCO


def validacion_consumodecombustibles11(xml_etree):

  print('CONSUMODECOMBUSTIBLES11') if settings.VERBOSE_EXTRA_VALIDATIONS else None

  namespaces = {'namespaces': {'consumodecombustibles11': 'http://www.sat.gob.mx/ConsumoDeCombustibles11'}}

  consumocombustibles11 = xml_etree.findall('.//consumodecombustibles11:ConsumoDeCombustibles', **namespaces)
  if consumocombustibles11:
    namespaces = {'namespaces': xml_etree.nsmap}
    try:
      for cc11 in consumocombustibles11:
        conceptos = cc11.findall('.//consumodecombustibles11:ConceptoConsumoDeCombustibles', **namespaces)
        for consumo_concepto in conceptos:
          taxpayer_id = consumo_concepto.get('rfc')
          iva_determinado_fronterizo = consumo_concepto.xpath('.//consumodecombustibles11:Determinado[@tasaOCuota = 0.08 and @impuesto = "IVA"]', **namespaces)
          if len(iva_determinado_fronterizo):
            if not LCO.objects.filter(rfc=taxpayer_id, validity_obligation='2').exists():
              return False, 'CCO101'
            for iva_df in iva_determinado_fronterizo:
              tasa_cuota = iva_df.get('tasaOCuota')
              if tasa_cuota != '0.080000':
                return False, 'CCO102'
          elif not LCO.objects.filter(rfc=taxpayer_id, validity_obligation__in=('1', '2')).exists():
            return False, 'CCO103'
    except Exception as e:
      print(f'Exception consumodecombustibles validacion_consumodecombustibles11 => {e}')
      return False, 'CCO999'

  return True, None