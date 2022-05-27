# -*- coding: UTF-8 -*-
from __future__ import absolute_import
#from django.db.models import Q
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, Http404 
from django.template.response import TemplateResponse

from django.db.models import Q
from .models import HBL_ROL_GROUP, USER_GROUPS, USER_ROLES
from app.core.models import Business

from datetime import datetime, timedelta
import locale
from pdb import set_trace

from django.utils import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group, User


def is_superuser(user):
  return user.is_superuser

def get_query(function):

  def wrap(request):
    try:
      if request.method == 'POST' and request.is_ajax():
        query = ~Q(profile__role='A')
        if request.user.profile.role != 'A':
          query = Q(is_superuser=False) & ~Q(username__endswith='finkok.com')

        if 'email' in request.POST:
          email = request.POST.get('email')
          query = query.__and__(Q(username__icontains=email))
        if 'name' in request.POST:
          name = request.POST.get('name')
          query = query.__and__(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if 'status' in request.POST:
          status = request.POST.get('status')
          if status in ('active', 'suspended'):
            status_ = 1 if status == 'active' else 0            
            query = query.__and__(Q(is_active=status_))        
        if 'taxpayer_id' in request.POST:
          query = query.__and__(Q(business__taxpayer_id__icontains=request.POST.get('taxpayer_id')))
        if 'group' in request.POST:
          group = request.POST.get('group')
          if group in ['admins', 'billing', 'client', 'support']:
            query = query.__and__(Q(groups__name=group))
            # if group == 'staff':
              # query = query.__and__(Q(is_staff=1))
            # else:

        # query = query.__and__(~Q(profile__role='A'))

        return function(request, query)
      else:
        total_users = 0

        if request.user.profile.role != 'A':
          total_users = User.objects.filter(Q(is_superuser=False) & ~Q(username__endswith='finkok.com')).count()
        else:
          total_users = User.objects.filter(~Q(profile__role='A')).count()
          
        parameters = {
          'username': u'{} {}'.format(request.user.first_name, request.user.last_name),
          'groups': Group.objects.all(),
          'roles': USER_GROUPS,
          'businesses': Business.objects.filter(is_staff=True).values_list('id', 'taxpayer_id'), # This view is supposed to be seen only by the staff
          'total_users': total_users
        }
        template = 'users/users.html'
        return TemplateResponse(request, template, parameters)
    except Exception as e:
      print("Exception get_query() | {}".format(e))
      parameters = {
        'username': u'{} {}'.format(request.user.first_name, request.user.last_name),
        'groups': Group.objects.all(),
        'roles': USER_GROUPS,
        'businesses': Business.objects.filter(is_staff=True).values_list('id', 'taxpayer_id') # This view is supposed to be seen only by the staff
      }
      return render(request, 'users/users.html', parameters)

  return wrap


def group_required(group, login_url=None, raise_exception=False):
  '''
  Decorator for views that checks whether a user has a group permission, redirecting to the log-in page if necessary.
  If the raise_exception parameter is given the PermissionDenied exception is raised.
  '''
  def check_perms(user):
    if isinstance(group, six.string_types):
      groups = (group, )
    else:
      groups = group
    if user.groups.filter(name__in=groups).exists():
      return True
    if raise_exception:
      raise PermissionDenied
    return False
  return user_passes_test(check_perms, login_url=login_url)


def has_group(group_name):
  def _has_group(function):
    def wrap(request, *args, **kwargs):
      if request.user.is_superuser:
        return function(request, *args, **kwargs)
      if not request.user.has_group(group_name):
        raise PermissionDenied
      return function(request, *args, **kwargs)
    return wrap
  return _has_group

def has_groups(group_lst, _all=True):
  def _has_groups(function):
    def wrap(request, *args, **kwargs):
      if request.user.is_superuser:
        return function(request, *args, **kwargs)
      result = request.user.has_groups(group_lst, _all)
      if result:
        return function(request, *args, **kwargs)
      raise PermissionDenied
    return wrap
  return _has_groups


def block_account(function):
  def wrap(request):
    from app.core.models import User
    from app.users.models import Profile
    user = User.objects.filter(username=request.POST.get('email'))
    if user:
      user = user[0]
      if user.profile.role is not 'A':
        if user.last_login is None:
          user.is_active = True
          user.save()
          user.last_login = datetime.now()
        last_login = user.last_login.replace(tzinfo=None)
        now = datetime.now() - timedelta(days=settings.TIME_INACTIVITY_SAT)
        #if last_login and last_login <= now:
        #  Profile.objects.filter(user=user).update(status='L')
    return function(request)
  return wrap