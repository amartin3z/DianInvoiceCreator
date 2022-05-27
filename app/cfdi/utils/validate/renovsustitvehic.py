from django.conf import settings
from app.sat.utils.validate import Catalogos


def validacion_renovsustitvehic10(xml_etree):

  print('RENOVSUSTITVEHIC') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  namespaces = {'namespaces': {'decreto': 'http://www.sat.gob.mx/renovacionysustitucionvehiculos'}}
  complement_renovsustitutvehic = xml_etree.xpath('//decreto:renovacionysustitucionvehiculos', **namespaces)
  if complement_renovsustitutvehic:
    namespaces = {'namespaces': xml_etree.nsmap}
    try:
      catalogos_obj = Catalogos(xml_etree.get('Fecha'))

      tipodecreto = complement_renovsustitutvehic[0].get('TipoDeDecreto')
      if not catalogos_obj.validar('TipoDecreto', bien):
        return False, 'REN101'

      enajejados = complement_renovsustitutvehic[0].xpath('//decreto:DecretoRenovVehicular/@VehEnaj', **namespaces)
      for enajejado in enajejados:
        if not catalogos_obj.validar('VehiculoEnajenado', enajejado):
          return False, 'REN102'

      enajejados = complement_renovsustitutvehic[0].xpath('//decreto:DecretoSustitVehicular/@VehEnaj', **namespaces)
      for enajejado in enajejados:
        if not catalogos_obj.validar('VehiculoEnajenado', enajejado):
          return False, 'REN103'

      tipovehiculo_r = complement_renovsustitutvehic[0].xpath('//decreto:DecretoRenovVehicular/decreto:VehiculosUsadosEnajenadoPermAlFab/@TipoVeh', **namespaces)
      for tipov in tipovehiculo_r:
        if not catalogos_obj.validar('TipoVehiculoR', tipov):
          return False, 'REN104'

      tipovehiculo_s = complement_renovsustitutvehic[0].xpath('//decreto:DecretoSustitVehicular/decreto:VehiculoUsadoEnajenadoPermAlFab/@TipoVeh', **namespaces)
      for tipov in tipovehiculo_s:
        if not catalogos_obj.validar('TipoVehiculoS', tipov):
          return False, 'REN105'

    except Exception as e:
      print(f"Exception validacion_renovsustitvehic10 => {e}")
      return False, 'REN999'

  return True, None