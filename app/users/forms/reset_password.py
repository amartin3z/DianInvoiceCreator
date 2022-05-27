# -*- coding: utf-8 -*-
from django import forms

class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Cuenta de correo"), max_length=254)

class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': (u"Las contraseñas no coinciden"),
        }
    new_password1 = forms.CharField(label=(u"Nueva Contraseña"), widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=(u"Repetir Contraseña"), widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                    )
        return password2