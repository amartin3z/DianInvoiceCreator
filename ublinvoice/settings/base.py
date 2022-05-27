# -*- encoding: UTF-8 -*-
import os
from unipath import Path
#from lxml import etree
#import libxml2
#import libxslt
### CELERY 
from celery.schedules import crontab
from kombu import Queue, Exchange

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).ancestor(3)
SECRET_KEY = 'v!v*(%f9yles&xa!zz#15lwr@kw#^o!=2hhi_w!2wj(o%o5d7o'

DEBUG = True
LOCALDEV = True

ALLOWED_HOSTS = [
  'localhost',
  '*',
]

ADMINS = (
  ('Desarrollo Finkok', 'desarrollo@finkok.com'),
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
)

LOCAL_APPS = (
  'app.core',
  'app.users',
  'app.invoicing',
  'app.cancel',
  'app.support',
  'app.sat',
  'app.cfdi',
  'app.peppol',
)

THIRDPARTY_APPS = (
  'django_celery_beat',
  'crispy_forms',
  #'registration',
  'multiselectfield',
  'markdown_deux',
  'bootstrapform',
  'helpdesk',
  'sequences.apps.SequencesConfig'
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRDPARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.core.middleware.wizard_middleware',
    'app.core.middleware.blocked_middleware',
    'app.core.middleware.CustomSessionMiddleware',
]

ROOT_URLCONF = 'ublinvoice.urls'

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
  },    
  {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
  },
  {
    'NAME': 'app.users.password_validation.CustomPasswordValidator',
  },
]

TEMPLATES_DIR = Path(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.core.context_processors.business.business',
                # 'app.core.context_processors.faq.faq',
            ],

        },
    },
]

WSGI_APPLICATION = 'ublinvoice.wsgi.application'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

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

