# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import transaction, IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# from validate_email import validate_email
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse, Http404, HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.core import signing
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from .decorators import is_superuser, get_query, has_group, has_groups, block_account
from django.contrib.auth.models import User, Group
from app.core.models import Business, Log
# from app.billing.decorators import get_query_dashboard
from app.core.decorators import get_default_business
from app.core.logs import MESSAGES_LOGS
from .models import HBL_ROL_GROUP, USER_GROUPS, Profile
# from app.billing.models import Billing
from django.core.cache import cache
from pdb import set_trace
#from django.shortcuts import render, render_to_response, redirect
from django_registration.backends.activation.views import RegistrationView as BaseRegistrationView
from django_registration.backends.activation.views import ActivationView as BaseActivateView
from .forms.registration import UserForm, ActivationForm
from django.contrib.sites.shortcuts import get_current_site

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from app.core.utils.profile import validate_pass_one, validate_pass, email_validator
from app.core.models import PasswordHistory
from django.contrib.auth.hashers import check_password, make_password
from django.utils import timezone
from django.core.mail import EmailMessage
from helpdesk.models import Queue, Ticket, FollowUp, Attachment, TicketDependency

from django.utils.translation import ugettext as _
from app.invoicing.models import ProdServ, Receiver, Invoice, Buyer


GROUPBUTTON = {
  '': u'<button class="btn btn-default btn-sm" title="{sin_grupo}"><strong>{sin_grupo}</strong></button>'.format(sin_grupo=_('Without Group')),
  'providers': u'<button class="btn btn-info btn-sm" title="{proveedor}"><strong>{proveedor}</strong></button>'.format(proveedor=_('Provider')),
  #'proveedores': u'<button class="btn btn-info btn-sm" title="Proveedor"><strong>Proveedor</strong></button>',
  'staff': u'<button class="btn btn-warning btn-sm" title="{staff}"><strong>{staff}</strong></button>'.format(staff=_('Staff')), 
  'agents': u'<button class="btn btn-success btn-sm" title="{empleado}"><strong>{empleado}</strong></button>'.format(empleado=_('Employee')),
  'clients': u'<button class="btn btn-danger btn-sm" title="{cliente}"><strong>{cliente}</strong></button>'.format(cliente=_('Client')),
}

GROUPS = ['providers', 'staff', 'agents', 'clients']

MONTS = {
  1 :  'Enero',
  2 :  'Febrero',
  3 :  'Marzo',
  4 :  'Abril',
  5 :  'Mayo',
  6 :  'Junio',
  7 :  'Julio',
  8 :  'Agosto',
  9 :  'Septiembre',
  10 : 'Octubre',
  11 : 'Noviembre',
  12 : 'Diciembre',
}

