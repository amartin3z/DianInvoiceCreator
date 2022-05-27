# -*- encoding: UTF-8 -*-
from .local import *

DJANGO_ROOT = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'morocco',
        'USER' : 'unnamedpac',
        'PASSWORD': 'ChangeMe1$',
        'HOST' : 'localhost',
        'PORT' : '',
    },
}


CACHES = {
    'default': {
        'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION':'127.0.0.1:11211',
    }
}

STORAGE_PATH = Path('/var/unnamedpac')
STORAGE_DOWNLOAD = Path(STORAGE_PATH, 'download')
LOGOS_PATH = Path(STORAGE_PATH, 'logo')

#SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_COOKIE_HTTPONLY = True
#SESSION_COOKIE_AGE = 300
#SESSION_SAVE_EVERY_REQUEST = True

#if LOCALDEV:
#  DJANGO_ROOT = ''
#  SESSION_COOKIE_DOMAIN = None
#  SESSION_COOKIE_SECURE = False
#  CSRF_COOKIE_DOMAIN = None
SESSION_ENGINE ='django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS =  "default"
###############################################################################
## Authentication
###############################################################################
LOGIN_REDIRECT_URL = '%s/app/' % DJANGO_ROOT