SAT_RECEPCION = True
SAT_CANCELACION = True
SAT_CERT_STR = """MIIF4jCCA8qgAwIBAgIUMjAwMDEwMDAwMDAzMDAwMjIzMjMwDQYJKoZIhvcNAQEL
BQAwggFmMSAwHgYDVQQDDBdBLkMuIDIgZGUgcHJ1ZWJhcyg0MDk2KTEvMC0GA1UE
CgwmU2VydmljaW8gZGUgQWRtaW5pc3RyYWNpw7NuIFRyaWJ1dGFyaWExODA2BgNV
BAsML0FkbWluaXN0cmFjacOzbiBkZSBTZWd1cmlkYWQgZGUgbGEgSW5mb3JtYWNp
w7NuMSkwJwYJKoZIhvcNAQkBFhphc2lzbmV0QHBydWViYXMuc2F0LmdvYi5teDEm
MCQGA1UECQwdQXYuIEhpZGFsZ28gNzcsIENvbC4gR3VlcnJlcm8xDjAMBgNVBBEM
BTA2MzAwMQswCQYDVQQGEwJNWDEZMBcGA1UECAwQRGlzdHJpdG8gRmVkZXJhbDES
MBAGA1UEBwwJQ295b2Fjw6FuMRUwEwYDVQQtEwxTQVQ5NzA3MDFOTjMxITAfBgkq
hkiG9w0BCQIMElJlc3BvbnNhYmxlOiBBQ0RNQTAeFw0xNjA3MjkyMzE1MzJaFw0y
MDA3MjkyMzE1MzJaMIHOMSIwIAYDVQQDExlBWlVMIFNJTiBMSU1JVEVTIFNBIERF
IENWMSIwIAYDVQQpExlBWlVMIFNJTiBMSU1JVEVTIFNBIERFIENWMSIwIAYDVQQK
ExlBWlVMIFNJTiBMSU1JVEVTIFNBIERFIENWMSUwIwYDVQQtExxEQUwwNTA2MDFM
MzUgLyBGVUFCNzcwMTE3QlhBMR4wHAYDVQQFExUgLyBGVUFCNzcwMTE3TURGUk5O
MDkxGTAXBgNVBAsUEFBBQyBDRkRJX1BSVUVCQVMwggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCuhhm16MtcFTmOaqVJiK4rb4Dyt+wTV23JCo5UcVmvUJnJ
lSaNWau7dbW4PQaBsxLLu2HDVCJ+X0GxsWo3Z+kJ/28yEu6k+WNGyYBFZy0APNzX
kEH7fAKNKiInJ7gGyyWHHzeurUfP7XyTI9JOQoM+xXDxJu2LkIU/T8vaaXRlWzVQ
iMIT2Rx4CsZ5/lqsTZmvOq/QuDZo0KHj1jN66KC3AATF2Aq+Xnlswrkhtd7zt4fh
/3wVS9NEYxeDtHtctwQTUeHwl7Ji3VA7qD/pPZ48Sb6QAun6HZTx4zX8s3t4j5yz
/30t3mBsAX/CqbON5rhQs8nGVyRNjswVCM2Y7ILvAgMBAAGjHTAbMAwGA1UdEwEB
/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQADLbB3nGXh5g+v
qDiuMtzay7MtOrquzr7S+tZbi0SleNx5yjnqBvZB+iQg4V67hsQG/SfOFuFW0of1
tYSTztXQCJKcTqZgAsvX6JaPf3hcVfxgY1KMZYsP8siFkpL8RY0oBcEFKoOWpFH0
8xRO+mADl1xJV7t8E20+ytPvixK5vJqgoeN2gKYihsde7DD8imEU3M3IWbLqdqF9
B1zZDFHcVyY86Db7D/HeTMF5RgC5waYLNk+ymD1z65M0SaRYTMUKbfiZq7SZ0gSI
LzuZd0jXdatT3lpoV+79VPmdlSnc/wZzArohoW07CkvpXM+reWdIDRSOGJU5AxlH
+dO18z8dbTFvKJlHn4JEJwV3VP61gvn5bGpgf2njkM1TmJTibNOJHMq6bTnrKKhC
Xg9aetA78OgJeIzDtqTEhSNayMZL3ELRIJkuEOn+R3vu/3au0NpXz2RuOY2W8/7R
AsR2seN6W+KAd2G3PscgtHMHURi8394CxlkJ4tThfq+NEVTwowmoSRMN4wsOeCQO
ize2Cj/nSyX3s++XcQ2pF41HJ2F8Ici4VBZBjpp7kvMdRpLvezpxXkIaYH8nr4Qq
y6I4Hn2//xHlQGd3FrQ+8e4NYjCPF9y9ulIrmrLSmy4UCt/igZgg6nbvK2XiyIGe
gLDXJzpBHcfMGga4HtCGmWmpDh+HJg=="""
SAT_AUTENTICA_URL_R = 'https://pruebacfdirecepcion.cloudapp.net/Seguridad/Autenticacion.svc?wsdl'
SAT_AUTENTICA_URL_C = 'https://pruebacfdicancelacion.cloudapp.net/Autenticacion/Autenticacion.svc?wsdl'
SAT_CONSULTA_URL = 'https://pruebacfdiconsultaqr.cloudapp.net/ConsultaCFDIService.svc?wsdl'
SAT_CANCELA_URL = 'https://pruebacfdicancelacion.cloudapp.net/Cancelacion/CancelaCFDService.svc?wsdl'
SAT_RECIBE_URL = 'https://pruebacfdirecepcion.cloudapp.net/Recepcion/CFDI33/RecibeCFDIService.svc?wsdl'

