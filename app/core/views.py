# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.urls import reverse
from django.db import connection
from django.conf import settings
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import (
  JsonResponse, 
  HttpResponseRedirect, 
  HttpResponse, 
  Http404, 
  HttpResponseForbidden
)

from .models import (
  PasswordHistory, 
  Business, 
  Address, 
  SatFile, 
  Branch, 
  Log, 
  COUNTRY, 
  LOG_ACTIONS,
  FISCAL_REGIME, 
  Manifest,
)
from .decorators import (
  get_query_logs, 
  get_query_branch, 
  get_query_branch_location, 
  get_query_conciliacion, 
  get_query_invoicing_sat, 
  get_report_sat, 
  get_default_business
)
from .catalogs import LOG_MODULES
from .utils.profile import (
  email_validator, 
  imgext_val, 
  validate_csd, 
  validate_pass, 
  datos_series, 
  not_only_numbers
)

from app.users.models import Profile
from app.sat.models.cfdi import CodigoPostal
from app.sat.models.cfdi import RegimenFiscal
from app.users.decorators import has_group, has_groups
from app.invoicing.models import Invoice, InvoicingSerial, Buyer
from app.core.logs import MESSAGES_LOGS

import os
import time
import uuid
import base64
import hashlib
import zipfile
import datetime
import tempfile
from lxml import etree
from unipath import Path
from M2Crypto import EVP
from pdb import set_trace
from M2Crypto import X509
from psycopg2  import sql
from datetime import date
from datetime import datetime
from io import StringIO, BytesIO, TextIOWrapper

import signxml
from helpdesk.models import Queue
from sequences import get_next_value
from sequences.models import Sequence
from signxml import XMLSigner, XMLVerifier
from helpdesk.models import Queue, Ticket, FollowUp, Attachment

from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A3, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image


INVOICE_TYPE = {
  'I': '<span class="label label-success">{}</span>'.format(_('Income')),
  'E': '<span class="label label-warning">{}</span>'.format(_('Expenses')),
  'P': '<span class="label label-default">{}</span>'.format(_('Payments')),
  'T': '<span class="label label-danger">{}</span>'.format(_('Transfers')),
  'N': '<span class="label label-info">{}</span>'.format(_('Payroll')),
}

@login_required(login_url='/')
#@get_default_business
def home(request, *args, **kwargs):
  template, context = 'core/home.html', {}
  tab = ''
  role = request.user.profile.role

  if role == 'G' and request.user.has_group('sat'):
    template = 'core/home_sat.html'
  elif role == 'E' and request.user.has_group('staff'):
    return HttpResponseRedirect('/')

  return TemplateResponse(request, template, context)

from django.utils import timezone
@login_required(login_url='/')
@has_groups(['admins','logs'],False)
@get_query_logs
def logs(request, query, *args, **kwargs):
  user = request.user
  template = 'core/logs.html'
  context = {}
  datatable = {
    'data' : [],
    'iTotalRecords': 0,
    'iTotalDisplayRecords': 0,
  }
  log_message = ''
  #set_trace()
  if request.method == 'POST':
    oper = request.POST.get('oper')
    #print ('Que obtiene MESSAGES_LOGS.get() {}'.format(MESSAGES_LOGS))
    log_message = MESSAGES_LOGS.get('mensaje1').get(settings.DEFAULT_LANGUAGE_CODE)
    #log_message = _('Logs were listed')
    Log.objects.log_action(request, '1', 'R', log_message, 'L', '')
    if request.is_ajax() and oper == 'list-logs':
      try:
        start = int(request.POST.get('iDisplayStart'))
        length = int(request.POST.get('iDisplayLength'))
        events_list = []
        logs_append = events_list.append
        logs = Log.objects.filter(query)
        total = logs.count()
        logs = logs[start:start+length]
        for e in logs:
          ip = e.data['ip'] if 'ip' in e.data else ''
          message = e.data['message'] if 'message' in e.data else ''
          info = u'(IP {}) {}'.format(ip, message)
          show_err_exception = (render_to_string('core/strings/log_options.html', {'err_exception':e.err_exception}, request))
          # print(e.user.username, e.action, e.module, info, e.timestamp, show_err_exception)
          logs_append([e.user.username, dict(LOG_ACTIONS)[e.action], LOG_MODULES[e.module], info, e.timestamp, show_err_exception])
        datatable.update({
          'data' : events_list,
          'iTotalRecords': total,
          'iTotalDisplayRecords': total,
        })
        return JsonResponse(datatable)
      except Exception as e:
        print('Events datatable exception {}'.format(e))
        log_message = MESSAGES_LOGS.get('mensaje2').get(settings.DEFAULT_LANGUAGE_CODE)
        #log_message = _('An exception occurred in the Logs view')
        Log.objects.log_action(request, 2, 'R', log_message, 'L', 'Events datatable exception {}'.format(e))
        return JsonResponse(datatable)
      # Log.objects.log_action(request, 5, 'R', "{}".format(message), 'C', '')  
      return JsonResponse(context)
  return TemplateResponse(request, template, context)


@login_required(login_url='/')
def blocked(request):
  return TemplateResponse(request, 'blocked.html')

