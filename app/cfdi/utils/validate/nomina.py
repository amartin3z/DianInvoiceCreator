from django.conf import settings

from app.sat.utils.validate import Catalogos
from app.sat.models import LRFC, LCO

from .adicionales import trunc, normal_round, sat_round
from decimal import Decimal

import re
from datetime import datetime


def validacion_nomina12(xml_etree):

  is_valid = True

  for namespace in xml_etree.xpath('//namespace::*' ):
    if namespace[1] == 'http://www.sat.gob.mx/nomina12' and namespace[0] != 'nomina12':
      raise Exception('Prefijo no valido.')
  namespaces = {'namespaces': xml_etree.nsmap}
  complements_nom = xml_etree.findall('.//tmp:Nomina', namespaces={'tmp': 'http://www.sat.gob.mx/nomina12'})
  #Puede existir más de un complemento Nómina en un comprobante (CFDI) y deben tener contenido diferenciado.
  for no, complement_nom in enumerate(complements_nom):
    for no1, complement_nom1 in enumerate(complements_nom):
      if no != no1:
        if complement_nom.values().__eq__(complement_nom1.values()):
          return False, 'nom900'
  tipo_comprobante = xml_etree.get('TipoDeComprobante')
  fecha_emision = xml_etree.get('Fecha')
  version = xml_etree.get('Version')
  #Si versión del CFDI = 3.3 entonces en el atributo TipoDeComprobante, El valor registrado debe ser la clave N que corresponde a  “Nómina”.
  if tipo_comprobante == 'N' and not complements_nom:
    return False, 'nom134' 
  if complements_nom:
    catalogos_obj = Catalogos(fecha_emision)
    # PATCH namespaces nomina12:Nomina in complement
    if ('nomina12' not in namespaces['namespaces']):
      raise Exception('Missing nomina12 prefix.')
    # ENDPATCH
    try:
      # Comprobante Validations
      cfdi_xpath = xml_etree.xpath
      print('nomina12 Version') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      if version != '3.3':
        raise Exception('version 3.2 is not allowed')
      if version == '3.3':
        
        print('nomina12 SubTotal nom106') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # subtotal: Para este atributo se debe registrar la suma de los atributos nomina/@TotalPercepciones más nomina/@TotalOtrosPagos
        subtotal = trunc(xml_etree.get('SubTotal'), 2)
        subtotal_flag = cfdi_xpath('sum(.//nomina12:Nomina/@TotalPercepciones | .//nomina12:Nomina/@TotalOtrosPagos)', **namespaces)
        subtotal_flag = trunc(subtotal_flag, 2)
        if subtotal_flag != subtotal:
          return False, 'nom106'

        print('nomina12 Moneda nom132') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        #Si versión del CFDI = 3.3 entonces en el atributo Moneda debe registrar el valor MXN.
        moneda_mxn = xml_etree.get('Moneda', '') == 'MXN'
        if not moneda_mxn:
          return False, 'nom132'
        
        print('nomina12 FormaPago nom133') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # Si versión del CFDI = 3.3 entonces en el atributo FormaPago, debe tener la clave 99 que corresponde a la descripción “Por definir”.
        metodo_na = cfdi_xpath("boolean(@FormaPago = '99')", **namespaces)
        if not metodo_na:
          return False, 'nom133'
        
        print('nomina12 TipoDeComprobante nom134') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # Si versión del CFDI = 3.3 entonces en el atributo TipoDeComprobante, El valor registrado debe ser la clave N que corresponde a  “Nómina”.
        egreso = cfdi_xpath('boolean(@TipoDeComprobante = "N")', **namespaces)
        if not egreso:
          return False, 'nom134'

        print('nomina12 Rfc Emisor Subcontratación nom115') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        
        # Si el RFC se encuentra registrado en el listado de RFC inscritos en el SAT con marca de subcontratación se debe registrar el nodo Subcontratacion
        emisor_inc = LRFC.objects.filter(rfc=cfdi_xpath('string(//cfdi:Emisor/@Rfc)', **namespaces))
        if emisor_inc.exists():
          if emisor_inc.get().subcontratacion and not cfdi_xpath('boolean(//nomina12:SubContratacion)', **namespaces):
            return False, 'nom115' 

        print('nomina12 Rfc Receptor nom137') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        emisor = xml_etree.find('.//cfdi:Emisor', **namespaces)
        ## Receptor ##
        # Si versión del CFDI = 3.3 y el atributo Comprobante.Receptor.Rfc debe ser persona fisica.
        rfc = cfdi_xpath('string(.//cfdi:Receptor/@Rfc)', **namespaces)
        if len(rfc) < 13:
          return False, 'nom137'
        
        print('nomina12 Rfc nom138') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # Si versión del CFDI = 3.3 y el atributo Comprobante.Receptor.Rfc debe estar en la lista de RFC inscritos no cancelados en el SAT (l_RFC).
        if rfc != 'XAXX010101000':
          rfc_receptor_inc = LRFC.objects.filter(rfc=rfc)
          if not rfc_receptor_inc.exists():
            return False, 'nom138'

        print('nomina12 Concepto nom139') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        ## Comprobante Conceptos Concepto ##
        # Si versión del CFDI = 3.3 entonces en el nodo Comprobante.Conceptos.Concepto, debe registrar solo un nodo concepto sin elementos hijo.
        nodos_concepto  = cfdi_xpath('count(//cfdi:Conceptos/cfdi:Concepto) = 1 and not(boolean(//cfdi:Conceptos/cfdi:Concepto/*))', **namespaces)
        if not nodos_concepto:
          return False, 'nom139'
        
        print('nomina12 ClaveProdServ nom140') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # Si versión del CFDI = 3.3 entonces en el atributo Comprobante.Conceptos.Concepto,ClaveProdServ debe registrar el valor "84111505".
        if not cfdi_xpath('//cfdi:Conceptos/cfdi:Concepto[@ClaveProdServ = "84111505"]', **namespaces):
          return False, 'nom140'
        
        print('nomina12 NoIdentificacion nom141') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # Si versión del CFDI = 3.3 entonces en el atributo Comprobante.Conceptos.Concepto.NoIdentificacion, No debe registrarse.
        if len(cfdi_xpath('//cfdi:Conceptos/cfdi:Concepto/@NoIdentificacion', **namespaces)):
          return False, 'nom141'
        
        print('nomina12 Concepto =1 nom142') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # Si versión del CFDI = 3.3 entonces en el atributo Comprobante.Conceptos.Concepto,Cantidad debe registrar el valor “1”.
        if not cfdi_xpath('//cfdi:Conceptos/cfdi:Concepto[@Cantidad = "1"]', **namespaces):
          return False, 'nom142'
        
        print('nomina12 ClaveUnidad=ACT nom143') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # unidad, para este atributo se debe registrar el valor "ACT"
        if not cfdi_xpath('//cfdi:Conceptos/cfdi:Concepto[@ClaveUnidad = "ACT"]', **namespaces):
          return False, 'nom143'
        
        print('nomina12 Unidad nom144') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # Si versión del CFDI = 3.3 entonces en el atributo Comprobante.Conceptos.Concepto,Unidad No debe registrarse.
        if len(cfdi_xpath('//cfdi:Conceptos/cfdi:Concepto/@Unidad', **namespaces)):
          return False, 'nom144'
        
        print('nomina12 Descripción nom145') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # Si versión del CFDI = 3.3 entonces en el atributo Comprobante.Conceptos.Concepto,Descripcion debe registrar el valor “Pago de nómina”.
        concepto = xml_etree.find('.//cfdi:Conceptos/cfdi:Concepto', **namespaces)
        descripcion = concepto.get('Descripcion')
        if descripcion != u'Pago de nómina':
          return False, 'nom145'

        
        print('nomina12 Subtotal = TotalPercepciones + TotalOtrosPagos nom146') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # valorUnitario, para este atributo se debe registrar la suma de los atributos totalPercepciones más TotalOtrosPagos
        subtotal_129 = cfdi_xpath('sum(.//nomina12:Nomina/@TotalPercepciones | .//nomina12:Nomina/@TotalOtrosPagos)', **namespaces)
        valor_unitario = trunc(concepto.get('ValorUnitario'), 2)
        subtotal_129 = trunc(subtotal_129, 2)
        if valor_unitario != subtotal_129:
          return False, 'nom146'
        
        print('nomina12 Subtotal = importes nom147') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # Si versión del CFDI = 3.3 entonces en el atributo Comprobante.Conceptos.Concepto,Importe debe registrar la suma de los atributos TotalPercepciones más TotalOtrosPagos.
        importe = trunc(concepto.get('Importe'), 2)
        if importe != subtotal_129:
          return False, 'nom147'
        
        print('nomina12 Descuento = sum(TotalDeducciones) nom148') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # El valor del atributo Comprobante.Conceptos.Concepto,Descuento no es igual a el valor del campo Nomina12:TotalDeducciones.
        total_deducciones = cfdi_xpath('sum(.//nomina12:Nomina/@TotalDeducciones)', **namespaces)
        descuento = concepto.get('Descuento', 0.0)
        if trunc(descuento, 2) != trunc(total_deducciones, 2):
          return False, 'nom148'

        print('nomina12 Impuestos nom149') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # Si versión del CFDI = 3.3 entonces en el nodo Comprobante.Impuestos. no se debe registrar.
        if cfdi_xpath('//cfdi:Comprobante/cfdi:Impuestos', **namespaces):
          return False, 'nom149'
      # End Comprobante 3.3 Validations
      for complement_nom in complements_nom:

        nom_xpath = complement_nom.xpath

        # El nodo Nomina se debe registrar como un nodo hijo del nodo Complemento en el CFDI.
        print('nomina12 complemento nom150') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        if complement_nom.getparent().tag != '{http://www.sat.gob.mx/cfd/3}Complemento':
          return False, 'nom150'  

        ## Emisor ##
        if version == '3.2':
          raise Exception('version 3.2 is not allowed')

        elif version == '3.3':
          # Si versión del CFDI = 3.3 y el atributo Comprobante.Emisor.Rfc, tiene longitud 12 (RFC de persona moral), entonces  no debe existir el atributo Nomina12:Emisor:Curp,

          print('nomina12 Rfc nom135') if settings.VERBOSE_EXTRA_VALIDATIONS else None
          if emisor is not None:
            rfc = emisor.get('Rfc')
            emisor_nom = xml_etree.find('.//nomina12:Nomina/nomina12:Emisor', **namespaces)
            curp = emisor_nom.xpath('boolean(@Curp)', **namespaces)
            if len(rfc) == 12 and curp:
              return False, 'nom135'
            if len(rfc) == 13 and not curp:
              return False, 'nom136'
        
        
        print('nomina12 TotalPercepciones TotalOtrosPagos TotalPercepciones TotalOtrosPagos nom151') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # El nodo Nomina no tiene TotalPercepciones y/o TotalOtrosPagos.
        if nom_xpath('not(boolean((@TotalPercepciones or @TotalOtrosPagos) or (@TotalPercepciones and @TotalOtrosPagos)))', **namespaces):
          return False, 'nom151'

        print('nomina12 TipoNomina nom152') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # El valor del atributo Nomina.TipoNomina no cumple con un valor del catálogo c_TipoNomina.
        tipo_nomina = nom_xpath('string(@TipoNomina)', **namespaces)
        if not catalogos_obj.validar('TipoNomina', tipo_nomina):
          return False, 'nom152'

        print('nomina12 PeriodicidadPago == 99 Nomina O nom153') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # El valor del atributo tipo de periodicidad no se encuentra entre 01 al 09.
        periocidad_pago = nom_xpath('string(.//nomina12:Receptor/@PeriodicidadPago)', **namespaces)
        # OLD: Si el atributo Nomina.TipoNomina es ordinaria el tipo de periodicidad de pago debe ser del 01 al 09.
        # NEW: Si el atributo Nomina.TipoNomina es ordinaria el tipo de periodicidad de pago debe ser distinta a 99
        if tipo_nomina == 'O' and periocidad_pago == '99':
          return False, 'nom153'
        
        print('nomina12 PeriodicidadPago != 99 Nomina E nom154') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # Si el atributo Nomina.TipoNomina es extraordinaria el tipo de periodicidad de pago debe ser 99.
        if tipo_nomina == 'E' and periocidad_pago != "99":
          return False, 'nom154'

        print('nomina12 FechaIniciaPago > FechaFinalPago nom155') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # El valor del atributo FechaInicialPago no es menor o igual al valor del atributo FechaFinalPago.
        fecha_inicial = nom_xpath('string(@FechaInicialPago)', **namespaces)
        fecha_final = nom_xpath('string(@FechaFinalPago)', **namespaces)
        fecha_inicial_obj = datetime.strptime(fecha_inicial, "%Y-%m-%d")
        fecha_final_obj = datetime.strptime(fecha_final, "%Y-%m-%d")
        if fecha_inicial_obj > fecha_final_obj:
          return False, 'nom155'

        if fecha_final_obj < fecha_inicial_obj:
          return False, 'nom901'
        
        print('nomina12 TotalPercepciones && Percepciones nom156') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        nodo_percepciones = nom_xpath('.//nomina12:Percepciones', **namespaces)
        # El atributo Nomina.TotalPercepciones, no debe existir.
        no_percepciones = nom_xpath('boolean(not(@TotalPercepciones))', **namespaces)
        percepciones = nom_xpath('boolean(@TotalPercepciones)', **namespaces)
        if len(nodo_percepciones) and no_percepciones:
          return False, 'nom156'
        elif not len(nodo_percepciones) and percepciones:
          return False, 'nom156'

        print('nomina12 TotalPercepciones == sumatoria nom157') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # El valor del atributo Nomina.TotalPercepciones no coincide con la suma TotalSueldos más TotalSeparacionIndemnizacion más TotalJubilacionPensionRetiro del  nodo Percepciones.
        total_percepciones_calculado = nom_xpath('sum(.//nomina12:Percepciones/@TotalSueldos | .//nomina12:Percepciones/@TotalSeparacionIndemnizacion | .//nomina12:Percepciones/@TotalJubilacionPensionRetiro)', **namespaces)
        total_percepciones = nom_xpath('sum(@TotalPercepciones)', **namespaces)
        if len(nodo_percepciones) and trunc(total_percepciones, 2) != trunc(total_percepciones_calculado, 2):
          return False, 'nom157'

        print('nomina12 TotalDeducciones and Deducciones nom158') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        nodo_deducciones = nom_xpath('.//nomina12:Deducciones', **namespaces)
        # El atributo Nomina.TotalDeducciones, no debe existir.
        no_deducciones = nom_xpath('boolean(not(@TotalDeducciones))', **namespaces)
        deducciones = nom_xpath('boolean(@TotalDeducciones)', **namespaces)
        if len(nodo_deducciones) and no_deducciones or not len(nodo_deducciones) and deducciones:
          return False, 'nom158'

        print('nomina12 TotalDeducciones == sumatoria nom159') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # El valor del atributo Nomina.TotalDeducciones no coincide con la suma de los atributos TotalOtrasDeducciones más TotalImpuestosRetenidos del elemento Deducciones.
        total_deducciones = '%.2f' % nom_xpath('sum(@TotalDeducciones)', **namespaces)
        total_deducciones_sum = '%.2f' % float(nom_xpath('sum(.//nomina12:Deducciones/@TotalOtrasDeducciones | .//nomina12:Deducciones/@TotalImpuestosRetenidos)', **namespaces))
        #total_deducciones = '%.2f' % float(nom_xpath('string(.//@TotalDeducciones)', **namespaces))
        if len(nodo_deducciones) and trunc(total_deducciones, 2) != trunc(total_deducciones_sum, 2):
          return False, 'nom159'

        print('nomina12 TotalOtrosPagos == sumatoria nom160') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # El valor del atributo Nomina.TotalOtrosPagos no está registrado o  no coincide con la suma de los atributos Importe de los nodos nomina12:OtrosPagos:OtroPago.
        nodo_otros_pagos = nom_xpath('.//nomina12:OtrosPagos', **namespaces)
        otros_pagos = nom_xpath('boolean(.//nomina12:OtrosPagos)', **namespaces)
        total_otros_pagos = nom_xpath('boolean(.//@TotalOtrosPagos)', **namespaces)
        total_otros_pagos_sumados = nom_xpath('sum(.//nomina12:OtrosPagos/nomina12:OtroPago/@Importe)', **namespaces)
        total_otros_pagos_calculados = nom_xpath('sum(.//@TotalOtrosPagos)', **namespaces)
        if otros_pagos and not total_otros_pagos:
          return False, 'nom160'
        elif not otros_pagos and total_otros_pagos:
          return False, 'nom160'
        
        if otros_pagos and trunc(total_otros_pagos_calculados, 2) != trunc(total_otros_pagos_sumados, 2):
          return False, 'nom160'
        
        print('nomina12 RfcPatronOrigen LRFC nom161') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # El atributo Nomina.Emisor.RfcPatronOrigen no está inscrito en el SAT (l_RFC).
        rfc_p = nom_xpath('string(.//nomina12:Emisor/@RfcPatronOrigen)', **namespaces) 
        if rfc_p: 
          rfc_patron =  LRFC.objects.filter(rfc=rfc_p)
          if not rfc_patron.exists(): 
            return False, 'nom161'

        print('nomina12 RfcPatronOrigen LRFC nom160') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        # El atributo Nomina.Emisor.RegistroPatronal se debe registrar.
        tipo_contrato = nom_xpath('string(.//nomina12:Receptor/@TipoContrato)', **namespaces)
        registro_patronal = nom_xpath('string(.//nomina12:Emisor/@RegistroPatronal)', **namespaces)
        if tipo_contrato in ("01", "02", "03", "04", "05", "06", "07", "08") and not registro_patronal:
          return False, 'nom162'

        # Si el atributo TipoContrato tiene el valor 09, 10 ó 99, el atributo Nomina.Emisor.RegistroPatronal no debe existir.
        if tipo_contrato in ("09", "10", "99") and registro_patronal:
          return False, 'nom163'
        
        # Si atributo Nomina.Emisor.RegistroPatronal existe, entonces deben existir los atributos nomina12:Receptor: NumSeguridadSocial,  nomina12:Receptor:FechaInicioRelLaboral, nomina12:Receptor:Antigüedad,  nomina12:Receptor:RiesgoPuesto y nomina12:Receptor:SalarioDiarioIntegrado.            
        if registro_patronal and not nom_xpath(u'boolean(.//nomina12:Receptor[@NumSeguridadSocial and @FechaInicioRelLaboral and @RiesgoPuesto and @SalarioDiarioIntegrado]) and boolean(.//nomina12:Receptor/@*[starts-with(name(), "Antig")])', **namespaces):
          return False, 'nom164'
        
        # Validación inversa. (XML nomina confiniquito e indemnización)
        elif not registro_patronal and nom_xpath(u'boolean(.//nomina12:Receptor[@NumSeguridadSocial and @FechaInicioRelLaboral and @RiesgoPuesto and @SalarioDiarioIntegrado]) and boolean(.//nomina12:Receptor/@*[starts-with(name(), "Antig")])', **namespaces):
          return False, 'nom164.A'

        # Si el RFC del emisor existe en el listado de RFC inscritos no cancelados en el SAT (l_RFC) con marca de unidad adherida al Sistema Nacional de Coordinación Fiscal, el nodo Nomina.Emisor.EntidadSNCF debe existir.
        if emisor_inc.exists():
          if emisor_inc.get().sncf and nom_xpath('not(boolean(.//nomina12:Emisor/nomina12:EntidadSNCF))', **namespaces):
            return False, 'nom165'

        if emisor_inc.exists():
          # Si el RFC del emisor existe en el listado de RFC inscritos no cancelados en el SAT (l_RFC) sin marca de unidad adherida al Sistema Nacional de Coordinación Fiscal, el nodo Nomina.Emisor.EntidadSNCF no debe existir.
          if not emisor_inc.sncf and nom_xpath('boolean(.//nomina12:Emisor/nomina12:EntidadSNCF)', **namespaces):
            return False, 'nom166'

        nodo_entidad_sncf = nom_xpath('.//nomina12:Emisor/nomina12:EntidadSNCF', **namespaces)
        # El atributo Nomina.Emisor.EntidadSNCF.OrigenRecurso debe ser una clave del catálogo c_OrigenRecurso publicado en el portal del SAT en internet.
        if len(nodo_entidad_sncf):
          for entidad_sncf  in nodo_entidad_sncf:
            origen_recurso = entidad_sncf.xpath('string(@OrigenRecurso)', **namespaces)
            if not catalogos_obj.validar("OrigenRecurso", origen_recurso):
              return False, 'nom167'
            monto_recurso = entidad_sncf.xpath('sum(@MontoRecursoPropio)', **namespaces)
            monto_recurso_exists = entidad_sncf.xpath('boolean(@MontoRecursoPropio)', **namespaces)
            # El atributo Nomina.Emisor.EntidadSNCF.OrigenRecurso Si el valor registrado corresponde a la clave IM (Ingresos Mixtos), el atributo MontoRecursoPropio debe existir.
            if origen_recurso == 'IM' and not monto_recurso_exists:
              return False, 'nom168'
            # El atributo Nomina.Emisor.EntidadSNCF.OrigenRecurso Si el valor registrado es diferente a la clave IM (Ingresos Mixtos), el atributo MontoRecursoPropio no debe existir.
            if origen_recurso != 'IM' and monto_recurso_exists:
              return False, 'nom169'
            # El atributo Nomina.Emisor.EntidadSNCF.MontoRecursoPropio debe ser menor que la suma de los valores de los atributos TotalPercepciones y TotalOtrosPagos. 
            monto_recurso = '%.2f' % float(monto_recurso)
            if origen_recurso == 'IM' and float(monto_recurso) > float(subtotal):
                return False, 'nom170'
        # elif emisor_inc.sncf:
        #   raise Exception('Deberiamos realizar esta validación????')

        # El atributo Nomina.Receptor.TipoContrato debe ser una clave del catálogo c_TipoContrato publicado en el portal del SAT en internet.
        #if tipo_contrato not in ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "99"):
        if not catalogos_obj.validar("TipoContrato", tipo_contrato):
          return False, 'nom171'
        
        # El atributo Nomina.Receptor.TipoJornada debe ser una clave del catálogo de c_TipoJornada publicado en el portal del SAT en internet.
        tipo_jornada = nom_xpath('string(.//nomina12:Receptor/@TipoJornada)', **namespaces)
        #if tipo_jornada and tipo_jornada not in ("01", "02", "03", "04", "05", "06", "07", "08", "99"):
        if tipo_jornada and not catalogos_obj.validar("TipoJornada", tipo_jornada):
          return False, 'nom172'
        
        # El atributo Nomina.Receptor.FechaInicioRelLaboral, debe ser menor o igual al atributo FechaFinalPago.
        fecha_inicio_laboral = nom_xpath('string(.//nomina12:Receptor/@FechaInicioRelLaboral)', **namespaces)
        if fecha_inicio_laboral:
          fecha_inicio_laboral_obj = datetime.strptime(fecha_inicio_laboral, "%Y-%m-%d")
          if fecha_inicio_laboral_obj > fecha_final_obj:
            return False, 'nom173'
        
        antiguedad_str = nom_xpath(u'string(.//nomina12:Receptor/@*[starts-with(name(), "Antig")])', **namespaces)
        from dateutil.relativedelta import relativedelta
        if antiguedad_str:
          # Si el atributo Nomina.Receptor.Antigüedad tiene el patrón P[1-9][0-9]{0,3}W, entonces el valor numérico del atributo Nomina.Receptor.Antigüedad, debe ser menor o igual al cociente de (la suma del número de días transcurridos entre la FechaInicioRelLaboral y la FechaFinalPago más uno) dividido entre siete.
          dias_transcurridos = fecha_final_obj -  fecha_inicio_laboral_obj
          #antiguedad_regex = re.match(r'^P([1-9][0-9]{0,3})W$', antiguedad_str)
          antiguedad_regex = re.match(r'^P(([1-9][0-9]{0,3})|0)W$', antiguedad_str)
          if antiguedad_regex:
            antiguedad = int(antiguedad_regex.groups()[0])
            cociente = (dias_transcurridos.days + 1) // 7
            if antiguedad > cociente:
              return False, 'nom174'
          
          # Si el atributo Nomina.Receptor.Antigüedad tiene el patrón P(([1-9][0-9]?Y)?([1-9]|1[012])M)?([0]|[1-9]|[12][0-9]|3[01])D, entonces el valor registrado debe corresponder con el número de años, meses y días transcurridos entre la FechaInicioRelLaboral y la FechaFinalPago.
          #antiguedad_regex = re.match('^P((([1-9][0-9]?)(Y))?([1-9]|1[012])(M))?(([0]|[1-9]|[12][0-9]|3[01])(D))$', antiguedad_str)
          antiguedad_regex = re.match('^P(([1-9][0-9]?)(Y))?(([1-9]|1[012])(M))?(0|[1-9]|[12][0-9]|3[01])(D)$', antiguedad_str)
          if antiguedad_regex:
            dias_transcurridos = relativedelta(fecha_final_obj, fecha_inicio_laboral_obj)
            anios_calculados = dias_transcurridos.years
            meses_calculados = dias_transcurridos.months
            #if meses_calculados == 0 and anios_calculados > 1:
            #  anios_calculados -= 1
            #  meses_calculados = 12
            #if meses_calculados == 0 and anios_calculados == 1:
            #  anios_calculados = 0
            #  meses_calculados = 12
            anios, meses, dias = 0, 0, 0
            dias_transcurridos_regex = antiguedad_regex.groups()
            if 'Y' in dias_transcurridos_regex:
              anios = int(dias_transcurridos_regex[dias_transcurridos_regex.index('Y') - 1])
            if 'M' in dias_transcurridos_regex:
              meses = int(dias_transcurridos_regex[dias_transcurridos_regex.index('M') - 1])
              #if meses == 12:
              #  anios += 1
              #  meses = 0
            if 'D' in dias_transcurridos_regex:
              dias = int(dias_transcurridos_regex[dias_transcurridos_regex.index('D') - 1])
            #if not (anios == anios_calculados and meses == meses_calculados and (dias == dias_transcurridos.days or dias == dias_transcurridos.days + 1))  and not (days==dias and meses==0 and anios==0 and dias_transcurridos.years==0 and dias_transcurridos.months == 1 and dias_transcurridos.days==0):
            if not (anios == anios_calculados and meses == meses_calculados and (dias == dias_transcurridos.days or dias == dias_transcurridos.days + 1)):
              return False, 'nom175'

        # El atributo Nomina.Receptor.TipoRegimen debe ser una clave del catálogo de c_TipoRegimen publicado en el portal del SAT en internet.  
        tipo_regimen = nom_xpath('string(.//nomina12:Receptor/@TipoRegimen)', **namespaces)
        #if tipo_regimen not in ("03", "02", "04", "05", "06", "07", "08", "09", "10", "11", "99"):
        if not catalogos_obj.validar("TipoRegimen", tipo_regimen):
          return False, 'nom176'

        # Si el atributo TipoContrato tiene una clave entre los valores 01 y 08 del catálogo c_TipoContrato entonces el atributo Nomina.Receptor.TipoRegimen debe ser 02, 03 ó 04.
        if tipo_contrato in ('01', '02', '03', '04', '05', '06', '07', '08') and tipo_regimen not in ("02", "03", "04"):
          return False, 'nom177'
        
        # Si el atributo TipoContrato tiene un valor 09 ó superior entonces el atributo Nomina.Receptor.TipoRegimen debe ser 05 hasta el 99.
        if tipo_contrato in ("09", "10", "99") and tipo_regimen not in ("05", "06", "07", "08", "09", "10", "11", "12", "13", "99"):
          return False, 'nom178'
        
        # El atributo RiesgoPuesto debe ser una clave del catálogo de c_RiesgoPuesto publicado en el portal del SAT en internet.
        riesgo_puesto = nom_xpath('string(.//nomina12:Receptor/@RiesgoPuesto)', **namespaces)
        if riesgo_puesto and not catalogos_obj.validar("RiesgoPuesto", riesgo_puesto):
          return False, 'nom179'

        # El atributo PeriodicidadPago debe ser una clave del catálogo de c_PeriodicidadPago publicado en el portal del SAT en internet.
        #if periocidad_pago not in ("01", "02", "03", "04", "05", "06", "07", "08", "09", "99"):
        if not catalogos_obj.validar("PeriodicidadPago", periocidad_pago):
          return False, 'nom180'

        banco = nom_xpath('string(.//nomina12:Receptor/@Banco)', **namespaces)
        if banco and not catalogos_obj.validar("Banco", banco):
          return False, 'nom181'

        # El atributo CuentaBancaria debe tener una longitud de 10, 11, 16 ó 18 posiciones.
        cta_bancaria = nom_xpath('string(.//nomina12:Receptor/@CuentaBancaria)', **namespaces)
        len_cta_bancaria = len(cta_bancaria)
        if cta_bancaria:
          if len_cta_bancaria not in (10, 11, 16, 18):
            return False, 'nom182'

          # Si se registra una cuenta CLABE (número con 18 posiciones), el atributo Banco no debe existir.
          if len_cta_bancaria == 18 and banco:
            return False, 'nom183'

          # Se debe confirmar que el dígito de control es correcto.
          if len_cta_bancaria == 18:
            sumatoria = 0
            clabe = cta_bancaria[:-1]
            # peso_posicion = [3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7]
            digito_control = int(cta_bancaria[17])
            for no, i in enumerate(clabe):
              posicion = (no + 1) % 3
              peso_posicion = 3 if posicion == 1 else 7 if posicion == 2 else 1
              sumatoria += ((int(i) * peso_posicion))
              sumatoria_mod_10 = sumatoria % 10
              digito_control_calculado = (10 - sumatoria_mod_10) % 10
            if digito_control_calculado != digito_control:
              return False, 'nom184'
        
          # Si se registra una cuenta de tarjeta de débito a 16 posiciones o una cuenta bancaria a 11 posiciones o un número de teléfono celular a 10 posiciones, debe existir el banco.
          if len_cta_bancaria in (10, 11, 16) and not banco:
            return False, 'nom185'
        
        # El valor del atributo ClaveEntFed debe ser una clave del catálogo de c_Estado, donde la clave de país es MEX.
        clave_entidad_f = nom_xpath('string(.//nomina12:Receptor/@ClaveEntFed)', **namespaces)
        if not catalogos_obj.validar("Estado", clave_entidad_f):
          return False, 'nom186'

        nodo_subcontratacion = nom_xpath('.//nomina12:Receptor/nomina12:SubContratacion', **namespaces)
        for subc in nodo_subcontratacion:
          # El valor del atributo Nomina.Receptor.SubContratacion.RfcLabora debe existir en la lista de RFC inscritos no cancelados en el SAT (l_RFC).
          rfc_l = subc.get('RfcLabora')  
          rfc_labora = LRFC.objects.filter(rfc=rfc_l)
          if not rfc_labora.exists() and rfc_l != 'XEXX010101000':
            return False, 'nom187'
        
        if len(nodo_subcontratacion):
          # El valor del atributo Nomina.Receptor.SubContratacion.PorcentajeTiempo La suma de los valores PorcentajeTiempo registrados debe ser igual a 100.
          porcentaje_tiempo = '%.3f' % float(nom_xpath('sum(.//nomina12:Receptor/nomina12:SubContratacion/@PorcentajeTiempo)', **namespaces))
          if porcentaje_tiempo != '100.000':
            return False, 'nom188'          
        # En el elemento Nomina.Percepciones , La suma de los valores de los atributos TotalSueldos más TotalSeparacionIndemnizacion más TotalJubilacionPensionRetiro debe ser igual a la suma de los valores de los atributos TotalGravado más TotalExento.
        if len(nodo_percepciones):
          percepciones = nodo_percepciones[0]
          nodo_percepcion = percepciones.xpath('.//nomina12:Percepcion', **namespaces)
          percepciones_totales = percepciones.xpath('''sum(@TotalGravado | @TotalExento)''', **namespaces)
          # En el elemento Nomina.Percepciones , La suma de los valores de los atributos TotalSueldos más TotalSeparacionIndemnizacion más TotalJubilacionPensionRetiro debe ser igual a la suma de los valores de los atributos TotalGravado más TotalExento.
          if trunc(total_percepciones_calculado, 2) != trunc(percepciones_totales, 2):
            return False, 'nom189'
          # El valor del atributo Nomina.Percepciones.TotalSueldos , debe ser igual a la suma de los atributos ImporteGravado e ImporteExento donde la clave expresada en el atributo TipoPercepcion sea distinta de 022 Prima por Antigüedad, 023 Pagos por separación, 025 Indemnizaciones, 039 Jubilaciones, pensiones o haberes de retiro en una exhibición y 044 Jubilaciones, pensiones o haberes de retiro en parcialidades.
          atributo_total_sueldos = percepciones.xpath('''string(@TotalSueldos)''', **namespaces)
          if atributo_total_sueldos:
            total_sueldos = '%.2f' % float(atributo_total_sueldos)
            total_sueldos_calculado = '%.2f' % float(percepciones.xpath('''sum(.//nomina12:Percepcion[not(@TipoPercepcion="022" or @TipoPercepcion="023" or @TipoPercepcion="025" or @TipoPercepcion="039" or @TipoPercepcion="044")]/@ImporteGravado | .//nomina12:Percepcion[not(@TipoPercepcion="022" or @TipoPercepcion="023" or @TipoPercepcion="025" or @TipoPercepcion="039" or @TipoPercepcion="044")]/@ImporteExento)''', **namespaces))
            if total_sueldos != total_sueldos_calculado:
              return False, 'nom190'
          elif float(percepciones.xpath('''sum(.//nomina12:Percepcion[not(@TipoPercepcion="022" or @TipoPercepcion="023" or @TipoPercepcion="025" or @TipoPercepcion="039" or @TipoPercepcion="044")]/@ImporteGravado | .//nomina12:Percepcion[not(@TipoPercepcion="022" or @TipoPercepcion="023" or @TipoPercepcion="025" or @TipoPercepcion="039" or @TipoPercepcion="044")]/@ImporteExento)''', **namespaces)) > 0.0:
            return False, 'nom190'

          # El valor del atributo Nomina.Percepciones.TotalSeparacionIndemnizacion, debe ser igual a la suma de los atributos ImporteGravado e ImporteExento donde la clave expresada en el atributo TipoPercepcion sea igual a 022 Prima por Antigüedad, 023 Pagos por separación ó 025 Indemnizaciones.
          atributo_total_separacion_indemnizacion = percepciones.xpath('''string(@TotalSeparacionIndemnizacion)''', **namespaces)
          if atributo_total_separacion_indemnizacion:
            total_indemnizacion = '%.2f' % float(atributo_total_separacion_indemnizacion)
            total_indemnizacion_calculado = '%.2f' % float(percepciones.xpath('''sum(.//nomina12:Percepcion[(@TipoPercepcion="022" or @TipoPercepcion="023" or @TipoPercepcion="025")]/@ImporteGravado | .//nomina12:Percepcion[(@TipoPercepcion="022" or @TipoPercepcion="023" or @TipoPercepcion="025")]/@ImporteExento)''', **namespaces))
            if total_indemnizacion !=  total_indemnizacion_calculado:
              return False, 'nom191'
          elif float(percepciones.xpath('''sum(.//nomina12:Percepcion[(@TipoPercepcion="022" or @TipoPercepcion="023" or @TipoPercepcion="025")]/@ImporteGravado | .//nomina12:Percepcion[(@TipoPercepcion="022" or @TipoPercepcion="023" or @TipoPercepcion="025")]/@ImporteExento)''', **namespaces)) > 0.0:
            return False, 'nom191'

          # El valor del atributo Nomina.Percepciones.TotalJubilacionPensionRetiro, debe ser igual a la suma de los atributos ImporteGravado e importeExento donde la clave expresada en el atributo TipoPercepcion sea igual a 039(Jubilaciones, pensiones o haberes de retiro en una exhibición)  ó 044 (Jubilaciones, pensiones o haberes de retiro en parcialidades).
          atributo_total_jubilacion = percepciones.xpath('''string(@TotalJubilacionPensionRetiro)''', **namespaces)
          if atributo_total_jubilacion:
            total_jubilacion = '%.2f' % float(atributo_total_jubilacion)
            total_jubilacion_calculado = '%.2f' % float(percepciones.xpath('''sum(.//nomina12:Percepcion[(@TipoPercepcion="039" or @TipoPercepcion="044")]/@ImporteGravado |.//nomina12:Percepcion[(@TipoPercepcion="039" or @TipoPercepcion="044")]/@ImporteExento)''', **namespaces))
            if total_jubilacion != total_jubilacion_calculado:
              return False, 'nom192'
          elif float(percepciones.xpath('''sum(.//nomina12:Percepcion[(@TipoPercepcion="039" or @TipoPercepcion="044")]/@ImporteGravado |.//nomina12:Percepcion[(@TipoPercepcion="039" or @TipoPercepcion="044")]/@ImporteExento)''', **namespaces)) > 0.0:
            return False, 'nom192'

          # El valor del atributo Nomina.Percepciones.TotalGravado, debe ser igual a la suma de los atributos ImporteGravado de los nodos Percepcion.
          total_gravado = '%.2f' % float(percepciones.xpath('''sum(@TotalGravado)''', **namespaces))
          total_gravado_calculado = '%.2f' % float(percepciones.xpath('''sum(.//nomina12:Percepcion/@ImporteGravado)''', **namespaces))
          if total_gravado != total_gravado_calculado:
            return False, 'nom193'

          # El valor del atributo Nomina.Percepciones.TotalExento, debe ser igual a la suma de los atributos ImporteExento de los nodos Percepcion.
          total_exento = '%.2f' % float(percepciones.xpath('''sum(@TotalExento)''', **namespaces))
          total_exento_calculado = '%.2f' % float(percepciones.xpath('''sum(.//nomina12:Percepcion/@ImporteExento)''', **namespaces))
          if total_exento != total_exento_calculado:
            return False, 'nom194'
          
          if float(total_exento) > normal_round(total_percepciones, 2):
            return False, 'nom194'

          for percepcion in nodo_percepcion:
            tipo_percepcion = percepcion.xpath('string(@TipoPercepcion)', **namespaces)
            nodo_horas_extras = percepcion.xpath('.//nomina12:HorasExtra', **namespaces)
            # El valor del atributo Nomina.Percepciones.Percepcion.ImporteGravado, La suma de los importes de los atributos ImporteGravado e ImporteExento debe ser mayor que cero.
            total_gravado_exento = percepcion.xpath('sum(@ImporteGravado | @ImporteExento)', **namespaces)
            if total_gravado_exento <= 0.00:
              return False, 'nom195'
            if not catalogos_obj.validar("TipoPercepcion", tipo_percepcion):
              return False, 'nom196'
            # Si la clave expresada en el atributo TipoPercepcion es 019, debe existir el elemento HorasExtra, en caso contrario no debe existir.
            if tipo_percepcion == '019' and not(len(nodo_horas_extras)):
              return False, 'nom204'
            # Si la clave expresada en el atributo TipoPercepcion no es 019, no debe existir el elemento HorasExtra.
            if tipo_percepcion != '019' and len(nodo_horas_extras):
              return False, 'nom205'
            # Si la clave expresada en el atributo TipoPercepcion es 045, debe existir el elemento AccionesOTitulos, en caso contrario no debe existir.
            acciones_titulos = percepcion.xpath("boolean(@TipoPercepcion='045' and not(.//nomina12:AccionesOTitulos))", **namespaces)
            if acciones_titulos:
              return False, 'nom202'
            # Si la clave expresada en el atributo TipoPercepcion es 045, no debe existir el elemento AccionesOTitulos.
            no_acciones_titulos = percepcion.xpath("boolean(not(@TipoPercepcion='045') and .//nomina12:AccionesOTitulos)", **namespaces)
            if no_acciones_titulos:
              return False, 'nom203'

            #El atributo Nomina.Percepciones.Percepcon.HorasExtra.TipoHoras debe ser una clave del catálogo de c_TipoHoras publicado en el portal del SAT en internet.
            if len(nodo_horas_extras):
              for he in nodo_horas_extras:
                tipo_horas_extra = he.xpath('string(@TipoHoras)', **namespaces)
                if not catalogos_obj.validar("TipoHoras", tipo_horas_extra):
                  return False, 'nom208'
            

          # El atributo TipoPercepcion: si la clave expresada es distinta de 022, 023, 025, 039 y 044, debe existir el atributo TotalSueldos.
          sueldos = percepciones.xpath('boolean(.//nomina12:Percepcion[not(@TipoPercepcion="022" or @TipoPercepcion="023" or @TipoPercepcion="025" or @TipoPercepcion="039" or @TipoPercepcion="044")])', **namespaces)
          if sueldos and not atributo_total_sueldos:
            return False, 'nom197'
          # Si la clave expresada en el atributo TipoPercepcion es 022 ó 023 ó 025, debe existir el atributo TotalSeparacionIndemnizacion y el elemento SeparacionIndemnizacion.
          indeminzacion = percepciones.xpath('boolean(.//nomina12:Percepcion[@TipoPercepcion="022" or @TipoPercepcion="023" or @TipoPercepcion="025"] and (not(.//nomina12:SeparacionIndemnizacion) or not(.//@TotalSeparacionIndemnizacion)))', **namespaces)
          if indeminzacion:
            return False, 'nom198'
          # Si la clave expresada en el atributo TipoPercepcion es 039 ó 044, debe existir el atributo TotalJubilacionPensionRetiro y el elemento JubilacionPensionRetiro, en caso contrario no deben existir.
          jubilacion = percepciones.xpath('boolean((.//nomina12:Percepcion/@TipoPercepcion="039" or .//nomina12:Percepcion/@TipoPercepcion="044") and (not(.//nomina12:JubilacionPensionRetiro) or not(@TotalJubilacionPensionRetiro)))', **namespaces)
          if jubilacion:
            return False, 'nom199'
          # Si la clave expresada en el atributo TipoPercepcion es 039 debe existir TotalUnaExhibicion, no deben existir TotalParcialidad, MontoDiario.
          #jubilacion_una_exhibicion = nom_xpath("boolean(.//nomina12:Nomina/nomina12:Percepciones/nomina12:JubilacionPensionRetiro[not(@TotalUnaExhibicion) and @TotalParcialidad and @MontoDiario])", **namespaces)
          #no_jubilacion_una_exhibicion = percepciones.xpath('boolean(.//nomina12:Percepcion/@TipoPercepcion="039") and (not(.//nomina12:JubilacionPensionRetiro/@TotalUnaExhibicion) or (@TotalParcialidad or @MontoDiario))', **namespaces)
          no_jubilacion_una_exhibicion = percepciones.xpath('boolean(.//nomina12:Percepcion/@TipoPercepcion="039") and (not(.//nomina12:JubilacionPensionRetiro/@TotalUnaExhibicion) or (.//nomina12:JubilacionPensionRetiro/@TotalParcialidad or .//nomina12:JubilacionPensionRetiro/@MontoDiario))', **namespaces)
          if no_jubilacion_una_exhibicion:
            return False, 'nom200'
          # Si la clave expresada en el atributo TipoPercepcion es 044 no debe existir TotalUnaExhibicion, deben existir TotalParcialidad, MontoDiario.
          #no_jubilacion_parcialidades = percepciones.xpath("boolean(.//nomina12:Percepcion/@TipoPercepcion='044' and (boolean(.//nomina12:JubilacionPensionRetiro/@TotalUnaExhibicion) or not(.//nomina12:JubilacionPensionRetiro/@TotalParcialidad and .//nomina12:JubilacionPensionRetiro/@MontoDiario)))", **namespaces)
          no_jubilacion_parcialidades = percepciones.xpath("boolean(.//nomina12:Percepcion/@TipoPercepcion='044') and (boolean(.//nomina12:JubilacionPensionRetiro/@TotalUnaExhibicion) or ( not(boolean(.//nomina12:JubilacionPensionRetiro/@TotalParcialidad)) or not(boolean(.//nomina12:JubilacionPensionRetiro/@MontoDiario))))", **namespaces)
          if no_jubilacion_parcialidades:
            return False, 'nom201'
          # Si la clave expresada en el atributo TipoPercepcion es 014 el nodo Incapacidades debe existir.
          codigo_incapacidad = percepciones.xpath("boolean(.//nomina12:Percepcion/@TipoPercepcion='014')", **namespaces)
          no_incapacidad = nom_xpath("boolean(not(.//nomina12:Incapacidades))", **namespaces)
          if codigo_incapacidad and no_incapacidad:
            return False, 'nom206'

          # Si la clave expresada en el atributo TipoPercepcion es 014 la suma de los campos ImporteMonetario debe ser igual a la suma de los valores ImporteGravado e ImporteExento de la percepción.
          importe_monetario = '%.2f' % float(nom_xpath("sum(.//nomina12:Incapacidades/nomina12:Incapacidad/@ImporteMonetario)", **namespaces))
          percepciones_14 = '%.2f' % float(nom_xpath("sum(.//nomina12:Percepcion[@TipoPercepcion='014']/@ImporteExento | .//nomina12:Percepcion[@TipoPercepcion='014']/@ImporteGravado)", **namespaces))
          if codigo_incapacidad and percepciones_14 != importe_monetario:
            return False, 'nom207'

          jubilacion = percepciones.xpath('.//nomina12:JubilacionPensionRetiro', **namespaces)
          # Si existe valor en el atributo Nomina.Percepciones.JubilacionPensionRetiro.TotalUnaExhibicion los atributos MontoDiario y TotalParcialidad no deben existir.
          if len(jubilacion):
            for jub in jubilacion:
              jubilacion_parcialidad = jub.xpath('boolean(@TotalUnaExhibicion and boolean(@MontoDiario or @TotalParcialidad))', **namespaces)
              if jubilacion_parcialidad:
                return False, 'nom209'
              # Si existe valor en el atributo Nomina.Percepciones.JubilacionPensionRetiro.TotalParcialidad el atributo MontoDiario debe existir y el atributo TotalUnaExhibicion no debe existir.
              jubilacion_una_exhibicion = jub.xpath('boolean(@TotalParcialidad and (not(@MontoDiario) or boolean(@TotalUnaExhibicion)))', **namespaces)
              if jubilacion_una_exhibicion:
                return False, 'nom210'
                
        if len(nodo_deducciones):
          deducciones = nodo_deducciones[0]             
          atributo_total_impuestos_retenidos = deducciones.get('TotalImpuestosRetenidos')
          nodo_deduccion = deducciones.xpath('.//nomina12:Deduccion', **namespaces)
          total_impuestos_retenidos_calculados = '%.2f' % float(deducciones.xpath('''sum(.//nomina12:Deduccion[@TipoDeduccion="002"]/@Importe)''', **namespaces))
          #atributo_total_impuestos_retenidos_bool = nom_xpath('''boolean(.//nomina12:Nomina/nomina12:Deducciones/@TotalImpuestosRetenidos)''', **namespaces)
          if atributo_total_impuestos_retenidos or total_impuestos_retenidos_calculados:
            # El valor en el atributo Nomina.Deducciones.TotalImpuestosRetenidos debe ser igual a la suma de los atributos Importe de las deducciones que tengan expresada la clave 002 en el atributo TipoDeduccion.
            atributo_total_impuestos_retenidos = 0.0 if not atributo_total_impuestos_retenidos else atributo_total_impuestos_retenidos
            total_impuestos_retenidos = '%.2f' % float(atributo_total_impuestos_retenidos)
            if  total_impuestos_retenidos != total_impuestos_retenidos_calculados:
              return False, 'nom211'
          # Si no existen deducciones con clave 002, el valor en el atributo Nomina.Deducciones.TotalImpuestosRetenidos no debe existir.
          if deducciones.xpath('''boolean(not(.//nomina12:Deduccion/@TipoDeduccion="002"))''', **namespaces) and atributo_total_impuestos_retenidos:
            return False, 'nom212'
          # El valor de Nomina.Deducciones.Deduccion.TipoDeduccion debe ser una clave del catálogo de c_TipoDeduccion publicado en el portal del SAT en internet.
          for deduccion in nodo_deduccion:
            tipo_deduccion = deduccion.xpath('''string(@TipoDeduccion)''', **namespaces)
            if not catalogos_obj.validar("TipoDeduccion", tipo_deduccion):
              return False, 'nom213'
            # Si la clave expresada en Nomina.Deducciones.Deduccion.TipoDeduccion es 006, debe existir el elemento Incapacidades.
            if tipo_deduccion == "006":
              if nom_xpath("not(.//nomina12:Incapacidades)", **namespaces):
                return False, 'nom214'
              # Si la clave expresada en Nomina.Deducciones.Deduccion.TipoDeduccion es 006, el atributo Deduccion:Importe debe ser igual a la suma de los nodos Incapacidad:ImporteMonetario.
              importe_monetario = '%.2f' % float(nom_xpath("sum(.//nomina12:Incapacidades/nomina12:Incapacidad/@ImporteMonetario)", **namespaces))
              importe_monetario_calculado = '%.2f' % float(deducciones.xpath('''sum(.//nomina12:Deduccion[@TipoDeduccion="006"]/@Importe)''', **namespaces))
              if importe_monetario != importe_monetario_calculado:
                return False, 'nom215'
          # Nomina.Deducciones.Deduccion.Importe Debe ser mayor que cero.
          if deducciones.xpath('''.//nomina12:Deduccion/@Importe<="0.0"''', **namespaces):
            return False, 'nom216'

        # Nomina.Receptor.TipoRegimen si el valor de este atributo es 02 el elemento OtroPago debe contener al menos un atributo TipoOtroPago con clave 002.
        if tipo_regimen == '02':
          if nom_xpath('.//nomina12:OtroPago[@TipoOtroPago="002"]', **namespaces):
            if nom_xpath('.//nomina12:OtroPago[@TipoOtroPago="007" or @TipoOtroPago="008"]', **namespaces):
              return False, 'nom226'
          if nom_xpath('.//nomina12:OtroPago[@TipoOtroPago="007" or @TipoOtroPago="008"]', **namespaces):
            if nom_xpath('.//nomina12:OtroPago[@TipoOtroPago="002"]', **namespaces):
              return False, 'nom226'
          if not nom_xpath('.//nomina12:OtroPago[@TipoOtroPago="002" or @TipoOtroPago="007" or @TipoOtroPago="008"]', **namespaces):
            return False, 'nom226'
        elif nom_xpath('.//nomina12:OtroPago[@TipoOtroPago="002" or @TipoOtroPago="007" or @TipoOtroPago="008"]', **namespaces):
          return False, "nom227"

        if len(nodo_otros_pagos):
          anio_curso = datetime.now().year
          otro_pago = nodo_otros_pagos[0]
          # OLD: Nomina.OtrosPagos.OtroPago.Importe Debe ser mayor que cero.
          # NEW: Nomina.OtrosPagos.OtroPago.Importe si el valor del atributo TipoOtroPago es diferente a 002, este atributo debe ser mayor que cero.
          if otro_pago.xpath('''.//nomina12:OtroPago[@TipoOtroPago!="002"]/@Importe<=0.0''', **namespaces):
            return False, 'nom220'

          nodo_otro_pago = otro_pago.xpath('.//nomina12:OtroPago', **namespaces)
          for ot_pa in nodo_otro_pago:

            ot_pa_importe = ot_pa.get('Importe')
            # Nomina.OtrosPagos.OtroPago.TipoOtroPago debe ser una clave del catálogo de c_TipoOtroPago publicado en el portal del SAT en internet.
            tipo_otro_pago = ot_pa.xpath('string(@TipoOtroPago)', **namespaces)
            if not catalogos_obj.validar("TipoOtroPago", tipo_otro_pago):
              return False, 'nom217'
            # Si el valor de Nomina.OtrosPagos.OtroPago.TipoOtroPago es 004 es obligatorio el nodo CompensacionSaldosAFavor.
            nodo_compensacion_saldos = ot_pa.xpath('.//nomina12:CompensacionSaldosAFavor', **namespaces)
            if tipo_otro_pago == "004" and not len(nodo_compensacion_saldos):
              return False, 'nom218'

            if tipo_otro_pago != '004' and len(nodo_compensacion_saldos):
              return False, 'nom218'
            # Si el valor de Nomina.OtrosPagos.OtroPago.TipoOtroPago es 002 es obligatorio el nodo SubsidioAlEmpleo.
            nodo_subsidio_empleo = ot_pa.xpath('.//nomina12:SubsidioAlEmpleo', **namespaces)

            if tipo_otro_pago == "002":
              if not len(nodo_subsidio_empleo):
                return False, 'nom219'
            
            if tipo_otro_pago not in ("002", "007", "008") and len(nodo_subsidio_empleo):
              return False, 'nom219.A'

            num_dias_pagados = complement_nom.get('NumDiasPagados')

            if len(nodo_subsidio_empleo):
              for subsidio_empleo in nodo_subsidio_empleo:
                subsidio_nodo_otro_pago = subsidio_empleo.xpath('ancestor::nomina12:OtroPago[@TipoOtroPago="002"]', **namespaces)
                subsidio_causado = subsidio_empleo.get("SubsidioCausado")
                if subsidio_nodo_otro_pago:
                  subsidio_otro_pago = subsidio_empleo.xpath('sum(ancestor::nomina12:OtroPago[@TipoOtroPago="002"]/@Importe)', **namespaces)
                  #Nomina.OtrosPagos.OtroPago.Importe si el valor del atributo TipoOtroPago es 002, este atributo debe ser menor o igual que el valor del atributo SubsidioCausado.
                  if trunc(subsidio_causado, 2) < trunc(subsidio_otro_pago, 2):
                    return False, 'nom228'

                # OLD: Nomina.OtrosPagos.OtroPago.SubsidioAlEmpleo.SubsidioCausado debe ser mayor o igual que el valor del atributo "Importe” del nodo OtroPago.
                # NEW: Nomina.OtrosPagos.OtroPago.SubsidioAlEmpleo.SubsidioCausado el valor registrado en este atributo deberá ser menor o igual a 407.02 
                # cuando el valor registrado en el atributo NumDiasPagados es menor o igual a 31.
                if float(num_dias_pagados) <= 31.00 and trunc(subsidio_causado, 2) > 407.02:
                  return False, 'nom221'

                # Nomina.OtrosPagos.OtroPago.SubsidioAlEmpleo.SubsidioCausado el valor registrado en este atributo no debe ser mayor al resultado de multiplicar el factor de 13.39,
                # por el valor registrado en el atributo NumDiasPagados, siempre que este último sea mayor que 31.
                if float(num_dias_pagados) > 31.00 and (trunc((13.39 * float(num_dias_pagados)), 2) < trunc(subsidio_causado, 2)):
                  return False, 'nom229'

            if len(nodo_compensacion_saldos):
              for compensacion in nodo_compensacion_saldos:
                # Nomina.OtrosPagos.OtroPago.CompensacionSaldosAFavor.SaldoAFavor debe ser mayor o igual que el valor del atributo CompensacionSaldosAFavor:RemanenteSalFav.
                if compensacion.xpath("@SaldoAFavor<@RemanenteSalFav", **namespaces):
                  return False, 'nom222'
                try:
                  fecha_pago_str = complement_nom.get('FechaPago', '2017-01-01')
                  fecha_pago_obj = datetime.strptime(fecha_pago_str, '%Y-%m-%d')
                except:
                  fecha_pago_obj = datetime(1900, 1, 1)
                anio_saldo_favor = int(ot_pa.xpath(u'string(//@Año)', **namespaces))

                # OLD: Nomina.OtrosPagos.OtroPago.CompensacionSaldosAFavor.Año debe ser menor que el año en curso.
                # NEW: Nomina.OtrosPagos.OtroPago.CompensacionSaldosAFavor.Año el valor de este campo debe ser igual 
                # al año inmediato anterior o igual al año en curso siempre que el período de pago sea diciembre. 
                # Para determinar el año en curso se deberá considerar el atributo FechaPago.
                if fecha_pago_obj.month == 12 and anio_saldo_favor not in (fecha_pago_obj.year, fecha_pago_obj.year - 1):
                  return False, 'nom223'

        nodo_incapacidades = nom_xpath('.//nomina12:Incapacidades', **namespaces)
        if len(nodo_incapacidades):
          nodo_incapacidad = nodo_incapacidades[0].xpath('.//nomina12:Incapacidad', **namespaces)
          for incapacidad in nodo_incapacidad:
            tipo_incapacidad = incapacidad.xpath('string(@TipoIncapacidad)', **namespaces)
            if not catalogos_obj.validar("TipoIncapacidad", tipo_incapacidad):
              return False, 'nom224'

    except Exception as e:
      print('Exception in nomina validation')
      import sys, os
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      return False, 'nom225'
  return True, None