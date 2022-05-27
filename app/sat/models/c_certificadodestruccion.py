from django.db import models
from django.db.models import Q
from datetime import datetime, date

DB_PREFIX = 'sat_certificadodestruccion'


class TipoSerie(models.Model):
  clave = models.CharField(max_length=7, db_index=True)
  descripcion = models.CharField(max_length=200, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tiposerie'


  @staticmethod
  def obtener(clave, fecha=date.today()):
    tiposerie_obj = None
    try:
      tiposerie_obj = TipoSerie.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception TipoSerie obtener => {clave} => {e}")
    return tiposerie_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = TipoSerie.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception TipoSerie validar => {clave} => {e}")
    return es_valido