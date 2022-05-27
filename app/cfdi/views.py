from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.conf import settings

from .errors import errors
from .utils.controller import CFDIValidator
from .utils.controller import Cancelacion
from .utils.controller import Consultar
from app.core.models import Log

from spyne.application import Application
from spyne.model.complex import ComplexModel, Array
from spyne.decorator import rpc, srpc
from spyne.model.primitive import Unicode, Integer, String, Byte
from spyne.model.binary import ByteArray
from spyne.model.binary import File
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase

import base64
import time
import re

# Create your views here.


class resultado_timbrar(ComplexModel):
  Codigo = Unicode(encoding='utf8')
  Mensaje = Unicode(encoding='utf8')
  Fecha = String(encoding='utf8')
  UUID = String(encoding='utf8')
  RFCPac = String(encoding='utf8')
  Xml = Unicode(encoding='utf8')
  SelloSAT = Unicode(encoding='utf8')
  CodigoError = Unicode(encoding='utf8')
  MensajeError = Unicode(encoding='utf8')

class UUIDS(ComplexModel):
  uuids = Array(String.customize(min_occurs=1))

class Folio(ComplexModel):
  UUID = String(encoding='utf8')
  EstatusUUID = String(encoding='utf8')

class resultado_cancelar(ComplexModel):
  Codigo = Unicode()
  Mensaje = Unicode()
  Fecha = String(encoding='utf8')
  Folios = Array(Folio)
  Acuse = Unicode(encoding='utf8')
  CodigoError = Unicode(encoding='utf8')
  MensajeError = Unicode(encoding='utf8')

class resultado_consultar(ComplexModel):
  Codigo = Unicode()
  Mensaje = Unicode()
  CodigoEstatus = Unicode(encoding='utf8')
  Estado = Unicode(encoding='utf8')
  EstatusCancelacion =  Unicode(encoding='utf8')
  EsCancelable = Unicode(encoding='utf8')


def uuid_match(uuid_list):
  for uuid in uuid_list:
    r = re.search(r"^[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}$", uuid)
    if r is None:
      return True
  return False

