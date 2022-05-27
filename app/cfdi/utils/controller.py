# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils import timezone
from django.core.files.base import ContentFile

from .sign import Signer
from app.cfdi.models import Invoice, Cancel
from app.cfdi.utils.validate.base import *
from app.cfdi.utils.validate.adicionales import validacion_adicionales
from app.cfdi.utils.validate.pagos import validacion_pagos10
from app.cfdi.utils.validate.nomina import validacion_nomina12
from app.cfdi.utils.validate.cce import validacion_cce11
from app.cfdi.utils.validate.certificadodestruccion import validacion_certificadodestruccion10
from app.cfdi.utils.validate.ecc import validacion_ecc12
from app.cfdi.utils.validate.gech import validacion_gech10
from app.cfdi.utils.validate.ine import validacion_ine11
from app.cfdi.utils.validate.notariospublicos import validacion_notariospublicos10
from app.cfdi.utils.validate.obrasarte import validacion_obrasarte10
from app.cfdi.utils.validate.renovsustitvehic import validacion_renovsustitvehic10
from app.cfdi.utils.validate.ieeh import validacion_ieeh10
from app.cfdi.utils.validate.terceros import validacion_terceros11
from app.cfdi.utils.validate.consumocombustibles import validacion_consumodecombustibles11

from app.sat.utils.connector import SATConnector
from app.sat.tasks import enviar_sat, cancelar_sat, consultar_sat

import re
import M2Crypto
from lxml import etree



ALLOWED_NAMESPACES = {
  'http://www.sat.gob.mx/cfd/3': 'cfdi',
  'http://www.sat.gob.mx/Pagos': 'pago10',
  'http://www.sat.gob.mx/TimbreFiscalDigital': 'tfd',
}

NAMESPACE_DICT = {
  'cfdi': 'http://www.sat.gob.mx/cfd/3',
  'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital',
  'pago10': 'http://www.sat.gob.mx/Pagos',
}

