# -*- coding: utf-8 -*-

from app.core.models import Business
from django.views.decorators.cache import cache_page


def business(request, *args, **kwargs):
  user = request.user
  business = []
  business_id = None
  taxpayer_id = None
  first = None
  try:
    if not user.is_anonymous:
      if user.is_superuser or user.has_group('admins'):
        business = Business.objects.all()
      else:
        business = user.business_set.filter()


      business_id = request.session.get('business_id', None)
      if business_id is not None:
        first = Business.objects.get(id=business_id)
      elif business:
        first = business.first()
      else:      
        first = user.get_business()

      business_id = business_id if business_id is not None else first.id   
      taxpayer_id = first.taxpayer_id
  except Exception as e:
    pass

  result = {'business': business, 'default_business': business_id, 'active_taxpayer_id': taxpayer_id}

  return result
