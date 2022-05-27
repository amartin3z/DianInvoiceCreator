# -*- encoding: UTF-8 -*-

from django.conf import settings

from app.invoicing.utils import CFDI as CFDI33 
from app.invoicing.models import ProdServ, Receiver

from app.sat.models import CodigoPostal
from app.sat.utils.validate import Catalogos
from app.cfdi.utils.validate.adicionales import trunc, normal_round
from app.cfdi.utils.validate.utils import get_original_string, get_summer_dates

from io import StringIO as cStringIO
from io import StringIO
from datetime import datetime, timedelta
from copy import deepcopy
from json import loads
from decimal import (
  Decimal, 
  ROUND_UP,
  ROUND_HALF_EVEN, 
)

import pytz
import hashlib
from base64 import b64encode
from M2Crypto.RSA import load_key_string
from pdb import set_trace

# def trunc(num, digits, r=False):
#   if r:
#     factor = ''  
#     for n in range(digits-1):
#       factor += '0'
#     if r == 'EVEN':
#       num = Decimal(str(num)).quantize(Decimal('.%s1' % factor), rounding=ROUND_HALF_EVEN)
#     else:
#       num = Decimal(str(num)).quantize(Decimal('.%s1' % factor), rounding=ROUND_UP)
#   try:
#     sp = str(num).split('.')
#     if len(sp) > 1:
#       return float('.'.join([sp[0], sp[1][:digits]]))
#   except:
#     sp = str(Decimal(num)).split('.')
#     if len(sp) > 1:
#       return float('.'.join([sp[0], sp[1][:digits]]))
#   return Decimal(num)

