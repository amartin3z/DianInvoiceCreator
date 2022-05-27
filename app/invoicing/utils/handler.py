# -*- coding: UTF-8 -*-
from django.utils import timezone
from django.template.loader import render_to_string

from . import SatProcess
from .cfdi33 import trunc, CFDI

from app.invoicing.models import Invoice
from app.invoicing.forms.invoice import InvoiceForm
from app.invoicing.utils import create_json_asp, create_json_acp, create_json_delivery, create_json_payment_terms, create_json_allowance_charge
from app.invoicing.utils import create_json_tax_total, create_json_legal_monetary_total, create_json_invoice_lines, create_json_payment_means, create_ubl_extensions_json

from app.cfdi.errors import errors
from app.sat.models import TipoRelacion
from app.core.models import FISCAL_REGIME
from app.peppol.utils.generate import UBLInvoice12
from app.peppol.models import UNCL4461

import json
from pdb import set_trace
from datetime import datetime
from django.utils.translation import ugettext as _
from datetime import datetime
from app.invoicing.xades.test.test_xades import TestXadesSignature, parse_xml
from app.core.models import SatFile, Business
from lxml import etree, objectify
import tempfile
from xml.etree.ElementTree import fromstring, ElementTree, Element
from copy import deepcopy

FISCAL_REGIME_DICT = dict(FISCAL_REGIME)


def __invoice_json_extra_fields():
  issue_datetime = timezone.now()
  return {
      "IssueDate": issue_datetime.strftime('%Y-%m-%d'),
      "IssueTime": issue_datetime.strftime('%H:%M:%S'),
  }


