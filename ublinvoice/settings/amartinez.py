# -*- encoding: UTF-8 -*-
from .local import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'ublinvoice_db',
        'USER' : 'ublinvoice_user',
        'PASSWORD': 'ChangeMe1$.',
        'HOST' : 'localhost',
        'PORT' : '',
    },
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

SESSION_COOKIE_AGE = 60000

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'conf/locale/'),
)