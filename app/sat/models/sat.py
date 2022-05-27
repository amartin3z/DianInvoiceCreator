from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField, JSONField


class Receipt(models.Model):
  uuid = models.CharField(max_length=36, db_index=True) #, unique=True) # ???
  cod_status = models.CharField(max_length=255)
  date = models.DateTimeField()
  incidents = models.TextField(default='')    
  xml = models.FileField(upload_to='recepcion/%Y/%m/%d', null=True, blank=True)
  taxpayer_id = models.CharField(max_length=14, null=True)  


CANCELLATION_STATUS = (
  ('E', 'Pending'), 
  ('A', 'Accepted'), 
  ('R', 'Rejected'), 
  ('D', 'Due'), 
  ('C', 'Cancelled'), 
)


class Cancellation(models.Model):    
  taxpayer_id = models.CharField(max_length=14)
  cod_status = models.CharField(max_length=255, null=True)
  date = models.DateTimeField()
  uuid = models.CharField(max_length=36, db_index=True)
  uuid_status = models.CharField(max_length=36)
  faultcode = models.CharField(max_length=255, null=True)
  faultstring = models.CharField(max_length=255, null=True)
  xml = models.FileField(upload_to='cancelacion/%Y/%m/%d', null=True, blank=True)
  status = models.CharField(max_length=1, choices=CANCELLATION_STATUS, default='E')


SERVICELEVELDETAIL_TYPE = (
    ('R', 'Rejected'),
    ('E', 'Extemporaneous'),
    ('I', 'Incidents'),
)


class ServiceLevel(models.Model):
  year = models.PositiveSmallIntegerField()
  month = models.PositiveSmallIntegerField()
  initial = models.PositiveIntegerField(null=True)
  final = models.PositiveIntegerField(null=True)
  rejected = models.PositiveIntegerField(default=0)
  incidents = models.PositiveIntegerField(default=0)
  extemporaneous = models.PositiveIntegerField(default=0)
  satisfied = models.PositiveIntegerField(default=0)
  duplicated = models.PositiveIntegerField(default=0)


class  ServiceLevelDetail(models.Model):
  service = models.ForeignKey('ServiceLevel', on_delete=models.CASCADE)
  type = models.CharField(max_length=1, choices=SERVICELEVELDETAIL_TYPE, default='R')
  uuid = models.CharField(max_length=36, db_index=True)
  taxpayer_id = models.CharField(max_length=14, null=True)
  date = models.DateTimeField(auto_now_add=True)
  incidents = JSONField(null=True)
  detail = models.TextField(null=True)