SAT_BLOB_ACCOUNT = 'certificacionpac'
SAT_BLOB_CONTAINER = 'certificacionpac'
SAT_BLOB_SHARE_ACCESS_SIGNATURE = '?sr=c&si=WriteOnly&sig=eUe%2Fe7kcFcmiIzOVNgqbXd%2BjlIN3ZQd8fkQq3IsHQVQ%3D'
SAT_BLOB_URL = f'http://{SAT_BLOB_ACCOUNT}.blob.core.windows.net/{SAT_BLOB_CONTAINER}/{{filename}}{SAT_BLOB_SHARE_ACCESS_SIGNATURE}'
SAT_BLOB_PATH = f'http://{SAT_BLOB_ACCOUNT}.blob.core.windows.net/{SAT_BLOB_CONTAINER}/{{filename}}'
SAT_BLOB_HOST = f'{SAT_BLOB_ACCOUNT}.blob.core.windows.net'

SAT_GET_CERTIFICATES = 'TODOADDURL_SAT_DOWNLOAD_CERTIFICATE' 

STATIC_URL = '/static/'
CERTIFICATE_STORAGE = Path(BASE_DIR, 'cfdi', 'sat_certificados')

INVOICE_STORAGE = Path(BASE_DIR, 'tmp/')
STORAGE_PATH = Path('/var/marruecos/media')
LOGOS_PATH = Path(STORAGE_PATH, 'logo')
MEDIA_ROOT = LOGOS_PATH
STATIC_DIR = Path(BASE_DIR, 'static')
MEDIA_URL = '/media/'

WS_USERNAME = 'jantonioperez24@gmail.com'
WS_PASSWORD = 'diFerence25$'
WS_URL = 'https://demo-facturacion.finkok.com/servicios/soap/validation.wsdl'
WS_URL_LCO = 'https://demo-facturacion.finkok.com/servicios/soap/lco.wsdl'
WS_URL_SATINC = 'https://demo-facturacion.finkok.com/servicios/soap/satinc.wsdl'

FOREIGN_TAXPAYER = 'XEXX010101000'

URL_C69 = 'http://omawww.sat.gob.mx/cifras_sat/Documents/Listado_Completo_69.csv'
URL_C69B = 'http://omawww.sat.gob.mx/cifras_sat/Documents/Listado_Completo_69-B.csv'
URL_LGTAIP = 'http://omawww.sat.gob.mx/cifras_sat/Documents/Listado_completo_cancelados%20y%20condonados.csv'

## EMAIL SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST = '10.0.3.12'
EMAIL_HOST_USER = 'proveedor'
EMAIL_HOST_PASSWORD = 'g2dMRg99wauf'
EMAIL_PORT = 587
#SERVER_EMAIL = '<noreply@superportal.lacomer.com>'
#DEFAULT_FROM_EMAIL = '<superportal@lacomer.com>'
SERVER_EMAIL = '<noreply@ublinvoice.com>'
DEFAULT_FROM_EMAIL = '<noreply@ublinvoice.com>'

## IMAP SETTINGSSTORAGE_PATH
IMAP_USERNAME = 'facturacion@finkok.com.mx'
IMAP_PASSWORD = 'Wholet5theDogou7'
TAXPAYER_ID_LIST = [
  'TCM970625MB1',
  'CCF121101KQ4',
]

## DJANGO-HELPDESK SETTINGS
HELPDESK_DEFAULT_SETTINGS = {
  'use_email_as_submitter': True,
  'email_on_ticket_assign': True,
  'email_on_ticket_change': True,
  'login_view_ticketlist': True,
  'tickets_per_page': 25
}
HELPDESK_KB_ENABLED = False
HELPDESK_REDIRECT_TO_LOGIN_BY_DEFAULT = True
HELPDESK_FOLLOWUP_MOD = True
HELPDESK_VIEW_A_TICKET_PUBLIC = True
HELPDESK_SUBMIT_A_TICKET_PUBLIC = True
HELPDESK_ALLOW_NON_STAFF_TICKET_UPDATE = False
HELPDESK_UPDATE_PUBLIC_DEFAULT = False
HELPDESK_EMAIL_FALLBACK_LOCALE = "es"
HELPDESK_STAFF_ONLY_TICKET_CC = True


