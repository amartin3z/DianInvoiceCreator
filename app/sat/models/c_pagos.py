from django.db import models
from datetime import date


class TipoCadenaPago(models.Model):
  """
    Catálogo REP:
    @nombre_archivo: (catPagos.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catPagos.xls
    \copy sat_tipocadenapago(clave, descripcion) from '/tmp/catalogos/tipocadenapago.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=3, db_index=True)
  descripcion = models.CharField(max_length=255, blank=True, null=True)

  @staticmethod
  def obtener(clave, patente, ejercicio, fecha=date.today()):
    raise NotImplemented('TipoCadenaPago obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today()):
    raise NotImplemented('TipoCadenaPago validar is not implemented yet...')