# -*- encoding: UTF-8 -*-
from .local import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'unnamedpac',
        'USER' : 'unnamedpac',
        'PASSWORD': 'unnamedpac',
        'HOST' : 'localhost',
        'PORT' : '',
    },
}


CACHES = {
    'default': {
        'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION':'127.0.0.1:11211',
    },
    'sat_catalogos': {
        'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION':'10.2.11.82:11211',
    }
}


STORAGE_PATH = Path('/data/soriana')