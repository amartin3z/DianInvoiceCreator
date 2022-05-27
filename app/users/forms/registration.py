# -*- encoding: utf-8 -*-

from django import forms
from django.db import models
from django.forms import Form
from app.users.models import User
from django.forms import ModelForm


class UserForm(ModelForm):
  
  password = forms.CharField(
    label=('Password'),
    widget=forms.PasswordInput(
      attrs={
        'max_length' : 10,
        'min_length' : 5,
        'placehoder' : 'Contraseña',
        'class' : 'password required form-control ',
        'id' : 'password',
        'name' : 'password',
        'autocomplete' : 'off',
      },
      render_value=True),
  )
  password_confirmation = forms.CharField(
    label=('Password confirmation'),
    widget=forms.PasswordInput(
      attrs={
        'max_length' : 10,
        'min_length' : 5,
        'placehoder' : 'Confirmar contraseña',
        'class' : 'password required form-control',
        'id' : 'password_confirmation',
        'name' : 'password_confirmation',
        'autocomplete' : 'off',
      },
      render_value=True),    
  )
  taxpayer_id = forms.CharField(
    label=('RFC'),
    widget=forms.TextInput(
      attrs={
        'max_length' : 10,
        'min_length' : 5,
        'placehoder' : 'RFC',
        'class' : 'text required form-control ',
        'id' : 'taxpayer_id',
        'name' : 'taxpayer_id',
        'autocomplete' : 'off',
      },),    
  )

  class Meta:
    model = User
    fields = ['email']

  def clean_password(self):
    password = self.cleaned_data['password']
    #self.cleaned_data['password'] = None
    return self.cleaned_data['password']

  def clean_password_confirmation(self):
    password = self.cleaned_data['password']
    password_confirmation = self.cleaned_data['password_confirmation']
    if password and password != password_confirmation:
      raise forms.ValidationError(
        'Contraseñas no coiciden.'
      )
    return password_confirmation

  def clean_username(self):
    username = self.clean_username['email']
    try:
      User.objects.get(username__iexact=username)
    except User.DoesNotExist:
      self.clean_username['email'] = None
      return username
    raise forms.ValidationError("Usuario previamente registrado")

  def clean_taxpayer_id(self):
    taxpayer_id = self.cleaned_data['taxpayer_id']
    self.cleaned_data['taxpayer_id'] = None
    return taxpayer_id

  def save(self, commit=True):
    #import pdb; pdb.set_trace()
    user = super(UserForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password'])
    user.email = self.cleaned_data['email']
    user._taxpayer_id = self.cleaned_data['taxpayer_id']
    if commit:
      user.save()
    return user
"""
class RegistrationForm(Form):
  activation_key = forms.CharField(
    label=(u'Código'),
    max_length=40,
    required=True,
    widget=forms.TextInput(
      attrs={
        'max_length' : 40,
        'class' : 'text required form-control',
        'placeholder' : u'Ingresa tu código de activación'
      }),
      error_messages = {
        'required' : (u'El código de activación es requerido'),
        'max_length' : (u'El código de activación tiene más de 40 caracteres')
      }
  )
"""
class ActivationForm(Form):
  activation_key = forms.CharField(
    label=(u'Código'),
    max_length=40,
    required=True,
    widget=forms.TextInput(
      attrs={
        'max_length' : 40,
        'class' : 'text required form-control',
        'placeholder' : u'Ingresa tu código de activación'
      }),
      error_messages = {
        'required' : (u'El código de activación es requerido'),
        'max_length' : (u'El código de activación tiene más de 40 caracteres')
      }
  )