def post_invoice(request, business, _type='invoice'):
    context = {}
    # import pdb; pdb.set_trace()
    try:
      success, message = False, ''
      not_certificate = False
      json_invoice = request.POST.get('invoice')
      internal_notes = request.POST.get('notes')
      json_invoice_ = json.loads(json_invoice)
      invoice_json = json_invoice_['invoice']
      

      document_currency = invoice_json.get('DocumentCurrencyCode')

      invoice_json.update(**__invoice_json_extra_fields())

      payment_means_json = {
          "PaymentMeans": invoice_json.get('PaymentMeans', {})
      }

      # print(json_invoice)
      taxpayer_id = json_invoice_['asp']['taxpayer_id']
      rtaxpayer_id = json_invoice_['acp']['taxpayer_id']
      customer_country = json_invoice_['acp']['customer_country']
      uuid = json_invoice_['invoice']['ID']
      emission_date = json_invoice_['invoice']['IssueDate']

      asp_json = create_json_asp(taxpayer_id)
      acp_json = create_json_acp(taxpayer_id, rtaxpayer_id, customer_country)
      # delivery_json = create_json_delivery(invoice_json, taxpayer_id)
      delivery_json = {}
      payment_name = UNCL4461.objects.get(
          code=json_invoice_['items'][0]['payment_name'])

      #payment_means_json = create_json_payment_means(json_invoice_['items'][0]['payment_name'], payment_name.name)

      # payment_terms_json = create_json_payment_terms(json_invoice_['payment_terms']['note'])
      allowance_charge_json = create_json_allowance_charge()
      tax_total_json = create_json_tax_total(
          json_invoice_['taxes'], document_currency)
      legal_monetary_total_json = create_json_legal_monetary_total(
          json_invoice_['legal_monetary_total'])
      invoice_lines_json = create_json_invoice_lines(
          json_invoice_['items'], taxpayer_id)
      total = legal_monetary_total_json['LegalMonetaryTotal']['TaxInclusiveAmount']['value']
      subtotal = legal_monetary_total_json['LegalMonetaryTotal']['LineExtensionAmount']['value']
      rname = acp_json['AccountingCustomerParty']['Party']['PartyName']['Name']

      ubl_extensions_json = create_ubl_extensions_json(taxpayer_id)

      business = Business.objects.get(taxpayer_id=taxpayer_id)
      sat_file = SatFile.objects.filter(
          business_id=business.id, default=True).last()

      ubl_invoice_12 = UBLInvoice12(
          invoice_json,
          asp_json,
          acp_json,
          delivery_json,
          payment_means_json,
          {},
          allowance_charge_json,
          tax_total_json,
          legal_monetary_total_json,
          invoice_lines_json,
          ubl_extensions_json
      )

      # set_trace()
      ubl_string, ubl_etree = ubl_invoice_12.get_invoice()
      tmp_xml_ubl = tempfile.NamedTemporaryFile(delete=False)
      tmp_xml_ubl.write(ubl_string)
      tmp_xml_ubl.seek(0)
      invoice_obj_etree = parse_xml(tmp_xml_ubl.name)

      # etree.register_namespace('ds', 'http://www.w3.org/2000/09/xmldsig#')
      # ubl_extension_etree_obj = etree.fromstring(UBL_EXTENSIONS)

      print('--'*60)
      print(type(ubl_string))
      print(ubl_string)
      print('--'*60)
      xades_sign = TestXadesSignature()
      print()
      print()
      # set_trace()
      signature_obj_etree = xades_sign.test_create_2(
          ubl_string, sat_file._cer.path, sat_file._key.path, sat_file.passphrase)
      # ubl_extensions_obj = ubl_invoice_12._UBLInvoice12__ubl_extension()
      # ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
      # invoice_obj_etree.getroottree().getroot().set('ds', 'http://www.w3.org/2000/09/xmldsig#')
      # invoice_obj_etree.getroottree().getroot().set('ext', 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2')
      # invoice_obj_etree.append(signature_obj_etree)
      UBL_EXTENSIONS = """
      <Invoice xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2">
      <ext:UBLExtensions>
        <ext:UBLExtension>
            <ext:ExtensionContent>
            </ext:ExtensionContent>
        </ext:UBLExtension>
      </ext:UBLExtensions>
      </Invoice>
      """
      # invoice_obj_etree.getroottree().getroot().append(etree.fromstring('<ext:UBLExtensions></ext:UBLExtensions>'))
      # set_trace()
      ubl_extensions_obj = etree.fromstring(UBL_EXTENSIONS)
      namespaces = deepcopy(ubl_extensions_obj.nsmap)
      tmp_nsmap = namespaces.pop(None, None)
      if tmp_nsmap is not None:
        namespaces.update({ 'tmp': tmp_nsmap })
      
      
      # ubl_extensions_obj_etree = ubl_extensions_obj.xpath('//ext:UBLExtensions', namespaces=namespaces)[0]
      # for elem in ubl_extensions_obj_etree.getiterator():
      #   if not hasattr(elem.tag, 'find'): continue  # (1)
      #   i = elem.tag.find('}')
      #   if i >= 0:
      #       elem.tag = elem.tag[i+1:]
      # objectify.deannotate(ubl_extensions_obj_etree, cleanup_namespaces=True)
      extension_content = ubl_extensions_obj.xpath('./ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent', namespaces=namespaces)[0]
      extension_content.append(signature_obj_etree)
      ubl_extension = ubl_extensions_obj.xpath('./ext:UBLExtensions/ext:UBLExtension', namespaces=namespaces)[0]
      ubl_extension.append(extension_content)
      ubl_extensions = ubl_extensions_obj.xpath('./ext:UBLExtensions', namespaces=namespaces)[0]
      ubl_extensions.append(ubl_extension)
      invoice_obj_etree.append(ubl_extensions)

      # set_trace()
      print(etree.tostring(invoice_obj_etree))
      _xml = etree.tostring(invoice_obj_etree).decode('utf-8')
      
      xml_car_replaced = (_xml.replace('&#225;', '&aacute;').replace("&#233;", '&eacute;').replace("&#237;", '&iacute;').replace("&#243;", '&oacute;')
      .replace("&#250;", '&uacute;').replace("&#193;", '&Aacute;').replace("&#201;", '&Eacute;').replace("&#205;", '&Iacute;')
      .replace("&#211;", '&Oacute;').replace("&#218;", '&Uacute;').replace("&#209;", '&ntilde;').replace('&#241;', '&Ntilde;'))
      # DICT_ASCII = {
      #   "&#224;": '&aacute;',
      #   "&#232;": '&eacute;',
      #   "&#236;": '&iacute;',
      #   "&#242;": '&oacute;',
      #   "&#249;": '&uacute;',
      #   "&#192;": '&Aacute;',
      #   "&#200;": '&Eacute;',
      #   "&#204;": '&Iacute;',
      #   "&#210;": '&Oacute;',
      #   "&#217;": '&Uacute;',
      #   "&#209;": '&amp',
      #   "&amp;": '&ntilde;',

      # }

      if ubl_string:
        invoice_obj = Invoice.objects.create(
            taxpayer_id=taxpayer_id,
            rtaxpayer_id=rtaxpayer_id,
            uuid=uuid
        )
        # set_trace()
        invoice_obj.rname = rname
        invoice_obj.internal_notes = internal_notes
        invoice_obj.total = total
        invoice_obj.subtotal = subtotal
        invoice_obj.discount = 0.0
        invoice_obj.status = 'F'
        invoice_obj.status_sat = 'V'
        # invoice_obj.emission_date = emission_date
        invoice_obj.emission_date = timezone.now().replace(microsecond=0)
        invoice_obj.xml = bytes(xml_car_replaced, encoding='utf-8')
        # invoice_obj.xml = etree.tostring(invoice_obj_etree).decode('UTF-8')
        invoice_obj.save()
        context.update({
            'success': True,
            'message': 'La petición se proceso exitosamente.',
            'invoice': invoice_obj.encrypt,
            'data': {
                'UUID': invoice_obj.uuid,
                'rfc': invoice_obj.taxpayer_id,
                'rrfc': invoice_obj.rtaxpayer_id,
                'total': invoice_obj.total,
            }

        })
        # Log.objects.log_action(request, 5, 'C', '{}'.format(context['message']), 'I')
      else:
        message = u'Hubo un error al procesar la petición, si cfdi'
        context.update({
            "success": success,
            'message': message,
            'not_certificate': not_certificate
        })

      #certificate_json = business.get_csd()
      #sat_file_obj = certificate_json.get('satfile', None)
      #serial = certificate_json.get('serial', '')
      #public_certificate = sat_file_obj.get_cer_b64()
      #private_certificate = certificate_json.get('key')
      #print('--'*60)
      #print(json_invoice)
      #print('--'*60)
      #cfdi_obj = CFDI(json_invoice, business=business, public_certificate=public_certificate, private_certificate=private_certificate, serial=serial, tipo=_type)
      #cfdi_obj.get_cfdi_string()
      #print(cfdi_obj.xml_json)
      '''if cfdi_obj.success:
        cfdi_json = cfdi_obj.xml_json
        cfdi_string = cfdi_obj.xml_string
        stamp_obj = SatProcess(cfdi_string, request.user)
        stamp_obj.timbrado()
        if stamp_obj.is_valid:
          rtaxpayer_id =  cfdi_json.get('Receptor', {}).get('Rfc', '')
          invoice_obj = Invoice.objects.create(
            taxpayer_id=business.taxpayer_id,
            rtaxpayer_id=rtaxpayer_id,
            uuid=stamp_obj.uuid
          )
          try:
            from app.invoicing.models import InvoicingSerial
            from sequences import get_next_value
            serie_tmp = cfdi_json.get('Serie', '')
            serial_obj = InvoicingSerial.objects.filter(business=business, is_active=True, sequence=f'{business.taxpayer_id}-{serie_tmp}')
            if serial_obj.exists():
              serial_obj = serial_obj.get()
              get_next_value(f'{business.taxpayer_id}-{serie_tmp}')
          except Exception as e:
            print(f'Excepcion incrementando el folio {e}')
          invoice_obj.snapshot = cfdi_json
          invoice_obj.seal = cfdi_obj.seal
          if cfdi_obj.receiver is not None and cfdi_obj.receiver.name.strip():
            invoice_obj.rname = cfdi_obj.receiver.name

          invoice_obj.emission_date = cfdi_obj.emission_date
          invoice_obj.certificate_number = serial

          if cfdi_obj.total_tra:
            invoice_obj.total_tra = cfdi_obj.total_tra
          if cfdi_obj.total_ret:
            invoice_obj.total_ret = cfdi_obj.total_ret

          invoice_obj.total = cfdi_json.get('Total', 0.0)
          invoice_obj.subtotal = cfdi_json.get('SubTotal', 0.0)
          invoice_obj.discount = cfdi_json.get('Descuento', 0.0)
          invoice_obj.payment_way  = cfdi_json.get('FormaPago')
          invoice_obj.payment_method = cfdi_json.get('MetodoPago')
          invoice_obj.expedition_place = cfdi_json.get('LugarExpedicion')
          invoice_obj.type = cfdi_json.get('TipoDeComprobante', 'I')

          invoice_obj.status = 'F'
          invoice_obj.status_sat = 'V'

          invoice_obj.xml = stamp_obj.xml_signed
          invoice_obj.internal_notes = internal_notes

          invoice_obj.save()
        
          context.update({
            'success': True,
            'message': 'La petición se proceso exitosamente.',
            'invoice': invoice_obj.encrypt,
            'data': {
              'UUID': invoice_obj.uuid,
              'rfc': invoice_obj.taxpayer_id,
              'rrfc': invoice_obj.rtaxpayer_id,
              'total': invoice_obj.total,
            }

          })
          # Log.objects.log_action(request, 5, 'C', '{}'.format(context['message']), 'I')
        else:
          stamp_error = errors.get(stamp_obj.error_code.__str__(), {}).get('message')
          stamp_message = f'<div><strong>{stamp_obj.error_code}</strong> - <small class="lead">{stamp_error}</small></div>'
          context.update({
            'success': False,
            'message': f'Tu comprobante no pudo ser timbrado',
            'error': stamp_message
          })
      else:
        context.update({
          'success': False,
          'message': u'Hubo un error al procesar la petición, si cfdi '
        })'''
    except Exception as e:
      print(f'Ocurrio un error handler post_invoice {e}')
      context.update({
          'success': False,
          'message': _('There was an error processing the request')
      })
    return context


