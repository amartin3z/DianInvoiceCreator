from django.conf import settings

from app.sat.utils.validate import Catalogos
from app.sat.models import LRFC, LCO

from .adicionales import trunc, normal_round, sat_round
from decimal import Decimal

import os
import re

def validacion_cce11(xml_etree, cfdi_version='3.3'):
  try:
    namespace_dicc = {'cfdi': 'http://www.sat.gob.mx/cfd/3', 'cce11': 'http://www.sat.gob.mx/ComercioExterior11'}
    complement_cce11 = xml_etree.xpath('//cfdi:Complemento/cce11:ComercioExterior', namespaces=namespace_dicc)

    catalogos_obj = Catalogos(xml_etree.get('Fecha'))

    cfdi_version = xml_etree.get('version')
    if cfdi_version is None:
      cfdi_version = xml_etree.get('Version')

    if complement_cce11 and cfdi_version not in ('3.2', '3.3'):
      return False, 'CCE101'

    try:
      if xml_etree.xpath('//cce11:ComercioExterior', namespaces=namespace_dicc)[0].getparent().tag != '{http://www.sat.gob.mx/cfd/3}Complemento':
        return False, 'CCE154'
    except:
      pass

    if len(complement_cce11) == 1:

      for namespace in xml_etree.xpath('//namespace::*'):
        if namespace[1] == "http://www.sat.gob.mx/ComercioExterior11" and namespace[0] != 'cce11':
          return False, 'CCE999'
      namespace_dicc = xml_etree.nsmap
      if 'cce11' not in namespace_dicc:
        return False, 'CCE999'

      cce11 = complement_cce11[0]

      siblings = cce11.getparent().getchildren()
      for sibling in siblings:
        tag_name = sibling.tag.split('}', 1)[1]
        if tag_name not in ('ComercioExterior', 'TimbreFiscalDigital', 'ImpuestosLocales', 'LeyendasFiscales', 'CFDIRegistroFiscal', 'Pagos'):
          return False, 'CCE155'
      
      if cfdi_version == '3.2':
        tipo_de_comprobante = xml_etree.get('tipoDeComprobante')
        rfc_receptor = xml_etree.xpath('//cfdi:Receptor', namespaces=namespace_dicc)[0].get('rfc')
      elif cfdi_version == '3.3':
        tipo_de_comprobante = xml_etree.get('TipoDeComprobante')
        rfc_receptor = xml_etree.xpath('//cfdi:Receptor', namespaces=namespace_dicc)[0].get('Rfc')
      tipocambio = xml_etree.get('TipoCambio', '1')
      motivo_traslado = cce11.get('MotivoTraslado')
      propietario = cce11.xpath('//cce11:Propietario', namespaces=namespace_dicc)
      propietarios = cce11.xpath('//cce11:Propietario', namespaces=namespace_dicc)

      if cfdi_version == '3.3':

        print('cce11:Propietario') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        if tipo_de_comprobante not in ('I', 'E', 'T'):
          return False, 'CCE145'
        if tipo_de_comprobante == 'T':
          if not motivo_traslado:
            return False, 'CCE146'
          elif motivo_traslado != '05' and propietario:
            return False, 'CCE148'
          elif motivo_traslado == '05' and not propietario:
              return False, 'CCE147'
        elif motivo_traslado != '05' and propietario:
          return False, 'CCE148'

        print('cce11:Emisor') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        cfdi_emisor_rfc = xml_etree.xpath('//cfdi:Emisor', namespaces=namespace_dicc)[0].get('Rfc')
        if not xml_etree.xpath('//cfdi:Emisor', namespaces=namespace_dicc)[0].get('Nombre'):
          return False, 'CCE149'

        print('cce11:Receptor') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        if tipo_de_comprobante != 'T' and motivo_traslado != '02' and rfc_receptor != 'XEXX010101000':
          return False, 'CCE150'
        if tipo_de_comprobante == 'T' and motivo_traslado == '02':

          if rfc_receptor != 'XEXX010101000' and not LRFC.objects.filter(rfc=rfc_receptor).exists():
            return False, 'CCE151'            
        if not xml_etree.xpath('//cfdi:Receptor', namespaces=namespace_dicc)[0].get('Nombre'):
          return False, 'CCE152'

        #if motivo_traslado == '01' and not xml_etree.get('FolioFiscalOrig'):
        #    return False, 'CCE156'        
        #if motivo_traslado == '05' and len(propietarios) == 0:
        #  return False, 'cce160.2'
        #if motivo_traslado != '05' and len(propietarios):
        #  return False, 'cce160.3'

      print('cce11:CfdiRelacionados') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      if motivo_traslado == '01':
        if cfdi_version == '3.2' and not xml_etree.get('FolioFiscalOrig'):
          return False, 'CCE156'
        if cfdi_version == '3.3':
          try:
            tipo_relacion = xml_etree.xpath('//cfdi:CfdiRelacionados', namespaces=namespace_dicc)[0].get('TipoRelacion')
            if tipo_relacion == '05':
              if not xml_etree.xpath('//cfdi:CfdiRelacionado/@UUID', namespaces=namespace_dicc):
                return False, 'CCE157'
          except:
            return False, 'CCE157'

      tipo_operacion = cce11.get('TipoOperacion')
      clave_pedimento = cce11.get('ClaveDePedimento')
      certificado_origen = cce11.get('CertificadoOrigen')
      num_certificado_origen = cce11.get('NumCertificadoOrigen')
      num_exportador_confiable = cce11.get('NumeroExportadorConfiable')
      incoterm = cce11.get('Incoterm')
      subdivision = cce11.get('Subdivision')
      tipo_cambio_usd = cce11.get('TipoCambioUSD')
      total_usd = cce11.get('TotalUSD')
      mercancias = cce11.xpath('//cce11:Mercancias', namespaces=namespace_dicc)      

      if tipo_operacion == 'A':
        if motivo_traslado or clave_pedimento or certificado_origen or num_certificado_origen or num_exportador_confiable or incoterm or subdivision or tipo_cambio_usd or total_usd or len(mercancias):
          return False, 'CCE158'        
      elif tipo_operacion in ('1', '2'):
        if not (clave_pedimento and certificado_origen and incoterm and subdivision and tipo_cambio_usd and total_usd and len(mercancias)):
          return False, 'CCE159'

      if certificado_origen == '0' and num_certificado_origen:
        return False, 'CCE160'

      try:
        if cfdi_version == '3.2':
          pais_receptor = xml_etree.xpath('//cfdi:Receptor/cfdi:Domicilio/@pais', namespaces=namespace_dicc)[0]
        elif cfdi_version == '3.3':
          pais_receptor = cce11.xpath('//cce11:Receptor/cce11:Domicilio/@Pais', namespaces=namespace_dicc)[0]
      except:
        pais_receptor = None
      try:
        pais_destinatario_lst = cce11.xpath('//cce11:Destinatario/cce11:Domicilio/@Pais', namespaces=namespace_dicc)
      except:
        pais_destinatario_lst = []
      if num_exportador_confiable:
        if pais_receptor and not catalogos_obj.validar('Pais', pais_receptor, agrupaciones='Unión Europea', _type="agrupaciones"):
          return False, 'CCE161'
        for pais_destinatario in pais_destinatario_lst:
          if not catalogos_obj.validar('Pais', pais_receptor, agrupaciones='Unión Europea'):
            return False, 'CCE161'

      total_usd_sum = cce11.xpath('sum(//cce11:Mercancia/@ValorDolares)', namespaces=namespace_dicc)
      if round(float(total_usd),2) != round(total_usd_sum,2):
        return False, 'CCE162'

      total_split = total_usd.split('.')
      if len(total_split) != 2 or len(total_split[1]) != 2:
        return False, 'CCE163'

      print('cce11:Emisor') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      emisor = cce11.xpath('//cce11:Emisor', namespaces=namespace_dicc)
      if emisor:
        curp = emisor[0].get('Curp')        
        if curp and cfdi_emisor_rfc and len(cfdi_emisor_rfc) == 12:
          return False, 'CCE164'
        elif cfdi_emisor_rfc and len(cfdi_emisor_rfc) == 13 and not curp:
          return False, 'CCE165'

      print('cce11:Domicilio') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      cce11_emisor_domicilio = cce11.xpath('//cce11:Emisor/cce11:Domicilio', namespaces=namespace_dicc)
      if cce11_emisor_domicilio:
        if cfdi_version == '3.2':
          return False, 'CCE166'
        pais = cce11_emisor_domicilio[0].get('Pais')
        if pais != 'MEX':
          return False, 'CCE168'
        estado = cce11_emisor_domicilio[0].get('Estado')
        if not catalogos_obj.validar('Estado', estado, pais=pais):
          return False, 'CCE169'
        municipio = cce11_emisor_domicilio[0].get('Municipio')
        if municipio and not catalogos_obj.validar('Municipio', municipio, estado=estado):
          return False, 'CCE170'
        localidad = cce11_emisor_domicilio[0].get('Localidad')
        if localidad and not catalogos_obj.validar('Localidad', localidad, estado=estado):
          return False, 'CCE171'
        cp = cce11_emisor_domicilio[0].get('CodigoPostal')
        if not catalogos_obj.validar('CodigoPostal', cp, estado=estado, municipio=municipio, localidad=localidad):
          return False, 'CCE173'
        colonia = cce11_emisor_domicilio[0].get('Colonia')
        if colonia and re.match('^\d{4}$', colonia) and not catalogos_obj.validar('Colonia', colonia, cp=cp):
          return False, 'CCE172'
      elif cfdi_version == '3.3':
        return False, 'CCE167'

      print('cce11:Domicilio') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      for propietario in propietarios:
        num_reg_id_trib = propietario.get('NumRegIdTrib')
        pais = propietario.get('ResidenciaFiscal')
        if catalogos_obj.validar('Pais', pais):
          if not catalogos_obj.validar('Pais', pais, _type='rit', rit=num_reg_id_trib):
            return False, 'CCE174'
        else:
          if not catalogos_obj.validar('Pais', pais, _type='rit', rit=num_reg_id_trib):
            return False, 'CCE175'

      print('cce11:Receptor/@NumRegIdTrib') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      num_reg_id_trib = cce11.xpath('string(//cce11:Receptor/@NumRegIdTrib)', namespaces=namespace_dicc)

      if cfdi_version == '3.2':
        if not num_reg_id_trib:
          return False, 'CCE177'
        try:
          pais = xml_etree.xpath('//cfdi:Receptor/cfdi:Domicilio/@pais', namespaces=namespace_dicc)[0]
          if pais and catalogos_obj.validar('Pais', pais, _type='pais_rit'):
            if not catalogos_obj.validar('Pais', pais, _type='rit', rit=num_reg_id_trib):
              return False, 'CCE178'
          else:
            if pais and not catalogos_obj.validar('Pais', pais, _type='rit', rit=num_reg_id_trib):
              return False, 'CCE179'
        except Exception as e:
          return False, 'CCE178'
      elif cfdi_version == '3.3':
        if num_reg_id_trib:
          return False, 'CCE176'

      print('cce11:Receptor/cce11:Domicilio') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      receptor_domicilio = cce11.xpath('//cce11:Receptor/cce11:Domicilio', namespaces=namespace_dicc)
      if cfdi_version == '3.2' and receptor_domicilio:
        return False, 'CCE180'
      if cfdi_version == '3.3' and not receptor_domicilio:
        return False, 'CCE181'
      if receptor_domicilio:
        pais = receptor_domicilio[0].get('Pais')
        colonia = receptor_domicilio[0].get('Colonia')
        localidad = receptor_domicilio[0].get('Localidad')
        municipio = receptor_domicilio[0].get('Municipio')
        estado = receptor_domicilio[0].get('Estado')
        cp = receptor_domicilio[0].get('CodigoPostal')

        if cfdi_version == '3.3':
          if pais == 'MEX':
            if colonia and re.match('^\d{4}$', colonia) and not catalogos_obj.validar('Colonia', colonia, cp=cp):
                return False, 'CCE182'
            if not catalogos_obj.validar('Localidad', localidad, estado=estado):
                return False, 'CCE183'
            if not catalogos_obj.validar('Municipio', municipio, estado=estado):
                return False, 'CCE184'
          if catalogos_obj.validar('Estado', None, pais=pais) and not catalogos_obj.validar('Estado', estado, pais=pais):
            return False, 'CCE185'
          if pais != 'MEX' and not catalogos_obj.validar('Pais', pais, _type='pais_cp', cp=cp):
            return False, 'CCE186'
          if pais == 'MEX' and not catalogos_obj.validar('CodigoPostal', cp, estado=estado, municipio=municipio, localidad=localidad):
            return False, 'CCE187'

      print('cce11:Destinatario') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      destinatarios = cce11.xpath('//cce11:Destinatario', namespaces=namespace_dicc)
      if tipo_de_comprobante in ('T', 'traslado') and len(destinatarios) > 1:
        return False, 'CCE188'

      for destinatario in destinatarios:
        num_reg_id_trib = destinatario.get('NumRegIdTrib')
        if num_reg_id_trib:
          pais = destinatario.xpath('.//cce11:Domicilio/@Pais', namespaces=namespace_dicc)[0]
          if catalogos_obj.validar('Pais', pais, _type='pais_rit'):
            if not catalogos_obj.validar('Pais', pais, _type='rit', rit=num_reg_id_trib):
              return False, 'CCE189'
          else:
            if not catalogos_obj.validar('Pais', pais, _type='rit', rit=num_reg_id_trib):
              return False, 'CCE190'

        print('cce11:Domicilio') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        domicilio = destinatario.xpath('.//cce11:Domicilio', namespaces=namespace_dicc)[0]
        pais = domicilio.get('Pais')
        cp = domicilio.get('CodigoPostal')
        estado = domicilio.get('Estado')
        colonia = domicilio.get('Colonia')
        localidad = domicilio.get('Localidad')
        municipio = domicilio.get('Municipio')

        if pais == 'MEX':            
          if colonia and re.match('^\d{4}$', colonia) and not catalogos_obj.validar('Colonia', colonia, cp=cp):
            return False, 'CCE191'
          if not catalogos_obj.validar('Localidad', localidad, estado=estado):
            return False, 'CCE192'
          if not catalogos_obj.validar('Municipio', municipio, estado=estado):
            return False, 'CCE193'
          if not catalogos_obj.validar('CodigoPostal', cp, estado=estado, municipio=municipio, localidad=localidad):
            return False, 'CCE196'
        else:
          if pais != 'ZZZ' and catalogos_obj.validar('Estado', None, pais=pais) and not catalogos_obj.validar('Estado', estado, pais=pais):
            return False, 'CCE194'
          if not catalogos_obj.validar('Pais', pais, _type='pais_cp', cp=cp):
            return False, 'CCE195'

      print('cce11:Mercancias') if settings.VERBOSE_EXTRA_VALIDATIONS else None
      conceptos_cfdi = xml_etree.xpath('//cfdi:Conceptos/cfdi:Concepto', namespaces=namespace_dicc)
      if cfdi_version == '3.2':
        conceptos_noidentificacion_cfdi = xml_etree.xpath('//cfdi:Conceptos/cfdi:Concepto/@noIdentificacion', namespaces=namespace_dicc)
      elif cfdi_version == '3.3':
        conceptos_noidentificacion_cfdi = xml_etree.xpath('//cfdi:Conceptos/cfdi:Concepto/@NoIdentificacion', namespaces=namespace_dicc)
      mercancias_noidentificacion = cce11.xpath('//cce11:Mercancias/cce11:Mercancia/@NoIdentificacion', namespaces=namespace_dicc)

      if len(conceptos_cfdi) != len(conceptos_noidentificacion_cfdi):
        return False, 'CCE197'

      found = False
      for c_noidentificacion in conceptos_noidentificacion_cfdi:
        if c_noidentificacion in mercancias_noidentificacion:
          found = True
          break
      if not found:
        return False, 'CCE198'
      
      for m_noidentificacion in mercancias_noidentificacion:
        if m_noidentificacion not in conceptos_noidentificacion_cfdi:
          return False, 'CCE199'

    
      mercancias = cce11.xpath('//cce11:Mercancias/cce11:Mercancia', namespaces=namespace_dicc)
      same = set([True if item in mercancias_noidentificacion else False for item in conceptos_noidentificacion_cfdi]).pop()
      if False and not same:
        return False, 'cce181'

      moneda = xml_etree.get('Moneda')
      result_moneda = catalogos_obj.obtener('Moneda', moneda)
      
      noidentificacion_fraccionarancelaria = {}
      for mercancia in mercancias:
        noidentificacion = mercancia.get('NoIdentificacion')
        fraccion_arancelaria = mercancia.get('FraccionArancelaria')
        cantidad_aduana = mercancia.get('CantidadAduana')
        unidad_aduana = mercancia.get('UnidadAduana')
        valor_dolares = mercancia.get('ValorDolares')
        valor_unitario_aduana = mercancia.get('ValorUnitarioAduana')

        if noidentificacion not in noidentificacion_fraccionarancelaria.keys():
          noidentificacion_fraccionarancelaria[noidentificacion] = []
        if fraccion_arancelaria:          
          if fraccion_arancelaria not in noidentificacion_fraccionarancelaria[noidentificacion]:
            noidentificacion_fraccionarancelaria[noidentificacion].append(fraccion_arancelaria)
          else:
            return False, 'CCE200'

        if cfdi_version == '3.2':
          concepto_cfdi = xml_etree.xpath('//cfdi:Concepto[@noIdentificacion="%s"]' % noidentificacion, namespaces=namespace_dicc)[0]
          cantidad = concepto_cfdi.get('cantidad')        
          unidad = concepto_cfdi.get('unidad')
          importe = concepto_cfdi.get('importe')
          valor_unitario = concepto_cfdi.get('valorUnitario')
        elif cfdi_version == '3.3':
          try:
            concepto_cfdi = xml_etree.xpath('//cfdi:Concepto[@NoIdentificacion="%s"]' % noidentificacion, namespaces=namespace_dicc)[0]
          except:
            concepto_cfdi = xml_etree.xpath('''//cfdi:Concepto[@NoIdentificacion='%s']''' % noidentificacion, namespaces=namespace_dicc)[0]
          cantidad = concepto_cfdi.get('Cantidad')        
          unidad = concepto_cfdi.get('Unidad')
          importe = concepto_cfdi.get('Importe')
          valor_unitario = concepto_cfdi.get('ValorUnitario')

        if not cantidad_aduana:
          if float(cantidad) < 0.001 or not re.match('^[0-9]{1,14}(.([0-9]{1,3}))?$', cantidad):
            return False, 'CCE201'
          if not catalogos_obj.validar('UnidadMedida', unidad):
            return False, 'CCE202'
          if float(valor_unitario) < 0.0001 or not re.match('^[0-9]{1,16}(.([0-9]{1,4}))?$', valor_unitario):
            return False, 'CCE203'
          decimals = re.search('\.(\d+)', valor_unitario)
          if decimals and int(result_moneda['dec']) != len(decimals.group(1)):
            return False, 'CCE203'

        cantidad_decimales = 0
        try:
          cantidad_decimales = len(cantidad.split('.', 1)[1])
        except:
          pass
        valorunitario_decimales = 0
        try:
          valorunitario_decimales = len(valor_unitario.split('.', 1)[1])
        except:
          pass
        inferior = (float(cantidad) - (10**-cantidad_decimales) / 2.0) * (float(valor_unitario) - (10**-valorunitario_decimales) / 2.0 )
        superior =  (float(cantidad) + (10**-cantidad_decimales) / 2.0 - (10**-12)) * (float(valor_unitario) + (10**-valorunitario_decimales) / 2.0 - 10**-12)
        # @TODO: inferior truncado a la cantidad de decimales que soporta la moneda
        # @TODO: superior redondeado hacia arriba a la cantidad de decimales que soporta la moneda
        inferior = trunc(inferior, 2)
        superior = trunc(superior, 2, True)
        if not (float(importe) >= inferior and float(importe) <= superior):
          return False, 'CCE204'

        if valor_dolares and float(valor_dolares) not in (0.0, 1.0):
        #if (valor_dolares and float(valor_dolares) not in (0.0, 1.0)) and moneda != 'USD': # Comunicado SAT => SAT Orientación: Duda respecto a aplicación de validaciones Complemento Comercio Exterior 
          if cfdi_version == '3.2':
            importe = xml_etree.xpath('sum(//cfdi:Concepto[@noIdentificacion="%s"]/@importe)' % noidentificacion, namespaces=namespace_dicc)
          elif cfdi_version == '3.3':
            try:
              importe = xml_etree.xpath('sum(//cfdi:Concepto[@NoIdentificacion="%s"]/@Importe)' % noidentificacion, namespaces=namespace_dicc)
              importe_dec = xml_etree.xpath('//cfdi:Concepto[@NoIdentificacion="%s"]/@Importe' % noidentificacion, namespaces=namespace_dicc)[0]
            except:
              importe = xml_etree.xpath('''sum(//cfdi:Concepto[@NoIdentificacion='%s']/@Importe)''' % noidentificacion, namespaces=namespace_dicc)
              importe_dec = xml_etree.xpath('''//cfdi:Concepto[@NoIdentificacion='%s']/@Importe''' % noidentificacion, namespaces=namespace_dicc)[0]
          # @TODO: Convertir a la moneda en la que se expresa el comprobante
          importe_decimales = 0
          try:            
            importe_decimales = len(str(importe_dec).split('.', 1)[1])
          except:
            pass
          tipocambio_decimales = 0
          try:
            tipocambio_decimales = len(tipocambio.split('.', 1)[1])
          except:
            pass
          inferior = (float(importe) - (10**-importe_decimales) / 2.0 ) * (float(tipocambio) - (10**-tipocambio_decimales) / 2.0) / (float(tipo_cambio_usd) + (10**-tipocambio_decimales) / 2.0 - 10**-12 )
          superior = (float(importe) + (10**-importe_decimales) / 2.0 - 10**-12) * (float(tipocambio) + (10**-tipocambio_decimales) / 2.0 - 10**-12) / (float(tipo_cambio_usd) - (10**-tipocambio_decimales) / 2.0 )
          # @TODO: inferior truncado a centésimas
          # @TODO: superior redondeado hacia arriba a centésimas
          inferior = trunc(inferior, 2)
          superior = trunc(superior, 2, True)
          print('cce11:Mercancias/cce11:Mercancia') if settings.VERBOSE_EXTRA_VALIDATIONS else None
          try:
            sum_valor_dolares = cce11.xpath('sum(//cce11:Mercancias/cce11:Mercancia[@NoIdentificacion="%s"]/@ValorDolares)' % noidentificacion, namespaces=namespace_dicc)
          except:
            sum_valor_dolares = cce11.xpath('''sum(//cce11:Mercancias/cce11:Mercancia[@NoIdentificacion='%s']/@ValorDolares)''' % noidentificacion, namespaces=namespace_dicc)
          if not (sum_valor_dolares >= inferior and sum_valor_dolares <= superior):
            return False, 'CCE205'

        if not fraccion_arancelaria and not '99' in (unidad, unidad_aduana):
          return False, 'CCE206'
        if fraccion_arancelaria and '99' in (unidad, unidad_aduana):
          return False, 'CCE207'

        if cfdi_version == '3.2':          
          fecha_comprobante = xml_etree.get('fecha')
        elif cfdi_version == '3.3':          
          fecha_comprobante = xml_etree.get('Fecha')
        if fraccion_arancelaria and not catalogos_obj.validar('FraccionArancelaria', fraccion_arancelaria):
          return False, 'CCE208'
        if '99' not in (unidad, unidad_aduana):
          if unidad_aduana:
            if not catalogos_obj.validar('FraccionArancelaria', fraccion_arancelaria, unidad=unidad_aduana):
              return False, 'CCE209'
          elif unidad:
            if not catalogos_obj.validar('FraccionArancelaria', fraccion_arancelaria, unidad=unidad):
              return False, 'CCE210'

        print('cce11:Mercancias/cce11:Mercancia[@FraccionArancelaria') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        if fraccion_arancelaria == '98010001':
          if cfdi_version == '3.2':
            valor_dolares_sum = cce11.xpath('sum(//cce11:Mercancias/cce11:Mercancia[@FraccionArancelaria="98010001"]/@ValorDolares)', namespaces=namespace_dicc)
            valor = valor_dolares_sum * float(tipo_cambio_usd) / float(tipocambio) 
            descuento = xml_etree.get('descuento')
            if not descuento or float(descuento) < valor:
              return False, 'CCE211'
          elif cfdi_version == '3.3':
            try:
              descuento_sum = xml_etree.xpath('sum(//cfdi:Conceptos/cfdi:Concepto[@NoIdentificacion="%s"]/@Descuento)' % noidentificacion, namespaces=namespace_dicc)
            except:
              descuento_sum = xml_etree.xpath('''sum(//cfdi:Conceptos/cfdi:Concepto[@NoIdentificacion='%s']/@Descuento)''' % noidentificacion, namespaces=namespace_dicc)
            descuento = Decimal(descuento_sum) * Decimal(tipo_cambio_usd) / Decimal(tipocambio)
            try:
              valor_dolares_sum = cce11.xpath('sum(//cce11:Mercancias/cce11:Mercancia[@FraccionArancelaria="98010001" and @NoIdentificacion="%s"]/@ValorDolares)' % noidentificacion, namespaces=namespace_dicc)
            except:
              valor_dolares_sum = cce11.xpath('''sum(//cce11:Mercancias/cce11:Mercancia[@FraccionArancelaria="98010001" and @NoIdentificacion='%s']/@ValorDolares)''' % noidentificacion, namespaces=namespace_dicc)
            if float(descuento) < valor_dolares_sum:
              return False, 'CCE212'        
        
        if (cantidad_aduana or unidad_aduana or valor_unitario_aduana) and not (cantidad_aduana and unidad_aduana and valor_unitario_aduana):
          return False, 'CCE213'
        if cfdi_version == '3.2':
          count_conceptos = xml_etree.xpath('count(//cfdi:Conceptos/cfdi:Concepto[@noIdentificacion="%s"])' % noidentificacion, namespaces=namespace_dicc)
        elif cfdi_version == '3.3':
          try:
            count_conceptos = xml_etree.xpath('count(//cfdi:Conceptos/cfdi:Concepto[@NoIdentificacion="%s"])' % noidentificacion, namespaces=namespace_dicc)
          except:
            count_conceptos = xml_etree.xpath('''count(//cfdi:Conceptos/cfdi:Concepto[@NoIdentificacion='%s'])''' % noidentificacion, namespaces=namespace_dicc)
        if count_conceptos > 1 and not (cantidad_aduana and unidad_aduana and valor_unitario_aduana):
          return False, 'CCE213'
        try:
          count_mercancias = cce11.xpath('count(//cce11:Mercancias/cce11:Mercancia[@NoIdentificacion="%s"])' % noidentificacion, namespaces=namespace_dicc)
        except:
          count_mercancias = cce11.xpath('''count(//cce11:Mercancias/cce11:Mercancia[@NoIdentificacion='%s'])''' % noidentificacion, namespaces=namespace_dicc)
        if count_mercancias > 1 and not (cantidad_aduana and unidad_aduana and valor_unitario_aduana):
          return False, 'CCE213'

        print('cce11:Mercancias/cce11:Mercancia[@CantidadAduana') if settings.VERBOSE_EXTRA_VALIDATIONS else None
        if cantidad_aduana and unidad_aduana and valor_unitario_aduana:
          mandatory_mercancias = cce11.xpath('//cce11:Mercancias/cce11:Mercancia[@CantidadAduana and @UnidadAduana and @ValorUnitarioAduana]', namespaces=namespace_dicc)          
          if len(mercancias) != len(mandatory_mercancias):
            return False, 'CCE214'      
        if unidad_aduana != '99' and valor_unitario_aduana and not float(valor_unitario_aduana) > 0:
            return False, 'CCE215'
        
        if cantidad_aduana:
          decimales_cantidad = 0
          try:
            decimales_cantidad = len(cantidad_aduana.split('.', 1)[1])
          except:
            pass
          decimales_valorunitario = 0
          try:
            decimales_valorunitario = len(valor_unitario_aduana.split('.', 1)[1])
          except:
            pass
          
          
          inferior = (float(cantidad_aduana) - (10**-cantidad_decimales) / 2.0 ) * (float(valor_unitario_aduana) - (10**-valorunitario_decimales) / 2.0)
          superior = (float(cantidad_aduana) + (10**-cantidad_decimales) / 2.0 - 10**-12) * (float(valor_unitario_aduana) + (10**-valorunitario_decimales) / 2.0 - 10**-12)
          inferior = trunc(inferior, 2)
          superior = trunc(superior, 2, True)
          if not ((float(valor_dolares) >= inferior and float(valor_dolares) <= superior) or  valor_dolares in ('1', '1.0')):
            print ("valor_dolares => %s" % valor_dolares)
            print ("inferior => %s" % inferior)
            print ("superior => %s" % superior)
            return False, 'CCE216'        
        else:
          if cfdi_version == '3.2':
            importe_concepto = float(concepto_cfdi.get('importe'))          
            importe = xml_etree.xpath('sum(//cfdi:Concepto[@noIdentificacion="%s"]/@importe)' % noidentificacion, namespaces=namespace_dicc)
          elif cfdi_version == '3.3':
            importe_concepto = float(concepto_cfdi.get('Importe'))
            try: 
              importe = xml_etree.xpath('sum(//cfdi:Concepto[@NoIdentificacion="%s"]/@Importe)' % noidentificacion, namespaces=namespace_dicc)
              importe_dec = xml_etree.xpath('//cfdi:Concepto[@NoIdentificacion="%s"]/@Importe' % noidentificacion, namespaces=namespace_dicc)[0]
            except:
              importe = xml_etree.xpath('''sum(//cfdi:Concepto[@NoIdentificacion='%s']/@Importe)''' % noidentificacion, namespaces=namespace_dicc)
              importe_dec = xml_etree.xpath('''//cfdi:Concepto[@NoIdentificacion='%s']/@Importe''' % noidentificacion, namespaces=namespace_dicc)[0]
          tipo_cambio_comprobante = float(xml_etree.get('TipoCambio'))
          vd = importe_concepto * tipo_cambio_comprobante / float(tipo_cambio_usd)


          # @TODO: Convertir a la moneda en la que se expresa el comprobante
          importe_decimales = 0
          try:            
            importe_decimales = len(str(importe_dec).split('.', 1)[1])
          except:
            pass
          tipocambio_decimales = 0
          try:
            tipocambio_decimales = len(tipocambio.split('.', 1)[1])
          except:
            pass
          inferior = (float(importe) - (10**-importe_decimales) / 2.0 ) * (float(tipocambio) - (10**-tipocambio_decimales) / 2.0) / (float(tipo_cambio_usd) + (10**-tipocambio_decimales) / 2.0 - 10**-12 )
          superior = (float(importe) + (10**-importe_decimales) / 2.0 - 10**-12) * (float(tipocambio) + (10**-tipocambio_decimales) / 2.0 - 10**-12) / (float(tipo_cambio_usd) - (10**-tipocambio_decimales) / 2.0 )
          # @TODO: inferior truncado a centésimas
          # @TODO: superior redondeado hacia arriba a centésimas
          inferior = trunc(inferior, 2)
          superior = trunc(superior, 2, True)
          
          unidad_cce11 = 'unidad'
          if cfdi_version == '3.3':
            unidad_ce11 = 'Unidad'

          if not (vd >= inferior and vd <= superior):
            return False, 'CCE217'          
          elif (unidad_aduana == '99' or concepto_cfdi.get(unidad_cce11) == '99') and valor_dolares not in ('0', '0.0'):
              return False, 'CCE217'
          elif False and valor_dolares not in ('1', '1.0'):
            return False, 'CCE217'      

    elif len(complement_cce11) > 1:
      return False, 'CCE153'
  except Exception as e:
    print(f'Exception in cce11 validation {e}')
    import sys
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    return False, 'CCE218'

  return True, None