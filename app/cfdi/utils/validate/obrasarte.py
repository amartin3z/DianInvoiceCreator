from django.conf import settings
from app.sat.utils.validate import Catalogos


def validacion_obrasarte10(xml_etree):

  print('OBRASARTE') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  namespaces = {'namespaces': {'obrasarte': 'http://www.sat.gob.mx/arteantiguedades'}}
  complement_obrasarte = xml_etree.xpath('//obrasarte:obrasarteantiguedades', **namespaces)
  if complement_obrasarte:
    namespaces = {'namespaces': xml_etree.nsmap}
    try:
      catalogos_obj = Catalogos(xml_etree.get('Fecha'))

      tipobien = xml_etree.xpath('//obrasarte:obrasarteantiguedades/@TipoBien', **namespaces)
      for bien in tipobien:
        if not catalogos_obj.validar('TipoBien', bien):
          return False, 'OBR101'

      titulos = xml_etree.xpath('//obrasarte:obrasarteantiguedades/@TituloAdquirido', **namespaces)
      for titulo in titulos:
        if not catalogos_obj.validar('TituloAdquirido', titulo):
          return False, 'OBR102'

      caracteristicas = xml_etree.xpath('//obrasarte:obrasarteantiguedades/@CaracterísticasDeObraoPieza', **namespaces)
      for caracteristica in caracteristicas:
        if not catalogos_obj.validar('Caracteristica', caracteristica):
          return False, 'OBR103'

    except Exception as e:
      print(f"Exception validacion_obrasarte10 => {e}")
      return False, 'OBR999'

  return True, None