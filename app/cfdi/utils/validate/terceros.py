from django.conf import settings
from app.sat.utils.validate import Catalogos
from app.sat.models import LCO


def validacion_terceros11(xml_etree):

  print('TERCEROS11') if settings.VERBOSE_EXTRA_VALIDATIONS else None

  namespaces = {'namespaces': {'terceros': 'http://www.sat.gob.mx/terceros'}}
  terceros = xml_etree.findall('.//terceros:PorCuentadeTerceros', **namespaces)
  if terceros:
    namespaces = {'namespaces': xml_etree.nsmap}
    try:
      catalogos_obj = Catalogos(xml_etree.get('Fecha'))
      for tercero in terceros:
        taxpayer_id = tercero.get('rfc')
        if taxpayer_id in ('XAXX010101000', 'XEXX010101000'):
          return False, 'PCT107'
        frontier_concepts = xml_etree.xpath('.//cfdi:Conceptos/cfdi:Concepto/cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@TasaOCuota = 0.08 and @Impuesto = "002"]/ancestor::cfdi:Concepto', **namespaces)
        frontier_iva_tercero = tercero.xpath('.//terceros:Impuestos/terceros:Traslados/terceros:Traslado[@tasa = 8.0 and @impuesto = "IVA"]', **namespaces)
        if len(frontier_iva_tercero):
          if not LCO.objects.filter(rfc=taxpayer_id, validity_obligation='2').exists():
            self.message = taxpayer_id
            return False, 'PCT106'

          addresses = tercero.xpath('.//terceros:InformacionFiscalTercero', **namespaces)
          if not len(addresses):
            return False, 'PCT102'
          
          for address in addresses:
            postal_code = address.get('codigoPostal')
            frontier_expedition = catalogos_obj.validar('CodigoPostal', postal_code, tipo='fronterizo')
            if not frontier_expedition:
              return False, 'PCT102'

          for frontier_concept in frontier_concepts:
            frontier_taxes = frontier_concept.xpath('.//cfdi:Traslado[@TasaOCuota = 0.08 and @Impuesto = "002"]', **namespaces)
            prodserv = frontier_concept.get('ClaveProdServ')
            prodserv_frontier = catalogos_obj.validar('ClaveProdServ', prodserv, tipo='fronterizo')
            if not prodserv_frontier:
              return False, 'PCT103'
            for ftax in frontier_taxes:
              if ftax.get('TasaOCuota') != '0.080000':
                return False, 'PCT105'
          
          for f_iva in frontier_iva_tercero:
            tasa = f_iva.get('tasa')
            if tasa != '8.000000':
              return False, 'PCT104'

        elif len(frontier_concepts):
          for frontier_concept in frontier_concepts:
            nodes_ctercero = frontier_concept.findall('.//tmp:PorCuentadeTerceros', namespaces={'tmp': 'http://www.sat.gob.mx/terceros'}) 
            for node_ct in nodes_ctercero:
              frontier_iva_tercero = node_ct.xpath('.//terceros:Impuestos/terceros:Traslados/terceros:Traslado[@tasa = 8.0 and @impuesto = "IVA"]', **namespaces)
              if not len(frontier_iva_tercero):
                return False, 'PCT104'
              for f_iva in frontier_iva_tercero:
                tasa = f_iva.get('tasa')
                if tasa != '8.000000':
                  return False, 'PCT104'
              taxpayer_id = node_ct.get('rfc')
              addresses = node_ct.xpath('.//terceros:InformacionFiscalTercero', **namespaces)
              if addresses:
                is_special = False
                for address in addresses:
                  postal_code = address.get('codigoPostal')
                  frontier_expedition = catalogos_obj.validar('CodigoPostal', postal_code, tipo='fronterizo')
                  is_special = is_special or bool(frontier_expedition)
                if is_special and  LCO.objects.filter(rfc=taxpayer_id, validity_obligation='2').exists():
                  return False, 'PCT104'
                elif not LCO.objects.filter(rfc=taxpayer_id, validity_obligation__in=('1', '2')).exists():
                  return False, 'PCT101' 
              else:
                return False, 'PCT102'
        elif not LCO.objects.filter(rfc=taxpayer_id, validity_obligation__in=('1', '2')).exists():
          self.message = taxpayer_id
          return False, 'PCT101'

    except Exception as e:
      print(f'Exception terceros validacion_terceros11 => {e}')
      return False, 'PCT999'

  return True, None