## REGISTRATION SETTINGS
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_DEFAULT_FROM_EMAIL = 'registration@lacomer.com'
REGISTRATION_ADMINS = (('Alfredo Herrejon', 'aherrejon@finkok.com'),('Desarrollo Finkok', 'desarrollo@finkok.com'),)
REGISTRATION_FORM = 'app.users.forms.CustomRegistrationForm'
REGISTRATION_EMAIL_HTML = True
SEND_EMAIL_ON_PROVIDER_CREATION = True
SEND_EMAIL_ON_AGENT_CREATION = True
SEND_EMAIL_ON_RECEIVER_CREATION = True

SITE_ID = 1

# BUSINESS SORIANA
BUSINESS = (
  'TCM970625MB1',
  'CCF121101KQ4',
)

APPLY_ASYNC = False

BROKER_URL = 'redis://:guest@127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://:guest@127.0.0.1:6379'
CELERY_IMPORTS = ("app.invoicing.tasks",)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Mexico_City'
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERY_QUEUE_NAME = 'ublinvoice'

CELERYBEAT_SCHEDULE = {}

ADMIN_URL = 'admin'
SFTP_SEND_EMAIL = False
EMAIL_ATTACHED_ZIP = False

EMAIL_DOMAIN = 'lacomer.com.mx'

URL_C69 = 'http://omawww.sat.gob.mx/cifras_sat/Documents/Listado_Completo_69.csv'
URL_C69B = 'http://omawww.sat.gob.mx/cifras_sat/Documents/Listado_Completo_69-B.csv'
URL_LGTAIP = 'http://omawww.sat.gob.mx/cifras_sat/Documents/Listado_completo_cancelados%20y%20condonados.csv'

import locale
locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')

DIOT_QUERY_CSV = u'''COPY(SELECT 
billing_diotdetail.c1_t_tercero  as "Tipo Tercero",
billing_diotdetail.c2_t_operacion  as "Tipo Operación",
billing_diotdetail.c3_rfc  as "Rfc Proveedor",
billing_diotdetail.c4_id_fiscal  as "Identificación Fiscal",
billing_diotdetail.c5_nom_extranjero  as "Nombre Extranjero",
billing_diotdetail.c6_pais_residencia  as "País Residencia",
billing_diotdetail.c7_nacionalidad  as "Nacionalidad",
billing_diotdetail.c8_aa_15_16_iva  as "Valor de los actos o actividades pagados a la tasa del 15%% ó 16%% ",
billing_diotdetail.c9_aa_15_iva  as "Valor de los actos o actividades pagados a la tasa del 15%% de IVA ",
billing_diotdetail.c10_monto_na_15_16_iva  as " Monto del IVA pagado no acreditable a la tasa del 15%% ó 16%% ",
billing_diotdetail.c11_aa_10_11_iva  as "Valor de los actos o actividades pagados a la tasa del 10%% u 11%% de IVA",
billing_diotdetail.c12_aa_10_iva  as "Valor de los actos o actividades pagados a la tasa del 10%% ",
billing_diotdetail.c13_aa_8_iva  as "Valor de los actios o actividades pagados a la tasa del 8%% ",
billing_diotdetail.c14_monto_na_10_11_iva  as "Monto del IVA pagado no acreditable a la tasa del 10%% u 11%% ",
billing_diotdetail.c15_monto_na_8_iva  as "Monto del IVA pagado no acreditable 8%% ",
billing_diotdetail.c16_aa_importacion_15_16_iva  as "Valor de los actos o actividades pagados en la importación de bienes y servicios a la tasa del 15%% ó 16%% de IVA",
billing_diotdetail.c17_monto_na_importacion_15_16_iva  as "Monto del IVA pagado no acreditable por la importacion a la tasa del 15%% ó 16%% ",
billing_diotdetail.c18_aa_importacion_10_11_iva  as "Valor de los actos o actividades pagados en la importacion de bienes y servicios a la tasa del 10%% u 11%% de IVA",
billing_diotdetail.c19_monto_na_importacion_10_11_iva  as "Monto del IVA pagado no acreditable por la importacion a la tasa del 10%% u 11%% (Correspondiente en la proporcion de las deducciones autorizadas)",
billing_diotdetail.c20_aa_0_iva  as "Valor de los demás actos o actividades pagados a la tasa del 0%% de IVA", 
billing_diotdetail.c21_aa_exento_iva  as "Valor de los actos o actividades pagados por los que no se pagará el IVA (Exentos)",
billing_diotdetail.c22_iva_retenido  as "IVA Retenido por el contribuyente",
billing_diotdetail.c23_iva_dev_desc_bon  as " IVA correspondiente a las devoluciones, descuentos y bonificaciones sobre compras" 
from billing_diotdetail LEFT JOIN billing_diot ON (billing_diotdetail.diot_id=billing_diot.id) WHERE "billing_diot"."business_id"=%(business_id)s and "billing_diotdetail"."diot_id"=%(diot_id)s order by billing_diotdetail.c3_rfc) TO STDOUT WITH CSV HEADER DELIMITER ',';
'''


