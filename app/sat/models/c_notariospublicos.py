from django.db import models
from django.db.models import Q
from django.conf import settings
from datetime import datetime, date


DB_PREFIX = 'sat_notariospublicos'


class TipoInmueble(models.Model):
  clave = models.CharField(max_length=2)
  descripcion = models.CharField(max_length=55, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f"{self.clave} - {self.descripcion}"

  class Meta:
    db_table = f'{DB_PREFIX}_tipoinmueble'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    tipoinmueble_obj = None
    try:
      tipoinmueble_obj = TipoInmueble.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception TipoInmueble obtener => {clave} => {e}")
    return tipoinmueble_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = TipoInmueble.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception TipoInmueble validar => {clave} => {e}")
    return es_valido



class EntidadFederativa(models.Model):
  clave = models.CharField(max_length=2)
  descripcion = models.CharField(max_length=55, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f"{self.clave} - {self.descripcion}"

  class Meta:
    db_table = f'{DB_PREFIX}_entidadfederativa'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    entidadfederativa_obj = None
    try:
      entidadfederativa_obj = EntidadFederativa.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception EntidadFederativa obtener => {clave} => {e}")
    return entidadfederativa_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = EntidadFederativa.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception EntidadFederativa validar => {clave} => {e}")
    return es_valido
