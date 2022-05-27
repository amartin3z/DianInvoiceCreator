from django.conf import settings

from app.sat.utils.validate import Catalogos
from app.sat.models import LCO, LRFC
from .adicionales import trunc, normal_round, sat_round
from decimal import Decimal

from app.sat.models import LRFC

def validacion_pagos10(xml_etree): 

  print('PAGOS10') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  namespace_dicc = {'cfdi': 'http://www.sat.gob.mx/cfd/3', 'pago10': 'http://www.sat.gob.mx/Pagos'}

  complement_pago10 = xml_etree.xpath('//cfdi:Complemento/pago10:Pagos', namespaces=namespace_dicc)

  catalogos_obj = Catalogos(xml_etree.get('Fecha'))

  tipo_de_comprobante = xml_etree.get('TipoDeComprobante')
  if len(complement_pago10) == 1:
    namespace_dicc = xml_etree.nsmap
    pago10 = complement_pago10[0]  
    if pago10.getparent().tag != '{http://www.sat.gob.mx/cfd/3}Complemento':
      return False, 'PAGO154'

    print('Comprobante') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    if tipo_de_comprobante != 'P':
      return False, 'CRP101'
    subtotal = xml_etree.get('SubTotal')
    if subtotal != '0':
      return False, 'CRP102'
    moneda = xml_etree.get('Moneda')
    if moneda != 'XXX':
        return False, 'CRP103'
    forma_pago = xml_etree.get('FormaPago')
    if forma_pago:
      return False, 'CRP104'
    metodo_pago = xml_etree.get('MetodoPago')
    if metodo_pago:
      return False, 'CRP105'
    condiciones_pago = xml_etree.get('CondicionesDePago')
    if condiciones_pago:
      return False, 'CRP106'
    descuento = xml_etree.get('Descuento')
    if descuento:
      return False, 'CRP107'
    tipo_cambio = xml_etree.get('TipoCambio')
    if tipo_cambio:
      return False, 'CRP108'
    total = xml_etree.get('Total')
    if total != '0':
        return False, 'CRP109'
    usocfdi = xml_etree.xpath('//cfdi:Receptor/@UsoCFDI', namespaces=namespace_dicc)[0]
    if usocfdi != 'P01':
      return False, 'CRP110'
    
    print('Comprobante:Conceptos') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    conceptos = xml_etree.xpath('//cfdi:Conceptos/cfdi:Concepto', namespaces=namespace_dicc)
    if len(conceptos) != 1:
      return False, 'CRP111'
    concepto = conceptos[0]
    concepto_children = concepto.getchildren()
    if len(concepto_children) > 1: 
      return False, 'CRP112'
    elif len(concepto_children) == 1:
      if concepto_children[0].tag != '{http://www.sat.gob.mx/cfd/3}ComplementoConcepto':
        return False, 'CRP112'
      elif len(concepto_children[0].getchildren()) !=  len(concepto.xpath('cfdi:ComplementoConcepto/terceros:PorCuentadeTerceros', namespaces=xml_etree.nsmap)):
        return False, 'CRP112'
    claveprodserv = concepto.get('ClaveProdServ')
    if claveprodserv != '84111506':
      return False, 'CRP113'
    no_identificacion = concepto.get('NoIdentificacion')
    if no_identificacion:
      return False, 'CRP114'
    cantidad = concepto.get('Cantidad')
    if cantidad != '1':
      return False, 'CRP115'
    clave_unidad = concepto.get('ClaveUnidad')
    if clave_unidad != 'ACT':
      return False, 'CRP116'
    unidad = concepto.get('Unidad')
    if unidad:
      return False, 'CRP117'
    descripcion = concepto.get('Descripcion')
    if descripcion != 'Pago':
      return False, 'CRP118'
    valor_unitario = concepto.get('ValorUnitario')
    if valor_unitario != '0':
      return False, 'CRP119'
    importe = concepto.get('Importe')
    if importe != '0':
      return False, 'CRP120'
    descuento = concepto.get('Descuento')
    if descuento:
      return False, 'CRP121'

    print('Comprobante:Impuestos') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    impuestos = xml_etree.xpath('//cfdi:Impuestos', namespaces=namespace_dicc)
    if impuestos:
      return False, 'CRP122'

    print('Pagos:Pago') if settings.VERBOSE_EXTRA_VALIDATIONS else None
    pagos = pago10.xpath('//pago10:Pago', namespaces=namespace_dicc)
    if len(pagos) == 0:
      return False, 'CRP996'

    for pago in pagos:

      print('Pago:FormaDePagoP') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      forma_pago_p = pago.get('FormaDePagoP')
      if forma_pago_p == '99':
        return False, 'CRP201'
      if not catalogos_obj.validar('FormaPago', forma_pago_p):
        return False, 'CRP201'
      print('Pagos:MonedaP') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      moneda_p = pago.get('MonedaP')
      if moneda_p == 'XXX':
        return False, 'CRP202'
      print('Pagos:TipoCambioP') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      tipo_cambio_p = pago.get('TipoCambioP')
      if moneda_p != 'MXN':
        if not tipo_cambio_p:
          return False, 'CRP203'
      elif tipo_cambio_p:
        return False, 'CRP204'
      moneda_obj = catalogos_obj.obtener('Moneda', moneda_p)
      print(moneda_p)
      print(moneda_obj)
      confirmacion = xml_etree.get('Confirmacion')
      if moneda_obj is None:
        return False, 'CRP205'
      if tipo_cambio_p:
        tipo_cambio_minimo = float(moneda_obj.tipo_cambio) * ((100.0 - float(moneda_obj.variacion.replace('%', ''))) / 100.0)
        tipo_cambio_maximo = float(moneda_obj.tipo_cambio) * ((100.0 + float(moneda_obj.variacion.replace('%', ''))) / 100.0)
        if (float(tipo_cambio_p) <= tipo_cambio_minimo or float(tipo_cambio_p) >= tipo_cambio_maximo) and not confirmacion:
          return False, 'CRP205'
      
      print('Pagos:Monto') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      monto = pago.get('Monto')
      tipo_cambio_monto = pago.get('TipoCambioP')
      monedap = pago.get('MonedaP')
      new_monto = trunc(float(monto), 6)
      importe_pagado = 0
      doctos = pago.xpath("./pago10:DoctoRelacionado", namespaces=namespace_dicc)
      if len(doctos) == 0:
        return False, 'CRP997'
      elif len(doctos) == 1:
        try:
          tipocambiodr = doctos[0].get('TipoCambioDR')
          monedadr = doctos[0].get('MonedaDR')
          imppagado = doctos[0].get('ImpPagado')
          if tipocambiodr:
            try:
              imppagado = float(imppagado)
              imppagado_convertido = imppagado / float(tipocambiodr)
              imppagado_decimales = 0
              try:
                imppagado_decimales = len(str(valor_unitario).split('.')[-1])
              except:
                pass
              try:
                tipocambiodr_decimales = len(str(tipocambiodr).split('.')[-1])
              except:
                pass
              inferior = (imppagado - (10 ** - imppagado_decimales) / 2) / (float(tipocambiodr) + (10** - tipocambiodr_decimales) / 2 - 0.0000000001) #Calcula limite inferior para el Monto
              superior = (imppagado+(10** - imppagado_decimales)/2-0.0000000001)/(float(tipocambiodr)-(10**-tipocambiodr_decimales/2)) #Calcula limite superior
              if not (float(imppagado_convertido) >= inferior and float(imppagado_convertido) <= superior):
                return False, 'CRP999.A'
              importe_pagado = imppagado_convertido
            except:
              return False, 'CRP218'
          else:
            importe_pagado = imppagado
        except:
          importe_pagado = new_monto
      else:
        for docto in doctos:
          monedadr = docto.get('MonedaDR')
          if monedadr == monedap:
            importe_pagado += float(docto.get('ImpPagado', '0'))
          else:
            try:
              tipocambiodr = docto.get('TipoCambioDR')
              imppagado = float(docto.get('ImpPagado')) 
              imppagado_convertido = imppagado / float(tipocambiodr)
              imppagado_decimales = 0
              try:
                imppagado_decimales = len(str(imppagado).split('.')[-1])
              except:
                pass
              try:
                tipocambiodr_decimales = len(str(tipocambiodr).split('.')[-1])
              except:
                pass
              inferior = (imppagado - (10 ** - imppagado_decimales) / 2) / (float(tipocambiodr) + (10** - tipocambiodr_decimales) / 2 - 0.0000000001) #Calcula limite inferior para el Monto
              superior = (imppagado+(10** - imppagado_decimales)/2-0.0000000001)/(float(tipocambiodr)-(10**-tipocambiodr_decimales/2)) #Calcula limite superior
              if not (float(imppagado_convertido) >= inferior and float(imppagado_convertido) <= superior):
                return False, 'CRP999.A'
              importe_pagado += imppagado_convertido
            except:
              return False, 'CRP218'            
      if importe_pagado and trunc(new_monto, 2,True) < trunc(importe_pagado, 2, 'EVEN'):        
        return False, 'CRP206'        

      if float(monto) <= 0.0:
        return False, 'CRP207'
      monto_dec = len(monto.split('.')[1]) if '.' in str(monto) else 0
      if monto_dec > moneda_obj.decimales:
        return False, 'CRP208'
      tipo_de_comprobante_obj = catalogos_obj.obtener('TipoDeComprobante', tipo_de_comprobante)
      monto_maximo = float(tipo_de_comprobante_obj.maximo.replace(',',''))
      if tipo_de_comprobante_obj and float(monto) > monto_maximo and not confirmacion:
        return False, 'CRP209'

      rfcemisorctaord = pago.get('RfcEmisorCtaOrd')
      if rfcemisorctaord and (rfcemisorctaord != 'XEXX010101000' and not LRFC.objects.filter(rfc=rfcemisorctaord).exists()):
        return False, 'CRP210'

      nombancoordext = pago.get('NomBancoOrdExt')
      if rfcemisorctaord == 'XEXX010101000' and not nombancoordext:
        return False, 'CRP211'
      if nombancoordext and rfcemisorctaord != 'XEXX010101000' and False: # Disabled this validation, is not in the matriz
        return False, 'CRP998'

      ctaordenante = pago.get('CtaOrdenante')
      if forma_pago_p not in ('02', '03', '04', '05', '06', '28', '29') and ctaordenante:
        return False, 'CRP212'
      if ctaordenante and not catalogos_obj.validar('FormaPago', forma_pago_p, cuenta=ctaordenante, tipo='ordenante', _type='cuenta'):
        return False, 'CRP213'
      rfcemisorctaben = pago.get('RfcEmisorCtaBen')
      if forma_pago_p not in ('02', '03', '04', '05', '28', '29') and rfcemisorctaben:
        return False, 'CRP214'
      ctabeneficiario = pago.get('CtaBeneficiario')
      if forma_pago_p not in ('02', '03', '04', '05', '28', '29') and ctabeneficiario:
        return False, 'CRP215'
      tipocadpago = pago.get('TipoCadPago')
      if forma_pago_p != '03' and tipocadpago:
        return False, 'CRP216'

      certificadopago = pago.get('CertPago')
      cadenapago = pago.get('CadPago')
      sellopago = pago.get('SelloPago')
      pattern = '^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$'
      if sellopago and not re.match(pattern, sellopago):
        return False, 'CRP231'
      pattern = '^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$'
      if certificadopago and not re.match(pattern, certificadopago):
        return False, 'CRP227'

      if tipocadpago:
        if not certificadopago:
          return False, 'CRP227'          
        if not cadenapago:
          return False, 'CRP229'
        if not sellopago:
          return False, 'CRP231'
      else:
        if certificadopago:
          return False, 'CRP228'
        if cadenapago:
          return False, 'CRP230'
        if sellopago:
          return False, 'CRP232'

      print('Pago:DoctoRelacionado') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      docto_relacionados = pago.xpath('./pago10:DoctoRelacionado', namespaces=namespace_dicc)
      for docto_relacionado in docto_relacionados:
        print('DoctoRelacionado:MonedaDR') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        monedadr = docto_relacionado.get('MonedaDR')
        monedadr_obj = catalogos_obj.obtener('Moneda', monedadr)
        if monedadr == 'XXX':
          return False, 'CRP217'
        tipocambiodr = docto_relacionado.get('TipoCambioDR')
        if monedadr != moneda_p and not tipocambiodr:
          return False, 'CRP218'
        if monedadr == moneda_p and tipocambiodr:
          return False, 'CRP219'        
        
        print('DoctoRelacionado:ImpSaldoAnt') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        impsaldoant = docto_relacionado.get('ImpSaldoAnt')
        if impsaldoant and float(impsaldoant) <= 0.0:
          return False, 'CRP221'
        impsaldoant_dec = len(impsaldoant.split('.')[1]) if '.' in str(impsaldoant) else 0
        if impsaldoant and impsaldoant_dec > monedadr_obj.decimales:
          return False, 'CRP222'

        print('DoctoRelacionado:ImpPagado') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        imppagado = docto_relacionado.get('ImpPagado')
        if imppagado and float(imppagado) <= 0.0:
          return False, 'CRP223'
        imppagado_dec = len(imppagado.split('.')[1]) if '.' in str(imppagado) else 0
        if imppagado and imppagado_dec > monedadr_obj.decimales:
          return False, 'CRP224'          

        print('DoctoRelacionado:ImpSaldoInsoluto') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        impsaldoinsoluto = docto_relacionado.get('ImpSaldoInsoluto')
        impsaldoinsoluto_dec = len(impsaldoinsoluto.split('.')[1]) if '.' in str(impsaldoinsoluto) else 0
        if impsaldoinsoluto and impsaldoinsoluto_dec > monedadr_obj.decimales:
          return False, 'CRP225'          
        if impsaldoinsoluto and float(impsaldoinsoluto) < 0.0:
          return False, 'CRP226'
        impsaldoinsoluto_calc = 0.0
        if imppagado and impsaldoant:
          impsaldoinsoluto_calc = trunc((Decimal(impsaldoant) - Decimal(imppagado)), moneda_obj.decimales, True)
        elif impsaldoant and monto:
          impsaldoinsoluto_calc = trunc((float(impsaldoant) - float(monto)), moneda_obj.decimales, True) # Considerando la conversion a MonedaDR
        if impsaldoinsoluto and trunc(impsaldoinsoluto, 2) != trunc(impsaldoinsoluto_calc, 2):      
          return False, 'CRP226'

        print('DoctoRelacionado:MetodoDePagoDR') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        metodopagodr = docto_relacionado.get('MetodoDePagoDR')
        numparcialidad = docto_relacionado.get('NumParcialidad')
        if metodopagodr == 'PPD' and not numparcialidad:
          return False, 'CRP233'
        impsaldoant = docto_relacionado.get('ImpSaldoAnt')
        if metodopagodr == 'PPD' and not impsaldoant:
          return False, 'CRP234'

        if len(docto_relacionados) > 1 and not imppagado:
          return False, 'CRP235'
        if len(docto_relacionados) == 1 and tipocambiodr and not imppagado:
          return False, 'CRP235'

        impsaldoinsoluto = docto_relacionado.get('ImpSaldoInsoluto')
        if metodopagodr == 'PPD' and not impsaldoinsoluto:
          return False, 'CRP236'

      print('Pago:Impuestos') if settings.VERBOSE_EXTRA_VALIDATIONS else None      
      impuestos = pago.xpath('./pago10:Impuestos', namespaces=namespace_dicc)
      if impuestos:
        return False, 'CRP237'

      if forma_pago_p not in ('02','03','04','05','06','28','29') and rfcemisorctaord:
        return False, 'CRP238'

      if ctabeneficiario and not catalogos_obj.validar('FormaPago', forma_pago_p, cuenta=ctabeneficiario, tipo='beneficiaria', _type='cuenta'):
        return False, 'CRP239'

  elif len(complement_pago10) > 1:
    return False, 'CRP999'

  elif len(complement_pago10) == 0 and tipo_de_comprobante == 'P':
      return False, 'CRP999'

  return True, None