WIZARD_MIDDLEWARE = True

####################################
########### CFDI SECTION ###########
import M2Crypto
import os
SAT_ROOT_CERTS = []
if LOCALDEV:
  ROOT_CERTS_PATH = Path(BASE_DIR, 'app', 'sat', 'files', 'rootcerts', 'Pruebas')
else:
  ROOT_CERTS_PATH = Path(BASE_DIR, 'app', 'sat', 'files', 'rootcerts', 'Produccion')
for root_cert in os.listdir(ROOT_CERTS_PATH):
  cert_flag = False
  if os.path.isfile(os.path.join(ROOT_CERTS_PATH, root_cert)):
    try:
      ca_root = M2Crypto.X509.load_cert("%s/%s" % (ROOT_CERTS_PATH, root_cert), M2Crypto.X509.FORMAT_DER)
      cert_flag = True
    except M2Crypto.X509.X509Error:
      ca_root = M2Crypto.X509.load_cert("%s/%s" % (ROOT_CERTS_PATH, root_cert), M2Crypto.X509.FORMAT_PEM)
      cert_flag = True
    except Exception as e:
      print(e)
      continue
    finally:
      if cert_flag:
        SAT_ROOT_CERTS.append(ca_root.get_pubkey())

from lxml import etree
CFDI_VERSION = '3.3'
XSD_NAME = 'cfdv33.xsd'
XSLT_NAME = "cadenaoriginal_3_3.xslt"
XSD_PATH = Path(BASE_DIR, 'app', 'sat', 'files', CFDI_VERSION, 'xsd')
XSD_FILE = Path(XSD_PATH, XSD_NAME)
XSD_STR = XSD_FILE.read_file()
XSD_STR = XSD_STR.replace('{{XSD_PATH}}', XSD_PATH)
XSD_SCHEMA_ROOT = etree.XML(XSD_STR)
XSD_SCHEMA = etree.XMLSchema(XSD_SCHEMA_ROOT)
XSD_PARSER = etree.XMLParser(schema=XSD_SCHEMA)

XSLT_PATH = Path(BASE_DIR, 'app', 'sat', 'files', CFDI_VERSION, 'xslt')
XSLT_PATH_FILE = Path(XSLT_PATH, XSLT_NAME)
XSLT_STR = XSLT_PATH_FILE.read_file('rb')
XSLT_STR = XSLT_STR.replace(b'{{XSLT_PATH}}', bytes(bytearray(XSLT_PATH, encoding='utf-8')))

from pdb import set_trace
class FileResolver(etree.Resolver):
  def resolve(self, filename, id, context):
    filename = filename.replace('file://', '')
    current_filename = Path(filename)
    if not current_filename.exists() or './' in current_filename.__str__():
      filename = filename.replace('./', '/')
      filename = BASE_DIR.absolute() + filename
    filename = 'file://' + filename
    #print ('Resolving url %s ' % filename)
    return self.resolve_filename(filename, context)