def get_context(request, business=None, sat_file=None, _type='invoice'):

    context = {}

    add_concept = ''
    concept_name = ''
    address = business.address

    form_data = None
    form_initital_data = {"initial": {"user": request.user},  "pagos": None}
    fiscal_regime_code = business.fiscal_regime

    if _type == 'invoice':
      pass
    elif _type == 'payment':
      concept_name = 'Pago'
      add_concept = 'pagos'
      form_initital_data['pagos'] = {"concepto": {'claveprodserv': '84111506',
                                                  'claveunidad': 'ACT',
                                                  'descripcion': 'Pago',
                                                  'valorunitario': '0',
                                                  'cantidad': '1',
                                                  'importe': '0', },
                                     'comprobante': {
          'tipodecomprobante': 'P',
          'moneda': 'XXX',
          'subtotal': '0',
          'total': '0',
      }, 'receptor': {'usocfdi': 'P01', }
      }

    invoice_form = InvoiceForm(form_data, **form_initital_data)

    context = {
        'no_cer': sat_file.serial if sat_file and hasattr(sat_file, 'serial') else '',
        'validity': sat_file.expiration_date if sat_file and hasattr(sat_file, 'expiration_date') else '',
        'business_name': business.name,
        'business_taxpayer_id': business.taxpayer_id,
        #'business_fiscal_regime': '{} - {}'.format(fiscal_regime_code, FISCAL_REGIME_DICT[fiscal_regime_code]),
        'invoice_form': invoice_form,
        'relations_type': TipoRelacion.objects.all(),
        'tax_template': render_to_string('invoicing/strings/invoice-tax-template.html', {}, request),
        'add_concept': add_concept,
        'concept_name': concept_name,
    }

    return context
