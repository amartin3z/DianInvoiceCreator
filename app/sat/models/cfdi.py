from django.db import models
from django.db.models import Q

import re
from datetime import datetime, date


DB_PREFIX = 'sat_catalogos'


class Aduana(models.Model):
  """
    Catálogo CFDI:
    @nombre_archivo: (catCFDI.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    \copy sat_aduana(clave, descripcion, inicio) from '/tmp/catalogos/aduana.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=4, db_index=True)
  descripcion = models.TextField(blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_aduana'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    raise NotImplemented('Aduana obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = Aduana.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_aduana Exception => code:{clave}   {e}")
    return es_valido


class ClaveUnidad(models.Model):
  """
    Catálogo CFDI:
    @nombre_archivo: (catCFDI.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    \copy sat_claveunidad(clave, nombre, descripcion, nota, inicio, fin, simbolo) from '/tmp/catalogos/claveunidad.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=3, db_index=True)
  nombre = models.CharField(max_length=250, blank=True, null=True)
  descripcion = models.TextField(blank=True, null=True)
  nota = models.TextField(blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)
  simbolo = models.CharField(max_length=50, blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_claveunidad'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    raise NotImplemented('ClaveUnidad obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = ClaveUnidad.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_claveunidad Exception => {clave}   {e}")
    return es_valido


class ClaveProdServ(models.Model):
  """
      Catálogo CFDI:
      @nombre_archivo: (catCFDI.xls)
      @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
      \copy sat_claveprodserv(clave, descripcion, iva_trasladado, ieps_trasladado, complemento, inicio, fin, frontera, palabras_similares) from '/tmp/catalogos/claveprodserv.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=10, unique=True)
  descripcion = models.CharField(max_length=255, blank=True, null=True)
  iva_trasladado = models.CharField(max_length=50, default='Sí', blank=True, null=True )
  ieps_trasladado = models.CharField(max_length=50, default='Opcional', blank=True, null=True)
  complemento = models.CharField(max_length=50, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)
  frontera = models.CharField(max_length=1, default='0', blank=True, null=True)
  palabras_similares = models.TextField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_claveprodserv'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    claveprodserv_obj = None
    try:
      claveprodserv_obj = ClaveProdServ.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"get_claveprodserv Exception => {clave}   {e}")
    return claveprodserv_obj

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      tipo = kwargs.get('tipo', None)
      if tipo == 'fronterizo':
        es_valido = ClaveProdServ.objects.filter(clave=clave, frontera='1', inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
      else:
        es_valido = ClaveProdServ.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_claveprodserv Exception => {clave}   {e}")
    return es_valido


class CodigoPostal(models.Model):
  """
      Catálogo CFDI, Comercio Exterior, Nómina:
      @nombre_archivo: (catCFDI.xls, c_CodigoPostal.xls, catNomina.xls)
      @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls (CFDI)
      @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_CodigoPostal.xls (Comercio Exterior)
      @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls (Nómina)
      \copy sat_codigopostal(clave, estado, municipio, localidad, frontera, inicio, fin, descripcion_hh, mes_inicio_hv, dia_inicio_hv, hora_inicio_hv, diferencia_hv, mes_inicio_hi, dia_inicio_hi, hora_inicio_hi, diferencia_hi) from '/tmp/catalogos/cp.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=10, db_index=True)
  estado = models.CharField(max_length=3, blank=True, null=True)
  municipio = models.CharField(max_length=3, blank=True, null=True)
  localidad = models.CharField(max_length=3, blank=True, null=True)
  frontera =  models.CharField(max_length=1, default='0')
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)
  descripcion_hh = models.CharField(max_length=70, blank=True, null=True, verbose_name='Descripción del Huso Horario')
  mes_inicio_hv = models.CharField(max_length=20, blank=True, null=True, verbose_name='Mes Inicio Horario Verano')
  dia_inicio_hv = models.CharField(max_length=20, blank=True, null=True, verbose_name='Día Inicio Horario Verano')
  hora_inicio_hv = models.CharField(max_length=10, blank=True, null=True, verbose_name='Hora Horario Verano')
  diferencia_hv = models.IntegerField(blank=True, null=True, verbose_name='Diferencia Horaria Verano')
  mes_inicio_hi = models.CharField(blank=True, null=True, max_length=20, verbose_name='Mes Inicio Horario Invierno')
  dia_inicio_hi = models.CharField(max_length=20, blank=True, null=True, verbose_name='Día Inicio Horario Invierno')
  hora_inicio_hi = models.CharField(max_length=10, blank=True, null=True, verbose_name='Hora Horario Invierno')
  diferencia_hi = models.IntegerField(blank=True, null=True, verbose_name='Diferencia Horaria Invierno')

  def __str__(self):
    return f'{self.clave} - {self.estado} - {self.municipio} - {self.localidad} - {self.frontera}'.strip()

  class Meta:
    db_table = f'{DB_PREFIX}_codigopostal'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    tz_key, tz_name = None, None
    try:
      cp = CodigoPostal.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None))
      if cp.exists():
        cp = cp[0]
        tz_name = cp.descripcion_hh
        inicio = cp.inicio
        fin = cp.fin
        if cp.diferencia_hi != cp.diferencia_hv:
          tz_key = "{}-{}".format(abs(cp.diferencia_hv), abs(cp.diferencia_hi))
        else: 
          tz_key =  "{}".format(abs(cp.diferencia_hv))
    except Exception as e:
      print(f"Exception get cp obtener_cp_husohorario => {e}")
    return tz_key, tz_name

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      tipo = kwargs.get('tipo', None)
      if tipo == 'fronterizo':
        es_valido = CodigoPostal.objects.filter(clave=clave, frontera='1', inicio__lte=fecha).filter(Q(fin=None) | Q(fin__gt=fecha)).exists()
      elif tipo == 'cce':
        estado = kwargs.get('estado', None)
        municipio = kwargs.get('municipio', None)
        localidad = kwargs.get('localidad', None)
        if estado is not None and municipio is not None and localidad is not None:
          es_valido = CodigoPostal.objects.filter(clave=clave, estado=estado, municipio=municipio, localidad=localidad, inicio__lte=fecha).filter(Q(fin=None) | Q(fin__gt=fecha)).exists()
      else:
        es_valido = CodigoPostal.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin=None) | Q(fin__gt=fecha)).exists()
    except Exception as ex:
      print(f'Exception on validate_cp =>{clave}    {ex}')
    return es_valido