class CFDIValidator(object):


  def __init__(self, xml_string, user, _type='F'):

    self.xml_string = xml_string
    self.user = user
    self._type = _type
    self.is_valid = False
    self.error = None
    self.message = None
    self.confirmation = None
    self.tfd_dict = {}
    self.complement_lst = []
    self.uuid = None

    try:
      xml_etree = etree.fromstring(xml_string, parser=settings.XMLPARSER)
      self.xml_etree = xml_etree
    except Exception as e:
      print(f"Exception CFDIValidator __init__ => {e}")
      self.error = 101
      self.message = 'Estructura inválida'
      return

    for namespace in self.xml_etree.xpath('//namespace::*' ):
      if namespace[1] in ALLOWED_NAMESPACES and ALLOWED_NAMESPACES[namespace[1]] != namespace[0]:
        self.error = 102
        self.message = 'Prefijo y Namespace inválidos {}:{}'.format(namespace[1], namespace[0])
        return

    self.version = self.xml_etree.get('Version')
    if self.version != '3.3':
      self.error = 103
      self.mesage = 'Versión de CFDI inválida {version}'
      return

    self.fecha = self.xml_etree.get('Fecha')
    self.codigopostal = self.xml_etree.get('LugarExpedicion')
    self.no_certificado = self.xml_etree.get('NoCertificado')
    sello = self.xml_etree.get('Sello')
    sello = re.sub('\s+', '', sello)
    self.sello = sello.strip()
    if not re.match('^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$', self.sello):
      self.error = 102
      self.message = 'El atributo Sello no cumple con el patrón de Base64'
      return

    self.certificado = self.xml_etree.get('Certificado')
    if not re.match('^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$', self.certificado):
      self.error = 103
      self.message = 'El atributo Certificado no cumple con el patrón de Base64'
      return
    try:
      split_string_cert = [self.certificado[i:i+64] for i in range(0, len(self.certificado), 64)]
      split_string_cert = "".join([x + "\n"for x in split_string_cert])
      self.certificado = "-----BEGIN CERTIFICATE-----\n" + split_string_cert + "-----END CERTIFICATE-----"
      self.x509_cert = M2Crypto.X509.load_cert_string(self.certificado, M2Crypto.X509.FORMAT_PEM)      
    except Exception as e:
      print(f"Exception CFDIValidator __init__ x509_cert => {e}")
      self.error = 104
      self.message = 'El atributo Certificado no pudo ser interpretado'
      return
    self.serial = hex(self.x509_cert.get_serial_number())[3::2]
    if self.no_certificado != self.serial:
      self.error = 105
      self.message = 'El atributo NoCertificado no coincide con el número de Serie del Certificado {no_certificado} {serial}'
      return

    tfd = self.xml_etree.xpath('//cfdi:Complemento/tfd:TimbreFiscalDigital', namespaces=NAMESPACE_DICT)
    if tfd:
      self.error = 106
      self.message = "El CFDI ya contiene el Complemento TimbreFiscalDigital"
      return

    self.rfc_em = self.xml_etree.xpath('//cfdi:Emisor', namespaces=NAMESPACE_DICT)[0].get('Rfc')
    self.rfc_re = self.xml_etree.xpath('//cfdi:Receptor', namespaces=NAMESPACE_DICT)[0].get('Rfc')
    self.total = self.xml_etree.get('Total')

    for complement in self.xml_etree.xpath('//cfdi:Complemento', namespaces=NAMESPACE_DICT):
      self.complement_lst.append(complement.tag)      

    self.is_valid = True


  def validar(self):
    self.is_valid = False
    if self.validar_usuario():
      if self.validar_timbreexistente():
        if self.validar_estructura():
          if self.validar_fecha():
            if self.validar_csd_expiracion():
              if self.validar_satcsd():
                if self.validar_fiel():
                  if self.validar_subjectdn():
                    if self.validar_lco():
                      if self.validar_lcocsd():
                        if self.validar_sello():
                          if self.validar_emission():
                            success, error = self.validar_adicionales()
                            if success:
                              success, error = self.validar_complementos()
                              if success:
                                self.is_valid = True
                              else:
                                self.error =  error
                            else:
                              self.error = error
                          else:
                            self.error = 401
                        else:
                          self.error = 302
                      else:
                        self.error = 304
                    else:
                      self.error = 402
                  else:
                    self.error = 303
                else:
                  self.error = 306
              else:
                self.error = 308
            else:
              self.error = 305
          else:
            self.error = 403
        else:
          self.error = 301
      else:
        self.error = 307
    else:
      self.error = self.error

    return self.is_valid


  def validar_usuario(self):
    result, error = False, 703
    try:
      result, self.error = validacion_usuario(self.user, self.rfc_em)
    except Exception as e:
      print(f"Exception CFDIValidator validar_usuario => {e}")
    return result

  def validar_timbreexistente(self):    
    result = False
    try:
      result, self.stamped_response = validacion_timbreexistente(self.sello)
    except Exception as e:
      print(f"Exception CFDIValidator validar_timbreexistente => {e}")
    return result

  def validar_estructura(self):
    result = False
    try:
      result = validacion_estructura(self.xml_string)
    except Exception as e:
      print(f"Exception CFDIValidator validar_estructura => {e}")
    return result

  def validar_fecha(self):
    result = False    
    try:
      result = validacion_fecha_403(self.fecha)
    except Exception as e:
      print(f"Exception CFDIValidator validar_fecha => {e}")
    return result

  def validar_csd_expiracion(self):
    result = False
    try:
      result = validacion_csd_expiracion(self.x509_cert, self.fecha, self.codigopostal)
    except Exception as e:
      print(f"Exception CFDIValidator validar_csd_expiracion => {e}")
    return result

  def validar_satcsd(self):
    result = False    
    try:
      result = validacion_satcsd(self.x509_cert)
    except Exception as e:
      print(f"Exception CFDIValidator validacion_satcsd => {e}")
    return result

  def validar_fiel(self):
    result = False
    try:
      result = validacion_fiel(self.x509_cert)
    except Exception as e:
      print(f"Exception CFDIValidator validar_fiel => {e}")
    return result

  def validar_subjectdn(self):
    result = False
    try:
      result = validacion_subjectdn(self.rfc_em, self.x509_cert)
    except Exception as e:
      print(f"Exception CFDIValidator validar_subjectdn => {e}")
    return result

  def validar_lco(self):
    result = False
    try:
      result = validacion_lco(self.x509_cert, self.rfc_em)
    except Exception as e:
      print(f"Exception CFDIValidator validacion_lco => {e}")
    return result

  def validar_lcocsd(self):
    result = False
    try:
      result = validacion_lcocsd(self.x509_cert, self.rfc_em)
    except Exception as e:
      print(f"Exception CFDIValidator validacion_lcocsd => {e}")
    return result

  def validar_sello(self):
    result = False
    try:
      result = validacion_sello(self.sello, self.x509_cert, self.xml_string)
    except Exception as e:
      print(f"Exception CFDIValidator validar_sello => {e}")
    return result

  def validar_emission(self):
    result = False
    try:
      result = validacion_fecha(self.fecha, self.codigopostal)
    except Exception as e:
      print(f"Exception CFDIValidator validar_emission => {e}")      
    return result

  def validar_adicionales(self):
    success = False
    error = None
    try:
      success, error = validacion_adicionales(self.xml_etree, self.xml_string)
    except Exception as e:
      print(f"Exception CFDIValidator validar_adicionales => {e}")      
    return success, error

  def validar_complementos(self):
    success = False
    error = None

    try:
      success, error = validacion_cce11(self.xml_etree)
      if success:
        success, error = validacion_certificadodestruccion10(self.xml_etree)
      if success:
        success, error = validacion_ecc12(self.xml_etree)
      if success:
        success, error = validacion_gech10(self.xml_etree)
      if success:
        success, error = validacion_ine11(self.xml_etree)
      if success:
        success, error = validacion_nomina12(self.xml_etree)
      if success:
        success, error = validacion_notariospublicos10(self.xml_etree)
      if success:
        success, error = validacion_obrasarte10(self.xml_etree)
      if success:
        success, error = validacion_pagos10(self.xml_etree)
      if success:
        success, error = validacion_renovsustitvehic10(self.xml_etree)
      if success:
        success, error = validacion_ieeh10(self.xml_etree)
      if success:
        success, error = validacion_terceros11(self.xml_etree)
      if success:
        success, error = validacion_consumodecombustibles11(self.xml_etree)    

    except Exception as e:
      error = 301
      success = False
      print(f"Exception controller validar_complementos => {e}")

    return success, error


  def generar_tfd(self):
    tfd = None
    if self.is_valid:
      self.is_valid = False
      uuid = generate_uuid(self.sello)
      self.uuid = uuid
      self.fecha_timbrado = timezone.now()
      fecha_timbrado_str = self.fecha_timbrado.strftime('%Y-%m-%dT%H:%M:%S')[:19]

      version = '1.1'
      no_certificado_sat = settings.SAT_NO_CERTIFICADO
      rfcprovcertif = settings.SAT_RFCPROVCERTIF
      tfd_dict = {
        'Version': version,
        'SelloCFD': self.sello,
        'NoCertificadoSAT': no_certificado_sat,
        'RfcProvCertif': rfcprovcertif,
        'UUID': uuid, 
        'FechaTimbrado': fecha_timbrado_str,
      }
      leyenda_str = ''
      if settings.SAT_LEYENDA:        
        tfd_dict['Leyenda'] = settings.SAT_LEYENDA_STR
        leyenda_str = '|{}'.format(settings.SAT_LEYENDA_STR)

      tfd_str = '||%s|%s|%s|%s%s|%s|%s||' % (version, uuid, fecha_timbrado_str, rfcprovcertif, leyenda_str, self.sello, no_certificado_sat)
      try:
        signer_obj = Signer()
        sello_sat = signer_obj.sign(data=tfd_str, mechanism='sha256')
        if sello_sat["success"]:
          tfd_dict['SelloSAT'] = sello_sat["message"]

          tfd = etree.Element(etree.QName('{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital'),
            attrib = {'{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': 'http://www.sat.gob.mx/TimbreFiscalDigital http://www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd'},
            nsmap = {'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'}
          )
          tfd.set('Version', version)
          tfd.set('UUID', uuid)
          tfd.set('FechaTimbrado', fecha_timbrado_str)
          tfd.set('RfcProvCertif', rfcprovcertif)
          tfd.set('SelloCFD', self.sello)
          tfd.set('NoCertificadoSAT', no_certificado_sat)
          tfd.set('SelloSAT', sello_sat["message"])
          if settings.SAT_LEYENDA:
            tfd.set('Leyenda', settings.SAT_LEYENDA_STR)

          complemento = self.xml_etree.find("cfdi:Complemento", namespaces=NAMESPACE_DICT)
          if complemento is None:
            new_complemento = etree.Element('{http://www.sat.gob.mx/cfd/3}Complemento')
            new_complemento.append(tfd)
            self.xml_etree.append(new_complemento)
          else:
            complemento.append(tfd)

          self.tfd_dict = tfd_dict
          self.xml_string_tfd = etree.tostring(self.xml_etree, encoding='utf8', xml_declaration=True)
          #self.xml_string_tfd = etree.tostring(self.xml_etree, encoding='utf8')
          self.is_valid = True
          
          if not self.guardar_cfdi():
            tfd = None
            self.is_valid = False

        else:
          raise Exception('No se pudo crear SelloSAT')
      except Exception as e:
        print(f"Exception CFDIValidator generar_tfd => {e}")
        self.error = 709
        self.mesage = 'Error al generar SelloSAT'

    return tfd


  def guardar_cfdi(self):
    result = None
    if self.is_valid and self.tfd_dict:
      cfdi = Invoice(
        version=settings.CFDI_VERSION,
        uuid=self.uuid,
        date=self.fecha_timbrado,
        status='S',
        type=self._type,
        taxpayer_id=self.rfc_em,
        rtaxpayer_id=self.rfc_re,
        total=self.total, 
        complement=", ".join(self.complement_lst)
      )
      cfdi.xml = ContentFile(self.xml_string_tfd, '{0}.xml'.format(self.uuid))
      cfdi.save()      
      if settings.APPLY_ASYNC:
        enviar_sat.apply_async(args=(self.uuid),)
      else:
        enviar_sat(self.uuid)
      result = True

    return result