parser = etree.XMLParser()
parser.resolvers.add(FileResolver())
xslt_root = etree.XML(XSLT_STR, parser)
XSLT_TRANSFORM = etree.XSLT(xslt_root)


XMLPARSER = etree.XMLParser(remove_blank_text=True)

UUID_NAMESPACE = 'https://www.ublinvoice.com'
########## ENDCFDI SECTION #########
####################################

SAT_NO_CERTIFICADO = '20001000000300022323'
SAT_RFCPROVCERTIF = 'AAA010101AAA'
#SAT_RFCPROVCERTIF = 'UNNAMEDPAC69'
SAT_LEYENDA = False
SAT_LEYENDA_STR = "LEYENDA SAT INFORMATIVA"
HSM_TYPE = 'software'
SAT_PAC_KEY = b'''-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCuhhm16MtcFTmO
aqVJiK4rb4Dyt+wTV23JCo5UcVmvUJnJlSaNWau7dbW4PQaBsxLLu2HDVCJ+X0Gx
sWo3Z+kJ/28yEu6k+WNGyYBFZy0APNzXkEH7fAKNKiInJ7gGyyWHHzeurUfP7XyT
I9JOQoM+xXDxJu2LkIU/T8vaaXRlWzVQiMIT2Rx4CsZ5/lqsTZmvOq/QuDZo0KHj
1jN66KC3AATF2Aq+Xnlswrkhtd7zt4fh/3wVS9NEYxeDtHtctwQTUeHwl7Ji3VA7
qD/pPZ48Sb6QAun6HZTx4zX8s3t4j5yz/30t3mBsAX/CqbON5rhQs8nGVyRNjswV
CM2Y7ILvAgMBAAECggEAbAuPTUQy6e4l9NpnO7AHi9J7NUjSOWMuD4Geff6ytEuk
+dyBwo6aN/L2rnnxVkiDwWdfberfc/cLF7QreuO0rUDbGVgJME9Iu+ExrUXj4TrM
yhOAFe4/Mh+8hxsa3fHUaOPVuCmExOBU+E77+wFIeYsIkfM0quus4nZHUQ9qRPh8
SWX4zPYKB/SNl3s3exbNSezr93foeuaKp6a7N/ZNIrbrCagH8m6P3BcGeaDWx4C9
tNn7SbnL2wy1kVoLZ+1DCcxo6QREIGgElZatXmWV+w6yn7hsmofEdoj9l52MC9CE
nMWOU0z8k512q7+6hfCb7/Q2AMubTvDpnjhsTKnA+QKBgQDq8k5Hf4A4FKFlYo7l
6ehMlTC5+hCO250S53K14Q0Y4SdMnqk7HrUf1lSusW4rC6ScIn11qZj6O93Byl30
YMzb59zUPdlv6a4J66DGPk/ZVlHAd5/VnlPpuC4e3qgMOxX5X3sloYAJH1a2rodJ
JAe1/rDR369LxTF3QEm+xFVc+wKBgQC+KbFlFuAQJUIcb7iAs5dw+T192jbdOOx6
K1RpViIXJUCycg8Bu1HVcPUwbLaSnwSViTwM8loBNsEOyniWjm0QDdStdHj104S9
CwnI7Bt+FndpMsYGXTYeWUcgIuO68mmTzOQG1I+oYWtQs9WmtDqmkzOcBTWSXcX1
zrH0tUTnnQKBgQDA5hC/Qz/Sy5130GPjARlpR1SqXVYa9NUSIFVeX1iRhMrvbZUk
pSGw8hi1FZiOXxDX4LmBUa34Rg7cfXqGmrOYGdaFrAJKkGIEYyGtopuMpgKZM55X
lZbv3fh//++Zmyl/hZVmYCLvWnunocQRmTN7iZFDv5P9cfobHv1tU2WC4QKBgEUk
ebjM4XldYrVeNdKt+hF8vkwFTM+RBALDwHRwegK6a9S2PhieGHooES6jSJr1MMCC
XpBCilFIrFeJbOEpNiSRMtRCtjyDxQ7LdapVlwV4e8CHUpM7zxKn2YGoze7Kd3Lj
G8IUBYvuqAt25+cuPukUOr6u8jSe3fyrQ+86/avNAoGACqCKFe5KI0boktVS2tUx
OXS55YsWIBogQy7uVi6ZR/hu+/lyJiUDbgXoeKN7i8GfEpZwL3+nanAuszgT+gvR
8toHrJLHQBBwE2myMqyREjtVHOMwP3teRICVZXxsgGwt/NY5gqfOiaZj4KnLdIOF
mZdVx5ilWZ6AA4LNPIzkirU=
-----END PRIVATE KEY-----
'''