class FormaPago(models.Model):
  """
    Catálogo Pagos, CFDI:
    @nombre_archivo: (catPagos.xls, catCFDI.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catPagos.xls
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    \copy sat_formapago(clave, descripcion, bancarizado, numero_operacion, rfc_ordenante, cuenta_ordenante, patron_ordenante, rfc_beneficiario, cuenta_beneficiario, patron_beneficiaria, cadenapago, nombrebancoemisor, inicio) from '/tmp/catalogos/formapago.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=3, db_index=True)
  descripcion = models.CharField(max_length=250, blank=True, null=True)
  bancarizado = models.CharField(max_length=250, blank=True, null=True)
  numero_operacion = models.CharField(max_length=250, blank=True, null=True)
  rfc_ordenante = models.CharField(max_length=250, blank=True, null=True)
  cuenta_ordenante = models.CharField(max_length=250, blank=True, null=True)
  patron_ordenante = models.CharField(max_length=250, blank=True, null=True)
  rfc_beneficiario = models.CharField(max_length=250, blank=True, null=True)
  cuenta_beneficiario = models.CharField(max_length=250, blank=True, null=True)
  patron_beneficiaria = models.CharField(max_length=250, blank=True, null=True)
  cadenapago = models.CharField(max_length=250, blank=True, null=True)
  nombrebancoemisor = models.CharField(max_length=250, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_formapago'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    raise NotImplemented('FormaPago obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      cuenta_exp = None
      _type = kwargs.get('_type', None)
      cuenta = kwargs.get('cuenta', None)
      tipo = kwargs.get('tipo', None)
      forma_pago_obj = FormaPago.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gt=fecha)| Q(fin=None))
      if _type == 'cuenta':
        forma_pago_obj = forma_pago_obj.get()
        if tipo == 'ordenante':
          cuenta_exp = forma_pago_obj.patron_ordenante
        elif tipo == 'beneficiaria':
          cuenta_exp = forma_pago_obj.patron_beneficiaria
      else:
        es_valido = forma_pago_obj.exists()
      if cuenta_exp is not None:
        cuenta_exp = f'^{cuenta_exp}$'
        es_valido = bool(re.match(cuenta_exp, cuenta))
      print(clave, cuenta, tipo, cuenta_exp)
    except Exception as e:
      print(f"validar_formapago Exception => {clave}    {e}")
    return es_valido


class Impuesto(models.Model):
  """
    Catálogo CFDI:
    @nombre_archivo: (catCFDI.xls, catPagos.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catPagos.xls
    \copy sat_impuesto(clave, descripcion, retencion, traslado, local_federal, entidad) from '/tmp/catalogos/impuesto.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=3, db_index=True)
  descripcion = models.CharField(max_length=255, blank=True, null=True)
  retencion = models.CharField(max_length=5, blank=True, null=True)
  traslado = models.CharField(max_length=5, blank=True, null=True)
  local_federal = models.CharField(max_length=50, blank=True, null=True)
  entidad = models.CharField(max_length=50, blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_impuesto'

  @staticmethod
  def obtener(clave, fecha=date.today(), *args, **kwargs):
    impuesto_obj = None
    try:
      tipo = kwargs.get('tipo', None)
      if tipo == 'retencion':
        impuesto_obj = Impuesto.objects.get(clave=clave, retencion='Si')
      elif tipo == 'traslado':
        impuesto_obj = Impuesto.objects.get(clave=clave, traslado='Si')
    except Exception as e:
      print(f"obtener Impuesto Exception tipo: {tipo}   clave:{clave} => {e}")
    return impuesto_obj

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      tipo = kwargs.get('tipo', None)
      if tipo == 'retencion':
        es_valido = Impuesto.objects.filter(clave=clave, retencion='Si').exists()
      elif tipo == 'traslado':
        es_valido = Impuesto.objects.filter(clave=clave, traslado='Si').exists()
    except Exception as e:
      print(f"validar_impuesto Exception tipo: {tipo}   clave:{clave} => {e}")
    return es_valido


class MetodoPago(models.Model):
  """
      Catálogo Pagos, CFDI:
      @nombre_archivo: (catPagos.xls, catCFDI.xls)
      @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catPagos.xls
      @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
      \copy sat_metodopago(clave, descripcion, inicio, fin) from '/tmp/catalogos/metodopago.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=3, db_index=True)
  descripcion = models.CharField(max_length=255, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_metodopago'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    raise NotImplemented('MetodoPago obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = MetodoPago.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_metodopago Exception => {clave}     {e}")
    return es_valido


class Moneda(models.Model):
  """
    Catálogo Comercio Exterior, Pagos, CFDI:
    @nombre_archivo: (c_Moneda.xls, catPagos.xls, catCFDI.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_Moneda.xls
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catPagos.xls
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    \copy sat_moneda(clave, descripcion, decimales, variacion, inicio) from '/tmp/catalogos/moneda.csv' CSV DELIMITER ',';

    import requests
    from requests.auth import HTTPBasicAuth
    from app.sat.models import Moneda
    url = 'http://www.xe.com/currencyconverter/convert/?Amount=1&To=MXN&From=%s'
    url = 'https://xecdapi.xe.com/v1/convert_to.json/?to={}&from=MXN&amount=1'
    monedas = Moneda.objects.all()
    for moneda in monedas:
      try:
        code = moneda.clave
        r = requests.get(url.format(code), auth=HTTPBasicAuth('fin196857806', 'j7ig6dsv1o05kol2n5u57mg35e'))
        response = r.json()
        rate = response.get('from', {})[0].get('mid')
        Moneda.objects.filter(clave=code).update(tipo_cambio=float(rate))
        print("%s => %s => DONE" % (code, rate))
      except Exception as e:
        print("%s: %s" % (code, str(e)))
    Moneda.objects.filter(clave='MXN').update(tipo_cambio='1')
  """
  clave = models.CharField(max_length=9)
  descripcion = models.CharField(max_length=450, blank=True, null=True)
  decimales = models.IntegerField(blank=True, null=True)
  variacion = models.CharField(max_length=50, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)
  tipo_cambio = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_moneda'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    moneda_obj = None
    try:
      moneda_obj = Moneda.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"validar_moneda Exception => {clave}     {e}")
    return moneda_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = Moneda.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_moneda Exception => {clave}     {e}")
    return es_valido


class NumeroPedimentoAduana(models.Model):
  """
      Catálogo CFDI:
      @nombre_archivo: (catCFDI.xls)
      @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
      \copy sat_numeropedimentoaduana(clave, patente, ejercicio, cantidad, inicio) from '/tmp/catalogos/numeropedimentoaduana.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=2, db_index=True)
  patente = models.CharField(max_length=50, blank=True, null=True)
  ejercicio = models.CharField(max_length=50, blank=True, null=True)
  cantidad = models.CharField(max_length=50, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    #return f'{self.clave} - {self.descripcion}'
    return f'{self.clave}'

  class Meta:
    db_table = f'{DB_PREFIX}_numeropedimentoaduana'

  @staticmethod
  def obtener(clave, fecha=date.today(), *args, **kwargs):
    numeropedimento_obj = None
    try:
      patente = kwargs.get('patente', None)
      ejercicio = kwargs.get('ano', None)
      numeropedimento_obj = NumeroPedimentoAduana.objects.filter(clave=clave, patente=patente, ejercicio=ejercicio, inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"obtener_numeropedimentoaduana Exception => {clave} {patente} {ejercicio}     {e}")
    return numeropedimento_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    raise NotImplemented('NumeroPedimentoAduana validar is not implemented yet...')


class Pais(models.Model):
  """
    Catálogo Comercio Exterior:
    @nombre_archivo: (c_Pais.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_Pais.xls
    \copy sat_pais(clave, descripcion, formato_codigopostal, rit, validacion_rit, agrupaciones) from '/tmp/catalogos/pais.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=9, db_index=True)
  descripcion = models.CharField(max_length=450, blank=True, null=True)
  formato_codigopostal = models.CharField(max_length=450, blank=True, null=True)
  rit = models.CharField(max_length=450, blank=True, null=True)
  validacion_rit = models.CharField(max_length=450, blank=True, null=True)
  agrupaciones = models.CharField(max_length=100, blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_pais'

  @staticmethod
  def obtener(clave, patente, ejercicio, fecha=date.today()):
    raise NotImplemented('Pais obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      rit = kwargs.get('rit', '-')
      tipo_validacion = kwargs.get('_type', None)

      pais_obj =  Pais.objects.filter(clave=clave)

      complemento = kwargs.get('complemento', None)
      if complemento == 'notariospublicos':
        pais_obj.exclude(clave='ZZZ')

      if tipo_validacion == 'rit':
        if pais_obj.exists():
          pais_obj = pais_obj.get()
          if pais_obj.rit and pais_obj.rit != '':
            es_valido = bool(re.match(f'^{pais_obj.rit}$', rit))
      elif tipo_validacion == 'pais_rit':
        pais_obj = pais_obj.get()
        if pais_obj.rit and pais_obj.rit != '':
          es_valido = True
      elif tipo_validacion == 'pais_cp':
        cp = kwargs.get('cp', None)
        pais_obj = pais_obj.get()
        es_valido = bool(re.match(f'^{pais_obj.formato_codigopostal}$', cp))
      elif tipo_validacion == 'agrupaciones':
        agrupaciones = kwargs.get('agrupaciones', None)
        es_valido = Pais.objects.filter(clave=clave, agrupaciones=agrupaciones).exists()
      else:
        es_valido = pais_obj.exists()
    except Exception as e:
      print(f"validar_pais_cp Exception => {e}")
    return es_valido

  def __str__(self):
    return f"{self.clave} - {self.descripcion}"


class PatenteAduanal(models.Model):
  """
    Catálogo CFDI:
    @nombre_archivo: (catCFDI.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    \copy sat_patenteaduanal(clave, inicio, fin) from '/tmp/catalogos/patenteaduanal.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=6, db_index=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_patenteaduanal'

  @staticmethod
  def obtener(clave, patente, ejercicio, fecha=date.today()):
    raise NotImplemented('PatenteAduanal obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = PatenteAduanal.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_patenteaduanal Exception => {e}")
    return es_valido


class RegimenFiscal(models.Model):
  """
    Catálogo Comercio Exterior, Nómina, CFDI:
    @nombre_archivo: (c_RegimenFiscal.xls, catNomina.xls, catCFDI.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_RegimenFiscal.xls
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    \copy sat_regimenfiscal(clave, descripcion, fisica, moral, inicio, fin) from '/tmp/catalogos/regimenfiscal.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=4, db_index=True)
  descripcion = models.CharField(max_length=255)
  fisica = models.CharField(max_length=4, blank=True, null=True)
  moral = models.CharField(max_length=4, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)


  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_regimenfiscal'

  @staticmethod
  def obtener(clave, patente, ejercicio, fecha=date.today()):
    raise NotImplemented('RegimenFiscal obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      persona = kwargs.get('persona', None)
      if persona is not None:
        if persona == 'fisica':
          es_valido = RegimenFiscal.objects.filter(clave=clave, fisica='Sí', inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
        elif persona == 'moral':
          es_valido = RegimenFiscal.objects.filter(clave=clave, moral='Sí', inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
      else:
        es_valido =  RegimenFiscal.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin=None) | Q(fin__gt=fecha)).exists()
    except Exception as cex:
      print(f'Exception on validate_regimenfiscal => {cex}')
    return es_valido


class TasaOCuota(models.Model):
  """
    Catálogo CFDI, Pagos:
    @nombre_archivo: (catCFDI.xls, catPagos.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catPagos.xls
    \copy sat_tasaocuota(rango, minimo, maximo, impuesto, factor, traslado, retencion, inicio, fin) from '/tmp/catalogos/tasaocuota.csv' CSV DELIMITER ',';
  """
  rango = models.CharField(max_length=255, blank=True, null=True)
  minimo = models.CharField(max_length=20, blank=True, null=True, db_index=True)
  maximo = models.CharField(max_length=20, blank=True, null=True, db_index=True)
  impuesto = models.CharField(max_length=40, blank=True, null=True)
  factor = models.CharField(max_length=20, blank=True, null=True)
  traslado = models.CharField(max_length=20, blank=True, null=True)
  retencion = models.CharField(max_length=20, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.rango} - {self.minimo} - {self.maximo} - {self.impuesto} - {self.factor}'

  class Meta:
    db_table = f'{DB_PREFIX}_tasaocuota'

  @staticmethod
  def obtener(clave, patente, ejercicio, fecha=date.today()):
    raise NotImplemented('TasaOCuota obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      impuesto = kwargs.get('impuesto', None)
      tipofactor = kwargs.get('tipofactor', None)
      tipo = kwargs.get('tipo', None)
      impuesto_obj = Impuesto.obtener(impuesto, fecha=fecha, tipo=tipo)
      clave_len = len(clave.split('.')[-1])
      assert clave_len == 6, "TasaOCuota debe tener 6 decimales"
      if impuesto_obj is not None:
        impuesto_str = impuesto_obj.descripcion
        try:
          if tipo == 'traslado':
            tasaocuota_obj = TasaOCuota.objects.filter(maximo=clave, impuesto=impuesto_str, factor=tipofactor, traslado='Sí', inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
            es_valido = True
          elif tipo == 'retencion':
            tasaocuota_obj = TasaOCuota.objects.filter(maximo=clave, impuesto=impuesto_str, factor=tipofactor, retencion='Sí', inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
            es_valido = True
        except TasaOCuota.DoesNotExist:
          if tipo == 'traslado':
            code = TasaOCuota.objects.filter(rango='Rango', impuesto=impuesto_str, factor=tipofactor, traslado='Sí', inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
          elif tipo == 'retencion':
            code = TasaOCuota.objects.filter(rango='Rango', impuesto=impuesto_str, factor=tipofactor, retencion='Sí', inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
          if float(clave) >= float(code.minimo) and float(clave) <= float(code.maximo):
            es_valido = True
    except Exception as e:
      print(f'Exception on TasaOCuota validar {e}   clave {clave}   impuesto {impuesto}   tipofactor   {tipofactor}   tipo{tipo}')
    return es_valido


class TipoDeComprobante(models.Model):
  """
    Catálogo CFDI:
    @nombre_archivo: (catCFDI.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    \copy sat_tipodecomprobante(clave, descripcion, maximo, inicio, fin) from '/tmp/catalogos/tipodecomprobante.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=3, db_index=True)
  descripcion = models.CharField(max_length=255, blank=True, null=True)
  maximo = models.CharField(max_length=50, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipodecomprobante'

  @staticmethod
  def obtener(clave, fecha=date.today(), *args, **kwargs):
    tipocomprobante_obj = None
    try:
      tipocomprobante_obj = TipoDeComprobante.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"get_tipocomprobante Exception => {e}")
    return tipocomprobante_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido =  TipoDeComprobante.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_tipocomprobante Exception => {e}")
    return es_valido


class TipoFactor(models.Model):
  """
    Catálogo CFDI:
    @nombre_archivo: (catCFDI.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    \copy sat_tipofactor(clave) from '/tmp/catalogos/tipofactor.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=20, db_index=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tipofactor'

  @staticmethod
  def obtener(clave, patente, ejercicio, fecha=date.today()):
    raise NotImplemented('TipoFactor obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = True
    try:
      es_valido = TipoFactor.objects.filter(clave=clave).exists()
    except Exception as e:
      print(f"validar_tipofactor Exception => {e}")
    return es_valido


class TipoRelacion(models.Model):
  """
    Catálogo CFDI:
    @nombre_archivo: (catCFDI.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    \copy sat_tiporelacion(clave, descripcion, inicio) from '/tmp/catalogos/tiporelacion.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=3, db_index=True)
  descripcion = models.CharField(max_length=255, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_tiporelacion'

  @staticmethod
  def obtener(clave, patente, ejercicio, fecha=date.today()):
    raise NotImplemented('TipoRelacion obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido =  TipoRelacion.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_tiporelacion Exception => {e}")
    return es_valido


class UsoCFDI(models.Model):
  """
    Catálogo CFDI:
    @nombre_archivo: (catCFDI.xls)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI.xls
    \copy sat_usocfdi(clave, descripcion, fisica, moral, inicio) from '/tmp/catalogos/usocfdi.csv' CSV DELIMITER ',';
  """
  clave = models.CharField(max_length=3, db_index=True)
  descripcion = models.CharField(max_length=255, blank=True, null=True)
  fisica = models.CharField(max_length=10, blank=True, null=True)
  moral = models.CharField(max_length=10, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_usocfdi'

  @staticmethod
  def obtener(clave, patente, ejercicio, fecha=date.today()):
    raise NotImplemented('UsoCFDI obtener is not implemented yet...')

  @staticmethod
  def validar(clave, fecha=date.today(), *args, **kwargs):
    es_valido = False
    try:
      persona = kwargs.get('persona', None)
      if persona is not None:
        if persona == 'fisica':
          es_valido = UsoCFDI.objects.filter(clave=clave, fisica='Sí', inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
        elif  persona == 'moral':
          es_valido = UsoCFDI.objects.filter(clave=clave, moral='Sí', inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
      else:
        es_valido = UsoCFDI.objects.filter(clave=clave, inicio__lte=fecha).filter(Q(fin__gte=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"validar_usocfdi Exception => {e}  clave {clave}   persona {persona}")
    return es_valido


class Estado(models.Model):
  """
    Catálogo Comercio Exterior, Nómina:
    @nombre_archivo: (c_Estado.xsl, catNomina.xsl)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/C_Estado.xls (Comercio Exterior)
    @url_descarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catNomina.xls (Nómina)
  """
  clave = models.CharField(max_length=9, db_index=True)
  pais = models.CharField(max_length=9, db_index=True)
  descripcion = models.CharField(max_length=450, blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'

  class Meta:
    db_table = f'{DB_PREFIX}_estado'

  @staticmethod
  def obtener(clave, *args, **kwargs):
    estado_obj = None
    try:
      estado_obj = Estado.objects.filter(clave=clave).get()
    except Exception as e:
      print(f"obtener_estado Exception => {clave}     {e}")
    return estado_obj

  @staticmethod
  def validar(clave, *args, **kwargs):
    es_valido = False
    try:
      pais = kwargs.get('pais', None)
      if clave and pais:
        es_valido = Estado.objects.filter(clave=clave, pais=pais).exists()
      elif clave and not pais:
        es_valido = Estado.objects.filter(clave=clave).exists()
      else:
        es_valido = Estado.objects.filter(pais=pais).exists()
    except Exception as e:
      print(f"validar_estado Exception => {clave}     {e}")
    return es_valido


class Mes(models.Model):
  clave = models.CharField(max_length=2)
  descripcion = models.CharField(max_length=30)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)

  def __str__(self):
    return f"{self.clave} - {self.descripcion}"

  class Meta:
    db_table = f'{DB_PREFIX}_mes'

  @staticmethod
  def obtener(clave, fecha=date.today()):
    mes_obj = None
    try:
      mes_obj = Mes.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).get()
    except Exception as e:
      print(f"Exception Mes obtener => {clave} => {e}")
    return mes_obj

  @staticmethod
  def validar(clave, fecha=date.today()):
    es_valido = False
    try:
      es_valido = Mes.objects.filter(clave=clave).filter(inicio__lte=fecha).filter(Q(fin__gt=fecha) | Q(fin=None)).exists()
    except Exception as e:
      print(f"Exception Mes validar => {clave} => {e}")


class Pedimento(models.Model):
  """
      Catálogo Comercio Exterior:
      @nombre_archivo: c_ClavePedimento.xls
      @url_descripcionarga: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/c_ClavePedimento.xls
      @detalles: Es solo una clave y no se usa el catálogo.
  """
  clave = models.CharField(max_length=9)
  descripcion = models.CharField(max_length=450, blank=True, null=True)
  inicio = models.DateField(blank=True, null=True)

  def __str__(self):
    return f'{self.clave} - {self.descripcion}'
  
  class Meta:
    db_table = f'{DB_PREFIX}_pedimento'

  @staticmethod
  def obtener(clave, *args, **kwargs):
    pedimento_obj = None
    try:
      pedimento_obj = Pedimento.objects.filter(clave=clave).get()
    except Exception as e:
      print(f"obtener_pedimento Exception => {clave}     {e}")
    return pedimento_obj

  @staticmethod
  def validar(clave, *args, **kwargs):
    es_valido = False
    try:
      es_valido = Pedimento.objects.filter(clave=clave).exists()
    except Exception as e:
      print(f"validar_pedimento Exception => {clave}     {e}")
    return es_valido