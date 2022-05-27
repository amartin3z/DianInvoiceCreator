from django.conf import settings
from app.sat.utils.validate import Catalogos


def validacion_certificadodestruccion10(xml_etree):

  print('CERTIFICADODEDESTRUCCION') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  
  namespaces = {'namespaces': {'destruccion': 'http://www.sat.gob.mx/certificadodestruccion'}}

  complement_destruccion = xml_etree.xpath('//destruccion:certificadodedestruccion', **namespaces)
  if complement_destruccion:
    namespaces = {'namespaces': xml_etree.nsmap}
    try:
      catalogos_obj = Catalogos(xml_etree.get('Fecha'))
      serie = complement_destruccion[0].get('Serie')
      if not catalogos_obj.validar('TipoSerie', serie):
        return False, 'DES101'
    except Exception as e:
      print(f"Exception validacion_certificadodestruccion10 => {e}")
      return False, 'DES999'

  return True, None