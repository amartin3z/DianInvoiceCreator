# -*- encoding: UTF-8 -*-
from .local import *

BROKER_URL = 'redis://:pass@127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://:pass@127.0.0.1:6379'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'marruecosdb',
        'USER' : 'marruecos',
        'PASSWORD': 'ChangeMe1$.',
        'HOST' : 'localhost',
        'PORT' : '',
    },
}

WORK_DIR = '/tmp/data/soriana'
SFTP_PATH = Path(WORK_DIR, 'SFTP')
SFTP_PATH_ENTRADA = Path(SFTP_PATH, 'ENTRADA')
SFTP_PATH_PROCESADOS = Path(SFTP_PATH, 'PROCESADOS')
SFTP_PATH_REPROCESADOS = Path(SFTP_PATH, 'REPROCESADOS')
SFTP_PATH_ERRONEOS = Path(SFTP_PATH, 'ERRONEOS')
SFTP_PATH_ERRONEOS_DB = Path(SFTP_PATH_ERRONEOS, 'DB')
SFTP_PATH_CFDI = Path(SFTP_PATH, 'CFDI')

### STORAGE
STORAGE_PATH = Path('/tmp/data/soriana/')
STORAGE_DOWNLOAD = Path(STORAGE_PATH, 'download')
LOGOS_PATH = Path(STORAGE_PATH, 'logo/')

MEDIA_ROOT = LOGOS_PATH
MEDIA_URL = os.path.join(LOGOS_PATH)
WIZARD_MIDDLEWARE = True

CACHES = {
	'default': {
	 	'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': '127.0.0.1:11211',
	}
}

SESSION_EXPIRE_SECONDS = 3600  # 1 hour
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60 # group by minute

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '58ccc7fa683785'
EMAIL_HOST_PASSWORD = '0771678a7448d7'
EMAIL_PORT = 2525
EMAIL_USE_TLS = False
SERVER_EMAIL = ' <noreply@benamedic.com.mx>'
ACCOUNT_ACTIVATION_DAYS = 7