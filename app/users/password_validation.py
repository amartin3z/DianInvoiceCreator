# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
import string


class CustomPasswordValidator:
    
    def __init__(self, min_length=8):
        self.min_length = min_length
        self.has_upper = False
        self.has_lower = False
        self.has_number = False
        self.has_special = False

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError('La contraseña debe contener al menos 8 caracteres.', code='password_too_short')

        if not any(c.isupper() for c in password):
            raise ValidationError('La contraseña debe contener al menos 1 mayúscula.', code='password_not_upper')

        if not any(c.islower() for c in password):
            raise ValidationError('La contraseña debe contener al menos 1 minúscula.', code='password_not_lower')

        if not any(c.isdigit() for c in password):
            raise ValidationError('La contraseña debe contener al menos 1 número.', code='password_not_number')

        if not any(c.isdigit() for c in password):
            raise ValidationError('La contraseña debe contener al menos 1 número.', code='password_not_number')

        if not any(c in string.punctuation for c in password):
            raise ValidationError('La contraseña debe contener al menos 1 caracter especial ({}).'.format(string.punctuation), code='password_not_number')

    def get_help_text(self):
        return 'La contraseña debe contener al menos 8 caracteres, 1 mayúscula, 1 minúscula, 1 número, 1 caracter especial ({})'.format(string.punctuation)