def password_reset_confirm(request, uidb64, token, *args, **kwargs):
  try:
    user_id, validlink, token_resetcheck = force_text(urlsafe_base64_decode(uidb64)), False, TokenGenerator_passreset()
    try:
      user = User.objects.get(pk=user_id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
      user = None
    if request.method == 'POST':
      success, message = False, 'Error..'
      option  = request.POST.get('option')
      password = request.POST.get('password')
      object_last = PasswordHistory.objects.filter(user_id = user_id)
      if option == 'password_one':
        success, message = validate_pass_one(password)
        if success and object_last.exists():
          object_pass = object_last.get(user_id = user)
          success, message = False, _('The password must not be equal to a previously established one.')
          if not check_password(password, object_pass.old) and not check_password(password, object_pass.older) and not check_password(password, object_pass.oldest):
            success, message = True, ''
        elif success and not object_last.exists():
          success, message = False, _('The password cannot be the same as the previous one.')
          if not check_password(password, user.password):
            success, message = True, ''
      elif option == 'password_all':
        password2 = request.POST.get('password2')
        success, message = validate_pass(password, password2)
        if success:
          message =  _('The password cannot be the same as the previous one.') #_('La contraseña no pueder la misma que la anterior.')
          if object_last.exists():
            object_pass = object_last.get(user_id = user)
            message = _('The password must not be equal to a previously established one.') #_('La contraseña no deber ser igual a una anteriormente establecida.')
            if not check_password(password, object_pass.old) and not check_password(password, object_pass.older) and not check_password(password, object_pass.oldest):
              user.set_password(password)
              object_pass.rotate(make_password(password))
              user.save()
              success, message = True, ''
          else:
            if not check_password(password, user.password):
              objects, created = PasswordHistory.objects.get_or_create(user_id = user.id, old = make_password(password), older = user.password, oldest = user.password, last_rotation_date = timezone.now())
              user.set_password(password)
              user.save()
              success, message = True, ''
      context = {'success': success, 'message': message}
      return JsonResponse(context)
    elif request.method == 'GET':
      if user:
        validlink = token_resetcheck.check_token(user, token)
      return render(request, 'registration/password_reset_confirm.html', {'validlink':validlink})
  except Exception as e:
    print ('Exception in password_reset_confirm => {}'.format(str(e)))
    raise Http404("SignUp Page does not exist")

def password_reset(request, *args, **kwargs):
  try:
    if request.method == 'POST':
      success, message, token_resetcheck, context = False, _('The email structure is not correct.'), TokenGenerator_passreset(), {} #La estructura del correo electrónico no es correcta.
      email = request.POST.get('email')
      val_success, val_message = email_validator(email)
      if email and val_success:
        exist_user = User.objects.filter(username = email)
        if exist_user.filter(username = email, is_active = True).exists():
          try:
            subject = _('UBL | Change of password') #_('Finkok | Cambio de Contraseña')
            user = exist_user.get(username = email)  
            user_list = user.username
            uid, token = urlsafe_base64_encode(force_bytes(user.pk)), token_resetcheck.make_token(user)
            email_message = render_to_string('registration/password_reset_email.html', {
              'user': user,
              'activation_url': request.build_absolute_uri(reverse('password_reset_confirm', args=(uid, token))),
            })
            email = EmailMessage(subject, email_message, to=[user_list])
            email.content_subtype = 'html'
            email.send()
            success, message = True, ''
          except Exception as e:
            print ('Exception in envio_email => {}'.format(str(e)))
            message = _('Error sending mail, please try again') #_('Error al enviar correo, por favor intenta nuevamente mas tarde')
        elif exist_user.filter(username = email, is_active = False).exists():
          message = _('Your account is deactivated, contact support for more information.') 
        else:
          message = _('The email does not match any account.') 
      context = { 'success': success, 'message': message}
      return JsonResponse(context)
    elif request.method == 'GET':
      return render(request, 'registration/password_reset_form.html')
  except Exception as e:
    print ('Exception in password_reset => {}'.format(str(e)))


#### === > tokens
class TokenGenerator_passreset(PasswordResetTokenGenerator):
	def _make_hash_value(self, user, timestamp):
		login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
		return(six.text_type(user.pk) + user.password + six.text_type(login_timestamp) + six.text_type(timestamp))
#### === > tokens

@login_required()
@get_default_business
def index(request, *args, **kwargs):
  #set_trace()
  import json
  MESES = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
  }

  user = request.user
  template, context = 'home.html', {'name':user.first_name, 'date':datetime.now()}
  role = request.user.profile.role
  business = kwargs.get('business', None)
  if business:
    request.session['logo']  = business.get_logo()
    context['name'] = business.name
    context['date'] = request.user.date_joined
  if role == 'A' and request.user.has_group('admin'):
    #user = request.user
    #template, context = 'home_sat.html', {'name':user.first_name, 'date':datetime.now()}
    return HttpResponseRedirect(reverse('invoices_sat'))

  data_business = []
  data_invoices = []
  data_prodserv = []
  labels_months = []

  if business:
    for number_month in range(0, 12):
      number_month += 1
      labels_months.append(MESES[number_month])
      data_invoices.append(Invoice.objects.filter(emission_date__month=number_month, emission_date__year=datetime.now().year, taxpayer_id=business.taxpayer_id).count())
      data_prodserv.append(ProdServ.objects.filter(creation_date__month=number_month, creation_date__year=datetime.now().year, business_id=business.id).count())
      data_business.append(Buyer.objects.filter(modified__month=number_month, modified__year=datetime.now().year, business_id=business.id).count())
  

  total_inv = Invoice.objects.filter(taxpayer_id=business.taxpayer_id, status='F').count()
  total_prodser = ProdServ.objects.filter(business_id=business.id).count()
  context.update({
    'total_business': Buyer.objects.filter(business=business).count(),
    'total_invoices': total_inv,
    'total_prodserv': total_prodser,
    'total_tickets': Ticket.objects.filter(submitter_email=request.user.username).count(),
    'data_invoice': data_invoices,
    'labels': json.dumps(labels_months),
    'data_prodserv': data_prodserv,
    'data_business': data_business,
    'role': role

  })
  return TemplateResponse(request, template, context)

@login_required(login_url='/')
@has_groups(['sat'], False)
def index_sat(request):
  #set_trace()
  user = request.user
  template, context = 'home.html', {'name':user.first_name, 'date':datetime.now()}
  if request.method =='POST' and request.is_ajax():
    role = request.user.profile.role
    if role == 'G' and request.user.has_group('sat'):
      print ("ROLE = G")
      if request.session['logo']:
        context['name'] = request.user
        #return TemplateResponse(request, 'home_sat.html', context)
  return HttpResponseRedirect(reverse('invoices_sat'))
  #return render(request, template, context)