@login_required(login_url='/')
@has_groups(['clients', 'billings'],False)
def wizard(request, *args, **kwargs):
  context = {}
  template_name = 'wizard/wizard.html'
  user = request.user
  profile = user.profile
  role = profile.role
  is_valid = True
  tax_contract_manifest = request.POST.get('taxpayer_id')
  
  if request.method == 'POST' and request.is_ajax():
    oper = request.POST.get('oper', 'undefined')
    if oper == 'add_bussines':
      # import pdb; pdb.set_trace()
      # set_trace()
      from .utils.wizard import validate_wizard
      # tax_regime = request.POST.get("tax_regime")

      name = request.POST.get("name", '')
      # taxpayer_id = request.POST.get("org_id")

      country = request.POST.get("contry", '')
      # CountrySubentity = request.POST.get('CountrySubentity', '') 
      city = request.POST.get('city', '') 
      stree = request.POST.get('stree', '')
      cp = request.POST.get("cp", '')

      schemeid = request.POST.get("schemeID", '')
      org_id = request.POST.get("org_id", '')
      org_id_party = request.POST.get('org_id_party', '')
      # legal_org_id = request.POST.get('legal_org_id', '')
      # sl_elect_add = request.POST.get("sl_elect_add", '')

      # exter_numb = request.POST.get("exter_numb", '')
      # inter_numb = request.POST.get("inter_numb", '')

      #stree_additional = request.POST.get('stree_additional', None)
      #address_line = request.POST.get('address_line', None)
      # or not CountrySubentity   or not exter_numb or not inter_numb  or not sl_elect_add
      if not country or not stree or not city or not org_id_party:
        return  context.update({"success": False, "message": _("All fields * are required.")})

      # context['taxpayer_id'] = taxpayer_id

      context['taxpayer_id'] = org_id
      account_exists = user.business_set.exists()
      if not account_exists:
        # is_wizard_valid, message = validate_wizard(tax_regime, taxpayer_id, cp)
        # if is_wizard_valid:
        if True: #Verificar lo del regimen fiscal para validarlo
          if not account_exists:
            business = user.business_set.create(
              taxpayer_id= org_id,
            )
          else:
            business = user.business_set.get()

          # business.fiscal_regime =  tax_regime
          business.name = name
          business.organization_id = org_id_party
          # business.legal_organization_id = legal_org_id
          business.schemeid = schemeid
          # business.seller_elect_address = sl_elect_add

          address = Address.objects.create(zipcode=cp)

          # address.street_aditional = stree_additional
          # address.address_line = address_line
          address.country = country
          # address.state = CountrySubentity
          address.city = city
          # address.external_number = exter_numb
          # address.internal_number = inter_numb
          address.street = stree
          address.save()

          business.address = address
          business.save()
          context.update({"success": True, "message": _("Account successfully registered.")})
        else:
          context.update({"success": False, "message": message})
        Log.objects.log_action(request, 5, 'C', MESSAGES_LOGS.get('mensaje3').get(settings.DEFAULT_LANGUAGE_CODE), 'C', '')
      else:
        # set_trace()
        business = user.business_set.get()
        if business.schemeid is None:
          business.schemeid = schemeid
        if not business.organization_id:
          business.organization_id = org_id_party
          # business.legal_schemeid = legal_org_id
        business.save()

        context.update({"success": True, "message": _("Account previously registered.")})
      Log.objects.log_action(request, 5, 'C', MESSAGES_LOGS.get('mensaje4').get(settings.DEFAULT_LANGUAGE_CODE), 'C', '')
    elif oper == 'validate-key-fiel':
      private_key = request.FILES.get('private_key', None)
      if private_key:
        pwd_key = base64.b64decode(request.POST.get('pwd_key'))
        if not pwd_key:
          is_valid = False
          context['message'] = _('Enter the password for the private key.')

        tmp_private_key_cer = tempfile.NamedTemporaryFile(delete=False)
        tmp_private_key_cer.write(private_key.read())
        tmp_private_key_cer.close()

        tmp_private_key_pem = tempfile.NamedTemporaryFile(delete=False)
        tmp_private_key_pem.write(private_key.read())
        tmp_private_key_pem.close()

        command_key = b'openssl pkcs8 -inform DER -in %s -out %s -passin pass:\'%s\'' % (bytes(bytearray(tmp_private_key_cer.name, encoding='utf-8')), bytes(bytearray(tmp_private_key_pem.name, encoding='utf-8')), pwd_key)
        is_valid_key = os.system(command_key)

        if is_valid and is_valid_key != 0:
          is_valid = False
          context['message'] = _('Private key is not valid, it is possible that it is corrupt or the password is not correct.')
          Log.objects.log_action(request, 2, 'U', MESSAGES_LOGS.get('mensaje5').get(settings.DEFAULT_LANGUAGE_CODE), 'C', '')
      
    elif oper == 'validate-cer-fiel':
      from app.core.models import Business
      business_queryset = request.user.business_set
      taxpayer_id = request.POST.get('taxpayer_id')
      public_key = request.FILES.get('public_key')
      private_key = request.FILES.get('private_key', None)
      context['taxpayer_id'] = taxpayer_id

      if taxpayer_id is None:
        if business_queryset.exists():
          business = business_queryset.get()
          taxpayer_id = business.taxpayer_id
        else:
          is_valid = False
          context['message'] = _('The user {request.user} does not have taxpayer id.')
      
      pwd_key = base64.b64decode(request.POST.get('pwd_key'))

      tmp_private_key = tempfile.NamedTemporaryFile(delete=False)
      tmp_private_key.write(private_key.read())
      tmp_private_key.close()

      tmp_pem_key = tempfile.NamedTemporaryFile(delete=False)
      tmp_pem_key.write(private_key.read())
      tmp_pem_key.close()

      tmp_public_key = tempfile.NamedTemporaryFile(delete=False)
      tmp_public_key.write(public_key.read())
      tmp_public_key.close()

      tmp_pem_cer = tempfile.NamedTemporaryFile(delete=False)
      tmp_pem_cer.write(private_key.read())
      tmp_pem_cer.close()

      command_cer = 'openssl x509 -inform DER -in %s -pubkey -out %s' % (tmp_public_key.name, tmp_pem_cer.name)
      is_valid_cer = os.system(command_cer)
      if is_valid and is_valid_cer != 0:
        is_valid = False
        context['message'] = _('The private key is not valid, it may be corrupted.')
        Log.objects.log_action(request, 5, 'C', u'The electronic signature {}, {} is not valid, it may be corrupt'.format(tmp_public_key.name, tmp_pem_cer.name), 'C', '')

      command_key= b'openssl pkcs8 -inform DER -in %s -out %s -passin pass:\'%s\'' % (bytes(bytearray(tmp_private_key.name, encoding='utf-8')), bytes(bytearray(tmp_pem_key.name, encoding='utf-8')), pwd_key)
      is_valid_key = os.system(command_key)
      if is_valid and is_valid_key != 0:
        is_valid = False
      
      import re
      # LA FIEL no contiene el atributo 'OU=....'
      command_cer_fiel_or_csd = str(os.popen('openssl x509 -inform DER -in {} -subject -noout'.format(tmp_public_key.name, encoding='utf-8')).read())
      is_fiel = True if len(re.findall('OU=',command_cer_fiel_or_csd.strip().replace(' ', ''))) == 0 else False
      if not is_fiel:
        context['message'] = _('Certificates are not type FIEL.')
        is_valid = False
        Log.objects.log_action(request, 5, 'C', u'The file {} corresponds to a certificate, not an electronic signature'.format(tmp_public_key.name), 'C', '')

      command_validate_dates = str(os.popen('openssl x509 -noout -in {} -dates'.format(tmp_pem_cer.name, encoding='utf-8')).read())
      dates = command_validate_dates.strip().replace('notBefore=', '').replace('notAfter=','')
      dates_list = dates.split('\n')
      date_from_valid = datetime.strptime(dates_list[0], "%b %d %H:%M:%S %Y %Z")
      date_to_valid = datetime.strptime(dates_list[1], "%b %d %H:%M:%S %Y %Z")

      if not datetime.now() > date_from_valid:
        is_valid = False
        context['message'] = _('Certificate validity period begins on {}'.format(date_from.strftime('%d-%b-%Y %H:%M:%S')))
        Log.objects.log_action(request, 3, 'C', u'Validity of the electronic signature invalid, the period of validity begins on {}'.format(date_from.strftime('%d-%b-%Y %H:%M:%S')), 'C', '')

      if not datetime.now() < date_to_valid:
        is_valid = False
        context['message'] = _('Certificate validity period ended on {}'.format(date_to.strftime('%d-%b-%Y %H:%M:%S')))
        Log.objects.log_action(request, 3, 'C', MESSAGES_LOGS.get('mensaje6').get(settings.DEFAULT_LANGUAGE_CODE).format(date_to.strftime('%d-%b-%Y %H:%M:%S')), 'C', '')

      cert = X509.load_cert(tmp_pem_cer.name)
      evp = EVP.load_key(tmp_pem_key.name)

      cer_modulus = cert.get_pubkey().get_modulus()
      key_modulus = evp.get_modulus()

      if is_valid and cer_modulus != key_modulus:
        is_valid = False
        context['message'] = _('The certificates do not match.')

      subject_certificate = str(cert.get_subject())
      if is_valid and taxpayer_id not in subject_certificate:
        context['message'] = _('The electronic signature does not correspond to the taxpayer')
        Log.objects.log_action(request, 5, 'C', context['message'], 'C', '')

    elif oper == 'sign-manifest':

      try:
        XML_BASE = settings.MANIFEST_BASE
        business_queryset = request.user.business_set
        if business_queryset.exists():
          business_obj = business_queryset.get()
          razon_social = request.POST.get('name')
          taxpayer_id_client = request.POST.get('taxpayer_id')
          checked_cont = request.POST.get('checked')
          checked_contract = True if checked_cont == 'true' else False
          razon_social_xml = ""
          if checked_contract:
            if business_obj.taxpayer_id == taxpayer_id_client:
              txt_manifest = open(os.path.join(settings.BASE_DIR, 'test_manifest.txt'), 'r+').read()
              txt_manifest = txt_manifest.format( settings.SAT_RFCPROVCERTIF, taxpayer_id_client, razon_social)

              print('taxpayer_id:' + taxpayer_id_client.strip())
              print('name: '+ razon_social.strip())
              
              especial_caracters = ['&', '"', '>', '<', '‘']
              caracters_value = {'&':'&amp;', '"':'&quot;', '>':'&lt;', '<':'&gt;', '‘':'&apos;'}

              contains_name = [car for car in list(razon_social) if car in especial_caracters]
              if len(contains_name) > 0:
                  for caracter in contains_name:
                    razon_social_xml = razon_social.replace(caracter, caracters_value[caracter])

              txt_manifest_hash = hashlib.md5()
              txt_manifest_hash.update(txt_manifest.encode('utf-8'))
              result_hash_b64_client = base64.encodestring(bytes(txt_manifest_hash.hexdigest(), 'utf-8')).strip()
              
              folio_template = f'{settings.UUID_NAMESPACE}/manifiesto/?RfcPac={settings.SAT_RFCPROVCERTIF}&?RfcClient={taxpayer_id_client}&?Manifiest={result_hash_b64_client}'

              #namespace = '{}/{}'.format(UUID_NAMESPACE, txt_manifest)
              manifest_folio = str(uuid.uuid5(uuid.NAMESPACE_DNS, folio_template)).upper()
          
              fiel_key = request.FILES.get('private_key_fiel')
              pwd_key = base64.b64decode(request.POST.get('pwd_key'))
              fiel_cer = request.FILES.get('fiel_cer')
          
              tmp_fiel_cer = tempfile.NamedTemporaryFile(delete=False)
              tmp_fiel_cer.write(fiel_cer.read())
              tmp_fiel_cer.close()

              tmp_fiel_key = tempfile.NamedTemporaryFile(delete=False)
              tmp_fiel_key.write(fiel_key.read())
              tmp_fiel_key.close()

              tmp_fiel_cer_pem = tempfile.NamedTemporaryFile(delete=False)
              tmp_fiel_cer_pem.write(fiel_cer.read())
              tmp_fiel_cer_pem.close()

              tmp_fiel_key_pem = tempfile.NamedTemporaryFile(delete=False)
              tmp_fiel_key_pem.write(fiel_key.read())
              tmp_fiel_key_pem.close()

              no_cer_fiel_command = 'openssl x509 -inform DER -in {} -noout -serial'.format(tmp_fiel_cer.name, encoding='utf-8')
              res_no_cer_fiel_command = os.popen(no_cer_fiel_command).read().strip()[7:]
              no_cer_fiel = ''.join( [car for cont, car in enumerate(res_no_cer_fiel_command) if cont%2 != 0])

              sign_manifest_date = datetime.now().replace(microsecond=0).isoformat('T')

              command_cer_pem= 'openssl x509 -inform DER -in {} -pubkey -out {}'.format(tmp_fiel_cer.name, tmp_fiel_cer_pem.name)
              is_valid_cer = os.system(command_cer_pem)

              command_key_pem = b'openssl pkcs8 -inform DER -in %s -out %s -passin pass:\'%s\'' % (bytes(bytearray(tmp_fiel_key.name, encoding='utf-8')), bytes(bytearray(tmp_fiel_key_pem.name, encoding='utf-8')), pwd_key)
              is_valid_key = os.system(command_key_pem)

              id_attribute_contribuyente = 'IdSignatureContribuyente'
              id_attribute_pac = 'IdSignatureProveedor'

              contribuyente_cer = open(bytes(bytearray(tmp_fiel_cer.name, encoding='utf-8')), 'rb').read()
              contribuyente_key = open(bytes(bytearray(tmp_fiel_key.name, encoding='utf-8')), 'rb').read()

              contribuyente_cer_pem = open(bytes(bytearray(tmp_fiel_cer_pem.name, encoding='utf-8')), 'rb').read()
              contribuyente_key_pem = open(bytes(bytearray(tmp_fiel_key_pem.name, encoding='utf-8')), 'rb').read()
              rs = razon_social_xml if razon_social_xml != '' else razon_social
              
              XML_BASE = XML_BASE.format(
                hash_manifest=result_hash_b64_client.decode('utf-8'),
                folio_manifest=manifest_folio,
                rfc_client=taxpayer_id_client.replace('&', '&amp;'),
                name_client=rs,
                no_cer_client=no_cer_fiel,
                rfc_pac=settings.SAT_RFCPROVCERTIF,
                name_pac='Finkok',
                no_cer_pac=settings.SAT_NO_CERTIFICADO,
                date=sign_manifest_date
              )

              pac_cer_pem_path = '/tmp/certificados/pac/cer.pem'
              pac_key_pem_path = '/tmp/certificados/pac/key.pem'

              pac_cer_path = '/tmp/certificados/pac/cer.cer'
              pac_key_path = '/tmp/certificados/pac/key.key'

              #pac_cer = open(pac_cer_path, 'rb').read()
              #pac_key = open(pac_key_path, 'rb').read()
              pac_cer_pem = settings.SAT_CERT_STR
              pac_key_pem = settings.SAT_PAC_KEY

              #pac_cer_pem = open(pac_cer_pem_path, 'rb').read()
              #pac_key_pem = open(pac_key_pem_path, 'rb').read()
              # set_trace()
              #parent_contribuyente = open('/tmp/certificados/Certificados_P/Certificado_AC_Pruebas/AC_4096_2018.crt', 'rb').read()
              # signature = ubl_extensions.xpath('string(//ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/ds:Signature/SignatureValue/text())', namespaces=namespaces)
              contribuyente_reference = "contribuyente"
              pac_reference = 'proveedor'
              
              xml_to_sign_etree = etree.fromstring(XML_BASE)
              signer1 = XMLSigner(method=signxml.methods.enveloped)
              # , id_attribute=id_attribute_contribuyente
              contribuyente_signed = signer1.sign(xml_to_sign_etree, key=contribuyente_key_pem, cert=contribuyente_cer_pem, always_add_key_value=True, reference_uri=contribuyente_reference)
              # '/tmp/certificados/'+manifest_folio+'_contribuyente.xml'
              #manifest_contribuyente_xml_path = os.path.join(BASE_PATH, manifest_folio+'_contribuyente.xml')
              # set_trace()
              # if contribuyente_signed is not None:
              contribuyente_signed_obj = BytesIO()
              if checked_contract:
                root = contribuyente_signed.getroottree()
                root.write(contribuyente_signed_obj)
              
              contribuyente_signed_str = contribuyente_signed_obj.getvalue()

              placeholder = etree.fromstring('<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#" Id="placeholder"></ds:Signature>')
              contribuyente_signed.find('./tmp:ProveedorCertificacion', namespaces={'tmp': 'https://ublinvoice.mx/manifiesto'}).append(placeholder)

              signer = XMLSigner(method=signxml.methods.enveloped)
              pac_signed = signer.sign(contribuyente_signed, key=pac_key_pem, cert=pac_cer_pem, reference_uri=pac_reference)

              pac_signed_obj = BytesIO()

              root = pac_signed.getroottree()
              root.write(pac_signed_obj)
              
              pac_signed_str = pac_signed_obj.getvalue()

              months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
              date = datetime.now()
              day = date.day
              month = months[date.month-1]
              year = date.year
              date_pdf = '{}/{}/{} {}'.format(day, month, year, date.strftime('%H:%M:%S'))
              contribuyente_node = pac_signed.find('.//tmp:Contribuyente', namespaces={"tmp": "https://ublinvoice.mx/manifiesto"})
              pac_node = pac_signed.find('.//tmp:ProveedorCertificacion', namespaces={"tmp": "https://ublinvoice.mx/manifiesto"})
              sign_cont = contribuyente_node.find('.//ds:SignatureValue', namespaces={"ds": "http://www.w3.org/2000/09/xmldsig#"}).text
              sign_pac = pac_node.find('.//ds:SignatureValue', namespaces={"ds": "http://www.w3.org/2000/09/xmldsig#"}).text

              # pdf_name_manifest = os.path.join(BASE_PATH, manifest_folio+'.pdf')
              pdf_signed = BytesIO()
              doc = SimpleDocTemplate(pdf_signed, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
              pdf_data = []
              img_log_pac = 'static/img/logos/logo.png'
              estilos = getSampleStyleSheet()
              estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, fontSize=10, fontName='Times-Roman'))
              style_bold = '<font name="Times-Roman" size="10"><strong>{}</strong></font>'          

              imagen = Image(img_log_pac, 1*inch, 1*inch)
              pdf_data.append(imagen)

              pdf_data.append(Spacer(1,20))
              pdf_data.append(Paragraph('{}: {}'.format(style_bold.format('Fecha'), date_pdf), estilos['Normal']))
              pdf_data.append(Spacer(1,2))

              pdf_data.append(Paragraph('{}: {}'.format(style_bold.format(u'Razón Social/Nombre'), razon_social), estilos['Normal']))
              pdf_data.append(Spacer(1,2))

              pdf_data.append(Paragraph('{}: {}'.format(style_bold.format('Folio De Documento'), manifest_folio), estilos['Normal']))
              pdf_data.append(Spacer(1,12))

              pdf_data.append(Paragraph(txt_manifest, estilos['Justify']))
              pdf_data.append(Spacer(1,20))

              pdf_data.append(Paragraph('{}: {}'.format(style_bold.format('Firma Contribuyente'), sign_cont), estilos['Normal']))
              pdf_data.append(Spacer(1,7))

              pdf_data.append(Paragraph('{}: {}'.format(style_bold.format('Firma PAC'), sign_pac), estilos['Normal']))
              pdf_data.append(Spacer(1,5))
              doc.build(pdf_data)
              # set_trace()
              # cfdi.xml = ContentFile(self.xml_string_tfd, '{0}.xml'.format(self.uuid))
              pdf_signed_file = ContentFile(pdf_signed.getvalue(), '{}.pdf'.format(manifest_folio))
              xml_signed_file = ContentFile(pac_signed_str, '{}.xml'.format(manifest_folio))
              # copy_filelike_to_filelike(pdf_signed.getvalue(), pdf_signed_file)
              # print(type(pdf_signed_file))
              if pac_signed_str:
                  account_queryset = user.business_set
                  business_obj.name = razon_social
                  business_obj.save()
                  sign_manifest, created = Manifest.objects.get_or_create(business=business_obj,signed=True, 
                    signed_contract_xml=xml_signed_file, signed_contract_pdf=pdf_signed_file,
                    date_signed=date
                   )
                  if created:
                    context.update({
                      'taxpayer_id':sign_manifest.business.taxpayer_id,
                      'sign_manifest': sign_manifest.signed,
                      'razon_social':sign_manifest.business.name,
                      'success':True,
                      'message': _('Manifest signed correctly.')
                      })
                    Log.objects.log_action(request, 5, 'U', u'The user with taxpayer id {} and name {} signed the manifest'.format(taxpayer_id_client, razon_social), 'C', '')
                  else:
                    context.update({
                      'success': False,
                      'message': _('An error occurred while signing the manifest.')
                      })
                    Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje7').get(settings.DEFAULT_LANGUAGE_CODE), 'C', '')
              else:
                context.update({
                  'success': False,
                  'message': _('An error occurred while signing the manifest.')
                  })
            else:
              context.update({
                    'success': False,
                    'message': _('An error occurred while signing the manifest.')
              })

          else:
            context.update({
              'message': _('You need to accept the contract.'),
              'success': False
              })
        else:
          context.update({
            'success':False,
            'message': _('An error occurred, could not get taxpayer information.')
            })
      except Exception as e:
        print('Exception in sign-manifest => ' + str(e))
        context.update({
            'success':False,
            'message': _('An error occurred while signing the manifest.')
            })
        Log.objects.log_action(request, 2, 'U', MESSAGES_LOGS.get('mensaje7').get(settings.DEFAULT_LANGUAGE_CODE), 'C','Exception in sign-manifest => ' + str(e) )
        #Log.objects.log_action(request, 2, 'U', _('An error occurred when signing the manifest'), 'C', 'Exception in sign-manifest => ' + str(e))

    elif oper == 'sign_agreement':
      business_queryset = user.business_set
      if business_queryset.exists():
        business = business_queryset.get()
        business.contract = True
        business.privacy = True
        business.status = 'A'
        business.save()
        context.update({ 'success': True, 'message': _('Manifest signed correctly.'), 'taxpayer_id_billing': '', 'is_valid': is_valid})
      else:
        context.update({'message': _('User does not have any taxpayer information registered.')})
      Log.objects.log_action(request, 5, 'U', context['message'], 'C', '')
    return JsonResponse(context)
  else:
    # import pdb; pdb.set_trace() 
    account_queryset = user.business_set
    taxpayer_id = tax_contract_manifest
    account = None
    account_status = 'P'
    fiscal_regime = '601'
    contract = False
    privacy = False
    manifest = None

    try:
      if account_queryset.exists():
        account = account_queryset.get()
        #account_taxpayer_id = account.taxpayer_id
        account_status = account.status
        fiscal_regime = account.fiscal_regime
        contract = account.contract
        privacy = account.privacy
        sign_manifest_reg = Manifest.objects.all().count()
        if sign_manifest_reg > 0:
          manifest = Manifest.objects.filter(business=account).last()
          if manifest:
            context.update({
              'taxpayer_id':account.taxpayer_id,
              'sign_manifest': manifest.signed,
              'path_pdf_contract': manifest.signed_contract_pdf,
              'razon_social':account.name,
              'show_pdf': manifest.signed_contract_pdf.path
              })
        else:
          context.update({
          'success': False,
          'message': _('Business was not found.')
          })
      else:
        context.update({
          'success': False,
          'message': _('Business was not found.')
          })
    except Exception as e:
      print('Exception in else sign-manifest => {}'.format(e))

    try:
      data_adrees = {}
      if account.schemeid:
        idc = ICD.objects.filter(code=account.schemeid).values('code','name')

      if account.address:
          data_adrees = account.address.user_address()
    except Exception as e1:
      pass
    context.update({
      "account_status": account_status,
      "account": account,
      "data_adrees":data_adrees,
      'account_address': account.id if account is not None else '', #if account.address_id else {},
      "role":  role,
      "fiscal_regime": fiscal_regime,
      "fiscal_regimes": RegimenFiscal.objects.filter(Q(fin=None) | Q(fin__lt=datetime.today())),
      'contract': contract,
      'privacy': privacy,
      'taxpayer_id':account.taxpayer_id if account else None,
      'success_account': True if account else False,
      'success_manifest': True if manifest else False,
      'success_agreement': True if account and account.privacy and account.contract else False,
      # 'list_icd': list(idc)
      'list_icd': ICD.objects.get(code=account.schemeid) if account and account.schemeid else "",
    })
    # print(context)
  return render(request, template_name, context)

