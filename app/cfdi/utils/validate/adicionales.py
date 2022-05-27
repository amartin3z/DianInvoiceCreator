from django.conf import settings

from app.sat.utils.validate import Catalogos
from app.sat.models import LCO, LRFC
from .base import validacion_sello

from decimal import Decimal, ROUND_UP, ROUND_HALF_EVEN, ROUND_HALF_UP
from lxml import etree
import math
import M2Crypto
import re
import datetime
from copy import deepcopy

def trunc(num, digits, r=False):
  if r:
    factor = ''  
    num_str = num if 'e-' in str(num) else str(num) 
    for n in range(digits-1):
      factor += '0'
    if r == 'EVEN':
      num = Decimal(num_str).quantize(Decimal('.%s1' % factor), rounding=ROUND_HALF_UP)
    else:
      num = Decimal(num_str).quantize(Decimal('.%s1' % factor), rounding=ROUND_UP)
  try:
    sp = str(num).split('.')
    if len(sp) > 1 and not 'e-' in str(num):
      return float('.'.join([sp[0], sp[1][:digits]]))
    elif 'e-' in str(num):
      return float(0)
  except:
    sp = str(Decimal(num)).split('.')
    if len(sp) > 1:
      return float('.'.join([sp[0], sp[1][:digits]]))
  return float(num)


def normal_round(n, decimals=0, truncar=False):
  n = float( n )
  expoN = n * 10 ** decimals
  if truncar or (abs(expoN) - abs(math.floor(expoN)) < 0.499999):
      return math.floor(expoN) / 10 ** decimals
  return math.ceil(expoN) / 10 ** decimals

def sat_round(n, decimals=0, truncar=False):
  n = float( n )
  expoN = n * 10 ** decimals
  if truncar:
      return math.floor(expoN) / 10 ** decimals
  return math.ceil(expoN) / 10 ** decimals


