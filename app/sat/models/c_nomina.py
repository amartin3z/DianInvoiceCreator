from django.db import models
from django.db.models import Q


DB_PREFIX = 'sat_nomina'


class TipoNomina(models.Model):
  """
      Catálogo Nómina:
      @nombre_archivo: (catNomina.xls)
      @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, db_index=True)
  descripcion = models.CharField(max_length=55, blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tiponomina'

  @staticmethod
  def obtener(clave, *args, **kwargs):
    tiponomina_obj = None
    try:
      tiponomina_obj = TipoNomina.objects.filter(clave=clave).get()
    except Exception as e:
      print(f"validar_tiponomin Exception => {clave}     {e}")
    return tiponomina_obj

  @staticmethod
  def validar(clave, *args, **kwargs):
    es_valido = False
    try:
      es_valido = TipoNomina.objects.filter(clave=clave).exists()
    except Exception as e:
      print(f"validar_tiponomina Exception => {clave}     {e}")
    return es_valido


class TipoContrato(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, db_index=True)
  descripcion = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipocontrato'

  @staticmethod
  def obtener(clave, *args, **kwargs):
    tipocontrato_obj = None
    try:
      tipocontrato_obj = TipoContrato.objects.filter(clave=clave).get()
    except Exception as e:
      print(f"obtener_tipocontraqto Exception => {clave}     {e}")
    return tipocontrato_obj

  @staticmethod
  def validar(clave, *args, **kwargs):
    es_valido = False
    try:
      es_valido = TipoContrato.objects.filter(clave=clave).exists()
    except Exception as e:
      print(f"validar_tipocontraqto Exception => {clave}     {e}")
    return es_valido


class TipoJornada(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, unique=True)
  descripcion = models.CharField(max_length=55, blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipojornada'

  @staticmethod
  def obtener(clave, *args, **kwargs):
    tipojornada_obj = None
    try:
      tipojornada_obj = TipoJornada.objects.filter(clave=clave).get()
    except Exception as e:
      print(f"obtener_tipojornada Exception => {clave}     {e}")
    return tipojornada_obj

  @staticmethod
  def validar(clave, *args, **kwargs):
    es_valido = False
    try:
      es_valido = TipoJornada.objects.filter(clave=clave).exists()
    except Exception as e:
      print(f"validar_tipojornada Exception => {clave}     {e}")
    return es_valido


class TipoRegimen(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, unique=True)
  descripcion = models.CharField(max_length=100, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tiporegimen'

  @staticmethod
  def obtener(clave, fecha, *args, **kwargs):
    tiporegimen_obj = None
    try:
      tiporegimen_obj = TipoRegimen.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"obtener_tiporegimen Exception => {clave}     {e}")
    return tiporegimen_obj

  @staticmethod
  def validar(clave, fecha, *args, **kwargs):
    es_valido = False
    try:
      es_valido = TipoRegimen.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_tiporegimen Exception => {clave}     {e}")
    return es_valido


class RiesgoPuesto(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, unique=True)
  descripcion = models.CharField(max_length=55, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_riesgopuesto'

  @staticmethod
  def obtener(clave, fecha, *args, **kwargs):
    riesgopuesto_obj = None
    try:
      riesgopuesto_obj = RiesgoPuesto.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"obtener_riesgopuesto Exception => {clave}     {e}")
    return riesgopuesto_obj

  @staticmethod
  def validar(clave, fecha, *args, **kwargs):
    es_valido = False
    try:
      es_valido = RiesgoPuesto.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_riesgopuesto Exception => {clave}     {e}")
    return es_valido


class PeriodicidadPago(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, unique=True)
  descripcion = models.CharField(max_length=55, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_periodicidadpago'

  @staticmethod
  def obtener(clave, fecha, *args, **kwargs):
    periodicidadpago_obj = None
    try:
      periodicidadpago_obj = PeriodicidadPago.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"obtener_periodicidadpago Exception => {clave}     {e}")
    return periodicidadpago_obj

  @staticmethod
  def validar(clave, fecha, *args, **kwargs):
    es_valido = False
    try:
      es_valido = PeriodicidadPago.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_periodicidadpago Exception => {clave}     {e}")
    return es_valido


class Banco(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, unique=True)
  descripcion = models.CharField(max_length=50, blank=True, null=True)
  nombre = models.TextField(blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_banco'

  @staticmethod
  def obtener(clave, fecha, *args, **kwargs):
    banco_obj = None
    try:
      banco_obj = Banco.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"obtener_banco Exception => {clave}     {e}")
    return banco_obj

  @staticmethod
  def validar(clave, fecha, *args, **kwargs):
    es_valido = False
    try:
      es_valido = Banco.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_banco Exception => {clave}     {e}")
    return es_valido


class TipoPercepcion(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, unique=True)
  descripcion = models.CharField(max_length=255, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipopercepcion'

  @staticmethod
  def obtener(clave, fecha, *args, **kwargs):
    percepcion_obj = None
    try:
      percepcion_obj = TipoPercepcion.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"obtener_tipopercepcion Exception => {clave}     {e}")
    return percepcion_obj

  @staticmethod
  def validar(clave, fecha, *args, **kwargs):
    es_valido = False
    try:
      es_valido = TipoPercepcion.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_tipopercepcion Exception => {clave}     {e}")
    return es_valido


class TipoHoras(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, db_index=True)
  descripcion = models.CharField(max_length=55, blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipohoras'

  @staticmethod
  def obtener(clave, *args, **kwargs):
    tipohoras_obj = None
    try:
      tipohoras_obj = TipoHoras.objects.filter(clave=clave).get()
    except Exception as e:
      print(f"obtener_tipohoras Exception => {clave}     {e}")
    return tipohoras_obj

  @staticmethod
  def validar(clave, *args, **kwargs):
    es_valido = False
    try:
      es_valido = TipoHoras.objects.filter(clave=clave).exists()
    except Exception as e:
      print(f"validar_tipohoras Exception => {clave}     {e}")
    return es_valido


class TipoDeduccion(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, unique=True)
  descripcion = models.CharField(max_length=255, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipodeduccion'

  @staticmethod
  def obtener(clave, fecha, *args, **kwargs):
    tipodeduccion_obj = None
    try:
      tipodeduccion_obj = TipoDeduccion.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"obtener_tipodeduccion Exception => {clave}     {e}")
    return tipodeduccion_obj

  @staticmethod
  def validar(clave, fecha, *args, **kwargs):
    es_valido = False
    try:
      es_valido = TipoDeduccion.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_tipodeduccion Exception => {clave}     {e}")
    return es_valido


class TipoOtroPago(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, unique=True)
  descripcion = models.CharField(max_length=255, blank=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipootropago'

  @staticmethod
  def obtener(clave, fecha, *args, **kwargs):
    tipootropago_obj = None
    try:
      tipootropago_obj = TipoOtroPago.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"obtener_tipootropago Exception => {clave}     {e}")
    return tipootropago_obj

  @staticmethod
  def validar(clave, fecha, *args, **kwargs):
    es_valido = False
    try:
      es_valido = TipoOtroPago.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_tipootropago Exception => {clave}     {e}")
    return es_valido


class TipoIncapacidad(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, unique=True)
  descripcion = models.CharField(max_length=100, blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipoincapacidad'

  @staticmethod
  def obtener(clave, fecha, *args, **kwargs):
    tipoincapacidad_obj = None
    try:
      tipoincapacidad_obj = TipoIncapacidad.objects.get(clave=clave)
    except Exception as e:
      print(f"obtener_tipootropago Exception => {clave}     {e}")
    return tipoincapacidad_obj

  @staticmethod
  def validar(clave, *args, **kwargs):
    es_valido = False
    try:
      es_valido = TipoIncapacidad.objects.filter(clave=clave).exists()
    except Exception as e:
      print(f"validar_tipootropago Exception => {clave}     {e}")
    return es_valido


class OrigenRecurso(models.Model):
  """
    Catálogo Nómina:
    @nombre_archivo: (catNomina.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
  """
  clave = models.CharField(max_length=3, unique=True)
  descripcion = models.CharField(max_length=55, blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_origenrecurso'

  @staticmethod
  def obtener(clave, *args, **kwargs):
    origenrecurso_obj = None
    try:
      origenrecurso_obj = OrigenRecurso.objects.get(clave=clave)
    except Exception as e:
      print(f"obtener_origenrecurso Exception => {clave}     {e}")
    return origenrecurso_obj

  @staticmethod
  def validar(clave, *args, **kwargs):
    es_valido = False
    try:
      es_valido = OrigenRecurso.objects.filter(clave=clave).exists()
    except Exception as e:
      print(f"validar_origenrecurso Exception => {clave}     {e}")
    return es_valido