@login_required(login_url='/')
@has_groups(['admins', 'clients'], False)
def download_manifest_files(request):
  try:
    business_queryset = request.user.business_set
    business = Manifest.objects.get(business=business_queryset.get())
    ZIP_STORAGE = Path(settings.MANIFEST_STORAGE, 'zip/')
    if not os.path.exists(ZIP_STORAGE):
      os.mkdir(ZIP_STORAGE)

    if business:
      xml = business.signed_contract_xml.path
      pdf = business.signed_contract_pdf.path
      download_zip = zipfile.ZipFile(os.path.join(ZIP_STORAGE ,str(business.business.taxpayer_id)+'.zip'), 'w')
      download_zip.write(xml, os.path.basename(xml), compress_type=zipfile.ZIP_DEFLATED)
      download_zip.write(pdf, os.path.basename(pdf), compress_type=zipfile.ZIP_DEFLATED)
      download_zip.close()
      response = HttpResponse(open(ZIP_STORAGE +str(business.business.taxpayer_id)+'.zip', 'rb'), content_type='application/zip')
      response['Content-Disposition'] = 'attachment; filename={}'.format(str(business.business.taxpayer_id)+'.zip')
      Log.objects.log_action(request, 5, 'U', u'The user {} downloaded the files corresponding to the contracts of the signing of the manifest in zip format {}'.format(request.user.username, str(business.business.taxpayer_id)+'.zip'), 'C', '')
    else:
      Log.objects.log_action(request, 2, 'U', _('The file cannot be found in the path'), 'C', u'The path of the zip file to download was not found')
      return Http404
    return response
  except Exception as e:
    print('Exception in download_manifest_files => {}'.format(e))
    Log.objects.log_action(request, 2, 'U', u'An exception occurred while downloading the zip file {}'.format(str(business.business.taxpayer_id)+'.zip'), 'C', 'Exception in download_manifest_files => {}'.format(e))
    return HttpResponseForbidden()

