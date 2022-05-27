from django.db import models
from django.db.models import Q
from django.conf import settings
from datetime import datetime, date
import re

DB_PREFIX = 'sat_cce'

class MotivoTraslado(models.Model):
  """
      Catálogo Comercio Exterior:
      @nombre_archivo: (c_MotivoTraslado.xls)
      @url_descripcionarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_MotivoTraslado.xls
      @detalles: no se usa.
  """
  clave = models.CharField(max_length=9)
  descripcion = models.CharField(max_length=450, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)
  
  def __str__(self):
    return f'{self.clave} - {self.descripcion}'
  
  class Meta:
    db_table = f'{DB_PREFIX}_motivotraslado'

class TipoOperacion(models.Model):
  """
      Catálogo Comercio Exterior:
      @nombre_archivo: (c_TipoOperacion.xls)
      @url_descripcionarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_TipoOperacion.xls
      @details: No se usa el modelo, solo tiene una clave.
  """
  clave = models.CharField(max_length=9, unique=True)
  descripcion = models.CharField(max_length=450, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'
  
  class Meta:
    db_table = f'{DB_PREFIX}_tipooperacion'


class UnidadMedida(models.Model):
  """
      Catálogo Comercio Exterior:
      @nombre_archivo: (c_UnidadAduana.xls)
      @url_descripcionarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_UnidadAduana.xls
      @details: No se usa el modelo.
  """
  clave = models.IntegerField()
  descripcion = models.CharField(max_length=450, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'
  
  class Meta:
    db_table = f'{DB_PREFIX}_unidadmedida'

  @staticmethod
  def obtener(clave, fecha=date.today(), *args, **kwargs):
    unidad_medida_obj = None
    try:
      unidad_medida_obj = UnidadMedida.objects.filter(clave=clave).get()
    except Exception as e:
      print(f"obtener_UnidadMedida Exception => {clave}     {e}")
    return unidad_medida_obj

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      es_valido = UnidadMedida.objects.filter(clave=clave).exists()
    except Exception as e:
      print(f"obtener_UnidadMedida Exception => {clave}     {e}")
    return es_valido


class Colonia(models.Model):
  """
      Catálogo Comercio Exterior:
      @nombre_archivo: c_Colonia.xls
      @url_descripcionarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_Colonia.xls
  """
  clave = models.CharField(max_length=12)
  cp = models.CharField(max_length=15)
  descripcion = models.CharField(max_length=450, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'
  
  class Meta:
    db_table = f'{DB_PREFIX}_colonia'
  
  @staticmethod
  def obtener(clave, fecha=date.today(), *args, **kwargs):
    colonia_obj = None
    try:
      colonia_obj = Colonia.objects.filter(clave=clave).get()
    except Exception as e:
      print(f"obtener_colonia Exception => {clave}     {e}")
    return colonia_obj

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      cp = kwargs.get("cp", None)
      if cp is not None:
        es_valido = Colonia.objects.filter(clave=clave, cp=cp).exists()
    except Exception as e:
      print(f"obtener_colonia Exception => {clave}     {e}")
    return es_valido


class FraccionArancelaria(models.Model):
  """
      Catálogo Comercio Exterior:
      @nombre_archivo: c_FraccionArancelaria.xls
      @url_descripcionarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_FraccionArancelaria.xls
  """
  clave = models.CharField(max_length=24, unique=True)
  descripcion = models.CharField(max_length=700, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)
  unidad = models.CharField(max_length=90)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'
  
  class Meta:
    db_table = f'{DB_PREFIX}_fraccionarancelaria'

  @staticmethod
  def obtener(clave, fecha=date.today(), *args, **kwargs):
    fraccion_arancelaria_obj = None
    try:
      fraccion_arancelaria_obj = FraccionArancelaria.objects.filter(clave=clave).get()
    except Exception as e:
      print(f"obtener_FraccionArancelaria Exception => {clave}     {e}")
    return fraccion_arancelaria_obj

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      tipo_validacion = kwargs.get('_type',None)
      if tipo_validacion == 'fraccion_unidad':
        unidad = kwargs.get('unidad',None)
        es_valido = FraccionArancelaria.objects.filter(clave=clave, unidad=unidad, inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
      else:
        es_valido = FraccionArancelaria.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_FraccionArancelaria Exception => {clave}     {e}")
    return es_valido


class Incoterm(models.Model):
  """
      Catálogo Comercio Exterior:
      @nombre_archivo: c_INCOTERM.xls
      @url_descripcionarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_INCOTERM.xls
      @details: No se usa
  """
  clave = models.CharField(max_length=9)
  descripcion = models.CharField(max_length=450, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'
  
  class Meta:
    db_table = f'{DB_PREFIX}_incoterm'


class Localidad(models.Model):
  """
      Catálogo Comercio Exterior:
      @nombre_archivo: c_Localidad.xls
      @url_descripcionarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_Localidad.xls
  """
  clave = models.CharField(max_length=6)
  estado = models.CharField(max_length=9)
  descripcion = models.CharField(max_length=450, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'
  
  class Meta:
    db_table = f'{DB_PREFIX}_localidad'

  @staticmethod
  def obtener(clave, fecha=date.today(), *args, **kwargs):
    localidad_obj = None
    try:
      localidad_obj = Localidad.objects.filter(clave=clave).get()
    except Exception as e:
      print(f"obtener_localidad Exception => {clave}     {e}")
    return localidad_obj

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      estado = kwargs.get("estado", None)
      if estado is not None:
        es_valido = Localidad.objects.filter(clave=clave, estado=estado).exists()
    except Exception as e:
      print(f"validar_localidad Exception => {clave}     {e}")
    return es_valido


class Municipio(models.Model):
  """
      Catálogo Comercio Exterior:
      @nombre_archivo: (c_Municipio.xls)
      @url_descripcionarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_Municipio.xls
  """
  clave = models.CharField(max_length=9)
  estado = models.CharField(max_length=9)
  descripcion = models.CharField(max_length=450, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'
  
  class Meta:
    db_table = f'{DB_PREFIX}_municipio'
  
  @staticmethod
  def obtener(clave, fecha=date.today(), *args, **kwargs):
    municipio_obj = None
    try:
      municipio_obj = Municipio.objects.filter(clave=clave).get()
    except Exception as e:
      print(f"obtener_municipio Exception => {clave}     {e}")
    return municipio_obj

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      estado = kwargs.get("estado", None)
      if estado is not None:
        es_valido = Municipio.objects.filter(clave=clave, estado=estado).exists()
    except Exception as e:
      print(f"validar_municipio Exception => {clave}     {e}")
    return es_valido
    