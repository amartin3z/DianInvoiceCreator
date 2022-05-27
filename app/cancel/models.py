# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
RESPONSE_TYPE = (
  ('A', u'Aceptación'),
  ('R', u'Rechazo'),
  ('U', u'Desconocida'),
)

INVOICE_STATUS = (
  ('V', u'Vigente'),
  ('C', u'Cancelado'),
)

INVOICE_STATUS_CANCELLATION = (
  ('W', u'Cancelado sin aceptación'),
  ('C', u'Cancelado con aceptación'),
  ('E', u'En proceso'),
  ('D', u'Plazo vencido'),
  ('U', u'Desconocido'),
)

INVOICE_TYPE = (
  ('I', 'Ingreso'),
  ('E', 'Egreso'),
  ('T', 'Traslado'),
  ('N', 'Nomina'),
  ('P', 'Pago'),
)

UUID_STATUS = (
  ('1000', u'Se recibió la respuesta de la petición de forma exitosa'),
  ('1001', u'No existen peticiones de cancelación en espera de respuesta para el uuid'),
  ('1002', u'Ya se recibió una respuesta para la petición de cancelación del uuid'),
  ('1003', u'Sello No Corresponde al RFC Receptor'),
  ('1004', u'Existen más de una petición de cancelación para el mismo uuid'),
  ('1005', u'El uuid es nulo no posee el formato correcto'),
  ('1006', u'Se rebaso el número máximo de solicitudes permitidas'),
  ('996',  u'Solicitud rechazada'),
  ('997',  u'Plazo vencido'),
  ('998',  u'Aceptación o Rechazo no realizado en el super portal' ),
  ('999',  u'Ocurrio un error durante el proceso de aceptacion rechazo'),
)


class Request(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  uuid = models.CharField(max_length=36)
  date = models.DateTimeField(null=True, auto_now_add=True)
  rtaxpayer_id = models.CharField(max_length=14)
  response = models.CharField(max_length=1, choices=RESPONSE_TYPE, default='A', null=False)
  status = models.CharField(max_length=10, choices=UUID_STATUS, default='1000')
  notes = models.TextField(null=True)
  last = models.BooleanField(default=True)
  
  class Meta:
    index_together = [['rtaxpayer_id', 'date']]
    indexes = [
      models.Index(fields=['uuid',]),
    ]


class Cancellation(models.Model):
  user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  uuid = models.CharField(max_length=36)
  date = models.DateTimeField(null=True)
  total = models.FloatField(default=0.00)
  invoice_type =  models.CharField(max_length=1, choices=INVOICE_TYPE, default='I', null=False)
  taxpayer_id = models.CharField(max_length=14)
  rtaxpayer_id = models.CharField(max_length=14)
  status = models.CharField(max_length=1, choices=INVOICE_STATUS_CANCELLATION, default='W')
  status_sat = models.CharField(max_length=1, choices=INVOICE_STATUS, default='V')
  notes = models.TextField(null=True)

  class Meta:
    index_together = [['taxpayer_id', 'date']]
    indexes = [
      models.Index(fields=['uuid',]),
    ]


class PendingCancellation(models.Model):
  uuid = models.CharField(max_length=36)
  date = models.DateTimeField(auto_now_add=True)
  taxpayer_id = models.CharField(max_length=14, null=True)
  rtaxpayer_id = models.CharField(max_length=14, null=True)
  invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE, default='I', null=True)
  total = models.FloatField(null=True, default=0.00)
