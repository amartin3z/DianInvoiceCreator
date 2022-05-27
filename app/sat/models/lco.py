from django.db import models


class LCO(models.Model):
  rfc = models.CharField(db_index=True, max_length=13)
  validez = models.CharField(max_length=1)
  estatus = models.CharField(max_length=1)
  serial = models.CharField(max_length=20)
  inicio = models.CharField(max_length=19)
  fin = models.CharField(max_length=19)

  def __str__(self):
    return self.rfc
  


class LRFC(models.Model):
  rfc = models.CharField(db_index=True, max_length=13)
  sncf = models.BooleanField(default=False)
  subcontratacion = models.BooleanField(default=False)

  def __str__(self):
    return self.rfc