# -*- encoding: UTF-8 -*-
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'soriana',
        'USER' : 'soriana',
        'PASSWORD': 'soriana',
        #'HOST' : 'localhost',
        'HOST' : '172.16.100.11',
        'PORT' : '5432',
    },
        'alfredo': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'soriana',
        'USER' : 'soriana',
        'PASSWORD': 'soriana',
        #'HOST' : 'localhost',
        'HOST' : '172.16.100.11',
        'PORT' : '5432',
    },
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR.child('static'),)

### DIRECTORIES
WORK_DIR = '/var/soriana'
SFTP_PATH = Path('/var/sftp/soriana')
SFTP_PATH_DUPLICATED = Path(SFTP_PATH, 'duplicated')
SFTP_PATH_ENTRADA = Path(SFTP_PATH, 'entrada')
SFTP_PATH_ERROR = Path(SFTP_PATH, 'error')
SFTP_PATH_SALIDA = Path(SFTP_PATH, 'salida')
SFTP_PATH_UNZIPPED = Path(SFTP_PATH, 'unzipped')
SFTP_PATH_UPLOADS = Path(SFTP_PATH, 'uploads')
SFTP_PATH_XML = Path(SFTP_PATH, 'xml')
### TMP FILES
PATH = Path('/tmp/soriana')
PATH.mkdir()
QR_PATH = Path('/tmp/soriana/png')
PDF_PATH = Path('/tmp/soriana/pdf')
ZIP_PATH = Path('/tmp/soriana/zip')
LOGOS_PATH = Path(PATH, 'logos')

QR_PATH.mkdir()
PDF_PATH.mkdir()
ZIP_PATH.mkdir()




##CELERY
BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'

CELERY_IMPORTS = ("app.providers.tasks", )
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Mexico_City'

#CELERY_QUEUES = (
#    Queue('high', Exchange('high'), routing_key='high', queue_arguments={'x-max-priority': 10}),
#    Queue('normal', Exchange('normal'), routing_key='normal', queue_arguments={'x-max-priority': 5}),
#    Queue('low', Exchange('low'), routing_key='low', queue_arguments={'x-max-priority': 1}),
#    Queue('default', Exchange('default'), routing_key='default', queue_arguments={'x-max-priority': 3}),
#)
#
#CELERY_DEFAULT_QUEUE = 'normal'
#CELERY_DEFAULT_EXCHANGE = 'normal'
#CELERY_DEFAULT_ROUTING_KEY = 'normal'

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'


### SMTP 
SMTP_SERVER = '10.0.3.12'
SMTP_USER = 'proveedor'
SMTP_PASSWORD = 'g2dMRg99wauf'
SMTP_PORT = 587
SMTP_EMAIL_TEST = True
SMTP_SUBJECT = u'Factura Electrónica (DEMO)'
SMTP_FROM_EMAIL = '<noreply@finkok.com>'
SMTP_TO_EMAIL = 'desarrollo@finkok.com'
SMTP_BCC_EMAIL = ''

### FINKOK
FK_STAMP_URL = 'https://demo-facturacion.finkok.com/servicios/soap/stamp.wsdl'
FK_CANCEL_URL = 'https://demo-facturacion.finkok.com/servicios/soap/cancel.wsdl'
FK_VALIDATION_URL = 'https://demo-facturacion.finkok.com/servicios/soap/validation.wsdl'
FK_LCO_URL = 'https://demo-facturacion.finkok.com/servicios/soap/lco.wsdl'
FK_SATINC_URL = 'https://demo-facturacion.finkok.com/servicios/soap/satinc.wsdl'
FK_USERNAME = 'herbalife@finkok.com'
FK_PASSWORD = 'DemoFinkok.15'

### STORAGE
STORAGE_PATH = Path('/var/soriana')
STORAGE_DOWNLOAD = Path(STORAGE_PATH, 'download')
MEDIA_ROOT = STORAGE_PATH

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '172.16.100.249:11211',
    }
}

