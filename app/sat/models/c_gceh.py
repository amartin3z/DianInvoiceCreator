from django.db import models
from django.db.models import Q
from django.conf import settings
from datetime import datetime, date


DB_PREFIX = 'sat_gceh'


class Actividad(models.Model):
  clave = models.CharField(max_length=2)
  descripcion = models.CharField(max_length=55, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f"{self.clave} - {self.descripcion}"

  class Meta:
    db_table = f'{DB_PREFIX}_actividad'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    actividad_obj = None
    try:
      actividad_obj = Actividad.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception Actividad obtener => {clave} => {e}")
    return actividad_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = Actividad.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception Actividad validar => {clave} => {e}")
    return es_valido


class SubActividad(models.Model):
  clave = models.CharField(max_length=3)
  actividad = models.CharField(max_length=2)
  descripcion = models.CharField(max_length=55)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f"{self.clave} - {self.descripcion}"

  class Meta:
    db_table = f'{DB_PREFIX}_subactividad'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    subactividad_obj = None
    try:
      subactividad_obj = SubActividad.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception SubActividad obtener => {clave} => {e}")
    return subactividad_obj

  @staticmethod
  def validar(clave, actividad, fecha=date.today()):
    es_valido = False
    try:
      es_valido = SubActividad.objects.filter(clave=clave, actividad=actividad).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception SubActividad validar => {clave} => {e}")
    return es_valido


class Tarea(models.Model):
  clave = models.CharField(max_length=4)
  subactividad = models.CharField(max_length=3)
  actividad = models.CharField(max_length=2)
  descripcion = models.CharField(max_length=200)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f"{self.clave} - {self.descripcion}"

  class Meta:
    db_table = f'{DB_PREFIX}_tarea'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    tarea_obj = None
    try:
      tarea_obj = Tarea.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception Tarea obtener => {clave} => {e}")
    return tarea_obj

  @staticmethod
  def validar(clave, actividad, subactividad, fecha=date.today()):
    es_valido = False
    try:
      es_valido = Tarea.objects.filter(clave=clave, actividad=actividad, subactividad=subactividad).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception Tarea validar => {clave} => {e}")
    return es_valido


class PagoPedimento(models.Model):
  clave = models.CharField(max_length=4)
  descripcion = models.CharField(max_length=150)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f"{self.clave} - {self.descripcion}"

  class Meta:
    db_table = f'{DB_PREFIX}_pagopedimento'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    pagopedimento_obj = None
    try:
      pagopedimento_obj = PagoPedimento.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception PagoPedimento obtener => {clave} => {e}")
    return pagopedimento_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = PagoPedimento.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception PagoPedimento validar => {clave} => {e}")
    return es_valido