@login_required(login_url='/')
@has_groups(['admins', 'clients'], False)
@require_http_methods(["GET"])
def download_manifest_pdf(request):
  try:
    business = request.user.business_set
    business_manifest = Manifest.objects.filter(business=business.get()).last()
    if business_manifest:
      pdf_path = business_manifest.signed_contract_pdf.path
      response = HttpResponse(open(pdf_path, 'rb'), content_type='application/pdf')
      response['Content-Disposition'] = 'attachment; filename={}'.format(str(business_manifest.business.taxpayer_id) + '.pdf')
      Log.objects.log_action(request, 5, 'U', u'The user {} downloaded the files corresponding to the contracts of the signing of the manifesto in pdf format {}'.format(request.user.username, str(business_manifest.business.taxpayer_id)+'.zip'), 'C', '')
      return response
    else:
      Log.objects.log_action(request, 2, 'U', _('The file cannot be found in the path'), 'C', u'The path of the PDF file to download was not found')
      return Http404
  except Exception as e:
    print('Exception in download_manifest_pdf => {}'.format(e))
    Log.objects.log_action(request, 2, 'U', u'An exception occurred while downloading the pdf file {}'.format( str(business.business.taxpayer_id)+'.pdf'), 'C', 'Exception in download_manifest_files => {}'.format(e))
    return HttpResponseForbidden()

@login_required(login_url='/')
@has_groups(['admins', 'clients'], False)
@require_http_methods(["GET"])
def download_manifest_xml(request):
  try:
    business = request.user.business_set
    business_manifest = Manifest.objects.filter(business=business.get()).last()
    if business_manifest:
      xml_path = business_manifest.signed_contract_xml.path
      response = HttpResponse(open(xml_path, 'rb'), content_type='application/xml')
      response['Content-Disposition'] = 'attachment; filename={}'.format(str(business_manifest.business.taxpayer_id) + '.xml')
      Log.objects.log_action(request, 5, 'U', u'The user {} downloaded the files corresponding to the contracts for signing the manifest in xml format {}'.format(request.user.username, str(business_manifest.business.taxpayer_id)+'.zip'), 'C', '')
      return response
    else:
      Log.objects.log_action(request, 2, 'U', MESSAGES_LOGS.get('mensaje8').get(settings.DEFAULT_LANGUAGE_CODE), 'C', u'The path of the XML file to download was not found')
      return Http404
  except Exception as e:
    print('Exception in download_manifest_xml => {}'.format(e))
    Log.objects.log_action(request,2,'U', MESSAGES_LOGS.get('mensaje9').get(settings.DEFAULT_LANGUAGE_CODE).format(str(business.business.taxpayer_id)+'.xml'), 'C', 'Exception in download_manifest_files => {}'.format(e))
    #@Log.objects.log_action(request, 2, 'U', u'An exception occurred while downloading the xml file {}'.format(str(business.business.taxpayer_id)+'.xml'), 'C', 'Exception in download_manifest_files => {}'.format(e))
    return HttpResponseForbidden()

