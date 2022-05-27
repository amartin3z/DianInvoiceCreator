# Copyright 2012 Finkok. Developed for Finkok by Intelium S.C.
#
# The code contained in this file is proprietary and confidential. 
# It may not be duplicated, redistributed, reused or displayed to any 
# other party without the expressed written consent of Finkok.

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from app.core.models import Log

try:
  import json
except ImportError:
  from django.utils import simplejson as json

from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

if settings.DEBUG:
  from pdb import set_trace
@csrf_exempt
@login_required()
def session_verify(request):
  """
  View that verify session timeout 
  """
  # set_trace()
  import datetime
  success = False
  message = ""
  seconds_left = 0
  username = request.user.username
  try:
    if (request.POST.get('action') == 'check_session_timeout' and request.user.is_authenticated):
      now = datetime.datetime.now()
      if settings.VERIFY_SESSION:
        print ("NOW")
        print (now)
      last_activity = request.session._session_cache
      if settings.VERIFY_SESSION:
        print(last_activity)
        print ("LAST ACTIVITY")
        print (last_activity)
      message = ''
      session_seconds = (now - last_activity['last_activity']).total_seconds()
      if settings.VERIFY_SESSION:
        print ("SESSION SECONDS")
        print (session_seconds)
      seconds_left = settings.SESSION_COOKIE_AGE - session_seconds
      if settings.VERIFY_SESSION:
        print ("SESSION LEFT")
        print (seconds_left)
      if seconds_left < 300:
        if seconds_left > 60: # -5 MIN LEFT
          message = 'La sesión caducara en menos de 5 minutos.'
        elif seconds_left > 0: # -1 MIN LEFT
          message = 'La sesión caducara en menos de 1 minuto.'
        else:
          #set_trace()
          Log.objects.log_action(request, 5, 'R', 'Sesión cerrada por inactividad, usuario {}'.format(username), 'U', "", user=request.user)
          request.session.flush()
          message = "Session Expired"
          print (message)
          raise Exception('Expired: %s' % seconds_left)
      success = True
  except Exception as e:
    print ("Session Verify Exception => %s" % str(e))

  # IF SOMEONE TRIES TO USE THIS VIEW WITHOUT AUTHENTICATION FIRST
  result = {'success': success, 'message': message, 'left': seconds_left}
  if settings.VERIFY_SESSION:
    print ("SESSION_VERIFY")
    print (result)
  return HttpResponse(json.dumps(result))
