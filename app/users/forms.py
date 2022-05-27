# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, MultiField, Field, Row, MultiWidgetField, Column
from app.users.password_validation import CustomPasswordValidator


class CustomRegistrationForm(forms.Form):
    email = forms.EmailField(label='Usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'autocomplete': 'off',
        }
    ))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(
        attrs={
            'autocomplete': 'off',
        }
    ))

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("El usuario ya existe.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")

        password_validator = CustomPasswordValidator()
        password_validator.validate(password2)
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)

        self.helper_form = FormHelper()
        self.helper_form.wrapper_class = 'form-group'

        self.helper_form.layout = Layout(
                Div('email', css_class='mx-auto col-lg-8'),
                Div('password1', css_class='mx-auto col-lg-8'),
                Div('password2', css_class='mx-auto col-lg-8'),
        )

        self.helper_form.add_input(Submit('submit', 'Registrar', css_class='col-lg-2 offset-lg-5'))