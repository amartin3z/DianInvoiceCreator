from app.sat.models.cfdi import *
from app.sat.models.c_cce import *
from app.sat.models.c_ecc import *
from app.sat.models.c_gceh import *
from app.sat.models.c_ine import *
from app.sat.models.c_nomina import *
from app.sat.models.c_notariospublicos import *
from app.sat.models.c_pagos import *
from datetime import datetime, date


class Catalogos(object):

  def __init__(self, fecha=date.today()):
    if isinstance(fecha, str):
      fecha = datetime.strptime(fecha, '%Y-%m-%dT%H:%M:%S').date()
    self.fecha = fecha

  def validar(self, catalogo, clave, *args, **kwargs):
    catalogo_obj = eval(catalogo)
    return catalogo_obj.validar(clave=clave, fecha=self.fecha, *args, **kwargs)

  def obtener(self, catalogo, clave, *args, **kwargs):
    catalogo_obj = eval(catalogo)
    return catalogo_obj.obtener(clave=clave, fecha=self.fecha, *args, **kwargs)



