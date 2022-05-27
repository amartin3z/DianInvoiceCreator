from django.conf import settings
from app.sat.models import LCO
from .adicionales import trunc, normal_round, sat_round


def validacion_ecc12(xml_etree):
  
  print('ESTADODECUENTACOMBUSTIBLE') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  namespace_dicc = {'cfdi': 'http://www.sat.gob.mx/cfd/3', 'ecc12': 'http://www.sat.gob.mx/EstadoDeCuentaCombustible12'}  

  complements_ecc12 = xml_etree.findall('.//ecc12:EstadoDeCuentaCombustible', namespaces=namespace_dicc)

  if complements_ecc12:
    namespace_dicc = xml_etree.nsmap
    try:
      tipo_comprobante = xml_etree.get('TipoDeComprobante')
      if tipo_comprobante != 'I':
        return False, 'ECC124'
      cfdi_version = xml_etree.get('Version')
      if cfdi_version != '3.3':
        return False, 'ECC125'

      for c_ecc12 in complements_ecc12:
        subtotal = trunc(c_ecc12.get('SubTotal'), 2)
        sum_importe = c_ecc12.xpath('sum(//ecc12:Conceptos/ecc12:ConceptoEstadoDeCuentaCombustible/@Importe)', namespaces=namespace_dicc)
        if subtotal != trunc(sum_importe, 2):
          return False, 'ECC121'
        
        total = c_ecc12.get('Total')
        sum_traslados = c_ecc12.xpath('sum(//ecc12:Conceptos/ecc12:ConceptoEstadoDeCuentaCombustible/ecc12:Traslados/ecc12:Traslado/@Importe)', namespaces=namespace_dicc)
        if trunc(total, 2) != trunc(sum([sum_traslados, subtotal]), 2):
          return False, 'ECC122'
      
      cecc = c_ecc12.xpath('//ecc12:Conceptos/ecc12:ConceptoEstadoDeCuentaCombustible', namespaces=namespace_dicc)
      for concept_ecc in cecc:
        taxpayer_id = concept_ecc.get('Rfc')
        if taxpayer_id in ('XAXX010101000', 'XEXX010101000'):
          return False, 'ECC129'
        frontier_iva_ecc12 = concept_ecc.xpath('.//ecc12:Traslados/ecc12:Traslado[@TasaOCuota = 0.08 and @Impuesto = "IVA"]', namespaces=namespace_dicc)
        if len(frontier_iva_ecc12):
          if not LCO.objects.filter(rfc=taxpayer_id, validity_obligation='2').exists():
            return False, 'ECC126'
        elif not LCO.objects.filter(rfc=taxpayer_id, validity_obligation__in=('1', '2')).exists():
          return False, 'ECC123'

      if len(cecc):
        concepts_frontier = xml_etree.xpath('.//cfdi:Conceptos/cfdi:Concepto/cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@TasaOCuota = 0.08 and @Impuesto = "002"]/ancestor::cfdi:Concepto', namespaces=namespace_dicc)
        frontier_iva_ecc12 = xml_etree.xpath('.//ecc12:Conceptos/ecc12:ConceptoEstadoDeCuentaCombustible/ecc12:Traslados/ecc12:Traslado[@TasaOCuota = 0.08 and @Impuesto = "IVA"]', namespaces=namespace_dicc)

        for f_iva in frontier_iva_ecc12:
          tasa_cuota = f_iva.get('TasaOCuota')
          if tasa_cuota != '0.080000':
            return False, 'ECC127'
      
        if len(concepts_frontier) != len(frontier_iva_ecc12):
          return False, 'ECC999'
      
    except Exception as e:
      print(f"Exception ecc validacion_ecc12 => {e}")
      return False, 'ECC999'

  return True, None