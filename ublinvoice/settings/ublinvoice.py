# -*- encoding: UTF-8 -*-
from .local import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME' : 'ublinvoice',
        'USER' : 'ublinvoice',
        'PASSWORD': '1nvo1c3#UBL',
        'HOST' : '127.0.0.1',
        'PORT' : '5432',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    }
}

DEBUG = True

ALLOWED_HOSTS = [
  '10.0.5.124',
  '72.172.186.24',
  'ciat-maroc.finkok.com', 
  'ciat-morroco.finkok.com', 
  'ciat-facturamorroco.finkok.com', 
  'maroc.finkok.com',
  #'demo-unnamedpac.com',
  #'72.172.186.21',
  #'app.finkok.com',
]

BROKER_URL = 'redis://@127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_IMPORTS = ("app.invoicing.tasks",)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Mexico_City'
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
#CELERY_QUEUE_NAME = 'unnamedpac'

WIZARD_MIDDLEWARE = True


UNNAMEDPAC_STORAGE_PATH = Path('/var/marruecos')

STATIC_ROOT = UNNAMEDPAC_STORAGE_PATH.child('static')
STATIC_URL = '/static/'

MEDIA_ROOT = UNNAMEDPAC_STORAGE_PATH.child('media')
MEDIA_URL = '/media/'

MANIFEST_STORAGE = UNNAMEDPAC_STORAGE_PATH.child('storage')

STORAGE_DOWNLOAD = UNNAMEDPAC_STORAGE_PATH.child('download')
#LOGOS_PATH = UNNAMEDPAC_STORAGE_PATH.child('logo')
LOGOS_PATH = MEDIA_ROOT.child('logo')
STORAGE_PATH = UNNAMEDPAC_STORAGE_PATH

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
    LOGOS_PATH
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_HTTPONLY = True
#SESSION_COOKIE_AGE = 1440
SESSION_COOKIE_AGE = 4320
SESSION_SAVE_EVERY_REQUEST = True


