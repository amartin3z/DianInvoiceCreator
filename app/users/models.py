# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from app.core.models import Business
from multiselectfield import MultiSelectField


# Create your models here.

USER_ROLES = (
  ('A', 'Admin'),
  ('B', 'Billing'),
  ('C', 'Client'),
  ('G', 'Government'),
  ('S', 'Support'),
)

USER_GROUPS= (
  ('AD', 'Admin'),
  ('BI', 'Billing'),
  ('CA', u'Cancelación'),
  ('CL', 'Client'),
  ('EM', 'Emission'),
  ('SA', 'Sat'),
  ('LO', 'Logs'),
  ('SU', 'Support'),
  ('US', 'Usuarios'),
)


HBL_ROL_GROUP = {
    'AD': ['staff', 'admins'],
    'EM': ['staff', 'emission'],
    'BI': ['staff', 'billing'],
    'CA': ['staff', 'cancelacion'],
    'CL': ['staff', 'clients'],
    'IN': ['staff', 'invoicing'],
    'SA': ['staff', 'sat'],
    'SU': ['staff', 'support'],
    'LO': ['staff', 'logs'],
    'US': ['staff', 'usuarios'],
}

STATUS_PROFILE = (
  ('A', 'Active'),
  ('L', 'Locked'),
  ('T', 'Attempt Blocking'),
  ('D', 'Pending Deactivation'),
  ('R', 'Delete'),
)


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.CharField(choices=USER_ROLES, max_length=1, default='C')
  group = MultiSelectField(choices=USER_GROUPS, max_choices=8, max_length=24)
  status = models.CharField(choices=STATUS_PROFILE, max_length=1, default='A')

  def is_client(self):
    return self.role == 'C'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


def get_business(self, default=True):
  business = None
  if self.is_staff:
    business = Business.objects.filter(is_staff=True, default=default)
  else:
    business = Business.objects.filter(users__id=self.id)
  business = business.first()

  return business
User.add_to_class("get_business", get_business)


def has_group(self, group_name):  
  return self.groups.filter(name=group_name.strip()).exists() or self.is_superuser
User.add_to_class("has_group", has_group)


def has_groups(self, group_lst, _all=True):
  for name in group_lst:
    if _all and not self.has_group(name):
      return False
    if not _all and self.has_group(name):
      return True
  return _all
User.add_to_class("has_groups", has_groups)