@block_account
def login(request):
  #set_trace()
  try:
    if request.method == 'POST':
      success = False
      url = ''
      message = ''
      username = request.POST.get('email')
      password = request.POST.get('password')
      try:
        user = authenticate(username=username, password=password)
        if user is not None:
          if user.is_active:
            attempts = cache.get('lockout_{}'.format(username), 0)
            if attempts > 2:
              message = MESSAGES_LOGS.get('mensaje45').get(settings.DEFAULT_LANGUAGE_CODE)
              #message = _('Account blocked for multiple failed attempts') #_('Cuenta bloqueada por múltiples intentos fallidos')
              Log.objects.log_action(request, 1, 'U', message, 'U', '', user=user)
              if settings.ATTEMPT_BLOCKING_ACCOUNT:
                user.profile.status = 'T' ## TRY
                user.save()
                success = True
            else:
              success = True
            if success and user.profile.role != 'G':
              cache.delete('lockout_{}'.format(username)) ## IF LOGGED DELETE CACHE
              auth_login(request, user)
              url = '/'
              if not request.session.get('business_id'):
                try:
                  business = user.get_business(default=True)
                  request.session['business_id'] = business.id
                  request.session['business_taxpayer_id'] = business.taxpayer_id  
                  message = _('Active user')
                except Exception as e:
                  pass
            elif user.profile.role == 'G':
              cache.delete('lockout_{}'.format(username)) ## IF LOGGED DELETE CACHE
              auth_login(request, user)
              url = 'index_sat'
              message = _('Active user')
          else:
            get_cache = cache.get('lockout_{}'.format(username))
            if get_cache:
              message = MESSAGES_LOGS.get('mensaje45').get(settings.DEFAULT_LANGUAGE_CODE)
              #message = _('Account blocked for multiple failed attempts')
              Log.objects.log_action(request, 1, 'U', message, 'U', '', user=user)
            else:
              message = _('Inactive user')
        else:
          confirm_user = User.objects.filter(username=username)
          if confirm_user.exists():
            user = confirm_user.get()
            attempts = cache.get('lockout_{}'.format(username), 0)
            if attempts > 2:
              message = MESSAGES_LOGS.get('mensaje45').get(settings.DEFAULT_LANGUAGE_CODE)
              #message = _('Account blocked for multiple failed attempts')
              Log.objects.log_action(request, 1, 'R', message, 'U', '', user=user)
            else:
              attempts += 1
              cache.set('lockout_{}'.format(username), attempts, settings.TIME_BLOCKED)
              message = MESSAGES_LOGS.get('mensaje67').get(settings.DEFAULT_LANGUAGE_CODE).format(username, attempts)
              #message = _('User {} entered an incorrect password ({} attemp)'.format(username, attempts)) #El usuario {} ingreso una contraseña incorrecta ({} intento)
              Log.objects.log_action(request, 1, 'U', message, 'U', '', user=user)
          else:
            message = MESSAGES_LOGS.get('mensaje46').get(settings.DEFAULT_LANGUAGE_CODE).format(username)
            #message = _('An attempt was made to log in with the user {}, and this is non-existent'.format(username))#Se intento iniciar sesión con el usuario {}, y este es inexistente
          Log.objects.log_action(request, 1, 'U', message, 'U', '')
      except Exception as e:
        if not message:
          message = str(e)
        Log.objects.log_action(request, 1, 'U', message, 'U', '')
      Log.objects.log_action(request, '5', 'R', MESSAGES_LOGS.get('mensaje68').get(settings.DEFAULT_LANGUAGE_CODE).format(username), 'U', "") # El usuario {} inicio sesión

      response = {
        'success': success,
        'url': url,
        'message': message
      }
      
      return JsonResponse(response)
    else:
      if not request.user.is_anonymous:
        if request.user.is_authenticated and request.user.profile.role != 'G':
          return HttpResponseRedirect(reverse('index'))
        elif request.user.profile.role == 'G':
          return HttpResponseRedirect(reverse('index_sat'))
  except Exception as e:
    print("Exception login => {}".format(e))
    Log.objects.log_action(request, 2, 'R', MESSAGES_LOGS.get('mensaje47').get(settings.DEFAULT_LANGUAGE_CODE), 'U', "Exception login => {}".format(e)) #Ocurrió una excepción al momento de iniciar sesión
    #return Http404()

  return render(request, 'users/login.html')

@login_required(login_url='/')
def logout(request):
  #set_trace()
  user = request.user.username
  Log.objects.log_action(request, '5', 'R', MESSAGES_LOGS.get('mensaje69').get(settings.DEFAULT_LANGUAGE_CODE).format(user), 'U', "") #El usuario {} cerro sesión.
  auth_logout(request)
  return HttpResponseRedirect('/login')