class Cancelacion(object):
  def __init__(self, UUIDS, user, _type='F'):
    self.user = user
    self.uuids = UUIDS
    self.type = _type
    self.is_valid = False
    self.error = ""
    self.mensaje = ""
    self.sat_obj = SATConnector()
    self.account = user.business_set.last()
    self.taxpayer_id = self.account.taxpayer_id
    for uuid in UUIDS:
      if not Invoice.objects.filter(uuid=uuid).exists():
        self.error = "205"
        return
      if not Invoice.objects.filter(uuid=uuid, taxpayer_id=self.taxpayer_id).exists():
        self.error = "203"
        return
    self.is_valid = True

  def sat_cacelacion(self):
    try:
      from app.invoicing.models import Invoice as InvoicingInvoice 
      self.is_valid = False
      result, self.cod_estatus = None, ""
      self.cancela_cfd_dict, self.folios_list, self.cancela_response = "", "", ""
      self.faultcode, self.faultstring  = None, None
      taxpayer_id = self.account.taxpayer_id
      sat_files = self.account.get_csd()
      cer, key = sat_files['cer'], sat_files['key']
      self.cancela_cfd_dict, self.folios_list, self.cancela_response, self.faultcode, self.faultstring  = cancelar_sat(self.uuids, self.taxpayer_id, cer, key)
      self.is_valid = True
      if 'RfcEmisor' in self.cancela_cfd_dict and "Fecha" in self.cancela_cfd_dict:
        if 'CodEstatus' in self.cancela_cfd_dict:
          self.cod_estatus = self.cancela_cfd_dict['CodEstatus']
        for folio in self.folios_list:
          self.folio = folio
          cancelacion = Cancel(
            uuid = self.folio["UUID"],
            date = self.cancela_cfd_dict["Fecha"],
            taxpayer_id = self.taxpayer_id,
            uuid_status = self.folio["EstatusUUID"],
            cod_status = self.cod_estatus,
            type = self.type,)
          cancelacion.save()
          if self.folio['EstatusUUID'] in ('201', '202'):
            try:
              cfdi = InvoicingInvoice.objects.get(uuid=self.folio["UUID"])
              cfdi.status = "C"
              cfdi.status_sat = "C"
              cfdi.save()
            except:
              pass
        self.is_valid = True
    except Exception as e:
      print("Exception in sat_cacelacion => {}".format(str(e)))
    return self.is_valid