def validacion_adicionales(xml_etree, xml_string=None):

  # namespace_dicc = {
  #   'cfdi': 'http://www.sat.gob.mx/cfd/3',
  #   'pago10': 'http://www.sat.gob.mx/Pagos',
  #   'cce11': 'http://www.sat.gob.mx/ComercioExterior11',
  # }

  print('Prefijos', xml_etree.nsmap)
  namespace_dicc = deepcopy(xml_etree.nsmap)
  namespace_dicc.update({
    'pago10': 'http://www.sat.gob.mx/Pagos',
    'cce11': 'http://www.sat.gob.mx/ComercioExterior11',
  })

  print('Fecha') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  emission_date = xml_etree.get('Fecha')
  if not re.match('^(20[1-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])$', emission_date):
    return False, 'CFDI33101'

  catalogos_obj = Catalogos(emission_date)

  sello = xml_etree.get('Sello')
  certificado = xml_etree.get('Certificado')
  try:
    print('Certificado') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    pattern = '^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$'
    if not re.match(pattern, certificado):
      return False, 'CFDI33105'
    split_string_cert = [certificado[i:i+64] for i in range(0, len(certificado), 64)]
    l = [x + "\n"for x in split_string_cert]
    split_string_cert = l
    split_string_cert = "".join(split_string_cert)
    certificado = "-----BEGIN CERTIFICATE-----\n" +  split_string_cert + "-----END CERTIFICATE-----"
    x509_cert = M2Crypto.X509.load_cert_string(certificado, M2Crypto.X509.FORMAT_PEM)
  except:
    return False, 'CFDI33105'
  try:
    print('Sello') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    #seal_validator = SealValidator(sello, x509_cert, None, etree.tostring(xml_etree))
    #original_string = seal_validator.original_string
    #result = seal_validator.is_valid()
    result = validacion_sello(sello, x509_cert, xml_string)
    print('CadenaOriginal') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    #print(original_string) if settings.VERBOSE_EXTRA_VALIDATIONS else None
    #if not result["success"]:      
    if not result:      
      return False, 'CFDI33102'
  except:
    return False, 'CFDI33102'

  print('FormaPago') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  forma_pago = xml_etree.get('FormaPago')
  complemento_pagos = xml_etree.xpath('//cfdi:Complemento/pago10:Pagos', namespaces=namespace_dicc)
  complemento_cce11 = xml_etree.xpath('//cfdi:Complemento/cce11:ComercioExterior', namespaces=namespace_dicc)
  if complemento_pagos and forma_pago:
    return False, 'CFDI33103'
  if forma_pago and not catalogos_obj.validar('FormaPago', forma_pago):
    return False, 'CFDI33104'

  print('SubTotal') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  subtotal = xml_etree.get('SubTotal')
  descuento = xml_etree.get('Descuento')
  moneda = xml_etree.get('Moneda')
  try:
    subtotal_dec_len = len(subtotal.split('.')[-1]) if subtotal and len(subtotal.split('.')[-1]) > 0 and len(subtotal.split('.'))>1 else 0
    descuento_dec_len = len(descuento.split('.')[-1]) if descuento and len(descuento.split('.')[-1]) > 0 and len(descuento.split('.'))>1 else 0     
    moneda_obj = catalogos_obj.obtener('Moneda', moneda)        
    if not moneda_obj or not catalogos_obj.validar('Moneda', moneda):
      return False, 'CFDI33112'
    if subtotal and subtotal_dec_len and (moneda_obj.decimales or moneda_obj.decimales==0)  and subtotal_dec_len > moneda_obj.decimales:
      return False, 'CFDI33106'
    if descuento and descuento_dec_len and (moneda_obj.decimales or moneda_obj.decimales==0) and descuento_dec_len > moneda_obj.decimales:
      return False, 'CFDI33111'
  except Exception as e:
    return False, 'CFDI33106'

  print('TipoDeComprobante') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  tipo_de_comprobante = xml_etree.get('TipoDeComprobante')
  tipo_de_comprobante_obj = catalogos_obj.obtener('TipoDeComprobante', tipo_de_comprobante)
  if tipo_de_comprobante in ('I', 'E', 'N'):
    subtotal_sum = Decimal(xml_etree.xpath('sum(//cfdi:Concepto/@Importe)', namespaces=namespace_dicc))
    if normal_round(subtotal, moneda_obj.decimales) != normal_round(subtotal_sum, moneda_obj.decimales):
      print(subtotal)
      print(moneda_obj.decimales)
      print(normal_round(subtotal, moneda_obj.decimales))
      print('****'*6)
      print(subtotal_sum)
      print(normal_round(subtotal_sum, moneda_obj.decimales))
      normal_round(subtotal_sum, moneda_obj.decimales)
      return False, 'CFDI33107'
  elif tipo_de_comprobante in ('T', 'P'):
    if float(subtotal) != 0.0:
      return False, 'CFDI33108'
    if False and descuento or xml_etree.xpath('boolean(.//cfdi:Concepto/@Descuento)', namespaces=namespace_dicc): ### Se agrego el False para que no sen las mismas validaciones que FK ###
      return False, 'CFDI33992'

  print('CondicionesDePago') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  condiciones_pago = xml_etree.get('CondicionesDePago')
  if tipo_de_comprobante in ('T', 'P', 'N'):
    if False and condiciones_pago: ### Se agrego el False para que no sen las mismas validaciones que FK ###
      return False, 'CFDI33991'
    if False and xml_etree.xpath('//cfdi:Impuestos', namespaces=namespace_dicc): ### Se agrego el False para que no sen las mismas validaciones que FK ###
      return False, 'CFDI33993'

  print('Descuento') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  if descuento and float(descuento) > float(subtotal):
    return False, 'CFDI33109'
  if tipo_de_comprobante in ('I', 'E', 'N') and ((xml_etree.xpath('//cfdi:Concepto/@Descuento', namespaces=namespace_dicc) and not descuento) or (not xml_etree.xpath('//cfdi:Concepto/@Descuento', namespaces=namespace_dicc) and descuento)):
    return False, 'CFDI33110'
  if descuento and tipo_de_comprobante in ('I', 'E', 'N'):
    descuento_sum = float(xml_etree.xpath('sum(//cfdi:Concepto/@Descuento)', namespaces=namespace_dicc))
    if (trunc(str(descuento), moneda_obj.decimales) != trunc(str(descuento_sum), moneda_obj.decimales)) and (trunc(str(descuento), moneda_obj.decimales, True) != trunc(str(descuento_sum), moneda_obj.decimales, True)):
      return False, 'CFDI33110'  
  elif descuento:
    return False, 'CFDI33110'

  print('TipoCambio') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  confirmacion = xml_etree.get('Confirmacion')
  tipo_cambio = xml_etree.get('TipoCambio')
  if moneda == 'MXN' and tipo_cambio and tipo_cambio != '1':
    return False, 'CFDI33113'
  if moneda not in ('MXN', 'XXX') and not tipo_cambio:
    return False, 'CFDI33114'
  if moneda == 'XXX' and tipo_cambio:
    return False, 'CFDI33115'
  if tipo_cambio and not re.match('^[0-9]{1,14}(.([0-9]{1,6}))?$', tipo_cambio):
    return False, 'CFDI33116'
  if tipo_cambio:
    tipo_cambio_minimo = float(moneda_obj.tipo_cambio) * ((100.0 - float(moneda_obj.variacion.replace('%', ''))) / 100.0)
    tipo_cambio_maximo = float(moneda_obj.tipo_cambio) * ((100.0 + float(moneda_obj.variacion.replace('%', ''))) / 100.0)
    if (float(tipo_cambio) <= tipo_cambio_minimo or float(tipo_cambio) >= tipo_cambio_maximo) and not confirmacion:
      return False, 'CFDI33117'

  print('Total') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  total = xml_etree.get('Total')
  total_len = len(total.split('.')[-1]) if len(total.split('.')) > 1 else 0
  total_impuestos_trasladados = '0.0'
  total_impuestos_retenidos = '0.0'
  try:
    total_impuestos_trasladados = xml_etree.xpath('//cfdi:Impuestos/@TotalImpuestosTrasladados', namespaces=namespace_dicc)[0]
  except:
    pass
  try:
    total_impuestos_retenidos = xml_etree.xpath('//cfdi:Impuestos/@TotalImpuestosRetenidos', namespaces=namespace_dicc)[0]
  except:
    pass
  total_calculated = Decimal(subtotal) + Decimal(total_impuestos_trasladados) - Decimal(total_impuestos_retenidos)
  total_calculated -= Decimal(descuento) if descuento else Decimal(0.0)  
  implocal_trasladados = '0.0'
  implocal_retenidos = '0.0'
  try:
    implocal_trasladados = xml_etree.xpath('//cfdi:Complemento/implocal:ImpuestosLocales/@TotaldeTraslados', namespaces=namespace_dicc)[0]
  except:
    pass
  try:
    implocal_retenidos = xml_etree.xpath('//cfdi:Complemento/implocal:ImpuestosLocales/@TotaldeRetenciones', namespaces=namespace_dicc)[0]
  except:
    pass
  total_calculated += Decimal(implocal_trasladados)
  total_calculated -= Decimal(implocal_retenidos)
  total = Decimal(total)
  total_calculated = Decimal(total_calculated)
  if float(total) != trunc(str(total_calculated), moneda_obj.decimales) or total_len > moneda_obj.decimales:
    return False, 'CFDI33118'
  
  print('TipoDeComprobante') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  if tipo_de_comprobante == 'N':
    total_maximo = 0.0
    total_separacion_indemnizacion = xml_etree.xpath('//nomina12:Percepciones/@TotalSeparacionIndemnizacion', namespaces=namespace_dicc)
    total_jubilacion_pension_retiro = xml_etree.xpath('//nomina12:Percepciones/@TotalJubilacionPensionRetiro', namespaces=namespace_dicc)
    if (total_separacion_indemnizacion or total_jubilacion_pension_retiro) and tipo_de_comprobante_obj:
      total_maximo += float(tipo_de_comprobante_obj.maximo.split('|')[1].replace(',',''))
    elif tipo_de_comprobante_obj:
      total_maximo += float(tipo_de_comprobante_obj.maximo.split('|')[0].replace(',',''))
  elif tipo_de_comprobante_obj:
    total_maximo = float(tipo_de_comprobante_obj.maximo.replace(',',''))
  if tipo_de_comprobante_obj and total > total_maximo and not confirmacion:
    return False, 'CFDI33119'
  if not catalogos_obj.validar('TipoDeComprobante', tipo_de_comprobante):
    return False, 'CFDI33120'

  print('MetodoPago') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  metodo_pago = xml_etree.get('MetodoPago')
  if metodo_pago and not catalogos_obj.validar('MetodoPago', metodo_pago):
    return False, 'CFDI33121'
  if metodo_pago == 'PIP' and tipo_de_comprobante in ('I', 'E') and not complemento_pagos:
    return False, 'CFDI33122'
  if tipo_de_comprobante in ('T', 'P') and metodo_pago:
    return False, 'CFDI33123'
  if complemento_pagos and metodo_pago:
    return False, 'CFDI33124'

  print('MetodoPago FormaPago') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  if tipo_de_comprobante in ('I', 'E', 'N'):
    if not forma_pago or not metodo_pago:
      return False, 'CFDI33107A'
  if tipo_de_comprobante in ('P', 'T'):
    if forma_pago or metodo_pago:
      return False, 'CFDI33107B'

  print('LugarExpedicion') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  lugar_expedicion = xml_etree.get('LugarExpedicion')
  if not catalogos_obj.validar('CodigoPostal', lugar_expedicion):
    return False, 'CFDI33125'

  if tipo_cambio and float(tipo_cambio) >= tipo_cambio_minimo and float(tipo_cambio) <= tipo_cambio_maximo and confirmacion:
    return False, 'CFDI33126'
  if total <= total_maximo and confirmacion:
    return False, 'CFDI33126'

  print('Confirmacion') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  taxpayer_id = xml_etree.xpath('//cfdi:Emisor/@Rfc', namespaces=namespace_dicc)[0]
  if confirmacion:
    try:
      confirmacion_obj = Confirmation.objects.get(taxpayer_id=taxpayer_id, code=confirmacion)
      if not confirmacion_obj:
        return False, 'CFDI33127'
      if confirmacion_obj.status == 'U':
        return False, 'CFDI33128'
      if (confirmacion_obj.added + datetime.timedelta(days=5)) < datetime.datetime.now():        
        return False, 'CFDI33128.1'
    except:
      return False, 'CFDI33127'

  print('CfdiRelacionados:TipoRelacion') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  tipo_relacion = xml_etree.xpath('string(//cfdi:CfdiRelacionados/@TipoRelacion)', namespaces=namespace_dicc)
  if tipo_relacion and not catalogos_obj.validar('TipoRelacion', tipo_relacion):
    return False, 'CFDI33129'

  print('RegimenFiscal') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  regimen_fiscal = xml_etree.xpath('string(//cfdi:Emisor/@RegimenFiscal)', namespaces=namespace_dicc)
  if not catalogos_obj.validar('RegimenFiscal', regimen_fiscal):
    return False, 'CFDI33130'
  persona = 'fisica' if len(taxpayer_id)==13 else 'moral'
  if not catalogos_obj.validar('RegimenFiscal', regimen_fiscal, persona=persona):
    return False, 'CFDI33131'

  print('Receptor:Rfc') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  rfc_re = xml_etree.xpath('//cfdi:Receptor/@Rfc', namespaces=namespace_dicc)[0]  
  if rfc_re not in ('XAXX010101000', 'XEXX010101000'):
    if not LRFC.objects.filter(rfc=rfc_re).exists():
      return False, 'CFDI33132'

  print('ResidenciaFiscal') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  residencia_fiscal = xml_etree.xpath('string(//cfdi:Receptor/@ResidenciaFiscal)', namespaces=namespace_dicc)
  numregidtrib = xml_etree.xpath('string(//cfdi:Receptor/@NumRegIdTrib)', namespaces=namespace_dicc)
  if (LRFC.objects.filter(rfc=rfc_re).exists() or rfc_re == 'XAXX010101000') and residencia_fiscal:
    return False, 'CFDI33134'
  if residencia_fiscal and not catalogos_obj.validar('Pais', residencia_fiscal):
    return False, 'CFDI33133'
  if residencia_fiscal and residencia_fiscal == 'MEX':
    return False, 'CFDI33135'
  if rfc_re == 'XEXX010101000' and (numregidtrib or complemento_cce11) and not residencia_fiscal:
    return False, 'CFDI33136'

  print('NumRegIdTrib') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  if (LRFC.objects.filter(rfc=rfc_re).exists() or rfc_re == 'XAXX010101000') and numregidtrib:
    return False, 'CFDI33137'
  if rfc_re == 'XEXX010101000' and complemento_cce11 and not numregidtrib:
    return False, 'CFDI33138'
  if numregidtrib and not catalogos_obj.validar('Pais', residencia_fiscal, _type='rit', rit=numregidtrib):
    return False, 'CFDI33139'

  print('UsoCFDI') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  usocfdi = xml_etree.xpath('//cfdi:Receptor/@UsoCFDI', namespaces=namespace_dicc)[0]
  if not catalogos_obj.validar('UsoCFDI', usocfdi):
    return False, 'CFDI33140'
  persona = 'fisica' if len(rfc_re)==13 else 'moral'
  if not catalogos_obj.validar('UsoCFDI', usocfdi, persona=persona):
    return False, 'CFDI33141'
  
  print('Conceptos') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  conceptos = xml_etree.xpath('//cfdi:Conceptos/cfdi:Concepto', namespaces=namespace_dicc)
  conceptos_len = len(conceptos)  
  success, error = validate_conceptos(conceptos, tipo_de_comprobante, moneda_obj, complemento_cce11, xml_etree=xml_etree)
  if not success:
    return False, error

  print('Impuestos') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  impuestos = xml_etree.xpath('./cfdi:Impuestos', namespaces=namespace_dicc)
  impuestos_conceptos_t = xml_etree.xpath('./cfdi:Conceptos/cfdi:Concepto/cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@TipoFactor!="Exento"]', namespaces=namespace_dicc)
  impuestos_conceptos_r = xml_etree.xpath('./cfdi:Conceptos/cfdi:Concepto/cfdi:Impuestos/cfdi:Retenciones', namespaces=namespace_dicc)
  if not impuestos and (len(impuestos_conceptos_t) or len(impuestos_conceptos_r)):
    return False, 'CFDI33183'

  if impuestos:
    impuestos = impuestos[0]
    if tipo_de_comprobante in ('T', 'P'):
      return False, 'CFDI33179'
    
    print('Impuestos:TotalImpuestosRetenidos') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    total_impuestos_retenidos = impuestos.get('TotalImpuestosRetenidos')
    try:
      total_impuestos_retenidos_dec_len = 0
      if total_impuestos_retenidos and '.' in total_impuestos_retenidos:
        total_impuestos_retenidos_dec_len = len(total_impuestos_retenidos.split('.')[1]) if total_impuestos_retenidos else 0
      if total_impuestos_retenidos and total_impuestos_retenidos_dec_len > moneda_obj.decimales and (moneda_obj.decimales or moneda_obj.decimales==0) and total_impuestos_retenidos_dec_len:
        return False, 'CFDI33180'
    except Exception as e:
      return False, 'CFDI33180'
    if total_impuestos_retenidos and trunc(float(total_impuestos_retenidos), moneda_obj.decimales) != trunc(impuestos.xpath('sum(./cfdi:Retenciones/cfdi:Retencion/@Importe)', namespaces=namespace_dicc), moneda_obj.decimales) and trunc(float(total_impuestos_retenidos), moneda_obj.decimales, True) != trunc(impuestos.xpath('sum(./cfdi:Retenciones/cfdi:Retencion/@Importe)', namespaces=namespace_dicc), moneda_obj.decimales, True):
      return False, 'CFDI33181'

    print('Impuestos:TotalImpuestosTrasladados') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    total_impuestos_trasladados = impuestos.get('TotalImpuestosTrasladados')
    try:
      total_impuestos_trasladados_dec_len = 0
      if total_impuestos_trasladados and '.' in total_impuestos_trasladados:
        total_impuestos_trasladados_dec_len = len(total_impuestos_trasladados.split('.')[1]) if total_impuestos_trasladados else 0
      if total_impuestos_trasladados and total_impuestos_trasladados_dec_len > moneda_obj.decimales and (moneda_obj.decimales or moneda_obj.decimales==0) and total_impuestos_trasladados_dec_len:
        return False, 'CFDI33182'    
    except Exception as e:
      return False, 'CFDI33182'
    if total_impuestos_trasladados and trunc(float(total_impuestos_trasladados), moneda_obj.decimales) != trunc(impuestos.xpath('sum(./cfdi:Traslados/cfdi:Traslado/@Importe)', namespaces=namespace_dicc), moneda_obj.decimales) and trunc(float(total_impuestos_trasladados), moneda_obj.decimales, True) != trunc(impuestos.xpath('sum(./cfdi:Traslados/cfdi:Traslado/@Importe)', namespaces=namespace_dicc), moneda_obj.decimales, True):
      return False, 'CFDI33183'

    print('Impuestos:Retenciones') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    retenciones = impuestos.xpath('./cfdi:Retenciones/cfdi:Retencion', namespaces=namespace_dicc)
    for retencion in retenciones:
      if not total_impuestos_retenidos:
        return False, 'CFDI33184'
      impuesto = retencion.get('Impuesto')
      importe = retencion.get('Importe')

      print('Retencion:Impuesto') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      if not catalogos_obj.validar('Impuesto', impuesto, tipo='retencion'):
        return False, 'CFDI33185'          
      retencion_impuesto_count = impuestos.xpath('count(./cfdi:Retenciones/cfdi:Retencion[@Impuesto="%s"])' % impuesto, namespaces=namespace_dicc)
      if retencion_impuesto_count > 1:
        return False, 'CFDI33186'
      importe_dec_len = len(importe.split('.')[-1]) if len(importe.split('.')) > 1 else 0
      if False and importe_dec_len != moneda_obj.decimales and (moneda_obj.decimales or moneda_obj.decimales==0): ### SAT removio esta validacion
        return False, 'CFDI33188'
      retencion_count = xml_etree.xpath('count(//cfdi:Conceptos/cfdi:Concepto/cfdi:Impuestos/cfdi:Retenciones/cfdi:Retencion[@Impuesto="%s"]/@Importe)' % impuesto, namespaces=namespace_dicc)
      importe_sum = xml_etree.xpath('sum(//cfdi:Conceptos/cfdi:Concepto/cfdi:Impuestos/cfdi:Retenciones/cfdi:Retencion[@Impuesto="%s"]/@Importe)' % impuesto, namespaces=namespace_dicc)
      if not retencion_count or not(trunc(float(importe), 6) == trunc(float(importe_sum), 6) or trunc(float(importe), moneda_obj.decimales) == trunc(float(importe_sum), moneda_obj.decimales, 'EVEN')):
        return False, 'CFDI33189'

    print('Impuestos:Traslados') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    traslados = impuestos.xpath('./cfdi:Traslados/cfdi:Traslado', namespaces=namespace_dicc)
    for traslado in traslados:
      if not total_impuestos_trasladados:
        return False, 'CFDI33190'
      impuesto = traslado.get('Impuesto')
      importe = traslado.get('Importe')
      tasaocuota = traslado.get('TasaOCuota')
      tipofactor = traslado.get('TipoFactor')

      print('Traslado:Impuesto') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      if not catalogos_obj.validar('Impuesto', impuesto, tipo='traslado'):
        return False, 'CFDI33191'
      traslado_impuesto_count = impuestos.xpath('count(./cfdi:Traslados/cfdi:Traslado[@Impuesto="%s" and @TipoFactor="%s" and @TasaOCuota="%s"])' % (impuesto, tipofactor, tasaocuota), namespaces=namespace_dicc)
      if traslado_impuesto_count > 1:
        return False, 'CFDI33192'
      print('Traslado:TasaOCuota') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      if not catalogos_obj.validar('TasaOCuota', tasaocuota, impuesto=impuesto, tipofactor=tipofactor, tipo='traslado'):
        return False, 'CFDI33193'
      importe_dec_len = len(importe.split('.')[-1]) if len(importe.split('.')) > 1 else 0
      if False and importe_dec_len != moneda_obj.decimales and (moneda_obj.decimales or moneda_obj.decimales==0): ### SAT removio esta validacion
        return False, 'CFDI33194'
      print('Traslado:Importe') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      traslado_count = xml_etree.xpath('count(//cfdi:Conceptos/cfdi:Concepto/cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@Impuesto="%s" and @TasaOCuota="%s" and @TipoFactor="%s"]/@Importe)' % (impuesto, tasaocuota, tipofactor), namespaces=namespace_dicc)
      importe_sum = xml_etree.xpath('sum(//cfdi:Conceptos/cfdi:Concepto/cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@Impuesto="%s" and @TasaOCuota="%s" and @TipoFactor="%s"]/@Importe)' % (impuesto, tasaocuota, tipofactor), namespaces=namespace_dicc)
      if not traslado_count or not (trunc(str(importe), 6) == trunc(str(importe_sum), 6) or trunc(str(importe), moneda_obj.decimales) == trunc(str(importe_sum), moneda_obj.decimales, 'EVEN')):
        return False, 'CFDI33195'
  
  conceptos_fronterizos = xml_etree.xpath('.//cfdi:Conceptos/cfdi:Concepto/cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@TasaOCuota = 0.08 and @Impuesto = "002"]/ancestor::cfdi:Concepto', namespaces=namespace_dicc)
  if len(conceptos_fronterizos):
    taxpayer_id = xml_etree.xpath('//cfdi:Emisor/@Rfc', namespaces=namespace_dicc)[0]
    certificate_num = xml_etree.get('NoCertificado')
    lco_fronterizo = LCO.objects.filter(rfc=taxpayer_id, serial=certificate_num, validez='2').exists()
    if not lco_fronterizo:
      return False, 'CFDI33196'
    for concepto_fronterizo in conceptos_fronterizos:
      prodserv = concepto_fronterizo.get('ClaveProdServ')
      prodserv_fronterizo = catalogos_obj.validar('ClaveProdServ', prodserv, tipo='fronterizo')
      if not (prodserv == '01010101' and rfc_re == 'XAXX010101000'):
        if not prodserv_fronterizo:
          return False, 'CFDI33197'
    expedicion_fronterizo = catalogos_obj.validar('CodigoPostal', lugar_expedicion, tipo='fronterizo')
    if not expedicion_fronterizo:
      return False, 'CFDI33198'

  return True, None




