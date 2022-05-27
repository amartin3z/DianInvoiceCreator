# -*- encoding: UTF-8 -*-
from .local import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME' : 'soriana',
        'USER' : 'soriana',
        'PASSWORD': 'soriana',
        'HOST' : 'localhost',
        'PORT' : '5432',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    }
}

DEBUG = False

ALLOWED_HOSTS = [
  'soriana-demo.finkok.com:8053',
  'soriana-demo.finkok.com',
]

CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True

#SFTP
SFTP_PATH = Path('/var/sftp/soriana')
SFTP_PATH_DUPLICATED = Path(SFTP_PATH, 'duplicated')
SFTP_PATH_ENTRADA = Path(SFTP_PATH, 'entrada')
SFTP_PATH_ERROR = Path(SFTP_PATH, 'error')
SFTP_PATH_SALIDA = Path(SFTP_PATH, 'salida')
SFTP_PATH_UNZIPPED = Path(SFTP_PATH, 'unzipped')
SFTP_PATH_UPLOADS = Path(SFTP_PATH, 'uploads')
SFTP_PATH_XML = Path(SFTP_PATH, 'xml')

#REDIS
BROKER_URL = 'redis://:demoHer$L1F3@127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://:demoHer$L1F3@127.0.0.1:6379'
CELERY_IMPORTS = ("app.providers.tasks",)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Mexico_City'
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