@login_required(login_url='/')
@has_groups(['admins'], False)
@get_query
def list_users(request, query):
  try:
    if request.method == 'POST' and request.is_ajax():
      start = int(request.POST.get('iDisplayStart'))
      length = int(request.POST.get('iDisplayLength'))
      
      users_list = []
      append = users_list.append
      
      users = User.objects.filter(query).exclude(username=request.user.username).order_by('-id')
      total = users.count()
      users = users[start:start+length]
      for user in users.iterator():
        status  = user.is_active
        email = user.username
        role = user.profile.role
        profile_status = user.profile.status
        name = u'{} {}'.format(user.first_name, user.last_name)
        user_status = (render_to_string('users/template_strings/users_status.html', {'status': status}, request))
        blocked = Profile.objects.filter(user=user, status='L').exists()
        options = render_to_string('users/template_strings/users_options.html', {'status': status, 'email': email, 'user': user, 'role':role, 'blocked': blocked, 'p_status':profile_status}, request)
        group_name = 'staff' if user.is_staff else user.groups.all().first().name if user.groups.all().count() > 0 else ''
        # group = GROUPBUTTON[group_name] if group_name in GROUPBUTTON else GROUPBUTTON['']
        group = render_to_string('users/template_strings/group.html', {'group': group_name if group_name in GROUPS else ''}, request)
        taxpayer_id = ''
        if role in ['P', 'S', 'C']:
          try:
            taxpayer_id = Business.objects.filter(users=user).values_list('taxpayer_id', flat=True)[0]
          except:
            pass
        append([user_status, email, name, taxpayer_id, group, options])

      Log.objects.log_action(request, '5', 'R', MESSAGES_LOGS.get('mensaje48').get(settings.DEFAULT_LANGUAGE_CODE), 'U', "") # Se listaron los usuarios

      result = {
        'aaData' : users_list,
        'iTotalRecords': total,
        'iTotalDisplayRecords': total
      }
      return JsonResponse(result)
    else:
      template = 'users/users.html'
      context = {
        'username': u'{} {}'.format(request.user.first_name, request.user.last_name),
        'groups': Group.objects.exclude(name__in=[]),
      }
      return TemplateResponse(request, template, context) 
  except Exception as e:
    print("Exception list_users => {}".format(e))
    Log.objects.log_action(request, 2, 'R', MESSAGES_LOGS.get('mensaje49').get(settings.DEFAULT_LANGUAGE_CODE), 'U', "Exception list_users => {}".format(e)) #Ocurrió una excepción al momento de listar los usuarios
    raise Http404()

