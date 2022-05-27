from django.conf import settings
from app.sat.utils.validate import Catalogos
from app.sat.models import LCO
from .adicionales import trunc, normal_round, sat_round
from decimal import Decimal
from datetime import datetime
from dateutil.relativedelta import relativedelta


def validacion_gech10(xml_etree):

  print('GASTOSHIDROCARBUROS10') if settings.VERBOSE_EXTRA_VALIDATIONS else None
  
  namespaces = {'namespaces': {'gceh': 'http://www.sat.gob.mx/GastosHidrocarburos10'}}
  complemento_gceh = xml_etree.findall('.//gceh:GastosHidrocarburos', **namespaces)
  if complemento_gceh:      
    namespaces = {'namespaces': xml_etree.nsmap}
    try:
      catalogos_obj = Catalogos(xml_etree.get('Fecha'))
      if len(complemento_gceh) == 1:
        cfdi_version_comprobante = xml_etree.get('Version')
        if cfdi_version_comprobante != '3.3':
          return False, 'GCEH101'

        tipo_comprobante = xml_etree.get('TipoDeComprobante')
        if tipo_comprobante != 'E':
          return False, 'GCEH102'
        
        nodo_erogacion = complemento_gceh[0].xpath('.//gceh:Erogacion', **namespaces)
        
        for erogacion in nodo_erogacion:
          documento_relacionado = erogacion.xpath('.//gceh:DocumentoRelacionado', **namespaces)
          
          for docto_rel in documento_relacionado:
            if docto_rel.xpath('boolean(@FolioFiscalVinculado and @OrigenErogacion="Extranjero")', **namespaces):
              return False, 'GCEH103'
            if docto_rel.xpath('boolean(@RFCProveedor and not(@FolioFiscalVinculado))', **namespaces):
              return False, 'GCEH104'
            if docto_rel.xpath('boolean(@FolioFiscalVinculado and not(@RFCProveedor))', **namespaces):
              return False, 'GCEH105'
            if docto_rel.xpath('boolean(@MontoTotalIVA and not(@FolioFiscalVinculado))', **namespaces):
              return False, 'GCEH106'
            if docto_rel.xpath('boolean(@FolioFiscalVinculado and not(@MontoTotalIVA))', **namespaces):
              return False, 'GCEH107'
            if docto_rel.xpath('boolean(@NumeroPedimentoVinculado and @OrigenErogacion="Nacional")', **namespaces):
              return False, 'GCEH108'
            if docto_rel.xpath('boolean(@ClavePedimentoVinculado and not(@NumeroPedimentoVinculado))', **namespaces):
              return False, 'GCEH109'
            if docto_rel.xpath('boolean(@NumeroPedimentoVinculado and not(@ClavePedimentoVinculado))', **namespaces):
              return False, 'GCEH110'
            if docto_rel.xpath('boolean(@ClavePagoPedimentoVinculado and not(@NumeroPedimentoVinculado))', **namespaces):
              return False, 'GCEH111'
            if docto_rel.xpath('boolean(@NumeroPedimentoVinculado and not(@ClavePagoPedimentoVinculado))', **namespaces):
              return False, 'GCEH112'
            if docto_rel.xpath('boolean(@MontoIVAPedimento and not(@NumeroPedimentoVinculado))', **namespaces):
              return False, 'GCEH113'
            if docto_rel.xpath('boolean(@NumeroPedimentoVinculado and not(@MontoIVAPedimento))', **namespaces):
              return False, 'GCEH114'
            if docto_rel.xpath('boolean(@FolioFiscalVinculado and not(@FechaFolioFiscalVinculado))', **namespaces):
              return False, 'GCEH132'
            
            if docto_rel.xpath('boolean(@NumeroPedimentoVinculado)', **namespaces):

              npv = docto_rel.xpath('string(@NumeroPedimentoVinculado)', **namespaces)

              if not re.match("[0-9]{2}  [0-9]{2}  [0-9]{4}  [0-9]{7}", npv):
                return False, 'GCEH133'
              
              today = datetime.now()
              max_years_allow = int(str(today.year)[2:4])
              min_years_allow = int(str((today - relativedelta(years=10)).year)[2:4])
              
              npv_year = int(npv[:2])
              npv_customs = npv[4:6]
              npv_patent = npv[8:12]
              npv_quantity = int(npv[14:][1:])
                            
              quantity_lst = catalogos_obj.obtener('NumeroPedimentoAduana', npv_customs, patente=npv_patent, ano='20%s'.format(npv_year))
              if quantity_lst is not None:
                quantity = int(quantity_lst['cantidad'])

              if (npv_year < min_years_allow or npv_year > max_years_allow) or not (catalogos_obj.validar('Aduana', npv_customs) or catalogos_obj.validar('PatenteAduanal', npv_patent)) or not (npv_quantity > 0 and npv_quantity <= quantity):
                return False, 'GCEH133'

            mes = docto_rel.xpath('string(@Mes)', **namespaces)
            if not catalogos_obj.validar('Mes', mes):
              return False, 'GCEH998'
            
            fecha_folio_fiscal_vinculado = docto_rel.xpath('string(@FechaFolioFiscalVinculado)', **namespaces)
            if fecha_folio_fiscal_vinculado:
              try:
                fecha_folio_fiscal_vinculado = datetime.datetime.strptime(fecha_folio_fiscal_vinculado, '%Y-%m-%d')
                allowed_ffv = fecha_folio_fiscal_vinculado - relativedelta(months=1)
                if int(mes) not in (fecha_folio_fiscal_vinculado.month, allowed_ffv.month):
                  return False, 'GCEH115'
              except:
                return False, 'GCEH115'
          
          porcentaje = erogacion.xpath('string(@Porcentaje)', **namespaces)
          if porcentaje and not float(porcentaje) > 0:
            return False, 'GCEH116'
          
          actividades = erogacion.xpath('.//gceh:Actividades', **namespaces)
          for actividad in actividades:
            act_rel = actividad.xpath('string(@ActividadRelacionada)', **namespaces)
            if not catalogos_obj.validar('Actividad', act_rel):
              return False, 'GCEH123'
            
            for sub_actividad in actividad.xpath('.//gceh:SubActividades', **namespaces):
              sub_act_rel = sub_actividad.xpath('string(@SubActividadRelacionada)', **namespaces)
              if not catalogos_obj.validar('SubActividad', sub_act_rel, actividad=act_rel):
                return False, 'GCEH124'
              
              for tarea in sub_actividad.xpath('.//gceh:Tareas', **namespaces):
                tarea_rel_bool = tarea.xpath('boolean(@TareaRelacionada)', **namespaces)
                tarea_rel = tarea.xpath('string(@TareaRelacionada)', **namespaces)
                if tarea_rel_bool and not catalogos_obj.validar('Tarea', tarea_rel, actividad=act_rel, subactividad=sub_act_rel):
                  return False, 'GCEH125'

                if not act_rel and (sub_act_rel or tarea_rel):
                  return False, 'GCEH117'
                if act_rel and not (sub_act_rel or tarea_rel):
                  return False, 'GCEH118'
                if not sub_act_rel and (act_rel or tarea_rel):
                  return False, 'GCEH119'
                if sub_act_rel and not (act_rel or tarea_rel):
                  return False, 'GCEH120'
                if not tarea_rel and (act_rel or sub_act_rel):
                  return False, 'GCEH121'
                if tarea_rel and not (act_rel or sub_act_rel):
                  return False, 'GCEH122'
            
          centro_costos = erogacion.xpath('.//gceh:CentroCostos', **namespaces)
          for c_costos in centro_costos:
            campo = c_costos.xpath('boolean(@Campo)', **namespaces)
            
            for yacimiento in c_costos.xpath('.//gceh:Yacimientos', **namespaces):
              yacimiento_bool = yacimiento.xpath('boolean(@Yacimiento)', **namespaces)
              
              for pozo in yacimiento.xpath('.//gceh:Pozos', **namespaces):
                pozo = pozo.xpath('boolean(@Pozo)', **namespaces)

                if not campo and (yacimiento_bool or pozo):
                  return False, 'GCEH126'
                if campo and not(yacimiento_bool or pozo):
                  return False, 'GCEH127'
                if not yacimiento_bool and (campo or pozo):
                  return False, 'GCEH128'
                if yacimiento_bool and not(campo or pozo):
                  return False, 'GCEH129'
                if not pozo and (yacimiento_bool or campo):
                  return False, 'GCEH130'
                if pozo and not(yacimiento_bool or campo):
                  return False, 'GCEH131'
        if complemento_gceh[0].getparent().tag != '{http://www.sat.gob.mx/cfd/3}Complemento':
          return False, 'GCEH997'
      
      elif len(complemento_gceh) > 1:
        return False, 'GCEH998'

    except Exception as e:
      print(f"Exception gech validacion_gech10 => {e}")
      return False, 'GCEH999'    

  return True, None