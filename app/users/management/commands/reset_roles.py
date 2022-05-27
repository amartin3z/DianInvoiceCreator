from django.core.management.base import BaseCommand, CommandError
import os
import sys
from django.template import TemplateDoesNotExist
from django.contrib.auth.models import User, Group
from django.core.validators import validate_email
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError

from app.users.models import HBL_ROL_GROUP

class Command(BaseCommand):

  help = 'Reasing Roles and Groups HBL'

  def handle(self, *args, **options):
    #import pdb; pdb.set_trace()
    users = User.objects.filter(is_staff=True)    
    for user in users:
      groups = []
      #hbl = user.profile.hbl
      hbls = user.profile.group
      for hbl in hbls:
        if hbl in HBL_ROL_GROUP:
          user.groups.clear()
          for g in HBL_ROL_GROUP[hbl]:
            try:
              group = Group.objects.get(name=g)
              groups.append(group)
              #user.groups.add(group)
            except Exception, e:
              print g
              print "Exception => %s" % str(e)
      user.groups.set(groups)
    print "Reseted roles!"