class Servicios_CFDI(ServiceBase):
  @srpc(String(encoding='utf8'), String(encoding='utf8'), File, _returns=resultado_timbrar)
  def timbrarCFDI(usuario, contrasena, xml):
    try:
      time1 = time.time()
      resultado = resultado_timbrar()
      try:
        xml_string = ""
        xml_string = base64.b64decode("".join(xml.data))
        if False and settings.DEBUG:
          print(xml_string)
      except:
        resultado.Codigo, resultado.Mensaje  = "727", errors["727"]["message"]
      user_authenticate = bool(authenticate(username=usuario, password=contrasena))
      if user_authenticate:
        user = User.objects.get(username=usuario)
        cfdi_validator_obj = CFDIValidator(xml_string=xml_string, user=user, _type='W')
        if cfdi_validator_obj.is_valid:
          if cfdi_validator_obj.validar():
            TFD = cfdi_validator_obj.generar_tfd()
            if cfdi_validator_obj.is_valid:
              resultado.Codigo = "200"
              resultado.Mensaje = "Timbre Exitoso"
              resultado.Fecha = TFD.get("FechaTimbrado")
              resultado.RFCPac = TFD.get("RfcProvCertif")
              resultado.UUID = TFD.get("UUID")
              resultado.Xml = cfdi_validator_obj.xml_string_tfd.decode()
              resultado.SelloSAT = TFD.get("SelloSAT")
          else:
            if cfdi_validator_obj.error == 307:
              resultado = resultado_timbrar(**cfdi_validator_obj.stamped_response)
            else:
              resultado.Codigo, resultado.Mensaje  = str(cfdi_validator_obj.error), errors[str(cfdi_validator_obj.error)]["message"]
        else:
          resultado.Codigo, resultado.Mensaje  = str(cfdi_validator_obj.error), cfdi_validator_obj.message 
      else:
        resultado.Codigo, resultado.Mensaje  = "300", errors["300"]["message"]
    except Exception as e:
      print("Exception in timbrarCFDI => {}".format(str(e)))
      resultado.Codigo, resultado.Mensaje  = "735", errors["735"]["message"]
      Log.objects.log_action(None, 2, 'C', u'{}. {}'.format(resultado.Mensaje, resultado.Codigo), 'I', "Exception in timbrarCFDI => {}".format(str(e)), user=user)
    total_time = time.time() - time1
    try:
      print(u"Timbrado => %s => %s => %s => %s" % (usuario, resultado.Codigo, resultado.UUID, total_time))
    except:
      pass
    return resultado

  @srpc(String(encoding='utf8'), String(encoding='utf8'), UUIDS, _returns=resultado_cancelar)
  def cancelarCFDI(usuario, contrasena, UUIDS):
    try:
      time1 = time.time()
      resultado = resultado_cancelar()
      user_authenticate = bool(authenticate(username=usuario, password=contrasena))
      if user_authenticate:
        user = User.objects.get(username=usuario)
        if user.is_active:
          list_uuiud = [u.upper() for u in UUIDS.uuids]
          if len(list_uuiud) > 0:
            if not uuid_match(list_uuiud):
              cancelacion_obj = Cancelacion(UUIDS=list_uuiud, user=user, _type="W")
              if cancelacion_obj.is_valid:
                result = cancelacion_obj.sat_cacelacion()
                folios_list = []
                if result:
                  for f in cancelacion_obj.folios_list:
                    folio = Folio()
                    folio.UUID = f['UUID']
                    folio.EstatusUUID = f['EstatusUUID'] if 'EstatusUUID' in f else ''
                    folios_list.append(folio)
                  resultado.Fecha = cancelacion_obj.cancela_cfd_dict["Fecha"]
                  resultado.Folios = cancelacion_obj.folios_list
                  resultado.Acuse = cancelacion_obj.cancela_response.decode()
                else:
                  resultado.CodigoError = cancelacion_obj.faultcode
                  resultado.MensajeError = cancelacion_obj.faultstring
              else:
                resultado.Codigo, resultado.Mensaje  = cancelacion_obj.error, errors[cancelacion_obj.error]["message"]
            else:
              resultado.Codigo, resultado.Mensaje  = "207", errors["207"]["message"]
          else:
            resultado.Codigo, resultado.Mensaje  = "206", errors["206"]["message"]
        else:
          resultado.Codigo, resultado.Mensaje  = "703", errors["703"]["message"]
      else:
        resultado.Codigo, resultado.Mensaje  = "300", errors["300"]["message"]
    except Exception as e:
      print("Exception in cancelarCFDI => {}".format(str(e)))
      resultado.Codigo, resultado.Mensaje  = "735", errors["735"]["message"]
      Log.objects.log_action(request, 2, 'D', u'Ocurrio una excepcion al enviar la peticion de cancelacion, {}'.format(resultado.Codigo), 'I', "Exception in cancelarCFDI => {}".format(str(e)))
    total_time = time.time() - time1
    try:
      print(u"Cancelacion => %s => %s" % (usuario, total_time))
    except:
      pass
    return resultado

  @srpc(String(encoding='utf8'), String(encoding='utf8'), String(encoding='utf8'), _returns=resultado_consultar)
  def consultarCFDI(usuario, contrasena, uuid):
    try:
      time1 = time.time()
      resultado = resultado_consultar()
      user_authenticate = bool(authenticate(username=usuario, password=contrasena))
      if user_authenticate:
        user = User.objects.get(username=usuario)
        if user.is_active:
          uuid = uuid.upper()
          if not uuid_match([uuid]):
            consulta_obj = Consultar(uuid=uuid, user=user)
            if consulta_obj.is_valid:
              result = consulta_obj.sat_consulta()
              if result['success']:
                resultado.CodigoEstatus =  result['codigo_estatus']
                resultado.Estado = result['estado']
                resultado.EstatusCancelacion = result['estatus_cancelacion']
                resultado.EsCancelable = result['es_cancelable']
            else:
              resultado.Codigo, resultado.Mensaje  = consulta_obj.error, errors[consulta_obj.error]["message"]
          else:
            resultado.Codigo, resultado.Mensaje  = "207", errors["207"]["message"]
        else:
          resultado.Codigo, resultado.Mensaje  = "703", errors["703"]["message"]
      else:
        resultado.Codigo, resultado.Mensaje  = "300", errors["300"]["message"]
    except Exception as e:
      print("Exception in consultarCFDI => {}".format(str(e)))
      resultado.Codigo, resultado.Mensaje  = "735", errors["735"]["message"]
    total_time = time.time() - time1
    try:
      print(u"Consulta => %s => %s" % (usuario, total_time))
    except:
      pass
    return resultado


soap_app = Application(
  [Servicios_CFDI],
  tns='http://facturacion.ublinvoice.com/CFDI',
  in_protocol=Soap11(),
  out_protocol=Soap11(),
)
soap_application = csrf_exempt(DjangoApplication(soap_app))