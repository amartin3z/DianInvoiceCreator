from django.conf import settings
from app.sat.utils.validate import Catalogos


def validacion_notariospublicos10(xml_etree):

  print('NOTARIOSPUBLICOS') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  namespaces = {'namespaces': {'notariospublicos': 'http://www.sat.gob.mx/notariospublicos'}}
  complement_notarios = xml_etree.xpath('//notariospublicos:NotariosPublicos', **namespaces)
  if complement_notarios:
    namespaces = {'namespaces': xml_etree.nsmap}
    try:
      catalogos_obj = Catalogos(xml_etree.get('Fecha'))

      tipoinmueble = xml_etree.xpath('//notariospublicos:NotariosPublicos/notariospublicos:DescInmuebles/notariospublicos:DescInmueble/@TipoInmueble', **namespaces)
      for inmueble in tipoinmueble:
        if not catalogos_obj.validar('TipoInmueble', inmueble):
          return False, 'NOT101'

      estados = xml_etree.xpath('//notariospublicos:NotariosPublicos/notariospublicos:DescInmuebles/notariospublicos:DescInmueble/@Estado', **namespaces)
      for estado in estados:
        if not catalogos_obj.validar('EntidadFederativa', estado):
          return False, 'NOT102'

      paises = xml_etree.xpath('//notariospublicos:NotariosPublicos/notariospublicos:DescInmuebles/notariospublicos:DescInmueble/@Pais', **namespaces)
      for pais in paises:
        if not catalogos_obj.validar('Pais', pais, complemento='notariospublicos'):
          return False, 'NOT103'

      entidades = xml_etree.xpath('//notariospublicos:NotariosPublicos/notariospublicos:DatosNotario/@EntidadFederativa', **namespaces)
      for entidad in entidades:
        if not catalogos_obj.validar('EntidadFederativa', entidad):
          return False, 'NOT104'
    except Exception as e:
      print(f"Exception validacion_notariospublicos10 => {e}")
      return False, 'NOT999'

  return True, None