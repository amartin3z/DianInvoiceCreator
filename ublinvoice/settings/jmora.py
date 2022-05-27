# -*- encoding: UTF-8 -*-
from .local import *
from django.conf import settings
from unipath import Path
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moroco',
        'USER': 'moroco',
        'PASSWORD': 'moroco',
        'HOST': 'localhost',
        'PORT': '',
    },
}

WIZARD_MIDDLEWARE = False

DEBUG = True
CACHES = {
    'default': {
       'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
       'LOCATION':'127.0.0.1:11211',
   }
}

SESSION_ENGINE ='django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS =  "default"

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

STORAGE_PATH = Path('/var/unnamedpac')
STORAGE_DOWNLOAD = Path(STORAGE_PATH, 'download')
LOGOS_PATH = Path(STORAGE_PATH, 'logo')

MEDIA_URL = '/media/'
MEDIA_ROOT = LOGOS_PATH

USE_TZ = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '45cc588acc65e9'
EMAIL_HOST_PASSWORD = 'eed669d3db5fc2'
EMAIL_PORT = 2525
EMAIL_USE_TLS = False
TO_EMAIL = ' 1f9b18d88b-8a3149@inbox.mailtrap.io'
ENTERPRICE_EMAIL = '<prueba@miempresa.com.mx>'

USER_EMAIL = ('jesuslive1970@gmail.com', )
CCO_EMAIL = ('samle961222@hotmail.com', )