class CFDI(object):

  def __init__(self, cfdi, business=None, public_certificate=None, private_certificate=None, serial=None, tipo='invoice'):
    
    self.emails = None
    self.success = False
    self.receiver = None    
    self.xml_string = None

    self.total_tra = Decimal(0.0)
    self.total_ret = Decimal(0.0)
    
    self.taxpayer_id = business.taxpayer_id

    self.certificate_number = serial
    self.public_certificate = public_certificate
    self.private_certificate = private_certificate

    self.emission_date = None
    
    self.xml_json = {}
    self.impuestos_generales = {'Retenciones': {}, 'Traslados': {}}

    self.negocio = business
    self.comprobante = cfdi
    # self.certificado = certificate
    
    self.output = StringIO()
    self.output_utf8 = cStringIO()
    self.seal = ''

    self.tipo = tipo
    self.decimales = 2

  def get_cfdi_string(self):
    try:
      comprobante = loads(self.comprobante)
      self.xml_json = deepcopy(comprobante)

      self.emission_date = self.get_emission_date(self.xml_json.get('LugarExpedicion'))

      self.decimales = self.get_currency_decimals(self.xml_json.get('Moneda'))

      conceptos = self.remove_empty_from_dict(comprobante.pop('Conceptos', []))
      conceptos_obj = CFDI33.ConceptosType()
      if self.tipo == 'invoice':
        for concepto in conceptos:
          #IMPUESTOS CONCEPTOS  
          if 'Impuestos' in concepto:
          
            traslados_concepto_obj = None
            retenciones_concepto_obj = None
            columnas_traslados = ['Impuesto', 'TipoFactor', 'TasaOCuota']

            impuestos_conceptos = self.remove_empty_from_dict(concepto.pop('Impuestos', []))
            
            traslados_concepto = self.remove_empty_from_dict(impuestos_conceptos.pop('Traslados', []))
            retenciones_concepto = self.remove_empty_from_dict(impuestos_conceptos.pop('Retenciones', []))
            #IMPUESTOS CONCEPTOS TRASLADOS
            if len(traslados_concepto):
              traslados_concepto_obj = CFDI33.TrasladosType()
              for trasladoc in traslados_concepto:
                tras_impuesto = trasladoc.get('Impuesto')
                tras_factor = trasladoc.get('TipoFactor')
                tras_tasa = trasladoc.get('TasaOCuota')
                id_impuesto = f'{tras_impuesto}-{tras_factor}-{tras_tasa}'
                if id_impuesto not in self.impuestos_generales:
                  self.impuestos_generales['Traslados'][id_impuesto] = Decimal(0.0)
                self.impuestos_generales['Traslados'][id_impuesto] += Decimal(trasladoc.get('Importe'))
                if 'exento' in id_impuesto.lower():
                  trasladoc.pop('TasaOCuota', None)
                  trasladoc.pop('Importe', None)
                traslados_concepto_obj.add_Traslado(CFDI33.TrasladoType(**trasladoc))
            #IMPUESTOS CONCEPTOS RETENIDOS
            if len(retenciones_concepto):
              retenciones_concepto_obj = CFDI33.RetencionesType()
              for retencionc in retenciones_concepto:
                id_impuesto = retencionc.get('Impuesto')
                if id_impuesto not in self.impuestos_generales:
                  self.impuestos_generales['Retenciones'][id_impuesto] = Decimal(0.0)
                self.impuestos_generales['Retenciones'][id_impuesto] += Decimal(retencionc.get('Importe'))
                retenciones_concepto_obj.add_Retencion(CFDI33.RetencionType(**retencionc))
            
            if traslados_concepto_obj or retenciones_concepto_obj:
              concepto['Impuestos'] = CFDI33.ImpuestosType(Traslados=traslados_concepto_obj, Retenciones=retenciones_concepto_obj)
            else:
              #Quitando la llave Impuestos de concepto json...
              concepto.pop('Impuestos', None)

          prodserv = ProdServ.objects.get(business=self.negocio, identifier=concepto['NoIdentificacion'], prodserv=concepto['ClaveProdServ'])
          concepto.update({
            'ValorUnitario': prodserv.unit_price
          })
          descuento = concepto.pop('Descuento', None)
          if descuento is not None and descuento and float(descuento) != 0.0:
            concepto.update({
              'Descuento': descuento
            })

          if prodserv.description:
            concepto.update({
              'Descripcion': prodserv.description
            })
          if prodserv.unit:
            concepto.update({
              'Unidad': prodserv.unit
            })


          conceptos_obj.add_Concepto(CFDI33.ConceptoType(**concepto))
        comprobante['Conceptos'] = conceptos_obj  
      elif self.tipo == 'payment':
        concepto = {
          'ValorUnitario': '0',
          'Descripcion': 'Pago',
          'ClaveUnidad': 'ACT',
          'ClaveProdServ': '84111506',
          'Importe': '0',
          'Cantidad': '1',
        }
        conceptos_obj.add_Concepto(CFDI33.ConceptoType(**concepto))
        comprobante['Conceptos'] = conceptos_obj
      #IMPUESTOS GENERALES
      if True or 'Impuestos' in comprobante:
        impuestos_general = comprobante.pop('Impuestos', None)

        traslados_obj = None
        retenciones_obj = None
        
        total_impuestos_retenidos = None
        total_impuestos_traslados = None


        #traslados = impuestos_general.pop('Traslados', None)
        #retenciones = impuestos_general.pop('Retenciones', None)
        traslados = self.impuestos_generales.pop('Traslados', None)
        retenciones = self.impuestos_generales.pop('Retenciones', None)
        #IMPUESTOS TRASLADOS
        if traslados:
          total_impuestos_traslados = Decimal(0.0)
          traslados_obj = CFDI33.TrasladosType()
          len_traslados = len(traslados)
          counter_traslados_exentos = 0
          for valores, importe in traslados.items():
            total_impuestos_traslados += importe
            if 'exento' in valores.lower():
              counter_traslados_exentos += 1
              continue
            impuestos = {
              'Importe': importe,
            }
            impuestos.update(zip(columnas_traslados, valores.split('-')))

            # if impuestos.get('TipoFactor', None) == 'Exento':
              # impuestos.pop('Importe', None)
              # impuestos.pop('TasaOCuota', None)

            traslados_obj.add_Traslado(CFDI33.TrasladoType6(**impuestos))
          
          if traslados is not None:
            if len_traslados == counter_traslados_exentos:
              traslados_obj = None
        
        if retenciones:
          total_impuestos_retenidos = Decimal(0.0)
          retenciones_obj = CFDI33.RetencionesType()
          for impuesto, importe in retenciones.items():
            total_impuestos_retenidos += importe
            
            retenciones_obj.add_Retencion(CFDI33.RetencionType4(Impuesto=impuesto, Importe=importe))

        if traslados_obj or retenciones_obj:
          impuestos_obj = CFDI33.ImpuestosType2(
            Traslados=traslados_obj,
            Retenciones=retenciones_obj,
          )
          if total_impuestos_retenidos is not None:
            impuestos_obj.set_TotalImpuestosRetenidos(trunc(total_impuestos_retenidos, self.decimales, True))
          if total_impuestos_traslados is not None:
            impuestos_obj.set_TotalImpuestosTrasladados(trunc(total_impuestos_traslados, self.decimales, True))

          comprobante['Impuestos'] = impuestos_obj
        else:
          comprobante.pop('Impuestos',None)
      # RECEPTOR
      receptor = comprobante.pop('Receptor')
      # self.emails = receptor.pop('emails')
      receiver = receptor.get('Rfc', '')
      
      self.receiver = Receiver.objects.get(business=self.negocio, taxpayer_id=receiver, status=True)
      if self.receiver.name:
        receptor.update({'Nombre': self.receiver.name})

      rit = receptor.pop('NumRegIdTrib', None)
      if rit is not None and rit.strip():
        receptor.update({'NumRegIdTrib': rit})

      receiver_fiscal_address = receptor.pop('ResidenciaFiscal', None)
      if receiver_fiscal_address is not None and receiver_fiscal_address.strip():
        receptor.update({'ResidenciaFiscal': receiver_fiscal_address})
      
      comprobante['Receptor'] = CFDI33.ReceptorType(**receptor)

      emisor_type_obj = CFDI33.EmisorType(
        Rfc=self.taxpayer_id,
        RegimenFiscal=self.negocio.fiscal_regime,
      )
      if self.negocio.name and self.negocio.name.strip():
        emisor_type_obj.set_Nombre(self.negocio.name)
      comprobante['Emisor'] = emisor_type_obj
      
      self.xml_json.update({
        'NoCertificado': self.certificate_number,
        'Fecha': self.emission_date,
        'Version': '3.3',
        'LugarExpedicion': self.negocio.address.zipcode
      })

      if 'CfdiRelacionados' in comprobante:
        cfdi_relacionados = self.remove_empty_from_dict(comprobante.pop('CfdiRelacionados'))
        if cfdi_relacionados.get('CfdiRelacionado', False):
          cfdi_relacionados_obj = CFDI33.CfdiRelacionadosType(cfdi_relacionados.get('TipoRelacion'))
          for uuid_relacionado in cfdi_relacionados.get('CfdiRelacionado', []):
            cfdi_relacionados_obj.add_CfdiRelacionado(CFDI33.CfdiRelacionadoType(**uuid_relacionado))

          comprobante['CfdiRelacionados'] = cfdi_relacionados_obj

      ##PAGOS##
      if self.tipo == 'payment':
        complemento_obj = self.generate_pagos(comprobante)
        comprobante['Complemento'] = complemento_obj
      #######
      namespaces = 'xmlns:cfdi="http://www.sat.gob.mx/cfd/3"'
      schemaLocation = ' xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd"'
      if self.tipo ==  'payment':
        namespaces = 'xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:pago10="http://www.sat.gob.mx/Pagos"'
        schemaLocation = ' xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd http://www.sat.gob.mx/Pagos http://www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos10.xsd"'
      #GENERAL
      comprobante.update({
        'NoCertificado': self.certificate_number,
        'Certificado': self.public_certificate,
        'Fecha': self.emission_date,
        'Version': '3.3',
        # 'LugarExpedicion': self.negocio.address.zipcode,
        'ns_': namespaces
      })
      comprobante = self.remove_empty_from_dict(comprobante)
      cfdi_obj = CFDI33.Comprobante(**comprobante)
      try:
        cfdi_obj.export(self.output, 0, schemaLocation=schemaLocation,pretty_print=False)
        self.xml_string = self.output.getvalue()
        print(self.xml_string)
      except:
        cfdi_obj.export(self.output_utf8, 0, pretty_print=False)
        self.xml_string = self.output_utf8.getvalue()
      try:
        self.xml_string = self.xml_string.encode('utf-8')
      except:
        pass
      self.xml_string = self.get_signed_invoice(self.get_scaped_cfdi(self.xml_string))
      try:
        impuestos = cfdi_obj.get_Impuestos()
        self.total_ret = impuestos.get_TotalImpuestosRetenidos()
        self.total_tra = impuestos.get_TotalImpuestosTrasladados()
      except Exception as e:
        pass
      self.success = True
    except Exception as e:
      import sys, os
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print('Exception get_cfdi_string {}'.format(e))


  def generate_pagos(self, comprobante):
    complemento = self.remove_empty_from_dict(comprobante.pop('Complemento', {}))
    pagos = self.remove_empty_from_dict(complemento.pop('Pagos'))
    pago = pagos.pop('Pago')
    fechapago = pago.pop('FechaPago', None)
    if fechapago is not None:
      pago['FechaPago'] = datetime.strptime(fechapago, '%m/%d/%Y').isoformat()
    docto = pago.pop('DoctoRelacionado')

    pagos_obj = CFDI33.Pagos()
    pago_obj = CFDI33.PagoType(**pago)

    for dr in docto:
      dr_obj = CFDI33.DoctoRelacionadoType(**dr)       
      pago_obj.add_DoctoRelacionado(dr_obj)
    pagos_obj.add_Pago(pago_obj)
    complemento_obj = CFDI33.ComplementoType(ns_="pago10:")
    complemento_obj.add_anytypeobjs_(pagos_obj)

    return complemento_obj


  def clean_cfdi(self, _):
   return {k:v for k,v in _.items() if v }


  def remove_empty_from_dict(self, d):
    if type(d) is dict:
      return dict((k, self.remove_empty_from_dict(v)) for k, v in d.items() if v and self.remove_empty_from_dict(v))
    elif type(d) is list:
      return [self.remove_empty_from_dict(v) for v in d if v and self.remove_empty_from_dict(v)]
    else:
      try:
        d = d.strip()
      except:
        pass
      return d


  def get_scaped_cfdi(self, xml_string, seal=''):
    try:
      from lxml import etree
      if seal:
        xml_etree = etree.fromstring(bytes(bytearray(xml_string, encoding='utf8')))
        xml_etree.set('Sello', seal)
      else:
        xml_etree = etree.fromstring(xml_string)
      xml_string = etree.tostring(xml_etree, encoding='utf8').decode('utf-8')#.replace('''<?xml version='1.0' encoding='utf8'?>\n''', '')
    except Exception as e:
      print(f'Exception on get_scaped_cfdi {e}')
    return xml_string


  def get_signed_invoice(self, xml_string):
    original_string = get_original_string(xml_string)
    assert original_string, 'OriginalString must have data'
    self.seal = self.signer(original_string)
    return self.get_scaped_cfdi(xml_string, self.seal)


  def signer(self, data, mechanism='sha256'):
    seal = ''
    try:
      rsa = load_key_string(self.private_certificate)
      assert len(rsa) in (1024, 2048)
      assert rsa.e == b'\000\000\000\003\001\000\001'
      md5_digest = hashlib.sha256(data).digest()
      rsa_signature = rsa.sign( md5_digest, mechanism)
      seal = b64encode(rsa_signature)
      seal = b"".join(seal.split())
      seal = seal.decode()
    except Exception as e:
      print('Exception on signer {e}')
      raise Exception(e)
    return seal

  def get_emission_date(self, zipcode):
    timezone_dict = {
      '5':     'America/Cancun',
      '7':     'America/Hermosillo',
      '5-6':   'America/Mexico_City',
      '6-7':   'America/Mazatlan',
      '7-8':   'America/Tijuana',
    }
    try:
      now = datetime.now()
      catalogos_obj = Catalogos(now)
      timezone_key, timezone_name = catalogos_obj.obtener('CodigoPostal', zipcode)
      new_emission_date = datetime.now(pytz.timezone(timezone_dict[timezone_key]))
      minutes = 0
      assert timezone_key is not None and timezone_key in timezone_dict, 'No se puede determinar la zona horaria'
      if timezone_key in ('5-6', '6-7', '7-8') and 'Frontera' in timezone_name:
        summer_dates = get_summer_dates(new_emission_date.year)
        if (now >= summer_dates['march'] and now <= summer_dates['april']) or (now >= summer_dates['october'] and now <= summer_dates['november']):
          if timezone_key in ('5-6', '6-7'):
            minutes = 60
      new_emission_date = new_emission_date + timedelta(minutes=minutes)
      new_emission_date = new_emission_date.replace(microsecond=0, tzinfo=None).isoformat('T')
    except Exception as e:
      print(f'Exeption on get_emission_date {e}')
      raise Exception(f'Ocurrio un error al intentar obtener la fecha {e}')
    return new_emission_date


  def get_currency_decimals(self, currency):
    decimals = self.decimales
    try:
      now = datetime.now()
      catalogos_obj = Catalogos(now)
      currency_obj = catalogos_obj.obtener('Moneda', currency)
      decimals = currency_obj.decimales
    except Exception as e:
      print(f'Exeption on get_currency_decimals {e}')
      raise Exception(f'Ocurrio un error al intentar obtener la cantidad de decimales de la moneda {e}')
    return decimals



