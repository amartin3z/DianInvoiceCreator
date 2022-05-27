# -*- encoding: UTF-8 -*-
from .local import *

BROKER_URL = 'redis://:pass@127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://:pass@127.0.0.1:6379'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'moroco',
        'USER' : 'moroco',
        'PASSWORD': 'moroco',
        'HOST' : 'localhost',
        'PORT' : '',
    },
}

CACHES = {
    'default': {
       'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
       'LOCATION':'127.0.0.1:11211',
   },
}


### STORAGE
STORAGE_PATH = Path('/var/unnamedpac')
STORAGE_DOWNLOAD = Path(STORAGE_PATH, 'download')
LOGOS_PATH = Path(STORAGE_PATH, 'logo')

MEDIA_URL = '/media/'
MEDIA_ROOT = LOGOS_PATH

DEFF_SALT="salt" 
DEFF_PASSWORD="password"

VERBOSE_EXTRA_VALIDATIONS = True

VERIFY_SESSION = False