@require_http_methods(['GET', 'POST'])
@login_required(login_url='/')
@has_groups(['admin'], False)
@get_query_invoicing_sat
def invoices_sat(request, *args, **kwargs):
  #set_trace()
  context = {}
  user = request.user
  #business = kwargs['business']
  template = 'home.html'
  log_message = ''

  datatable = {
    'aaData' : [],
    'iTotalRecords': 0,
    'iTotalDisplayRecords': 0,
  }

  if request.method == 'POST':
    oper = request.POST.get('oper')
    if request.is_ajax():
      if oper == 'list-invoices':
        log_message = MESSAGES_LOGS.get('mensaje10').get(settings.DEFAULT_LANGUAGE_CODE)
        print('LOG_MESSAGE {}'.format(log_message))
        Log.objects.log_action(request, 5, 'R', log_message , 'U', '')
        try:
          invoices_list = []
          invoices_append = invoices_list.append
          query = kwargs['query']
          start = int(request.POST.get('iDisplayStart'))
          length = int(request.POST.get('iDisplayLength'))
          
          invoices = Invoice.objects.filter(query).order_by('-id')
          total = invoices.count()
          invoices = invoices[start:start+length]
          for invoice in invoices:   
            #options_dic={'options': reverse('core:opciones', kwargs={'billing_id':billing_receipt.id})}     
            options = render_to_string('core/strings/opciones.html', {'uuid':invoice.uuid})
            invoices_append([
              invoice.taxpayer_id,
              invoice.rtaxpayer_id,
              invoice.rname,
              invoice.uuid,
              INVOICE_TYPE[invoice.type],
              invoice.total,
              invoice.emission_date,
              options
            ])
          datatable.update(
            aaData=invoices_list,
            iTotalRecords=total,
            iTotalDisplayRecords=total,
          )
          return JsonResponse(datatable)  
        except Exception as e:
          print ('Events datatable exception {}'.format(e))
          Log.objects.log_action(request, 2, 'R', u'An exception occurred in the invoices_sat view', 'U', u'Exception in invoices_sat => {}'.format(e))
          return JsonResponse(datatable)
        return JsonResponse(context)
  elif request.method == 'GET':
    from app.invoicing.models import ProdServ
    import json
    template_base = 'base.html' #if request.user.profile.role in ('G', ) else 'base.html'
    data_business = []
    data_invoices = []
    data_prodserv = []
    role = request.user.profile.role
  
    for number_month in range(0, datetime.now().month):
      number_month += 1
      data_invoices.append(Invoice.objects.filter(emission_date__month=number_month, emission_date__year=datetime.now().year).count())
      data_prodserv.append(ProdServ.objects.filter(creation_date__month=number_month, creation_date__year=datetime.now().year).count())
      data_business.append(Buyer.objects.filter(modified__month=number_month, modified__year=datetime.now().year).count())
    

    context.update({
      'template_base': template_base,
      'total_business': Buyer.objects.all().count(),
      'total_invoices': Invoice.objects.filter(status='F').count(),
      'total_tickets': Ticket.objects.filter(submitter_email=request.user.username).count(),
      'data_invoice': data_invoices,
      'data_prodserv': data_prodserv,
      'data_business': data_business,
      'role': role
    })
  return TemplateResponse(request, template, context)

@require_http_methods(['GET', 'POST'])
@login_required(login_url='/')
@has_groups(['admin'], False)
@get_query_invoicing_sat
def receivers(request, *args, **kwargs):
  context = {}
  user = request.user
  #business = kwargs.get('business', None)
  template = 'invoicing/receivers.html'

  datatable = {
    'aaData' : [],
    'iTotalRecords': 0,
    'iTotalDisplayRecords': 0,
  }
  #context.update({
  #  'list_use_cfdi': list(UsoCFDI.objects.all().values('clave', 'descripcion'))
  #  })

  #set_trace()
  if request.method == 'POST':
    if request.is_ajax():
      oper = request.POST.get('oper')
      if oper == 'list-receivers':
        receiver_list = []
        receiver_append = receiver_list.append
        role = request.user.profile.role
        query = kwargs['query']
        start = int(request.POST.get('iDisplayStart', 1))
        length = int(request.POST.get('iDisplayLength', 10))
        #receivers = Receiver.objects.filter(query).order_by('-id')
        
        receivers = Buyer.objects.filter(query).order_by('-id')
        
        total = receivers.count()
        receivers = receivers[start:start+length]
        
        for receiver in receivers:
          #emails = render_to_string('invoicing/strings/receiver-emails.html', {'emails': receiver.emails}, request)
          emails = render_to_string('invoicing/strings/receiver-emails.html', {'emails': receiver.email_contact}, request)
          #options = render_to_string('invoicing/strings/receiver-options.html', {'receiver': receiver, 'role': role}, request)
          options = render_to_string('invoicing/strings/receiver-options.html', {'receiver': receiver, 'role': role}, request)
          owner = receiver.business.users.last()
          receiver_append([
            '',
            #receiver.taxpayer_id,
            receiver.tax_idenfier_number,
            #receiver.name,
            receiver.company_name,
            '<button title="Detalles del Propietario" owner="%s" class="btn btn-xs btn-warning btn-details-owner"><b>%s</b></button>' % (owner.id, owner.username),
            #'<span class="label label-default"> %s </span>' % receiver.use_cfdi,
            emails,
            #RECEIVER_STATUS[receiver.status],
            #receiver.organization_id,
            options
          ])
        
        datatable.update(
          aaData=receiver_list,
          iTotalRecords=total,
          iTotalDisplayRecords=total,
        )
        Log.objects.log_action(request, 5, 'R', u'Se listaron los receptores', 'I', '')
        return JsonResponse(datatable)
      elif oper == 'add-buyer':
        try:
          identifier_number = request.POST.get('identifier_number')
          organizacion_id = request.POST.get('organizacion_id')
          custom_name = request.POST.get('custom_name')
          address_name = request.POST.get('address_name')
          city_name = request.POST.get('city_name')
          id_province = request.POST.get('id_province')
          postal_zone = request.POST.get('postal_zone')
          # id_country = request.POST.get('id_country')
          id_language = request.POST.get('id_language')
          id_currency = request.POST.get('id_currency')
          id_full_name = request.POST.get('id_full_name')
          id_department = request.POST.get('id_department')
          id_email = request.POST.get('id_email')
          id_telephone = request.POST.get('id_telephone')
          id_web = request.POST.get('id_web')
          id_category = request.POST.get('id_category')
          id_method = request.POST.get('id_method')
          payment_method = request.POST.get('payment_method')
          term = request.POST.get('term')

          buyer_obj, created = Buyer.objects.get_or_create(business= business, 
            tax_idenfier_number = identifier_number, 
            organization_id = organizacion_id,
            company_name=custom_name, 
            address_name=address_name, 
            city_name=city_name, 
            province = id_province,
            postal_zone=postal_zone, 
            # country=id_country,
            language=id_language, 
            currency=id_currency, 
            full_name=id_full_name, 
            department=id_department,
            email_contact=id_email,  
            telephone_contact=id_telephone, 
            web=id_web,
            category=id_category,
            method_category=id_method,
            payment_method=payment_method,
            term=term)

          buyer_obj.save()
          context.update({
            'success': True,
            'message': _('Registered buyer correctly')
          })
        except IntegrityError as e:
          context.update({
            'success': False,
            'message': 'Producto/Servicio duplicado'
          })
        except Exception as e:
          context.update({
            'success': False,
            'message': _('Registration is not possible, please try again later.')
          })
          Log.objects.log_action(request, 2, 'C',"{}".format(context['message']), 'I', u'Exception in add-receiver => {}'.format(str(e)))
      elif oper == 'get-info-edit':
        receiver_encr = request.POST.get('receiver')
        #receiver_obj = Receiver.objects.get_encrypted(receiver_encr)
        receiver_obj = Buyer.objects.get_encrypted(receiver_encr)
        if receiver_obj:
          context.update({
            'success': True,
            'receivers-info':{
              'buyer_name': receiver_obj.company_name,
              'identifier_number': receiver_obj.tax_idenfier_number,
              'organizacion_id': receiver_obj.organization_id,
              'buyer_emails': receiver_obj.email_contact,
              'id_telephone': receiver_obj.telephone_contact,
              'address_name': receiver_obj.address_name,
              'city_name': receiver_obj.city_name,
              # 'id_country': receiver_obj.country,
              'receiver_last_modified': receiver_obj.modified.strftime('%Y-%m-%d %H:%M:%S'),
              'receiver_id': receiver_obj.id,
              #'use_cfdi_values': list(uses_cfdi),
              #'receiver_use_cfdi_val': receiver_obj.use_cfdi
            }
            })
        else:
          context.update({
            'success':False,
            'message': _('It was not possible to obtain the information of this buyer.')
            })
    return JsonResponse(context)
  elif request.method == 'GET':
    template_base = 'base_providers.html' if request.user.profile.role in ('P', ) else 'base.html'
    addreceiverform = ReceiverForm()
    print(kwargs)
    context.update({
      'addreceiverform': addreceiverform,
      'template_base': template_base,
      'total_business': Business.objects.all().count()
    })
  return TemplateResponse(request, template, context)