VERBOSE_EXTRA_VALIDATIONS = True

LOGIN_REDIRECT_URL = '/'

TIME_INACTIVITY_SAT = 90

TIME_BLOCKED = 36000

ATTEMPT_BLOCKING_ACCOUNT = False


SESSION_ENGINE ='django.contrib.sessions.backends.cache'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_AGE = 300

VERIFY_SESSION = True


### MANIFIEST
MANIFEST_BASE = '''<Manifiesto xmlns="https://ublinvoice.mx/manifiesto" targetNamespace="https://ublinvoice.mx/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://ublinvoice.mx/manifiesto https://ublinvoice.mx/manifiesto/firma.xsd" Version="1.0">
    <Contribuyente ID="contribuyente">
        <Manifiesto>{hash_manifest}</Manifiesto>
        <FolioDeDocumento>{folio_manifest}</FolioDeDocumento>
        <RfcContribuyente>{rfc_client}</RfcContribuyente>
        <RazonSocialContribuyente>{name_client}</RazonSocialContribuyente>
        <NoCertificadoContribuyente>{no_cer_client}</NoCertificadoContribuyente>
        <RfcProveedor>{rfc_pac}</RfcProveedor>
        <RazonSocialProveedor>{name_pac}</RazonSocialProveedor>
        <NoCertificadoProveedor>{no_cer_pac}</NoCertificadoProveedor>
        <Fecha>{date}</Fecha>
        <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#" Id="placeholder"></ds:Signature>
    </Contribuyente>
    <ProveedorCertificacion ID="proveedor">
        <Manifiesto>{hash_manifest}</Manifiesto>
        <FolioDeDocumento>{folio_manifest}</FolioDeDocumento>
        <RfcContribuyente>{rfc_client}</RfcContribuyente>
        <RazonSocialContribuyente>{name_client}</RazonSocialContribuyente>
        <NoCertificadoContribuyente>{no_cer_client}</NoCertificadoContribuyente>
        <RfcProveedor>{rfc_pac}</RfcProveedor>
        <RazonSocialProveedor>{name_pac}</RazonSocialProveedor>
        <NoCertificadoProveedor>{no_cer_pac}</NoCertificadoProveedor>
        <Fecha>{date}</Fecha>
    </ProveedorCertificacion>
</Manifiesto>'''


MANIFEST_STORAGE = Path('/var/unnamedpac/')

from django.utils.translation import ugettext_lazy as _

LANGUAGE_CODE = 'en'
DEFAULT_LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

PROJECT_NAME = 'UBLINVOICE'
PROJECT_NAME_COMPLETE = f'{PROJECT_NAME} S.A. de C.V.'
PROJECT_AUTHOR = 'Finkok SAPI de CV'

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
)

PEPPOL_DIR = Path(BASE_DIR, 'app', 'peppol')
PEPPOL_CSV = Path(PEPPOL_DIR, 'csv')
if not os.path.exists(PEPPOL_CSV):
  os.makedirs(PEPPOL_CSV)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'conf/locale/'),
)
print(os.path.join(BASE_DIR, 'conf/locale/'))