class Consultar(object):
  def __init__(self, uuid, user,):
    from app.invoicing.models import Invoice as FInvoice 
    self.user = user
    self.uuid = uuid
    self.is_valid = False
    self.error = ""
    self.mensaje = ""
    self.account = user.business_set.last()
    self.taxpayer_id = self.account.taxpayer_id
    if not Invoice.objects.filter(uuid=uuid).exists() and not FInvoice.objects.filter(uuid=uuid).exists():
      self.error = "205"
      return
    if not Invoice.objects.filter(uuid=uuid, taxpayer_id=self.taxpayer_id).exists() and not FInvoice.objects.filter(uuid=uuid, taxpayer_id=self.taxpayer_id).exists():
      self.error = "203"
      return
    self.is_valid = True

  def sat_consulta(self):
    result = {'success': True}
    try:
      from app.invoicing.models import Invoice as FInvoice 
      invoice = Invoice.objects.filter(uuid=self.uuid)
      free_invoice = FInvoice.objects.filter(uuid=self.uuid)
      cfdi = invoice[0] if invoice.exists() else free_invoice[0]
      result = consultar_sat(cfdi.taxpayer_id, cfdi.rtaxpayer_id, cfdi.total, id=self.uuid)
    except Exception as e:
      print("Exception in sat_consulta => {}".format(str(e)))
    return result