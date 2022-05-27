from django.db import models
import string
from datetime import datetime
from django.conf import settings

# Create your models here.

CONFIRMATION_STATUS = (
  ('A', 'Active'),
  ('U', 'Used'),
  ('C', 'Confirmed'),
)

CONFIRMATION_CODE_SIZE = 5

class Confirmation(models.Model):
  taxpayer_id = models.CharField(max_length=14, null=True)
  added = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  code = models.CharField(max_length=256, null=True)
  status = models.CharField(max_length=1, choices=CONFIRMATION_STATUS, default='A')
  uuid = models.CharField(max_length=36, db_index=True)

  def save(self, *args, **kwargs):
    if not self.code:
      self.code = Confirmation.generate_code()
    return super(Confirmation, self).save(*args, **kwargs)

  @staticmethod
  def generate_code(size=CONFIRMATION_CODE_SIZE):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(size))

  class Meta:
    unique_together = ('taxpayer_id', 'code')


INVOICE_STATUS = (
  ('S', 'Signed'),
  ('F', 'Finished'),
  ('C', 'Cancelled'),
  ('E', 'Error'),
  ('R', 'Rejected'),
)

INVOICE_TYPE = (
  ('F', 'Free'),
  ('W', 'WebService'),
)


class Invoice(models.Model):
  uuid = models.CharField(max_length=36, unique=True)
  date = models.DateTimeField(default=datetime.now, db_index=True)
  status = models.CharField(max_length=1, choices=INVOICE_STATUS, default='S')
  type = models.CharField(max_length=1, choices=INVOICE_TYPE, default='F')
  taxpayer_id = models.CharField(max_length=14)
  rtaxpayer_id = models.CharField(max_length=14)
  total = models.FloatField(default=0.00)
  complement = models.CharField(max_length=50)
  xml = models.FileField(upload_to='cfdi/%Y/%m/%d', null=True, blank=True)
  version = models.CharField(max_length=4, default=settings.CFDI_VERSION)


class Cancel(models.Model):
  uuid = models.CharField(max_length=36, db_index=True)
  date = models.DateTimeField(default=datetime.now, db_index=True)
  taxpayer_id = models.CharField(max_length=14)
  uuid_status = models.CharField(max_length=3)
  cod_status = models.CharField(max_length=3)
  type = models.CharField(max_length=1, choices=INVOICE_TYPE, default='F')

  
