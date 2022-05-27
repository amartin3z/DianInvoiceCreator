from django.db import models
from django.db.models import Q
from django.conf import settings
from datetime import datetime, date


DB_PREFIX = 'sat_ine'

class Entidad(models.Model):
  clave = models.CharField(max_length=3, unique=True)
  pais = models.CharField(max_length=3)
  descripcion = models.CharField(max_length=55, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f"{self.clave} - {self.descripcion}"

  class Meta:
    db_table = f'{DB_PREFIX}_entidad'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    entidad_obj = None
    try:
      entidad_obj = Entidad.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception c_ine Entidad obtener => {clave} => {e}")
    return entidad_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = Entidad.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception c_ine Entidad validar => {clave} => {e}")
    return es_valido
