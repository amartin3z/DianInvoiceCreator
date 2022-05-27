from django.db import models
from django.db.models import Q
from datetime import datetime, date

DB_PREFIX = 'sat_renovsustitvehic'


class TipoDecreto(models.Model):
  clave = models.CharField(max_length=2, db_index=True)
  descripcion = models.CharField(max_length=150, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipodecreto'


  @staticmethod
  def obtener(clave, fecha=date.today()):
    tipodecreto_obj = None
    try:
      tipodecreto_obj = TipoDecreto.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception TipoDecreto obtener => {clave} => {e}")
    return tipodecreto_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = TipoDecreto.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception TipoDecreto validar => {clave} => {e}")
    return es_valido


class VehiculoEnajenado(models.Model):
  clave = models.CharField(max_length=2, db_index=True)
  descripcion = models.CharField(max_length=55, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_vehiculoenajenado'


  @staticmethod
  def obtener(clave, fecha=date.today()):
    vehiculoenajenado_obj = None
    try:
      vehiculoenajenado_obj = VehiculoEnajenado.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception VehiculoEnajenado obtener => {clave} => {e}")
    return vehiculoenajenado_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = VehiculoEnajenado.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception VehiculoEnajenado validar => {clave} => {e}")
    return es_valido


class TipoVehiculoR(models.Model):
  clave = models.CharField(max_length=2, db_index=True)
  descripcion = models.CharField(max_length=150, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipovehiculor'


  @staticmethod
  def obtener(clave, fecha=date.today()):
    tipovehiculo_obj = None
    try:
      tipovehiculo_obj = TipoVehiculoR.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception TipoVehiculoR obtener => {clave} => {e}")
    return tipovehiculo_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = TipoVehiculoR.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception TipoVehiculoR validar => {clave} => {e}")
    return es_valido



class TipoVehiculoS(models.Model):
  clave = models.CharField(max_length=2, db_index=True)
  descripcion = models.CharField(max_length=150, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipovehiculos'


  @staticmethod
  def obtener(clave, fecha=date.today()):
    tipovehiculo_obj = None
    try:
      tipovehiculo_obj = TipoVehiculoS.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception TipoVehiculoS obtener => {clave} => {e}")
    return tipovehiculo_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = TipoVehiculoS.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception TipoVehiculoS validar => {clave} => {e}")
    return es_valido