### DOWNLOAD SAT
AUTENTICA_URL = 'https://cfdidescargamasivasolicitud.clouda.sat.gob.mx/Autenticacion/Autenticacion.svc'
SOLICITUD_URL = 'https://cfdidescargamasivasolicitud.clouda.sat.gob.mx/SolicitaDescargaService.svc'
VERIFICA_URL = 'https://cfdidescargamasivasolicitud.clouda.sat.gob.mx/VerificaSolicitudDescargaService.svc'
DESCARGA_URL = 'https://cfdidescargamasiva.clouda.sat.gob.mx/DescargaMasivaService.svc'
FIEL_PATH_DEBUG = ''
METADATA_KEYS = ['uuid','taxpayer_id','name','rtaxpayer_id','rname','pac_taxpayer_id','emission_date','stamping_date','total','type','status','cancellation_date']
CSV_HEADERS = 'RFC Emisor,Nombre Proveedor,RFC Receptor,UUID Factura,Fecha Factura,Tipo Comprobante,Moneda,Metodo de Pago,Forma de Pago,Subtotal,Descuento,Total Impuestos Traslados,IEPS,IVA,Total Impuestos Retenidos,IVA,ISR,Total,UUID Complemento de Pago,ID documento,Fecha de Emision Complemento,Monto,Importe Pagado,Importe Saldo Anterior,Parcialidad,Saldo Insoluto,Fecha de Pago,Pagos Pendientes,Pagado/Total,Restante\n'
CSV_LINE = '"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",\n'
XLSX_HEADERS = ['RFC Emisor','Nombre Proveedor','RFC Receptor','UUID Factura','Fecha Factura','Tipo Comprobante','Moneda','Metodo de Pago','Forma de Pago','Subtotal','Descuento','Total Impuestos Traslados','IEPS','IVA','Total Impuestos Retenidos','IVA','ISR','Total','UUID Complemento de Pago','ID documento','Fecha de Emision Complemento','Monto','Importe Pagado','Importe Saldo Anterior','Parcialidad','Saldo Insoluto','Fecha de Pago','Pagos Pendientes','Pagado/Total','Restante']
THREADS_PACKAGES_PROCESSING = 60
COLUMNS = "taxpayer_id as RFCEmisor, name as NombreProveedor, rtaxpayer_id as RFCReceptor, uuid as UUID, emission_date as FechaFactura, type as TipoComprobante, currency as Moneda, payment_method as MetodoDePago, payment_way as FormaDePago, subtotal as Subtotal, discount as Descuento, taxes->>'total_tra' as TotalImpuestosTraslados, taxes->'IEPS'->>'tra' as IEPS, taxes->'IVA'->>'tra' as IVA, taxes->>'total_ret' as TotalImpuestosRetenidos, taxes->'IVA'->>'ret' as IVA, taxes->'ISR'->>'ret' as ISR, total as Total"
CSV_QUERY = "COPY (SELECT {columns} FROM download_invoice WHERE {where}) TO STDOUT WITH CSV HEADER DELIMITER ',';".format(columns=COLUMNS, where='{where}')
COLUMNS_STAMPING = "serial as NumeroOrden, taxpayer_id as RFCEmisor, rtaxpayer_id as RFCReceptor, uuid as UUID, emission_date as FechaFactura, type as TipoComprobante, currency as Moneda, payment_method as MetodoDePago, payment_way as FormaDePago, subtotal_precalculated as Subtotal, discount as Descuento, tax as Impuestos, total as Total"
CSV_QUERY_STAMPING = "COPY (SELECT {columns} FROM stamping_invoice WHERE {where}) TO STDOUT WITH CSV HEADER DELIMITER ',';".format(columns=COLUMNS_STAMPING, where='{where}')
PAYROLL_COLUMNS = "p.serial AS ORDERNUMBER, p.taxpayer_id AS RFCEMISOR, a.name AS NOMBRERECEPTOR, a.taxpayer_id AS RFCRECEPTOR, uuid AS UUID, p.emission_date AS FECHAFACTURA, p.type AS TIPOCOMPROBANTE, p.payroll_type AS TIPONOMINA, p.paid_date_from AS PAGADODESDE, p.paid_date_to AS PAGADOHASTA, p.payment_method AS METODODEPAGO, p.payment_way AS FORMADEPAGO, p.subtotal AS SUBTOTAL, p.discount AS DESCUENTO, p.total as TOTAL"
PAYROLL_CSV_QUERY = "COPY (SELECT {columns} FROM stamping_payroll AS p LEFT JOIN stamping_agent AS a ON (p.agent_id=a.id) WHERE {where}) TO STDOUT WITH CSV HEADER DELIMITER ',';".format(columns=PAYROLL_COLUMNS, where='{where}')
PACKAGES_BK = Path('/var/soriana_packages')
MAIL_SUB = 'Portal Soriana | Descarga SAT'
MAIL_PATH = 'download/strings/email.html'
MAIL_P_PATH = 'download/strings/email_packages.html'
PROVIDERS_QUERY_CSV = '''COPY(
SELECT i.taxpayer_id as "RFC Emisor", i.name as "Nombre Proveedor", i.rtaxpayer_id as "RFC Receptor", i.uuid as "UUID Factura", i.emission_date as "Fecha Factura", i.type as "Tipo Comprobante", i.moneda as "Moneda", i.payment_method as "Metodo de Pago", i.payment_way as "FormaPago", i.subtotal as "SubTotal", i.discount as "Discount", i.tax as "Total Impuestos Traslados", i.ieps, i.iva, i.tax_ret as "Total Impuestos Retenidos", i.ret_iva as "iva", i.ret_isr as "isr", i.total as "Total", 
pi.uuid as "UUID complemento de pago", p.id_documento as "ID documento", pi.emission_date as "Fecha de emision complemento", pi.monto as "Monto", p.imppagado as "Importe Pagado", p.impsaldoant as "Importe Saldo anterior",p.numparcialidad as "Parcialidad", p.imppagadoinsoluto as "Saldo Insoluto", pi.fecha_pago as "Fecha de pago",
CASE 
WHEN i.already_paid='f' and i.payment_method='PPD' THEN 'Si' 
ELSE 'NO'
END, 
CONCAT((CASE
WHEN i.paid is Null  and i.payment_method='PUE' THEN i.total
WHEN i.paid is Null  and i.payment_method='PPD' THEN 0.00
ElSE i.paid
END), ' / ', i.total) as "Pagado/Total",
CASE
WHEN i.paid is Null and i.payment_method='PUE' THEN 0.00
WHEN i.paid is Null and i.payment_method='PPD' THEN i.total
ELSE  i.remaining
END  as "Restante"
FROM providers_invoice i
LEFT JOIN providers_payment p ON i.uuid=p.id_documento
LEFT JOIN providers_invoice pi ON p.invoice_id=pi.id
WHERE {where} order by i.taxpayer_id, i.payment_method
) TO STDOUT WITH CSV HEADER DELIMITER ',';
'''

CREATE_USER_ACCOUNT = {
    'Provider': False,
    'Agent': False,
    'Client': False,
}


import locale
locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')