@login_required(login_url='/')
@has_groups(['sat'], False)
def download_xml_sat(request, **kwargs):
  #set_trace()
  try:
    uuid = kwargs['uuid']
    invoice = Invoice.objects.get(uuid=uuid)
    filename = '{}.xml'.format(invoice.uuid)
    xml = invoice.xml
    response = HttpResponse(xml, content_type='application/xml text/xml')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    Log.objects.log_action(request, '3', 'R', MESSAGES_LOGS.get('mensaje10').get(settings.DEFAULT_LANGUAGE_CODE).format(uuid, filename), 'S')
    return response
  except Exception as e:
    print ("Exception download_xml => %s" % str(e))
    raise Http404


@login_required(login_url='/')
@has_groups(['sat'], False)
@get_report_sat
def generatereport_sat(request, query, values, *args, **kwargs):
  #set_trace()
  response = {}
  success = False
  message = ''
  url = None
  COLUMNS = "taxpayer_id as RFC_Emisor, serial as Serial, folio as Folio, emission_date as Fecha_Emision, total as Total, total_tra as Total_Traslados, total_ret as Total_Retenciones, status_sat as Estatus_SAT, type as Tipo_Comprobante"
  CSV_QUERY_1 = "COPY (SELECT {columns} FROM invoicing_invoice WHERE {where} ORDER BY emission_date) TO STDOUT WITH CSV HEADER DELIMITER ',';".format(columns=COLUMNS, where='{where}')
  CSV_QUERY_2 = "COPY (SELECT {columns} FROM invoicing_invoice {where} ORDER BY emission_date) TO STDOUT WITH CSV HEADER DELIMITER ',';".format(columns=COLUMNS, where='{where}')
  CSV_QUERY_3 = "COPY (SELECT {columns} FROM invoicing_invoice WHERE {where}) TO STDOUT WITH CSV HEADER DELIMITER ',';".format(columns=COLUMNS, where='{where}')

  try:
    con = connection.cursor()
    today = datetime.now().replace(microsecond=0).isoformat().replace(':', '-').replace('T', '_')
    filename = 'Reporte_{}.csv'.format(today)
    csv_file = open('/tmp/{}'.format(filename), 'w')
    copy_statement = ''
    if 'uuid' in request.POST:
      copy_statement = con.mogrify(sql.SQL(CSV_QUERY_1).format(where=query), values)
    elif 'taxpayer_id' in request.POST:
      copy_statement = con.mogrify(sql.SQL(CSV_QUERY_1).format(where=query), values)
    elif 'rtaxpayer_id' in request.POST:
      copy_statement = con.mogrify(sql.SQL(CSV_QUERY_1).format(where=query), values)
    elif 'emission_date' in request.POST:
      copy_statement = con.mogrify(sql.SQL(CSV_QUERY_3).format(where=query), values)
    else:
      copy_statement = con.mogrify(sql.SQL(CSV_QUERY_2).format(where=query), values)
    con.copy_expert(copy_statement, csv_file)
    url = request.build_absolute_uri(reverse('core:downloadreport_sat', args=(filename,)))
    message = _('We are working on the report.')
    success = True
  except Exception as e:
    print ('generatereport_sat - An error was ocurren => {}'.format(str(e)))
    message = _('An error occurred.')
    Log.objects.log_action(request, 2, 'C', u'An error occurred while generating the report', 'C', 'generatereport_sat - An error was ocurren => {}'.format(str(e)))

  response = {
    'success': success,
    'message': message,
    'url': url
  }
  return JsonResponse(response)

