from django.db import models
from django.db.models import Q
from datetime import datetime, date

DB_PREFIX = 'sat_obrasarte'


class TipoBien(models.Model):
  clave = models.CharField(max_length=2, db_index=True)
  descripcion = models.CharField(max_length=50, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipobien'


  @staticmethod
  def obtener(clave, fecha=date.today()):
    tipobien_obj = None
    try:
      tipobien_obj = TipoBien.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception TipoBien obtener => {clave} => {e}")
    return tipobien_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = TipoBien.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception TipoBien validar => {clave} => {e}")
    return es_valido



class TituloAdquirido(models.Model):
  clave = models.CharField(max_length=2, db_index=True)
  descripcion = models.CharField(max_length=50, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tituloadquirido'


  @staticmethod
  def obtener(clave, fecha=date.today()):
    tituloadquirido_obj = None
    try:
      tituloadquirido_obj = TituloAdquirido.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception TituloAdquirido obtener => {clave} => {e}")
    return tituloadquirido_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = TituloAdquirido.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception TituloAdquirido validar => {clave} => {e}")
    return es_valido



class Caracteristica(models.Model):
  clave = models.CharField(max_length=2, db_index=True)
  descripcion = models.CharField(max_length=50, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_caracteristica'


  @staticmethod
  def obtener(clave, fecha=date.today()):
    caracteristica_obj = None
    try:
      caracteristica_obj = Caracteristica.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception Caracteristica obtener => {clave} => {e}")
    return caracteristica_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = Caracteristica.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception Caracteristica validar => {clave} => {e}")
    return es_valido