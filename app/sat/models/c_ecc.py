from django.db import models
from django.db.models import Q
from datetime import datetime, date

DB_PREFIX = 'sat_ecc'


class TipoCombustible(models.Model):
  clave = models.CharField(max_length=3, db_index=True)
  descripcion = models.CharField(max_length=55, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipocombustible'


  @staticmethod
  def obtener(clave, fecha=date.today()):
    tipocombustible_obj = None
    try:
      tipocombustible_obj = TipoCombustible.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception TipoCombustible obtener => {clave} => {e}")
    return tipocombustible_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = TipoCombustible.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception TipoCombustible validar => {clave} => {e}")
    return es_valido