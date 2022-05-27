from django.conf import settings

from app.sat.utils.validate import Catalogos
from .adicionales import trunc, normal_round, sat_round
from decimal import Decimal


def validacion_ine11(xml_etree):

  print('INE11') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  namespace_dicc = {'cfdi': 'http://www.sat.gob.mx/cfd/3', 'ine': 'http://www.sat.gob.mx/ine'}  
  complement_ine = xml_etree.xpath('//ine:INE', namespaces=namespace_dicc)
  if complement_ine:
    namespace_dicc = xml_etree.nsmap
    try:
      ine = complement_ine[0]
      tipo_proceso = ine.get('TipoProceso')
      tipo_comite = ine.get('TipoComite')
      id_contabiliad = ine.get('IdContabilidad')

      entidades = ine.xpath('//ine:Entidad', namespaces=namespace_dicc)
      entidades_ambito = ine.xpath('//ine:Entidad/@Ambito', namespaces=namespace_dicc)
      clave_entidad = ine.xpath('//ine:Entidad/@ClaveEntidad', namespaces=namespace_dicc)
    
      if tipo_proceso == 'Ordinario' and not tipo_comite:
          return False, 'INE180'
        
      elif tipo_proceso in ('Precampaña', 'Campaña'):
        if not entidades or len(entidades) != len(entidades_ambito):
          return False, 'INE181'
          
        if tipo_comite:
          return False, 'INE182'
                
        if id_contabiliad:
          return False, 'INE183'

      if tipo_comite == 'Ejecutivo Nacional':
        if entidades:
          return False, 'INE184'
        
      elif tipo_comite == 'Ejecutivo Estatal':
        if id_contabiliad:
          return False, 'INE185'

      if tipo_comite and tipo_comite != 'Ejecutivo Nacional':
        if not entidades or entidades_ambito:
          return False, 'INE186'

      if tipo_comite != 'Ejecutivo Nacional':      
        duplicates = {}
        if len(clave_entidad) == len(entidades_ambito):
          for idx, clave in enumerate(clave_entidad):
            if clave in duplicates:
              duplicates[clave].append(entidades_ambito[idx])
            else:
              duplicates[clave] = [entidades_ambito[idx]]
          for ambitos in duplicates.values():
            seen = []
            for ambito in ambitos:
              if ambito in seen:
                return False, 'INE187'
              else:
                seen.append(ambito)

      if entidades:
        for entidad in entidades:
          ambito = entidad.get('Ambito')
          if ambito == 'Local' and entidad.get('ClaveEntidad') in ('NAC', 'CR1', 'CR2', 'CR3', 'CR4', 'CR5'):
            return False, 'INE188'            
    except Exception as e:
      print(f"Exception ine validacion_ine11 => {e}")
      return False, 'INE999'

  return True, None