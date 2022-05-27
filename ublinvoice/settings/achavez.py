# -*- encoding: UTF-8 -*-
from .local import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'soriana',
        'USER': 'soriana',
        'PASSWORD': 'soriana',
        'HOST': 'localhost',
        'PORT': '',
    },
}

