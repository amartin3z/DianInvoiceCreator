from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse

from django.shortcuts import redirect
from app.users.models import Profile
from django.conf import settings
from django.http import Http404
from pdb import set_trace

from datetime import datetime, timedelta

def wizard_middleware(get_response):
  def middleware(request):
    response = get_response(request)
    try:
      if settings.WIZARD_MIDDLEWARE:
        user = request.user
        url = request.path
        if not user.is_anonymous:
          role = user.profile.role
          if role in ("C",):
            account = user.business_set
            if not account.exists():
              if url not in (reverse('wizard'), reverse('wizard_stuff'), reverse('login'), reverse('session_verify'), '/i18n/setlang/'):
                return redirect(reverse('wizard'))
            elif url in (reverse('wizard'),):
              account_obj = account.get()
              if account_obj.is_completed() and not request.is_ajax():
                return redirect(reverse('index'))
          elif url in (reverse('wizard'),):
            return redirect(reverse('index'))
    except Exception as e:
      print('Exception in wizard_middleware => {}'.format(str(e)))
      raise Http404()
    return response
  return middleware

def blocked_middleware(get_response):
  def middleware(request):
    response = get_response(request)
    try:
      if request.method == 'GET':
        if not request.user.is_anonymous:
          url = request.path
          if request.user.profile.role != 'A':
            status = request.user.profile.status
            if status in ('L', 'T', 'D') and url not in ('/blocked/', '/users/login/', '/reactivation/'):
              return redirect('/blocked/',)
            elif status in ('R',) and url == '/blocked/' or status in ('R',) and url not in ('/blocked/', '/users/login/', '/reactivation/'):
              return redirect('/logout/')
            elif status not in ('L', 'T', 'D') and url == '/blocked/':
              return redirect('/')          
          elif url == '/blocked/':
            return redirect('/')
    except Exception as e:
      print('Exception in blocked_middleware => {}'.format(str(e)))
      raise Http404()
    return response
  return middleware


class CustomSessionMiddleware(SessionMiddleware):
  def process_request(self, request):    
    import datetime
    now = datetime.datetime.now()
    path = request.path

    if not request.is_ajax() and request.user.is_authenticated:
      request.session['last_activity'] = now