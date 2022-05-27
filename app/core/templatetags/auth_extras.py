from django import template
from django.contrib.auth.models import Group 
from pdb import set_trace
register = template.Library() 
from django.conf import settings

@register.filter(name='has_group') 
def has_group(user, group_name):
  return user.groups.filter(name=group_name.strip()).exists() or user.is_superuser

@register.filter(name='has_groups') 
def has_groups(user, group_names):
  group_lst = group_names.strip().strip(',').split(',')
  _all = True
  if len(group_lst)>1:
    all_tmp = group_lst[-1]
    all_tmp = all_tmp.strip()
    if all_tmp in ['True', 'False']:
      _all = eval(all_tmp)
      group_lst.pop()
  for name in group_lst:
    if _all and not has_group(user, name.strip()):
      return False
    if not _all and has_group(user, name.strip()):
      return True
  return _all

@register.simple_tag
def blocked_account(user):
  status = user.profile.status
  reason = ''
  if status == 'L':
    reason = u'tras {} días de inactividad'.format(settings.TIME_INACTIVITY_SAT)
  elif status == 'T':
    reason = u'tras varios intentos de inicio de sesión'
  return { 'status': status, 'reason': reason}