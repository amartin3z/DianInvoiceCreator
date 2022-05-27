# -*- encoding: UTF-8 -*-
from .local import *

BASE_DIR = Path(__file__).ancestor(3)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'ublinvoice',
        'USER' : 'unnamedpac',
        'PASSWORD': 'CambiaMe1$',
        'HOST' : 'localhost',
        'PORT' : '',
    },
}

# WORK_DIR = '/tmp/data/soriana'
# SFTP_PATH = Path(WORK_DIR, 'SFTP')
# SFTP_PATH_ENTRADA = Path(SFTP_PATH, 'ENTRADA')
# SFTP_PATH_PROCESADOS = Path(SFTP_PATH, 'PROCESADOS')
# SFTP_PATH_REPROCESADOS = Path(SFTP_PATH, 'REPROCESADOS')
# SFTP_PATH_ERRONEOS = Path(SFTP_PATH, 'ERRONEOS')
# SFTP_PATH_ERRONEOS_DB = Path(SFTP_PATH_ERRONEOS, 'DB')
# SFTP_PATH_CFDI = Path(SFTP_PATH, 'CFDI')

### STORAGE
STORAGE_PATH = Path('/tmp/data/soriana/')
STORAGE_DOWNLOAD = Path(STORAGE_PATH, 'download')
LOGOS_PATH = Path(STORAGE_PATH, 'logo/')

MEDIA_ROOT = LOGOS_PATH
MEDIA_URL = os.path.join(LOGOS_PATH)
WIZARD_MIDDLEWARE = False

DEBUG = True
VERIFY_SESSION = True

CACHES = {
	'default': {
	 	'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': '127.0.0.1:11211',
	}
}

#--[smtp_email]-->
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '5b671e13a6549e'
EMAIL_HOST_PASSWORD = '2216ffb75934d6'
EMAIL_PORT = '2525'

REGISTRATION_DEFAULT_FROM_EMAIL = 'lalonso@finkok.com.mx'
# SITE_ID = 2

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'conf/locale/'),
)
