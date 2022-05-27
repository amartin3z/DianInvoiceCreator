# -*- encoding: UTF-8 -*-
from .local import *

STATIC_URL = '/static/'
DJANGO_ROOT = ''
### STORAGE
STORAGE_PATH = Path('/data/soriana')
STORAGE_DOWNLOAD = Path(STORAGE_PATH, 'download')
MEDIA_ROOT = STORAGE_PATH
LOGOS_PATH = Path(STORAGE_PATH, 'logo')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'ublinvoice3',
        'USER' : 'wis',
        'PASSWORD': 'ChangeMe1$',
        'HOST' : 'localhost',
        'PORT' : '',
    },
}

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
    LOGOS_PATH
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

LOGIN_REDIRECT_URL = '%s/app/' % DJANGO_ROOT
SESSION_CACHE_ALIAS =  "default"