@login_required(login_url='/')
@has_groups(['sat'], False)
def downloadreport_sat(request, filename):
  #set_trace()
  response = None
  try:
    data =  open('/tmp/{}'.format(filename), 'r').read()
    response = HttpResponse(data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    Log.objects.log_action(request, 4, 'C', 'The report was successfully downloaded {}'.format(filename), 'C', '')
  except Exception as e:
    print (str(e))

  return response

@login_required(login_url='/')
@has_groups(['admins', 'clients', 'sat'], False)
@get_default_business
def profile_options(request, *args, **kwargs):
  try:
    success, message, context, object_ = False, 'Error.', {}, {}
    try:
      business = kwargs['business']
    except Exception as e:
      business = {}
    log_message = ''
    if request.method == 'POST' and request.is_ajax():
      option = request.POST.get('option')
      if option:
        #logo
        if option == 'edit_logo':
          try:
            new_logo = request.FILES.get('logo')
            img_exts = imgext_val(new_logo.name)
            if img_exts and new_logo:
              business.logo = new_logo
              business.save()
              object_ = business.profile_logo()
              success, message = True, ''
              Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje11').get(settings.DEFAULT_LANGUAGE_CODE).format(new_logo), 'C', '')
          except Exception as e:
            Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje10').get(settings.DEFAULT_LANGUAGE_CODE).format(e), 'C', 'Exception in update logo => {}'.format(e))
        # tax information    
        elif option == 'upd_fisdata':
          # import pdb; pdb.set_trace()
          try:
            message = _('All fields * are required.')
            name_company = request.POST.get('name_company', '')
            tax_regime = request.POST.get('tax_regime', '')

            country = request.POST.get('country', '')

            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            states = request.POST.get('states', '')
            street = request.POST.get('street', '')

            city = request.POST.get('locality', '')
            # municipality = request.POST.get('municipality', '')
            # town = request.POST.get('town', '')
            zipcode = request.POST.get('zipcode', '')
            ext_num = request.POST.get('ext_num', '')
            int_num = request.POST.get('int_num', '')
            
            organization_id = request.POST.get('organization_id', '')
            schemeID = request.POST.get('schemeID', '')
            seller_elect_address = request.POST.get('seller_elect_address', '')


            # street_aditional = request.POST.get('street_aditional', '')            
            # address_line = request.POST.get('address_line', '')            

            # if zipcode and not CodigoPostal.objects.filter(clave = zipcode).exists():
            #   return JsonResponse({ 'success': False, 'message': _('Zip code does not exist.'), 'object': object_ })
            val_not_success = not_only_numbers({ 'states': states, 'locality':city, 'street':street})
            if not val_not_success:
              return JsonResponse({ 'success': val_not_success, 'message': _('Fields must not contain only numbers.'), 'object': object_ })
            if name_company and tax_regime != 'N' and country != 'N':
              if not business.address:
                try:
                  object_create = Address.objects.create()
                  business.address = object_create
                  business.save()
                  user_adress = business.address
                  Log.objects.log_action(request, 5, 'C', u"Client address is registered {}".format(business.address), 'C', '')
                except Exception as e:
                  Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje12').get(settings.DEFAULT_LANGUAGE_CODE).format(e), 'C', 'Exception in update fiscal data => '.format(e))
              else:
                user_adress = business.address

              # user_adress.address_line = address_line
              # user_adress.street_aditional =  street_aditional
              user_adress.country = country
              user_adress.state = states
              # user_adress.municipality = municipality
              user_adress.city = city
              # user_adress.neighborhood = town
              user_adress.zipcode = zipcode
              user_adress.street = street
              user_adress.external_number = ext_num
              user_adress.internal_number = int_num
              user_adress.phone = phone
              user_adress.save()

              business.fiscal_regime = tax_regime
              business.name = name_company
              if len(business.email) == 0: 
                business.email = [email]
              else:
                business.email[0] = email

              business.organization_id =  organization_id
              business.schemeid = schemeID
              business.seller_elect_address = seller_elect_address
              business.save()

              success, message = True, ''
              Log.objects.log_action(request, 5, 'U', 'The client fiscal information has been updated', 'C', '')
          except Exception as e:
            #print('An error occurred when registering the address {}'.format(e))
            #log_message = MESSAGES_LOGS.get('mensaje12').get(settings.DEFAULT_LANGUAGE_CODE
            Log.objects.log_action(request, 5, 'U', 'An error occurred when registering the address: {}'.format(e), 'C', '')
        #email
        elif option == 'add_emails':
          try:
            email = request.POST.get('email')
            sub_option = request.POST.get('sub')
            if sub_option == 'edit':
              # import pdb; pdb.set_trace()
              try:
                new_email = request.POST.get('new_email')
                success, message = email_validator(new_email)
                if email in business.email and success:
                  message, success = _('An error occurred, mail can not be modified.'), False
                  business.email.remove(email)
                  business.email.append(new_email)
                  business.save()
                  success, message = True, ''
                  Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje14').get(settings.DEFAULT_LANGUAGE_CODE).format(new_email), 'C', '')
              except Exception as e:
                Log.objects.log_action(request, 5, 'U','An error occurred when modifying email {}: {}'.format(new_email,e), 'C', '')
                #Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje15').get(settings.DEFAULT_LANGUAGE_CODE.format(new_email,e), 'C', '')
            else:
              try:
                success, message = email_validator(email)
                if email and success:
                  message, success = _('The mail was previously register.'), False
                  if not email in business.email:
                    if not business.email:
                      business.email.append('')
                    business.email.append(email)
                    business.save()
                    success, message = True, '' 
                    Log.objects.log_action(request, 5, 'C', MESSAGES_LOGS.get('mensaje16').get(settings.DEFAULT_LANGUAGE_CODE), 'C', '')
              except Exception as e:
                message = _('An error occurred while trying register mail.')
                Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje15').get(settings.DEFAULT_LANGUAGE_CODE).format(e), 'C', '')
          except Exception as e:
            Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje15').get(settings.DEFAULT_LANGUAGE_CODE).format(e), 'C', '')
        elif option == 'delect_email':
          try:
            message, success = _('An error occurred while trying delete mail.'), False
            del_email = request.POST.get('email')
            if del_email in business.email:
              business.email.remove(del_email)
              business.save()
              message, success = '', True
              Log.objects.log_action(request, 2, 'D', MESSAGES_LOGS.get('mensaje16').get(settings.DEFAULT_LANGUAGE_CODE).format(del_email), 'C', '')
          except Exception as e:
            Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje17').get(settings.DEFAULT_LANGUAGE_CODE).format(del_email,e), 'C', '')
        #CSD
        elif option == 'add_csd':
          try:
            cer = request.FILES.get('cer')
            key = request.FILES.get('key')
            password_csd = request.POST.get('pass')
            if key and cer and password_csd:
              success, message, obj_csd = validate_csd(key, cer, password_csd, business)
              if success:
                sat_file = SatFile(
                  business = business,
                  serial = obj_csd['cer_num'],
                  passphrase = password_csd,
                  certificate_type = obj_csd['type_cert'],
                  status = obj_csd['is_active'],
                  default = obj_csd['default'],
                  expedition_date = obj_csd['start_date'],
                  expiration_date = obj_csd['end_date'],
                )
                sat_file.cer = open(obj_csd['temp_cer']).read()
                sat_file.key = open(obj_csd['tem_key']).read()
                sat_file.save()
                business.has_fiel = obj_csd['type_cert'] == 'F'
                business.save()
                message, success = '', True
                Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje18').get(settings.DEFAULT_LANGUAGE_CODE).format(cer.name, key.name), 'C', '')
          except Exception as e:
            Log.objects.log_action(request, 3, 'U', MESSAGES_LOGS.get('mensaje19').get(settings.DEFAULT_LANGUAGE_CODE).format(e), 'C', '')
        elif option == 'csd_default':
          try:
            # set_trace()
            message, success = _('An error occurred while trying to set default certificate.'), False
            id_ = base64.b64decode(request.POST.get('data0')).decode()
            serial = base64.b64decode(request.POST.get('data1')).decode()
            if serial and id_:
              csd = SatFile.objects.filter(business_id = business.id)
              last_active = csd.filter(default = True).last()
              if last_active:
                last_active.default = False
                last_active.save()
              new_default = csd.get(id=id_, serial = serial)
              new_default.default = True
              new_default.save()
              message, success = '', True
              Log.objects.log_action(request, 5, 'U', "The certificate {} is successfully established by default".format(serial), 'C', '')
          except Exception as e:
            Log.objects.log_action(request, 5, 'U', "An error occurred when setting the certificate by default {}: {}".format(serial,e), 'C', '')
        #password
        elif option == 'upd_pass':
          try:
            message, success = _('An error occurred while trying to change password.'), False
            user = request.user.id
            query = User.objects.get(id=user, username = request.user.username, is_active = True)
            object_last = PasswordHistory.objects.filter(user_id = user)
            pass1 = request.POST.get('pass1')
            pass2 = request.POST.get('pass2')
            last_pass = request.POST.get('last_pass')
            print(pass1)
            print(pass2)
            print(last_pass)
            print(request.POST)
            success_val, message = validate_pass(pass1, pass2)
            print('SUCCESS VAL {}'.format(success_val))
            if success_val:
              message = _('Password is not valid.')
              if object_last.exists():
                object_pass = object_last.get(user_id = user) 
                if check_password(last_pass, object_pass.old):
                  message = _('The password must be different as the previously established.')
                  if pass1 != last_pass and not check_password(pass1, object_pass.older) and not check_password(pass1, object_pass.oldest):
                    query.set_password(pass1)
                    object_pass.rotate(make_password(pass1))
                    query.save()
                    success, message = True, ''
                    Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje20').get(settings.DEFAULT_LANGUAGE_CODE), 'C', '')
              else:
                # set_trace()
                if check_password(last_pass, query.password):
                  objects, created = PasswordHistory.objects.get_or_create(user_id = user, old = make_password(pass1), older = make_password(last_pass), oldest = make_password(last_pass), last_rotation_date = timezone.now())
                  query.set_password(pass1)
                  query.save()
                  success, message = True, ''
                  Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje20').get(settings.DEFAULT_LANGUAGE_CODE), 'C', '')
          except Exception as e:
            Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje21').get(settings.DEFAULT_LANGUAGE_CODE).format(e), 'C', '')
        #series
        elif option == 'add_serie':
          try:
            success, message, status = False, _('An error occurred, data is empty.'), True
            serie = request.POST.get('serie')
            folio = request.POST.get('folio')
            if serie and folio:
              da_success, message = datos_series(folio, serie)
              if da_success:
                #checar con alexis ya que el folio solo soporta un len de 10 en la tabla Sequence
                if len(folio)>10:
                  folio = folio[:10]
                message = _('Serie has been registered previously.')
                exists_serie = InvoicingSerial.objects.filter(business_id = business.id)
                if not exists_serie.filter(serie = serie).exists():
                  message = _('An error occurred while registered the serie.')
                  status = False if exists_serie.filter(status = True).exists() else True
                  sequence = Sequence.objects.create(last = folio, name = f"{business.taxpayer_id}-{serie}")
                  newserie = InvoicingSerial(business=business, serie=serie, sequence = sequence, status = status)
                  newserie.save()
                  success, message = True, ''
                  Log.objects.log_action(request, 5, 'C', MESSAGES_LOGS.get('mensaje22').get(settings.DEFAULT_LANGUAGE_CODE).format(serie), 'C', '')
          except Exception as e:
            Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje23').get(settings.DEFAULT_LANGUAGE_CODE).format(serie, e), 'C', '')
        elif option == 'edit_serie':
          try:
            success, message = False, _('An error occurred.')
            serie = base64.b64decode(request.POST.get('data1')).decode()
            newfolio = request.POST.get('data2')
            if serie and newfolio:
              da_success, message = datos_series(newfolio, serie)
              if da_success:
                #checar con alexis ya que el folio solo soporta un len de 10 en la tabla Sequence
                if len(newfolio)>10:
                  folio = folio[:10]
                serie_edit = Sequence(name='{}-{}'.format(business.taxpayer_id, serie), last=newfolio)
                serie_edit.save()
                success, message = True, ''
                Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje24').get(settings.DEFAULT_LANGUAGE_CODE).format(serie), 'C', '')
          except Exception as e:
            Log.objects.log_action(request, 5, 'U', MESSAGES_LOGS.get('mensaje25').get(settings.DEFAULT_LANGUAGE_CODE).format(serie), 'C', u'Exception in update serie => {}'.format(e))
        elif option == 'default_serie':
          try:
            id_serie = base64.b64decode(request.POST.get('data0')).decode()
            serie = base64.b64decode(request.POST.get('data1')).decode()
            success, message = False,  _('An error occurred.')
            query = InvoicingSerial.objects.filter(business_id=business.id)
            query_newdefault = query.get(serie=serie, id=id_serie)
            last_serie = query.get(status = True)
            last_serie.status = False
            query_newdefault.status = True
            last_serie.save()
            query_newdefault.save()
            success, message = True, ''
            Log.objects.log_action(request, 5, 'U', "The series was set correctly by default {}".format(serie), 'C', '')
          except Exception as e:
            Log.objects.log_action(request, 5, 'U', "An inconvenience occurred when editing the series {}".format(serie), 'C', u'Exception in update-serie =>'.format(e))
        elif option == 'activ/deact':
          try:
            id_serie = base64.b64decode(request.POST.get('data0')).decode()
            serie = base64.b64decode(request.POST.get('data1')).decode()
            success, message = False,  _('An error occurred.')
            suboption = request.POST.get('optionsub')
            query_serie = InvoicingSerial.objects.get(business_id=business.id, serie=serie, id=id_serie)
            query_serie.is_active = True
            if suboption == 'deactivate':
              query_serie.is_active = False
              Log.objects.log_action(request, 5, 'U', "The series {} was deactivated correctly".format(serie), 'C', '')
            else:
              Log.objects.log_action(request, 5, 'U', "The series {} was activated correctly".format(serie), 'C', '')
            query_serie.save()
            success, message = True, ''
          except Exception as e:
            Log.objects.log_action(request, 5, 'U', "An issue occurred when deactivating / activating the series: {}".format(serie), 'C', u'Exception in active/deactive serie => {}'.format(e))
        elif option == "queue":
          try:
            queue = Queue.objects.get(title = 'Baja', slug = 'baja', permission_name = 'helpdesk.queue_access_baja').id
            object_ = {'queue':queue}
            success, message = True, ''
          except Exception as e:
            Log.objects.log_action(request, 5, 'U', "An issue occurred while deactivating the account: {}".format(e), 'C', '')
        elif option == "add_ticket":
          user = request.user
          name = request.POST.get('name')
          phone = request.POST.get('phone')
          email = request.POST.get('email')
          why = request.POST.get('why_account')
          success, message = False, _("Fields * are required.")
          if why and name and phone:
            description = _('Hi support, the account has been requested to be removed {} :  Name: {},  Phone: {},  email: {},  comments: {}'.format(user.username, name, phone, email, why))
            subject = _('Cancellation account request {}'.format(user.username))
            try:
              ticket_obj = Ticket.objects.create(
                title = subject,
                submitter_email = user.username,
                status = 1,
                description = description,
                priority = '1',
                assigned_to_id = user.id,
                queue_id = 4,
              )
              followup_obj = FollowUp.objects.create(
                title = subject,
                comment = description,
                ticket_id = ticket_obj.id,
                user_id = user.id,
              )
              profile = Profile.objects.get(id = request.user.profile.id)
              profile.status = 'D' 
              profile.save()
              success, message = True, _("Your request has been created.")
              Log.objects.log_action(request, 5, 'C', u'A ticket was created subject: {}, priority: {}'.format(subject, priorty), 'C', '')
            except Exception as e:
              Log.objects.log_action(request, 5, 'U', "An inconvenience occurred when sending a request to cancel the account: {}".format(e), 'C', '')
      else:
        message =  _("Invalid request.")
  except Exception as e:
    print('Exception in action_profile => {}'.format(str(e)))
    Log.objects.log_action(request, 5, 'U', "An issue occurred while performing a profile action: {}".format(e), 'C', '')
  context = { 'success': success, 'message': message, 'object': object_ }
  if settings.DEBUG:
    print (context)
  return JsonResponse(context)

from app.peppol.models import ICD
@login_required(login_url='/')
@has_groups(['admins', 'sat', 'clients'], False)
@get_default_business
def profile(request, *args, **kwargs):
  try:
    success, message, context, object_ = False, _('An error occurred.'), {}, {}
    list_result, object_, total = [], {}, 0
    try:
      business = kwargs['business']
    except Exception as e:
      business = {}
    if request.method == 'POST' and request.is_ajax():
      option = request.POST.get('option')
      if option:
        #email
        if option == 'dt_email':
          query = []
          if business:
            query = business.email
          total = len(query)
          start = int(request.POST.get('iDisplayStart'))
          length = int(request.POST.get('iDisplayLength'))
          query_rows = query[start:start+length]
          for row in query_rows:
            if row != query_rows[0]:
              context = {'email': row }
              action = render_to_string('profile/strings/action.html', context)
              list_result.append([ row, action ])
          object_.update({'aaData': list_result, 'iTotalRecords': total, 'iTotalDisplayRecords': total,})
        #CSD
        elif option == 'dt_csd':
          query = SatFile.objects.none()
          if business:
            query = SatFile.objects.filter(business_id = business.id)
          total = query.count()
          start = int(request.POST.get('iDisplayStart'))
          length = int(request.POST.get('iDisplayLength'))
          query_rows = query[start:start+length]
          for row in query_rows:
            context = {
              'oper': 'default', 
              'default':row.default,
              'id':base64.b64encode(str(row.id).encode()).decode(),
              'serial':base64.b64encode(str(row.serial).encode()).decode(),
              'show_serial':row.serial
            }
            default = render_to_string('profile/strings/csd_additional.html', context)
            status = render_to_string('profile/strings/csd_additional.html', {'oper': 'status', 'status':row.status})
            list_result.append([
              status,
              row.serial,
              row.expedition_date.strftime("%d-%m-%Y %H:%M:%S").capitalize(),
              # row.expedition_date.strftime("%b. %d, %Y, %I:%M %p").capitalize(),
              row.expiration_date.strftime("%d-%m-%Y %H:%M:%S").capitalize(),
              # row.expiration_date.strftime("%b. %d, %Y, %I:%M %p").capitalize(),
              default,
              True       
            ])
          object_.update({'aaData': list_result, 'iTotalRecords': total, 'iTotalDisplayRecords': total,})
          success, message = True, ''
        #  series            
        elif option == 'dt_series':
          query = InvoicingSerial.objects.none()
          if business:
            query = InvoicingSerial.objects.filter(business_id = business.id)
          total = query.count()
          start = int(request.POST.get('iDisplayStart'))
          length = int(request.POST.get('iDisplayLength'))
          query_rows = query[start:start+length]
          for row in query_rows:
            context = {
              'active':row.is_active,
              'id': base64.b64encode(str(row.id).encode()).decode(),
              'serie':base64.b64encode(str(row.serie).encode()).decode(),
              'folio_decode':row.sequence.last,
              'serie_decode':row.serie,
              'status': row.status
            }
            action = render_to_string('profile/strings/action_serie.html', context)
            status = render_to_string('profile/strings/status_series.html', {'status': row.status})
            list_result.append([
              row.serie,
              row.sequence.last,
              status,
              action           
            ])
          object_.update({'aaData': list_result, 'iTotalRecords': total, 'iTotalDisplayRecords': total,})
          success, message = True, ''
        context = {
          'success': success,
          'message': message,
          'object': object_
        }
      return JsonResponse(context)
    elif request.method == 'GET':
      idc = ''
      data_adrees, user_log = {}, {}
      try:
        user_log = business
        business.email = business.get_email()
        if business.address:
          data_adrees = business.address.user_address()

        if user_log.schemeid:
          idc = ICD.objects.filter(code=user_log.schemeid).values('code','name')
      except Exception as e:
        pass
      context.update({
        'data': user_log,
        'user_address': data_adrees,
        'list_icd': list(idc)
      })
    if settings.DEBUG:
      print (context)
  except Exception as e:
    Log.objects.log_action(request, 5, 'R', MESSAGES_LOGS.get('mensaje26').get(settings.DEFAULT_LANGUAGE_CODE).format(e), 'C', '')
    print('Exception in profile => {}'.format(str(e)))
  return render(request, 'profile/profile.html', context)


from django.views.decorators.http import require_POST
from app.sat.models import CodigoPostal
from django.shortcuts import redirect
from app.peppol.models import ICD


@login_required(login_url='/')
@require_POST
@has_groups(['clients', 'billings'], False)
def wizard_stuff(request, *args, **kwargs):
  context = {}
  if request.method == 'POST' and request.is_ajax():
    oper = request.POST.get('oper', 'undefined')
    if oper == 'get-cp':
      clave = request.POST.get('clave', 'undefined')
      cps = CodigoPostal.objects.filter(clave__icontains=clave).values('clave', 'estado')[:10]
    elif oper == 'get-SchemeID' or oper == 'get-list-id':
      code = request.POST.get('code', 'undefined')
      print(code)
      cps = ICD.objects.filter(code__icontains=code).values('code', 'name')[:10]
    context = list(cps)
    return JsonResponse(context, safe=False)
  return redirect('index')