@login_required(login_url='/')
@has_groups(['admins'], False)
def user_options(request):
  success = False
  message = u'Error.'
  response = {}
  try:
    email = request.POST.get('email')
    option = request.POST.get('option')
    if option == 'P':
      user = User.objects.filter(username=email).last()
      if user and user.is_active and not user.is_superuser:
        user1 =  request.user.username
        user2 = email
        auth_login(request, user)
        success = True
        message = _(u'Successful customization.') #Personalización exitosa
        Log.objects.log_action(request, '5', 'R', MESSAGES_LOGS.get('mensaje50').get(settings.DEFAULT_LANGUAGE_CODE).format(user1, user2), 'U', "")
      else:
        message = _('The user has not activated their account or is suspended.') #_('El usuario no ha activado su cuenta o se encuentra suspendido.')
    elif option == 'get-info':
      #~ TODO Show modal and print user info in the form
      user = User.objects.filter(username=email).exclude(is_superuser=True).last()
      user_id = signing.dumps({'user_id': user.id})
      first_name = user.first_name
      last_name = user.last_name
      email_ = user.email
      username = user.username
      #groups = user.groups.values_list('id', flat=True)
      groups = user.profile.group
      businesses = Business.objects.filter(users=user).values_list('id')

      response.update({
        'info': {
          'edit_user_id': user_id,
          'edit_email': email_,
          'edit_username': username,
          'edit_firstname': first_name,
          'edit_lastname': last_name,
          'edit_group': groups,
          'edit_businesses': list(businesses),

        }
      })
      
      success = True
      message = _('User info got it successfully.')
    elif option == 'update-info':
      message = _('Error updating user information') #_(u'Error actualizando la información del usuario.')
      try:
        groups = []
        user_profile = []
        user_id = request.POST.get('user_id')
        user_data = signing.loads(user_id)
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        group_lst = request.POST.getlist('group[]')
        new_businesses = request.POST.getlist('businesses[]')
        new_password = request.POST.get('new_password', None)

        user = User.objects.get(id=user_data['user_id'], is_superuser=False)
        user.username = username
        user.email = username
        user.first_name = first_name
        user.last_name = last_name

        if new_password is not None:
          user.set_password(new_password)

        if user.profile.role == 'E':
          if not len(new_businesses):
            raise Exception(_('You must select at least one business')) #Debes seleccionar al menos un negocio

          if not len(group_lst):
            raise Exception(_('You must select at least one business group.'))

          user.groups.clear()
          for group in group_lst:
            if group in HBL_ROL_GROUP:
              user_profile.append(group)
              for g in HBL_ROL_GROUP[group]:
                group_ = Group.objects.get(name=g)
                groups.append(group_)
          user.groups.set(groups)
          user.profile.group = user_profile
          user.profile.save()
          # Edit business-user relationship
          businesses = Business.objects.filter(is_staff=True)
          for business in businesses:
            business_users = business.users.all()
            if (str(business.id) not in new_businesses) and (user in business_users):
              business.users.remove(user)
              business.save()
            elif (str(business.id) in new_businesses) and (user not in business_users):
              business.users.add(user)
              business.save()

        user.save()
        success = True
        message = _('User information has been updated') #_(u'La información del usuario ha sido actualizada.')
        
        Log.objects.log_action(request, '5', 'U',MESSAGES_LOGS.get('mensaje51').get(settings.DEFAULT_LANGUAGE_CODE).format(user.username), 'U', "")
      except Exception as e:
        print("Exception user_options update-info => {}".format(e))
        message = MESSAGES_LOGS.get('mensaje52').get(settings.DEFAULT_LANGUAGE_CODE)
        #message = _('There was a problem when updating the information') #_("Hubo inconveniente al momento de actualizar la información")
        Log.objects.log_action(request, 2, 'U', ''.format(message), 'U', "Exception user_options update-info => {}".format(e))
    elif option == 'AS':
      # user = User.objects.filter(email=email).exclude(is_superuser=True).last()
      #
      user = User.objects.filter(username=email).exclude(is_superuser=True).last()
      #
      if user and not user.last_login:
        now = datetime.now()
        user.last_login = now.isoformat()
        user.is_active = True
        user.save()
        message = _('The user has been activated') #_('El usuario ha sido activado.')
      else:
        query_profile = Profile.objects.get(user_id = user.id)
        user.is_active = not user.is_active 
        user.save()
        # 
        if 'D' in query_profile.status and not user.is_active:
          query_profile.status = 'R'
        else:
          query_profile.status = 'A'
        query_profile.save()
        # 
        message = _('The user has been %s.') % ( _('active') if user.is_active else _('suspend') )
      success = True
      Log.objects.log_action(request, '5', 'U', _('User {} {}').format(_('Active') if user.is_active else _('Suspend'), user.username), 'U', "")
    elif option == 'validate-email':
      print ('OPER validate-email')
      success = True
      username = request.POST.get('username')
      
      print ('OPER validate-email -----username {}'.format(username))
      try:
        #validate_email(username)
        user = User.objects.filter(username=username, is_superuser=False).exists()
        if user:
          success = False
          message = 'existing_user'
      except:
        success = False
        message = 'bad_email'
      print ('OPER validate-email -----success {} ------ message {}'.format(success, message))
      Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje53').get(settings.DEFAULT_LANGUAGE_CODE).format(message), 'U', "") #La respuesta obtenida al validar el usuario fue
    elif option == 'exists-rfc':
      message = _('Validating RFC...')
      taxpayer_id = request.POST.get('taxpayer_id')
      success = not Business.objects.filter(taxpayer_id=taxpayer_id).exists() # Note: The exists() result is being denied
      message = _('RFC validated!')
      Log.objects.log_action(request, 5, 'R', MESSAGES_LOGS.get('mensaje54').get(settings.DEFAULT_LANGUAGE_CODE).format(taxpayer_id), 'U', "") #Se valido correctamente el RFC 
    elif option == 'add-user':
      message = ''
      try:
        #set_trace() #oZO3x%Ph
        username = request.POST.get('username', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        #group = request.POST.get('group', None)
        group_lst = request.POST.getlist('group[]')
        _type = request.POST.get('type', None)
        taxpayer_id = request.POST.get('taxpayer_id', None)
        selected_businesses = request.POST.getlist('businesses[]', [])
        new_password = request.POST.get('password', None)

        try:
          validate_email(username)
          try:
            # with transaction.atomic():
            user, created = User.objects.get_or_create(username=username, is_superuser=False)
            print ('Se creo el usuario????? {}'.format(created))
            if created:
              groups = []
              user_profile = []
              user.email = username
              user.first_name = first_name
              user.last_name = last_name
              user.profile.role = _type
              user.set_password(new_password)
              print ('tipo de  usuario????? {}'.format(_type))
              if _type == 'A':
                user.is_superuser = True
                user.is_staff = True
                
              if _type in ['A', 'B', 'G', 'S']:
                # user.is_staff = True

                # set_trace()
                if len(group_lst) > 0:  
                  user.groups.clear()
                  for group in group_lst:
                    if group in HBL_ROL_GROUP:
                      user_profile.append(group)
                      for g in HBL_ROL_GROUP[group]:
                        group_ = Group.objects.get(name=g)
                        groups.append(group_)
                else:
                  admin = Group.objects.get(name='admins')
                  user_profile.append(admin)
                  groups.append(admin)

                user.groups.set(groups)
                user.profile.group = user_profile
                user.profile.save()
                user.save()
                print ('Se guardo el usuario?? {}'.format(user))
                Log.objects.log_action(request, 5, 'C', MESSAGES_LOGS.get('mensaje55').get(settings.DEFAULT_LANGUAGE_CODE).format(username), 'U', '') #Se registro un nuevo usuario con correo

                # Add business-employee relationship
                businesses = Business.objects.filter(is_staff=True, id__in=selected_businesses)
                for business in businesses:
                  business.users.add(user)
                  business.save()
                  print ('Se guardo  el negocio????? {}'.format(business))
              elif _type == 'C':
              
                # set_trace()
                # if _type == 'P':
                #   group_name = 'providers'
                # elif _type == 'S':
                #   group_name = 'agents'
                # else:
                #   group_name = 'clients'
                # user.groups.add(group)
                group = Group.objects.get(name='clients')
                group.user_set.add(user)
                print ('Usuario agregado al grupo????? {}'.format(group))
              
                # Create own business
                business, created = Business.objects.get_or_create(taxpayer_id=taxpayer_id)
                print ('Se creo  el negocio????? {}'.format(business))
                if not created:
                  message = MESSAGES_LOGS.get('mensaje56').get(settings.DEFAULT_LANGUAGE_CODE)
                  #message = _('Previously registered RFC {}.'.format(taxpayer_id)) #RFC {} previamente registrado.
                  Log.objects.log_action(request, 5, 'R', message, 'U', '')
                  raise Exception(message)

                business.name = '{} {}'.format(first_name, last_name)
                business.email = [username]
                business.status = 'A'
                business.has_fiel = False
                business.default = True
                business.is_staff = False
                business.users.add(user)
                business.save()
                user.save()
                print ('Se guardo  el negocio????? {}'.format(business))
              #elif _type == 'A':
              #  group = Group.objects.get(name='admins')
              #  group.user_set.add(user)
              else:
                raise Exception(_(u'The user type "{}" is invalid.').format(_type)) #El tipo de usuario "{}" es inválido.
              # user.save()
              print ('Se guardo  el usuario????? FINAL {}'.format(user))
              success = True
              message = MESSAGES_LOGS.get('mensaje57').get(settings.DEFAULT_LANGUAGE_CODE).format(username, _type)
              #message = _(u'User {} added successfully {}').format(username, _type) #Usuario {} agregado exitosamente
              Log.objects.log_action(request, 5, 'C', message, 'U', "")
            else:
              message = MESSAGES_LOGS.get('mensaje58').get(settings.DEFAULT_LANGUAGE_CODE).format(username)
              #message = _(u'User {} already has a previous registration'.format(username)) #El usuario {} ya cuenta con un registro previo
              Log.objects.log_action(request, 5, 'C', message, 'U', "")
          except Exception as e:
            print('Exception user_options => adding user => {}'.format(e))
            message = MESSAGES_LOGS.get('mensaje59').get(settings.DEFAULT_LANGUAGE_CODE)
            #message = _('Registering new user.') #_('Registrando nuevo usuario.')
            Log.objects.log_action(request, 5, 'C', message, 'U', 'Exception user_options => adding user => {}'.format(e))
        except Exception as e:
          print('Exception user_options => validate_email => {}'.format(e))
          message = MESSAGES_LOGS.get('mensaje60').get(settings.DEFAULT_LANGUAGE_CODE)
          #message = _('Invalid email')
          Log.objects.log_action(request, 5, 'C', message, 'U', 'Exception user_options => validate_email => {}'.format(e))
      except Exception as e:
        print("Exception user_options add-user => {}".format(e))
    elif option == 'unlock-user':
      user_id = request.POST.get('user_id')
      user = User.objects.get(id=user_id)
      Profile.objects.filter(user=user).update(status='A')
      user.last_login = datetime.now()
      user.save()
      success = True
      message = _('Unlocked account') #_('Cuenta desbloqueada')
    elif option == 'cancel-unlock':
      user_id = request.POST.get('user_id')  
      user_name = request.POST.get('username')
      user = User.objects.get(id=user_id, username = user_name)
      Profile.objects.filter(user=user).update(status='A')
      success, message = True, _('Account reactivated.') #Cuenta reactivada
  except Exception as e:
    print("Exception user_options general {}".format(e))
    if not message:
      message = MESSAGES_LOGS.get('mensaje61').get(settings.DEFAULT_LANGUAGE_CODE)
      #message = _('An error occurred while performing the operation.') #Ocurrió un error al realizar la operación.
      Log.objects.log_action(request, '5', 'C', message, 'U', "Exception user_options general {}".format(e))


  response.update({
    'success': success,
    'message': message
  })
  return JsonResponse(response)

class RegistrationView(BaseRegistrationView):
  email_body_template_html = "django_registration/activation_email.html"
  email_body_template_string = "django_registration/activation_email_string.txt"
  email_subject_template = "django_registration/activation_email_subject.txt"
  is_provider = True
  account = None
  role = 'C'
  business = ''
  taxpayer_id = ''
  association = False

  from django.http import Http404
  from django.shortcuts import get_object_or_404


  '''def validate_data(self, request, *args, **kwargs):
    self.role = request.GET.get('role')
    self.business = request.GET.get('business')

    if self.role not in ('P', 'S'):
      raise Http404('Role is not allowed')

    if self.business:
      business = get_object_or_404(Business, pk=self.business)
      if business.status != 'A':
        raise Http404('Business no ha pagado')

    if self.role == 'S' and self.request.GET.get('business'):
      raise Http404('URL incorrecta')

    self.taxpayer_id = self.request.POST.get('taxpayer_id')

  def setup(self, request, *args, **kwargs):
    super().setup(request, *args, **kwargs)
    self.validate_data(request, *args, **kwargs)'''

  def recaptcha_validate(self, request):
    import socket
    import urllib
    import json
    from urllib.request import urlopen
    data_response = ''
    try:
      '''if settings.DEBUG:
        data_response = True
        return data_response'''
      captcha = request.POST.get('g-recaptcha-response')
      secret_key = '6Ldfp9gUAAAAALJGJJAMGAu_dZycO45CRL8KQaFW' #Google reCAPTCHA "Secret Key"
      ip = socket.gethostbyname(socket.gethostname()) #Get the IP SERVER
      url = ('https://www.google.com/recaptcha/api/siteverify?secret={}&response={}&ipremote={}').format (secret_key, captcha, ip)

      request = urllib.request.Request(url, None)
      response = urllib.request.urlopen(request)
      response_key = response.read()
      response_key = response_key.decode('utf-8')
      data_response = json.dumps(response_key)

      if 'true' in data_response:
        data_response = True
        return data_response
      if 'false' in data_response:
        data_response = False
        return data_response
    except Exception as e:
      print(("Recaptcha Erro => {}".format (str(e))))
      data_response = False


  def register(self, form):
    try:
      groups = []
      user = form.save(commit = False)
      user.is_active = False
      user.username = self.request.POST.get('email')
      user._email = self.request.POST.get('email')
      user.save()
      #user._taxpayer_id = self.request.POST.get('taxpayer_id')
      group = 'clients'
      group_ = Group.objects.get(name=group)
      groups.append(group_)
      user.groups.set(groups)
      user.profile.role = self.role
      user.profile.group = 'CL'
      user.save()
      user.groups.add(group_)
      self.send_activation_email(user)
      return user
    except Exception as ex:
      print(f'Exception on register: {ex}')
      user = None
      transaction.rollback()
      return JsonResponse({
        "success": False,
        "message": _('An error occurred with the registration') #_("Ocurrio un error con el registro")
      })

  def get_email_context(self, activation_key):
    return {
      'role': self.role,
      'site': get_current_site(self.request),
      'activation_url' : self.request.build_absolute_uri(reverse('activation_key', args=(activation_key,)))
    }

  def send_activation_email(self, user):
    activation_key = self.get_activation_key(user)
    context = self.get_email_context(activation_key)
    subject = render_to_string(self.email_subject_template, context)
    subject = ''.join(subject.splitlines())

    string_message = render_to_string(self.email_body_template_string, context)
    html_message = render_to_string(self.email_body_template_html, context)
    
    kwargs = {'html_message' : html_message}    
    txt_content = ''
    email = user.email
    send_mail(subject, txt_content, settings.SERVER_EMAIL, [email], html_message=html_message, fail_silently=False)

  def get_form_class(self):
    return UserForm

  def get_success_url(self, user):
    return reverse("registro-correcto")

  def form_valid(self, form):
    import re
    password = form.cleaned_data['password']
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!#$%'()*+-.,:;<=>?@[\]^_`{|}~]).{8,16}$"
    errors_response = {}
    if User.objects.filter(username=self.request.POST.get('email')).exists():
      errors_response.update({
        'success': False, 
        'message': MESSAGES_LOGS.get('mensaje62').get(settings.DEFAULT_LANGUAGE_CODE)
        #'message': _(['The User is registered under another account']) #El Usuario se encuentra registrado bajo otra cuenta
      })
      Log.objects.log_action(self.request, 5, 'C','{} {}'.format(errors_response['message'], self.request.POST.get('email')), 'U', '')
      return JsonResponse(errors_response)
    if re.match(regex, password):
      print('Contraseña con Regex correcto')
    else:
      errors_response.update({
        'success': False, 
        'message': MESSAGES_LOGS.get('mensaje63').get(settings.DEFAULT_LANGUAGE_CODE)
        #'message': _(['The password must have at least 8 uppercase, lowercase characters, digits and a special character.']) #La contraseña debe tener al menos 8 carácteres entre mayúsculas, minúsculas, dígitos y un carácter especial.
      })
      Log.objects.log_action(self.request, 5, 'C','{} {}'.format(errors_response['message'], self.request.POST.get('email')), 'U', '')
      return JsonResponse(errors_response)
    data_response = self.recaptcha_validate(self.request)
    if data_response:
      print('reCaptcha CORRECTO')
    else:
      errors_response.update({
        'success': False, 
        'message': MESSAGES_LOGS.get('mensaje64').get(settings.DEFAULT_LANGUAGE_CODE)
        #'message': _(['Select the recaptcha.']) #Seleccione el recaptcha
      })
      Log.objects.log_action(self.request, 5, 'C','{} {}'.format(errors_response['message'], self.request.POST.get('email')), 'U', '')
      return JsonResponse(errors_response)
    super(RegistrationView, self).form_valid(form)
    return JsonResponse({'success':True, 'url': reverse("registro-correcto")})

  def form_invalid(self, form):
    errors = form.errors
    messages = []
    messages.append(errors['email'] if 'email' in errors else None)
    messages.append(errors['password'] if 'password' in errors else None)
    messages.append(errors['password_confirmation'] if 'password_confirmation' in errors else None)
    messages.append(errors['taxpayer_id'] if 'taxpayer_id' in errors else None)
    errors.update({
      'success': False, 
      'message': list(filter(lambda v: v is not None, messages))
    })
    return JsonResponse(errors)
  #return render(request, 'registration/registration_form.html')
class ActivationView(BaseActivateView):
  def get_context_data(self, **kwargs):
    context = super(ActivationView, self).get_context_data(**kwargs)
    context['form'] = ActivationForm
    return context
  
  def get(self, request, *args, **kwargs):
    activation_key = kwargs.get('activation_key', None)
    if activation_key:
      username = self.validate_key(activation_key)
      if username:
        try:
          user = User.objects.get(username=username)
          user.is_active = True
          user.save()
          url = reverse(login)
          url = url + '?activa=t'
        except Exception as e:
          print('1')
          print(f"Exception ActivationView get() | {e}")
        #return HttpResponseRedirect(url, {'success': True, 'message': 'La cuenta se activo satisfactoriamente.'})
        return HttpResponseRedirect(url)
      else:
        return HttpResponseRedirect(url, {'success': False, 'message': _('Activation code is incorrect')}) #El código de activación es incorrecto
    return super(ActivationView, self).get(request, *args, **kwargs)

def send_ticket(user):
  try:
    success, message = False, _('Error..')
    try:
      r_ticket = Ticket.objects.filter(assigned_to_id = user.id, status = 1).last()
    except Exception as e:
      r_ticket = None
    if r_ticket:
      description = _('Dear support partner, {} account reactivation has been requested, for more information check ticket dependencies'.format(user.username))#Estimado compañero de soporte, se ha solicitado la reactivación de la cuenta, para más información revisar las dependencias del ticket
      subject = _('{} Account reactivation request (test)'.format(user.username)) #Solicitud de reactivación de la cuenta {} (prueba)
      ticket_obj = Ticket.objects.create(
        title = subject,
        submitter_email = user.username,
        status = 1,
        description = description,
        priority = '1',
        assigned_to_id = user.id,
        queue_id = 4,
      )
      followup_obj = FollowUp.objects.create(
        title = subject,
        comment = description,
        ticket_id = ticket_obj.id,
        user_id = user.id,
      )
      dependency = TicketDependency.objects.create(
        depends_on_id = r_ticket.id,
        ticket_id = ticket_obj.id
      )
      success, message = True, _('Reactivation email sent')#Correo de reactivacion enviado
  except Exception as e:
    print ("Exception error un send_ticket => ".format(str(e)))
  return success, message

@login_required(login_url='/')
def send_reactivation(request):
  try:
    if request.method == 'POST' and request.is_ajax():
      from django.core.mail import EmailMessage
      action = request.POST.get('action')
      success = False
      username = request.user.username
      #cache.delete('react_{}'.format(username)) ## JUST FOT TEST
      name = '%s %s' % (request.user.first_name, request.user.last_name)
      request_sended = cache.get('react_{}'.format(username), False)
      email = request.user.email
      if not request_sended:
        success, message = send_ticket(request.user)
        if action == 'send' and success:
          url = request.build_absolute_uri(reverse('list_users'))
          email_body = 'registration/reactivation.txt'
          message = ''
          try:
            context = { 'email_from': email, 'name': name, 'url': url }
            html_message = render_to_string(email_body, context)
            kwargs = { 'html_message': html_message }
            sending_mail = EmailMessage(
              _('Reactivation Request'),
              html_message,
              settings.DEFAULT_FROM_EMAIL,
              #['jorgeroque957@gmail.com'],
              ['desarrollo@finkok.com'],
              reply_to = [EmailMessage]
            )
            try:
              sending_mail.content_subtype = 'html'
              sending_mail.send()
              success = True
              message = MESSAGES_LOGS.get('mensaje65').get(settings.DEFAULT_LANGUAGE_CODE)
              #message = _('Reactivation email sent') #_('Correo de reactivación enviado')
              Log.objects.log_action(request, 5, 'C','{} a {}'.format(message,email), 'U', '')
            except Exception as e:
              message = str(e)
          except Exception as e:
            print (str(e))
            send_reactivation.retry(args=[context])
        cache.set('react_{}'.format(username), True, 1800)
      else:
        message = MESSAGES_LOGS.get('mensaje66').get(settings.DEFAULT_LANGUAGE_CODE)
        #message = _('Wait at least 30 minutes to resend the request') #_('Espera al menos 30 minutos para reenviar la solicitud')
        Log.objects.log_action(request, 3, 'R','{} a {}'.format(message,email), 'U', '')
      print (message)
      return JsonResponse({ 'success': success, 'message': message })
  except Exception as e:
    print ("Exception error un send_reactivation => ".format(str(e)))
  return HttpResponseRedirect(reverse('index'))
