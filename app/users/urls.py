# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path, re_path
from .views import logout, login, list_users, user_options, send_reactivation, password_reset_confirm
from app.core.views import wizard, wizard_stuff, blocked
from django.contrib.auth import views as auth_views
from .views import RegistrationView, ActivationView
from django.views.generic import TemplateView

urlpatterns = [
  url(u'login/$', login, name='login'),
  url(u'^logout/$', logout, name='logout'),
  # url(u'^home/$', home, name='home'),
  url(u'^users/$', list_users, name='list_users'),
  url(u'^wizard/$', wizard, name="wizard"),
  url(u'^wizard/stuff/$', wizard_stuff, name="wizard_stuff"),
  #url(u'^users/(?P<status>[A|S])+/$', list_users, name='list_users'),
  url(u'^users/options$', user_options, name='user_options'),
  re_path('registry/', RegistrationView.as_view(), name='registration'),
  #re_path('registration/form/', RegistrationForm.as_view(), name='registration_key'),
  path('registry-success/', TemplateView.as_view(template_name='registration/success.html'), name='registro-correcto'),
  re_path('activate/(?P<activation_key>[-:\w]+)/', ActivationView.as_view(), name='activation_key'),
  #url(u'recaptcha_validate$', recaptcha_validate, name='recaptcha_validate'),
  #re_path('^recaptcha_validate$', recaptcha_validate, name='recaptcha_validate'),
  url(u'^blocked/$', blocked, name='blocked'),
  url(u'^reactivation/$', send_reactivation, name='send_reactivation'),
  url(r'^resetpassword/new-password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, name = 'password_reset_confirm'),
  url(u'^resetpassword/$', auth_views.PasswordResetView,
    {
        'template_name': 'users/password_reset/reset.html',
        'email_template_name': 'users/password_reset/password_reset.txt',
        'html_email_template_name': 'users/password_reset/email.html',
        'subject_template_name': 'users/password_reset/subject.txt'
    },
    name='password_reset'),
]