def validate_conceptos(conceptos, tipo_de_comprobante, moneda_obj, complemento_cce11=None, xml_etree=None):
  #namespace_dicc = {'cfdi': 'http://www.sat.gob.mx/cfd/3', 'pago10': 'http://www.sat.gob.mx/Pagos', 'cce11': 'http://www.sat.gob.mx/ComercioExterior11', 'nom12' : 'http://www.sat.gob.mx/nomina12', 'implocal': 'http://www.sat.gob.mx/implocal'}
  namespace_dicc = deepcopy(xml_etree.nsmap)
  namespace_dicc.update({
    'pago10': 'http://www.sat.gob.mx/Pagos',
    'cce11': 'http://www.sat.gob.mx/ComercioExterior11',
  })
  total_conceptos = len(conceptos)
  traslado_concepto_list = []
  retencion_concepto_list = []
  catalogos_obj = Catalogos(xml_etree.get('Fecha'))

  print('Conceptos') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  for no, concepto in enumerate(conceptos):
    claveprodserv = concepto.get('ClaveProdServ')
    claveunidad = concepto.get('ClaveUnidad')
    valor_unitario = concepto.get('ValorUnitario')
    importe = concepto.get('Importe')
    descuento = concepto.get('Descuento')
    print('Concepto:ClaveProdServ') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    claveprodserv_obj = catalogos_obj.obtener('ClaveProdServ', claveprodserv)
    if not claveprodserv_obj:
      return False, 'CFDI33142'
    if claveprodserv_obj and claveprodserv_obj.complemento and 'Opcional' not in (claveprodserv_obj.complemento):
      prefix = COMPLEMENTS_NAMESPACES[claveprodserv_obj.complemento]['prefix']
      tag = COMPLEMENTS_NAMESPACES[claveprodserv_obj.complemento]['tag']
      xmlns = COMPLEMENTS_NAMESPACES[claveprodserv_obj.complemento]['xmlns']          
      namespace_dicc[prefix] = xmlns          
      complement = xml_etree.xpath('//%s:%s' % (prefix, tag), namespaces=namespace_dicc)
      if not complement:
        return False, 'CFDI33143'
    if claveprodserv_obj and claveprodserv_obj.iva_trasladado.encode('utf8') == 'Sí':
      if not concepto.xpath('./cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@Impuesto=002]', namespaces=namespace_dicc):
        return False, 'CFDI33144'
    if claveprodserv_obj and claveprodserv_obj.ieps_trasladado.encode('utf8') == 'Sí':
      if not concepto.xpath('./cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@Impuesto=003]', namespaces=namespace_dicc):
        return False, 'CFDI33144'

    print('Concepto:ClaveUnidad') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    if not catalogos_obj.validar('ClaveUnidad', claveunidad):
      return False, 'CFDI33145'

    print('Concepto:ValorUnitario') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    valor_unitario_dec_len = len(valor_unitario.split('.')[-1]) if len(valor_unitario.split('.')) > 1 else 0
    if False and (moneda_obj.decimales or moneda_obj.decimales==0) and valor_unitario_dec_len and valor_unitario_dec_len != moneda_obj.decimales: ### SAT removio esta validacion
      return False, 'CFDI33146'
    if tipo_de_comprobante in ('I', 'E', 'N') and float(valor_unitario) <= 0.0:
      return False, 'CFDI33147'

    print('Concepto:Importe') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    importe_dec_len = len(importe.split('.')[-1]) if len(importe.split('.')) > 1 else 0
    if False and importe_dec_len and importe_dec_len != moneda_obj.decimales and (moneda_obj.decimales or moneda_obj.decimales==0): ### SAT removio esta validacion
      return False, 'CFDI33148'

    print('Concepto:Cantidad') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    cantidad = concepto.get('Cantidad')    
    try:
      cantidad_decimales = len(cantidad.split('.')[-1])
    except:
      cantidad_decimales = 0    
    try:
      valorunitario_decimales = len(valor_unitario.split('.')[-1])
    except:
      valorunitario_decimales = 0      
    inferior = (float(cantidad) - (10**-cantidad_decimales) / 2.0) * (float(valor_unitario) - (10**-valorunitario_decimales) / 2.0 )
    superior =  (float(cantidad) + (10**-cantidad_decimales) / 2.0 - (10**-12)) * (float(valor_unitario) + (10**-valorunitario_decimales) / 2.0 - 10**-12)
    inferior = trunc(inferior, moneda_obj.decimales)
    superior = trunc(superior, moneda_obj.decimales, True)
    if not (float(importe) >= inferior and float(importe) <= superior):
      return False, 'CFDI33149'

    print('Concepto:Descuento') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    if descuento:
      descuento_dec_len = len(descuento.split('.')[-1]) if len(descuento.split('.')) > 1 else 0
      if descuento_dec_len > importe_dec_len:
        return False, 'CFDI33150'
      if float(descuento) > float(importe) or float(descuento) < 0:
        return False, 'CFDI33151'

    print('Concepto:Impuestos') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    impuestos = concepto.xpath('./cfdi:Impuestos', namespaces=namespace_dicc)
    traslados = concepto.xpath('./cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado', namespaces=namespace_dicc)
    retenciones = concepto.xpath('./cfdi:Impuestos/cfdi:Retenciones/cfdi:Retencion', namespaces=namespace_dicc)
    if impuestos and not (traslados or retenciones):
      return False, 'CFDI33152'

    print('Concepto:Impuestos:Traslados') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    for traslado in traslados:
      base = traslado.get('Base')
      impuesto = traslado.get('Impuesto')
      tipo_factor = traslado.get('TipoFactor')
      tasaocuota = traslado.get('TasaOCuota')
      importe = traslado.get('Importe')

      print('Traslado:Base') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      base_dec_len = len(base.split('.')[-1]) if len(base.split('.'))>1 else 0
      if False and base_dec_len and base_dec_len != moneda_obj.decimales and (moneda_obj.decimales or moneda_obj.decimales==0): ### SAT removio esta validacion
        return False, 'CFDI33153'
      if float(base) <= 0.0:
        return False, 'CFDI33154'

      print('Traslado:Impuesto') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      if not catalogos_obj.validar('Impuesto', impuesto, tipo='traslado'):
        return False, 'CFDI33155'

      print('Traslado:TipoFactor') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      if not catalogos_obj.validar('TipoFactor', tipo_factor):
        return False, 'CFDI33156'
      if tipo_factor == 'Exento' and (tasaocuota or importe):
        return False, 'CFDI33157'
      if tipo_factor in ('Tasa', 'Cuota') and not (tasaocuota and importe):
        return False, 'CFDI33158'

      print('Traslado:TasaOCuota') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      if tasaocuota and not catalogos_obj.validar('TasaOCuota', tasaocuota, impuesto=impuesto, tipofactor=tipo_factor, tipo='traslado'):
        return False, 'CFDI33159'

      if importe:
        print('Traslado:Importe') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        if False and float(importe) < 0: ### Se agrego el False para que no sen las mismas validaciones que FK ###
          return False, 'CFDI33994'
        importe_dec_len = len(importe.split('.')[-1]) if '.' in importe else 0
        if False and importe and importe_dec_len != moneda_obj.decimales and (moneda_obj.decimales or moneda_obj.decimales==0): ### SAT removio esta validacion
          return False, 'CFDI33160'          
        inferior = (float(base) - (10**-base_dec_len) / 2.0) * float(tasaocuota)
        superior =  (float(base) + (10**-base_dec_len) / 2.0 - (10**-12)) * float(tasaocuota)
        inferior = sat_round(inferior, importe_dec_len, True)
        superior = sat_round(superior, importe_dec_len)          
        if not (float(importe) >= inferior and float(importe) <= superior):
          return False, 'CFDI33161'
        impuesto_concepto = '{}{}{}'.format(impuesto, tipo_factor, tasaocuota)
        if impuesto_concepto not in traslado_concepto_list:
          traslado_concepto_list.append(impuesto_concepto)
          impuesto_concepto_node = xml_etree.xpath('boolean(//cfdi:Comprobante/cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@Impuesto="%s" and @TipoFactor="%s" and @TasaOCuota="%s"])' % (impuesto, tipo_factor, tasaocuota), namespaces=namespace_dicc)
          if not impuesto_concepto_node:
            return False, 'CFDI33195'

    print('Concepto:Impuestos:Retenciones') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    for retencion in retenciones:      
      base = retencion.get('Base')
      impuesto = retencion.get('Impuesto')
      tipo_factor = retencion.get('TipoFactor')
      tasaocuota = retencion.get('TasaOCuota')
      importe = retencion.get('Importe')

      print('Retencion:Base') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      base_dec_len = len(base.split('.')[-1])
      if False and base_dec_len != moneda_obj.decimales and (moneda_obj.decimales or moneda_obj.decimales==0): ### SAT removio esta validacion
        return False, 'CFDI33162'
      if float(base) <= 0.0:
        return False, 'CFDI33163'
      
      print('Retencion:Impuesto') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      if not catalogos_obj.validar('Impuesto', impuesto, tipo='retencion'):
        return False, 'CFDI33164'

      print('Retencion:TipoFactor') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      if not catalogos_obj.validar('TipoFactor', tipo_factor):
        return False, 'CFDI33165'
      if tipo_factor == 'Exento':
        return False, 'CFDI33166'          

      print('Retencion:TasaOCuota') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      if not catalogos_obj.validar('TasaOCuota', tasaocuota, impuesto=impuesto, tipofactor=tipo_factor, tipo='retencion'):
        return False, 'CFDI33167'

      print('Retencion:Importe') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      importe_dec_len = len(importe.split('.')[-1])
      if False and importe_dec_len != moneda_obj.decimales and (moneda_obj.decimales or moneda_obj.decimales==0): ### SAT removio esta validacion
        return False, 'CFDI33168'          
      inferior = (float(base) - (10**-base_dec_len) / 2.0) * float(tasaocuota)
      superior =  (float(base) + (10**-base_dec_len) / 2.0 - (10**-12)) * float(tasaocuota)
      inferior = sat_round(inferior, importe_dec_len, True)
      superior = sat_round(superior, importe_dec_len)
      if not (float(importe) >= inferior and float(importe) <= superior):
        return False, 'CFDI33169'
      if impuesto not in retencion_concepto_list:
        retencion_concepto_list.append(impuesto)
        retencion_impuesto_c = xml_etree.xpath('boolean(//cfdi:Comprobante/cfdi:Impuestos/cfdi:Retenciones/cfdi:Retencion[@Impuesto="%s"])' % impuesto, namespaces=namespace_dicc)
        if not retencion_impuesto_c:
          return False, 'CFDI33189'

    print('InformacionAduanera:NumeroPedimento') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    numero_pedimentos = concepto.xpath('./cfdi:InformacionAduanera/@NumeroPedimento', namespaces=namespace_dicc)
    for numero_pedimento in numero_pedimentos:
      try:
        numero_pedimento_split = numero_pedimento.split('  ')
        ano = numero_pedimento_split[0]
        aduana = numero_pedimento_split[1]
        patente = numero_pedimento_split[2]
        consecutivo = numero_pedimento_split[3]
        now = datetime.datetime.now()
        if int(ano) > int(str(now.year)[-2:]) or int(ano) < (int(str(now.year)[-2:]) - 10):
          return False, 'CFDI33170'
        if not catalogos_obj.validar('Aduana', aduana):
          return False, 'CFDI33170'
        if not catalogos_obj.validar('PatenteAduanal', patente):
          return False, 'CFDI33170'
        numpedimentoaduana_obj = catalogos_obj.obtener('NumeroPedimentoAduana', aduana, patente=patente, ano=f'20{ano}')
        if not numpedimentoaduana_obj:
          return False, 'CFDI33170'
        if int(consecutivo) < 1 or int(consecutivo) > int(numpedimentoaduana_obj.cantidad):
          return False, 'CFDI33170'
        if complemento_cce11:
          return False, 'CFDI33171'
      except Exception as e:
        return False, 'CFDI33170'

    print('InformacionAduanera:Parte') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    parte = concepto.xpath('//cfdi:Parte', namespaces=namespace_dicc)
    if parte:
      parte = parte[0]
      claveprodserv = parte.get('ClaveProdServ')
      valor_unitario = parte.get('ValorUnitario')
      importe = parte.get('Importe')
      cantidad = parte.get('Cantidad')
      if not catalogos_obj.validar('ClaveProdServ', claveprodserv):
        return False, 'CFDI33172'
      if valor_unitario:
        valor_unitario_dec_len = len(valor_unitario.split('.')[-1])
        if False and valor_unitario_dec_len != moneda_obj.decimales and (moneda_obj.decimales or moneda_obj.decimales==0): ### SAT removio esta validacion
          return False, 'CFDI33173'
        if float(valor_unitario) <= 0.0:
          return False, 'CFDI33174'
      if importe:
        importe_dec_len = len(importe.split('.')[-1])
        if False and importe_dec_len != moneda_obj.decimales and (moneda_obj.decimales or moneda_obj.decimales==0): ### SAT removio esta validacion
          return False, 'CFDI33175'
        if valor_unitario:
          cantidad_dec_len = len(cantidad.split('.')[-1])
          inferior = (float(cantidad) - (10**-cantidad_dec_len) / 2.0) * (float(valor_unitario) - (10**-valor_unitario_dec_len) / 2.0 )
          superior =  (float(cantidad) + (10**-cantidad_dec_len) / 2.0 - (10**-12)) * (float(valor_unitario) + (10**-valor_unitario_dec_len) / 2.0 - 10**-12)
          inferior = trunc(inferior, moneda_obj.decimales)
          superior = trunc(superior, moneda_obj.decimales, True)
          if not (float(importe) >= inferior and float(importe) <= superior):
            return False, 'CFDI33176'

      print('Parte:NumeroPedimento') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      numero_pedimento = parte.xpath('./cfdi:InformacionAduanera/@NumeroPedimento', namespaces=namespace_dicc)
      if numero_pedimento:            
        numero_pedimento_split = numero_pedimento[0].split('  ')
        ano = numero_pedimento_split[0]
        aduana = numero_pedimento_split[1]
        patente = numero_pedimento_split[2]
        consecutivo = numero_pedimento_split[3]
        now = datetime.datetime.now()
        if int(ano) > int(str(now.year)[-2:]) or int(ano) < (int(str(now.year)[-2:]) - 10):
          return False, 'CFDI33177'
        if not catalogos_obj.validar('Aduana', aduana):
          return False, 'CFDI33177'
        if not catalogos_obj.validar('PatenteAduanal', patente):
          return False, 'CFDI33177'
        numpedimentoaduana_obj = catalogos_obj.obtener('NumeroPedimento', aduana, patente=patente, ano=ano)
        if int(consecutivo) < 1 or int(consecutivo) > numpedimentoaduana_obj.cantidad:
          return False, 'CFDI33177'
        if complemento_cce11:
          return False, 'CFDI33178'
  return True, ''
