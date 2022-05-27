from lxml import etree
from copy import deepcopy

from reportlab.pdfgen import canvas
from reportlab.platypus import (
  BaseDocTemplate,
  PageTemplate,
  SimpleDocTemplate,
  Frame,
  Paragraph,
  Image,
  Spacer,
  Table,
  TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter, inch
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.graphics.barcode import code93, code128, code39
import sys
from decimal import Decimal
from datetime import datetime
from pdb import set_trace

class CreatePDF(object):
  def __init__(self, xml_string, filename):
    self.style_title = ParagraphStyle('Caption', fontSize=10, leading=12, textColor=colors.white)
    self.style_header = ParagraphStyle('Caption', fontSize=10, leading=11)
    self.style_content = ParagraphStyle('Caption', fontSize=8, leading=15)
    self.style_content_header = ParagraphStyle('Caption', fontSize=8, leading=10)
    self.style_totals = ParagraphStyle('Caption', fontSize=8, alignment=TA_RIGHT)
    self.style_total = ParagraphStyle('Caption', fontSize=10, alignment=TA_RIGHT)

    self.style_sign_tittle = ParagraphStyle('Caption', fontSize=10, alignment=TA_LEFT)
    self.style_signature = ParagraphStyle('Caption', fontSize=8, alignment=TA_LEFT)

    self.bg_color = colors.Color(red=(0.188), green=(0.486), blue=(0.509))
    self.success = False
    #import pdb; pdb.set_trace()
    #wxml_string = xml_string.read()
    self.filename = filename
    self.status = 'V'
    self.pdf_path = ''
    self.page_cont_canvas = 0
    #xml_string = open('/home/jroque/Downloads/xml.xml', 'r').read()
    try:
      xml_parser = etree.XMLParser(remove_blank_text=True)
      xml_string_car = bytes((xml_string.decode('utf-8').replace('&aacute;', '&#225;').replace('&eacute;', "&#233;").replace('&iacute;', "&#237;").replace('&oacute;', "&#243;")
      .replace('&uacute;', "&#250;").replace('&Aacute;', "&#193;").replace('&Eacute;', "&#201;").replace('&Iacute;', "&#205;")
      .replace('&Oacute;', "&#211;").replace('&Uacute;', "&#218;").replace('&ntilde;', "&#209;").replace('&Ntilde;', "&#241;")), encoding='utf-8')
      # print(bytes(xml_string_car, encoding='utf-8'))
      
      if isinstance(xml_string_car, bytes):
        xml_etree = etree.fromstring(xml_string_car, parser=xml_parser)
      else:
        xml_etree = etree.fromstring(bytes(bytearray(xml_string_car, encoding='utf-8')),parser=xml_parser)
      #try:
      #  xml_decoded = xml_string.decode('utf-8')
      #except Exception as e:
      #  try:
      #    xml_decoded = xml_string.encode('utf-8')
      #  except Exception as ex:
      #    print(f'Exception in CreatePDF (Decoding XML) => {ex}')
    except Exception as e:
      print(f'Exception in CreatePDF (XMLParser) => {e}')

    try:
      namespaces = deepcopy(xml_etree.nsmap)
      tmp_nsmap = namespaces.pop(None, None)
      if tmp_nsmap is not None:
        namespaces.update({ 'tmp': tmp_nsmap })
      ############################################# METADATA #############################################
      try:
        issue_date = xml_etree.xpath('string(./cbc:IssueDate/text())', namespaces=namespaces)
        issue_time = xml_etree.xpath('string(./cbc:IssueTime/text())', namespaces=namespaces)
        str_date = str(issue_date) + " " + str(issue_time)
        issue_datetime = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S').replace(microsecond=0).isoformat()

        self.metadata = {
          'identifier': xml_etree.xpath('string(./cbc:ID/text())', namespaces=namespaces),
          'buyer_reference': xml_etree.xpath('string(./cbc:BuyerReference/text())', namespaces=namespaces),
          # 'issue_date': xml_etree.xpath('string(./cbc:IssueDate/text())', namespaces=namespaces),
          'issue_date': issue_datetime,
          'due_date': xml_etree.xpath('string(./cbc:DueDate/text())', namespaces=namespaces),
          'accounting_cost': xml_etree.xpath('string(./cbc:AccountingCost/text())', namespaces=namespaces),
          'currency': xml_etree.xpath('string(./cbc:DocumentCurrencyCode/text())', namespaces=namespaces)
        }
      except Exception as e:
        print(f'Exception in CreatePDF (METADATA) => {e}')
      ####################################################################################################
      ############################################## SUPPLIER ############################################
      try:
        supplier_name = xml_etree.xpath('string(./cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name/text())', namespaces=namespaces)
        
        supplier_taxpayer_id = xml_etree.xpath('string(./cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID/text())', namespaces=namespaces)
        supplier_street = xml_etree.xpath('string(./cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName/text())', namespaces=namespaces)
        supplier_extra = xml_etree.xpath('string(./cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName/text())', namespaces=namespaces)
        supplier_city = xml_etree.xpath('string(./cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName/text())', namespaces=namespaces)
        supplier_postal = xml_etree.xpath('string(./cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone/text())', namespaces=namespaces)
        supplier_country = xml_etree.xpath('string(./cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode/text())', namespaces=namespaces)
        supplier_code_tech = xml_etree.xpath('//cac:AccountingSupplierParty/cac:Party/cbc:EndpointID', namespaces=namespaces)
        supplier_cont_tech = xml_etree.xpath('string(./cac:AccountingSupplierParty/cac:Party/cbc:EndpointID/text())', namespaces=namespaces)
        supplier_tax_id = xml_etree.xpath('string(./cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID/text())', namespaces=namespaces)
        supplier_banking_code = xml_etree.xpath('//cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID', namespaces=namespaces)
        supplier_banking_reference = xml_etree.xpath('string(./cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID/text())', namespaces=namespaces)
        supplier_legal_name = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName/text())', namespaces=namespaces)
        supplier_legal_company_code = xml_etree.xpath('//cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID', namespaces=namespaces)
        supplier_legal_company_text = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/text())', namespaces=namespaces)

        self.supplier = {
          'name': supplier_name,
          'address': {
            'street': supplier_street,
            'extra': supplier_extra,
            'city': supplier_city,
            'postal': supplier_postal,
            'country': supplier_country,
          },
          'technical_address': "{}{}".format(supplier_code_tech[0].get('schemeID') + ':' if supplier_code_tech and supplier_code_tech[0].get('schemeID') else '', supplier_cont_tech),
          'tax_identification': f"VAT:{supplier_tax_id}",
          'banking_reference': "{}{}".format(supplier_banking_code[0].get('schemeID') + ':' if supplier_banking_code and supplier_banking_code[0].get('schemeID') and supplier_banking_code[0].get('schemeID') else '', supplier_banking_reference),
          'legal_info': {
            'name': supplier_legal_name,
            'company': '{}{}'.format(supplier_legal_company_code[0].get('schemeID') + ':' if supplier_legal_company_code and supplier_legal_company_code[0].get('schemeID') else '',  supplier_legal_company_text)
          }, 
          'supplier_taxpayer_id': supplier_taxpayer_id
        }
      except Exception as e:
        print(f'Exception in CreatePDF (SUPPLIER) => {e}')
      ####################################################################################################
      ############################################# CUSTOMER #############################################
      # set_trace()
      try:
        customer_name = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name/text())', namespaces=namespaces)
        customer_street = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName/text())', namespaces=namespaces)
        #customer_extra = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName/text())', namespaces=namespaces)
        customer_city = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName/text())', namespaces=namespaces)
        customer_postal = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone/text())', namespaces=namespaces)
        customer_country = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode/text())', namespaces=namespaces)
        #customer_code_tech = xml_etree.xpath('//cac:AccountingCustomerParty/cac:Party/cbc:EndpointID', namespaces=namespaces)
        #customer_cont_tech = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cbc:EndpointID/text())', namespaces=namespaces)
        # customer_contact_name = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name/text())', namespaces=namespaces)
        customer_contact_name = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name/text())', namespaces=namespaces)
        customer_contact_phone = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Telephone/text())', namespaces=namespaces)
        customer_contact_email = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:ElectronicMail/text())', namespaces=namespaces)
        customer_taxpayer_id = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID/text())', namespaces=namespaces)
        #customer_tax_id = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID/text())', namespaces=namespaces)
        customer_banking_code = xml_etree.xpath('//cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID', namespaces=namespaces)
        customer_banking_reference = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID/text())', namespaces=namespaces)
        customer_legal_name = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName/text())', namespaces=namespaces)
        #customer_legal_company_code = xml_etree.xpath('//cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID', namespaces=namespaces)
        #customer_legal_company_text = xml_etree.xpath('string(./cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/text())', namespaces=namespaces)
        # set_trace()
        self.customer = {
          'name': customer_name,
          'address': {
            'street': customer_street,
            #'extra': customer_extra,
            'city': customer_city,
            'postal': customer_postal,
            'country': customer_country,
          },
          #'technical_address': '{}{}'.format(customer_code_tech[0].get('schemeID') + ':' if customer_code_tech and customer_code_tech[0].get('schemeID') else '', customer_cont_tech),
          #'tax_identification': f'VAT:{customer_tax_id}',
          'banking_reference': '{}{}'.format(customer_banking_code[0].get('schemeID') + ':' if customer_banking_code and customer_banking_code[0].get('schemeID') else '', customer_banking_code),
          'legal_info': {
            'name': customer_legal_name,
            #'company': '{}{}'.format(customer_legal_company_code[0].get('schemeID') + ':' if customer_legal_company_code and customer_legal_company_code[0].get('schemeID') else '', customer_legal_company_text),
          },
          'contact': {
            'name': customer_contact_name,
            'phone': customer_contact_phone,
            'email': customer_contact_email,
            'taxpayer_id': customer_taxpayer_id,
          }
        }
      except Exception as e:
        print(f'Exception in CreatePDF (CUSTOMER) => {e}')
      ######################################################################################################
      ############################################# DELIVERY ###############################################
      try:
        deliver_name = xml_etree.xpath('string(./cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name/text())', namespaces=namespaces)
        delivery_date = xml_etree.xpath('string(./cac:Delivery/cbc:ActualDeliveryDate/text())', namespaces=namespaces)
        delivery_loc_code = xml_etree.xpath('//cac:Delivery/cac:DeliveryLocation/cbc:ID', namespaces=namespaces)
        delivery_loc_text = xml_etree.xpath('string(./cac:Delivery/cac:DeliveryLocation/cbc:ID/text())', namespaces=namespaces)
        deliver_street = xml_etree.xpath('string(./cac:Delivery/cac:DeliveryLocation/cac:Address/cbc:StreetName/text())', namespaces=namespaces)
        delivery_extra = xml_etree.xpath('string(./cac:Delivery/cac:DeliveryLocation/cac:Address/cbc:AdditionalStreetName/text())', namespaces=namespaces)
        delivery_city = xml_etree.xpath('string(./cac:Delivery/cac:DeliveryLocation/cac:Address/cbc:CityName/text())', namespaces=namespaces)
        delivery_postal = xml_etree.xpath('string(./cac:Delivery/cac:DeliveryLocation/cac:Address/cbc:PostalZone/text())', namespaces=namespaces)
        delivery_country = xml_etree.xpath('string(./cac:Delivery/cac:DeliveryLocation/cac:Address/cac:Country/cbc:IdentificationCode/text())', namespaces=namespaces)

        self.delivery = {
          'name': deliver_name,
          'date': delivery_date,
          'address': {
            'street': deliver_street,
            'extra': delivery_extra,
            'city': delivery_city,
            'postal': delivery_postal,
            'country': delivery_country,
          },
          'location': '{}{}'.format(delivery_loc_code[0].get('schemeID') + ':' if delivery_loc_code and delivery_loc_code[0].get('schemeID') else '', delivery_loc_text),
        }
      except Exception as e:
        print(f'Exception in CreatePDF (DELIVERY) => {e}')
      ######################################################################################################
      ########################################### PAYMENT ############################################
      try:
        payment_id = xml_etree.xpath('string(./cac:PaymentMeans/cbc:PaymentID/text())', namespaces=namespaces)
        payment_code_name = xml_etree.xpath('//cac:PaymentMeans/cbc:PaymentMeansCode', namespaces=namespaces)
        payment_code_code = xml_etree.xpath('string(./cac:PaymentMeans/cbc:PaymentMeansCode/text())', namespaces=namespaces)
        payment_account_id = xml_etree.xpath('string(./cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID/text())', namespaces=namespaces)
        payment_account_name = xml_etree.xpath('string(./cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name/text())', namespaces=namespaces)
        payment_financial_id = xml_etree.xpath('string(./cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID/text())', namespaces=namespaces)
        # payment_terms = xml_etree.xpath('string(./cac:PaymentTerms/cbc:Note/text())', namespaces=namespaces)
        # set_trace()
        # payment_name_code = xml_etree.xpath('string(./cac:PaymentMeans/cbc:PaymentMeansCode/text())')
        # payment_name = xml_etree.find('cac:PaymentMeans/cbc:PaymentMeansCode')

        self.payment = {
          'id': payment_id,
          'account': {
            'id': payment_account_id,
            'name': payment_account_name,
          },
          'financial': payment_financial_id,
          'code': payment_code_code,
          # 'terms': payment_terms,
          'terms': '{}-{}'.format(payment_code_code, payment_code_name)
        }
      except Exception as e:
        print(f'Exception in CreatePDF (PAYMENT) => {e}')
      ######################################################################################################
      ############################################## DETAILS ###############################################
      try:
        self.details = []
        all_charges = xml_etree.findall('cac:AllowanceCharge', namespaces=namespaces)#[1].xpath('string(./cbc:AllowanceChargeReason)', namespaces=namespaces)
        for charge in all_charges:
          details_indicator = charge.xpath('string(./cbc:ChargeIndicator/text())', namespaces=namespaces)
          details_reason = charge.xpath('string(./cbc:AllowanceChargeReason)', namespaces=namespaces)
          details_amount_text = charge.xpath('string(./cbc:Amount//text())', namespaces=namespaces)
          details_ammount_currency = charge.xpath('cbc:Amount', namespaces=namespaces)
          details_category_id = charge.xpath('string(./cac:TaxCategory/cbc:ID/text())', namespaces=namespaces)
          details_category_percent = charge.xpath('string(./cac:TaxCategory/cbc:Percent/text())', namespaces=namespaces)
          details_category_tax_id = charge.xpath('string(./cac:TaxCategory/cac:TaxScheme/cbc:ID/text())', namespaces=namespaces)

          details_data = {
            'indicator': details_indicator,
            'reason': details_reason,
            'amount': f"{details_amount_text} {details_ammount_currency[0].get('currencyID') if details_ammount_currency else ''}",
            'category': f"{details_category_tax_id}:{details_category_id} ({details_category_percent}%)"
          }
          self.details.append(details_data)

      except Exception as e:
        print(f'Exception in CreatePDF (DETAILS) => {e}')
      ######################################################################################################
      ################################################ TAX #################################################
      try:
        tax_amount_currency = xml_etree.xpath('//cac:TaxTotal/cbc:TaxAmount', namespaces=namespaces)
        tax_amount_text = xml_etree.xpath('string(./cac:TaxTotal/cbc:TaxAmount/text())', namespaces=namespaces)
        tax_subtotal_taxable_amount_currency = xml_etree.xpath('//cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount', namespaces=namespaces)
        tax_subtotal_taxable_amount_text = xml_etree.xpath('string(./cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount/text())', namespaces=namespaces)
        tax_subtotal_tax_amount_currency = xml_etree.xpath('//cac:TaxTotal/cac:TaxSubtotal/cbc:TaxAmount', namespaces=namespaces)
        tax_subtotal_tax_amount_text = xml_etree.xpath('string(./cac:TaxTotal/cac:TaxSubtotal/cbc:TaxAmount/text())', namespaces=namespaces)
        tax_subtotal_category_id = xml_etree.xpath('string(./cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID/text())', namespaces=namespaces)
        tax_subtotal_category_percent = xml_etree.xpath('string(./cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent/text())', namespaces=namespaces)
        tax_subtotal_category_taxscheme_id = xml_etree.xpath('string(./cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID/text())', namespaces=namespaces)

        self.tax = {
          'tax_amount': f"{self.truncate(Decimal(tax_amount_text),2)} {tax_amount_currency[0].get('currencyID') if tax_amount_currency and tax_amount_currency[0].get('currencyID') else ''}",
          'sub_taxable_amount': f"{self.truncate(Decimal(tax_subtotal_taxable_amount_text if tax_subtotal_taxable_amount_text else '0.0'),2)} {tax_subtotal_taxable_amount_currency[0].get('currencyID') if tax_subtotal_taxable_amount_currency and tax_subtotal_taxable_amount_currency[0].get('currencyID') else ''}",
          'sub_tax_amount': f"{self.truncate(Decimal(tax_subtotal_tax_amount_text if tax_subtotal_tax_amount_text else '0.0'),2)} {tax_subtotal_tax_amount_currency[0].get('currencyID') if tax_subtotal_tax_amount_currency and tax_subtotal_tax_amount_currency[0].get('currencyID') else ''}",
          'category': f'{tax_subtotal_category_taxscheme_id}:{tax_subtotal_category_id} ({tax_subtotal_category_percent}%)',
        }
      except Exception as e:
        print(f'Exception in CreatePDF (TAX) => {e}')
      ######################################################################################################
      ############################################### TOTALS ###############################################
      try:
        total_line_extension_currency = xml_etree.xpath('//cac:LegalMonetaryTotal/cbc:LineExtensionAmount', namespaces=namespaces)
        # total_line_extension_currency = xml_etree.xpath('//cac:InvoiceLine/cbc:LineExtensionAmount', namespaces=namespaces)
        total_line_extension_text = xml_etree.xpath('string(./cac:LegalMonetaryTotal/cbc:LineExtensionAmount/text())', namespaces=namespaces)
        
        total_tax_exclusive_currency = xml_etree.xpath('//cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount', namespaces=namespaces)
        total_tax_exclusive_text = xml_etree.xpath('string(./cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount/text())', namespaces=namespaces)
        total_tax_inclusive_currency = xml_etree.xpath('//cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount', namespaces=namespaces)
        total_tax_inclusive_text = xml_etree.xpath('string(./cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount/text())', namespaces=namespaces)
        total_charge_currency = xml_etree.xpath('//cac:LegalMonetaryTotal/cbc:ChargeTotalAmount', namespaces=namespaces)
        total_charge_text = xml_etree.xpath('string(./cac:LegalMonetaryTotal/cbc:ChargeTotalAmount/text())', namespaces=namespaces)
        total_payable_currency = xml_etree.xpath('//cac:LegalMonetaryTotal/cbc:PayableAmount', namespaces=namespaces)
        total_payable_text = xml_etree.xpath('string(./cac:LegalMonetaryTotal/cbc:PayableAmount/text())', namespaces=namespaces)
        total_prepaid_currency = xml_etree.xpath('//cac:LegalMonetaryTotal/cbc:PrepaidAmount', namespaces=namespaces)
        total_prepaid = xml_etree.xpath('string(./cac:LegalMonetaryTotal/cbc:PrepaidAmount/text())', namespaces=namespaces)

        payment_means = xml_etree.xpath('//cac:PaymentMeans/cbc:PaymentMeansCode', namespaces=namespaces)[0]
        payment_code_code = xml_etree.xpath('string(./cac:PaymentMeans/cbc:PaymentMeansCode/text())', namespaces=namespaces)
        note = xml_etree.xpath('string(./cbc:Note/text())', namespaces=namespaces)
        
        
        items = xml_etree.findall('cac:InvoiceLine', namespaces=namespaces)
        discount_total = 0
        for item in items:
          discount_total += float(item.xpath('string(./cac:AllowanceCharge/cbc:Amount/text())', namespaces=namespaces))
        
        namespaces['ext'] = 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2'
        namespaces['ds'] = 'http://www.w3.org/2000/09/xmldsig#'
        ubl_extensions = xml_etree.findall('ext:UBLExtensions', namespaces=namespaces)[0]
        signature = ubl_extensions.xpath('string(//ext:ExtensionContent/ds:Signature/ds:SignatureValue/text())', namespaces=namespaces).replace('\n', '')

        self.totals = {
          'line_extension': f"{self.truncate(Decimal(total_line_extension_text),2)} {total_line_extension_currency[0].get('currencyID') if total_line_extension_currency else ''}",
          'discount_total': f"{self.truncate(Decimal(discount_total),2)} {total_line_extension_currency[0].get('currencyID') if discount_total else ''}",
          'tax_exclusive': f"{self.truncate(Decimal(total_tax_exclusive_text),2)} {total_line_extension_currency[0].get('currencyID') if total_line_extension_currency else ''}",
          'tax_inclusive': f"{self.truncate(Decimal(total_tax_inclusive_text),2)} {total_tax_inclusive_currency[0].get('currencyID') if total_tax_inclusive_currency else ''}",
          'payable': f"{self.truncate(Decimal(total_payable_text),2)} {total_payable_currency[0].get('currencyID') if total_payable_currency else ''}",
          'charge': f"{self.truncate(Decimal(total_charge_text if total_charge_text else '0'),2)} {total_charge_currency[0].get('currencyID') if total_charge_currency else ''}",
          'prepaid': f"{self.truncate(Decimal(total_prepaid if total_prepaid else '0.0'), 2)} {total_prepaid_currency[0].get('currencyID') if total_prepaid else None}",
          
          'terms': '{}-{}'.format(payment_code_code, payment_means.values()[0]),
          'signature': signature,
          'note': note
        }
      except Exception as e:
        print(f'Exception in CreatePDF (TOTALS) => {e}')
      ######################################################################################################
      ############################################### ITEMS ################################################
      try:
        items = xml_etree.findall('cac:InvoiceLine', namespaces=namespaces)
        currency = xml_etree.xpath('string(./cbc:DocumentCurrencyCode/text())', namespaces=namespaces)
        self.items_list = []
        for item in items:
          try:
            inv_id = item.xpath('string(./cbc:ID/text())', namespaces=namespaces)
            inv_day_text = item.xpath('string(./cbc:InvoicedQuantity/text())', namespaces=namespaces)
            inv_day_code = item.xpath('cbc:InvoicedQuantity', namespaces=namespaces)
            inv_line_extension_text = item.xpath('string(./cbc:LineExtensionAmount/text())', namespaces=namespaces)
            inv_line_extension_code = item.xpath('cbc:LineExtensionAmount', namespaces=namespaces)
            inv_accounting_cost = item.xpath('string(./cbc:AccountingCost/text())', namespaces=namespaces)
            inv_order_line = item.xpath('string(./cac:OrderLineReference/cbc:LineID/text())', namespaces=namespaces)
            inv_price_text = item.xpath('string(./cac:Price/cbc:PriceAmount/text())', namespaces=namespaces)
            inv_price_currency = item.xpath('cac:Price/cbc:PriceAmount', namespaces=namespaces)
            
            
            # item_quantity = item.xpath('string(.cbc/cbc:InvoicedQuantity/text())', namespaces=namespaces)

            item_id_text = item.xpath('string(./cac:Item/cac:StandardItemIdentification/cbc:ID/text())', namespaces=namespaces)
            item_id_code = item.xpath('cac:Item/cac:StandardItemIdentification/cbc:ID', namespaces=namespaces)
            item_name = item.xpath('string(./cac:Item/cbc:Name/text())', namespaces=namespaces)
            item_desc = item.xpath('string(./cac:Item/cbc:Description/text())', namespaces=namespaces)
            item_country = item.xpath('string(./cac:Item/cac:OriginCountry/cbc:IdentificationCode/text())', namespaces=namespaces)
            item_discount_text = item.xpath('string(./cac:AllowanceCharge/cbc:Amount/text())', namespaces=namespaces)
            item_commodity_text = item.xpath('string(./cac:Item/cac:CommodityClassification/cbc:ItemClassificationCode/text())', namespaces=namespaces)
            item_commodity_code = item.xpath('cac:Item/cac:CommodityClassification/cbc:ItemClassificationCode', namespaces=namespaces)
            item_tax_id = item.xpath('string(./cac:Item/cac:ClassifiedTaxCategory/cbc:ID/text())', namespaces=namespaces)
            item_tax_percent = item.xpath('string(./cac:Item/cac:ClassifiedTaxCategory/cbc:Percent/text())', namespaces=namespaces)
            # item_tax_amount = item.xpath('string(./cac:AllowanceCharge/cbc:Amount/text())', namespaces=namespaces)
            item_tax_scheme_id = item.xpath('string(./cac:Item/cac:ClassifiedTaxCategory/cac:TaxScheme/cbc:ID/text())', namespaces=namespaces)
            
            try:
              unit_price = Decimal(self.truncate(Decimal(inv_line_extension_text)/Decimal(inv_day_text),2))
            except:
              unit_price = Decimal(str(self.truncate(Decimal(inv_line_extension_text)/Decimal(inv_day_text),2)).replace(',', ''))
            
            try:
              discount = Decimal(self.truncate(Decimal(item_discount_text), 2))
            except:
              discount = Decimal(str(self.truncate(Decimal(item_discount_text), 2)).replace(',', ''))

            import math
            from app.cfdi.utils.validate.adicionales import trunc
            from app.sat.utils.validate import Catalogos

            catalogos_obj = Catalogos(datetime.now())
            currency_obj = catalogos_obj.obtener('Moneda', currency)
            decimales = currency_obj.decimales
            amount = Decimal(trunc(((Decimal(unit_price)*Decimal(inv_day_text))-Decimal(discount)), 6, False))
            percent = Decimal(item_tax_percent) if item_tax_percent != '' else Decimal(0.0)
            total_tax_item = trunc(((percent * amount)/100), 6, False)
            # print(amount)

            print("========================")
            decimal, entera = math.modf(Decimal(total_tax_item))
            print("Decimal")
            print(decimal)
            print("Entera")
            print(entera)
            print("========================")

            is_round = int(str(round(decimal, 3)).replace('0.', '')) % 2
            _list = list(str(round(decimal, 3)).replace('0.', ''))
            print(_list)
            if len(_list) == 3:
              if int(_list[2]) == 0:
                subtotal_taxes_trunc = round(trunc((Decimal(total_tax_item)), 6, True), 2)
              elif int(_list[2]) > 0:
                subtotal_taxes_trunc = trunc((Decimal(total_tax_item)), decimales, True)
            else:
              subtotal_taxes_trunc = round(trunc((Decimal(total_tax_item)), 6, True), 2)
            
            print("Subtotal tax trunc")
            print(subtotal_taxes_trunc)
            

            values_item = {
              'inv_id': inv_id,
              'inv_day': f"{inv_day_text}/{inv_day_code[0].get('unitCode') if inv_day_code else ''}",
              'inv_amount': f"{self.truncate(Decimal(inv_line_extension_text), 2)} {inv_line_extension_code[0].get('currencyID') if inv_line_extension_code else ''}",
              'inv_accounting_cost': inv_accounting_cost,
              'inv_order_line': inv_order_line,
              'item': {
                'item_id': f"{item_id_code[0].get('schemeID') if item_id_code else ''}:{item_id_text}",
                'item_name': item_name,
                'item_desc': item_desc,
                'item_country': item_country,
                'item_commodity': f"{item_commodity_code[0].get('listID') if item_commodity_code else ''}:{item_commodity_text}",
                # 'item_tax': f"{item_tax_scheme_id}:{item_tax_id}({item_tax_percent}%)",
                'item_tax': f"{item_tax_percent if item_tax_percent != '' else '0.0'}% - {subtotal_taxes_trunc} {inv_line_extension_code[0].get('currencyID') if inv_line_extension_code else ''}",
                'item_discount': f"{self.truncate(Decimal(item_discount_text), 2)} {inv_line_extension_code[0].get('currencyID') if item_discount_text else ''}",
              },
              'price': f"{self.truncate(Decimal(inv_line_extension_text)/Decimal(inv_day_text),2)} {inv_price_currency[0].get('currencyID') if inv_price_currency else ''}"
            }
            self.items_list.append(values_item)
          except Exception as e:
            print(f'Exception in CreatePDF (ITEM) => {e}')

        self.success = self.tables_builder()
      except Exception as e:
        print(f'Exception in CreatePDF (ITEMS) => {e}')
      ######################################################################################################
    except Exception as e:
      print(f'Exception in CreatePDF (XMLContent) => {e}')

  def settings(self, canvas, doc):
    try:
      self.page_cont_canvas += 1
      canvas.saveState()
      canvas.setFont('Helvetica-Bold', 8)
      canvas.setFillColor(HexColor('#555759'))
      canvas.drawString(0.2*inch, 0.5*inch, 'Document')
      canvas.drawString(1.28*inch, 0.5*inch, 'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2::Invoice')
      canvas.drawString(0.2*inch, 0.35*inch, 'Customization')
      canvas.drawString(1.28*inch, 0.35*inch, 'urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0')
      canvas.drawString(0.2*inch, 0.2*inch, 'Profile')
      canvas.drawString(1.28*inch, 0.2*inch, 'urn:fdc:peppol.eu:2017:poacc:billing:01:1.0')
      # if self.page_cont_canvas == 1:
      self.header(canvas)

      canvas.restoreState()
    except Exception as e:
      print(f'Exception in settings => {e}')

  def tables_builder(self):
    try:
      success = False
      story = []
      table_concepts = self.concepts()
      table_totals, table_payable, table_terms, table_signature = self.totals_data()
      table_header, table_customer = self.header_info()
      # story.append(table_invoice)
      story.append(table_header)
      story.append(table_customer)
      table_delivery = self.delivery_payment_data()
      story.append(table_concepts)
      # story.append(Spacer(0,10))
      story.append(table_totals)
      story.append(table_payable)
      story.append(table_terms)
      story.append(Spacer(0,10))
      story.append(table_signature)
      # story.append(table_delivery)

      frame = Frame(inch, 0, 465, 520, leftPadding=0, bottomPadding=0, rightPadding=0, topPadding=-235, showBoundary=0)
      header = PageTemplate(id='header', frames=frame, onPage=self.settings)
      self.filename 
      self.pdf_path = f'/tmp/{self.filename}'
      #self.pdf_path = '/tmp/{}_{}.pdf'.format(self.metadata.get('identifier'), datetime.now().replace(microsecond=0).isoformat())
      self.doc = BaseDocTemplate(self.pdf_path, pageTemplates=[header], pagesize=letter)
      self.doc.build(story, canvasmaker=NumberedCanvas)

      success = True
    except Exception as e:
      print(f'Exception in  tables_builder => {e}')

    return success

  def header_info(self):
    try:

      header_data = []
      supplier_name = self.supplier.get('name')
      supplier_street = self.supplier.get('address').get('street')
      supplier_extra = self.supplier.get('address').get('extra')
      supplier_city = self.supplier.get('address').get('city')
      supplier_postal = self.supplier.get('address').get('postal')
      supplier_country = self.supplier.get('address').get('country')
      supplier_tech = self.supplier.get('technical_address')
      supplier_tax = self.supplier.get('tax_identification')
      supplier_banking = self.supplier.get('banking_reference')

      metadata_id = self.metadata.get('identifier')
      metadata_buyer = self.metadata.get('buyer_reference')
      metadata_issue = self.metadata.get('issue_date')
      metadata_due = self.metadata.get('due_date')
      metadata_acc = self.metadata.get('accounting_cost')
      metadata_curr = self.metadata.get('currency')

      customer_data = []
      #customer_name = self.customer.get('name')
      customer_street = self.customer.get('address').get('street')
      #customer_extra = self.customer.get('address').get('extra')
      customer_city = self.customer.get('address').get('city')
      customer_postal = self.customer.get('address').get('postal')
      customer_country = self.customer.get('address').get('country')
      #customer_tech = self.customer.get('technical_address')
      #customer_tax = self.customer.get('tax_identification')
      #customer_banking = self.customer.get('banking_reference')
      customer_contact_name = self.customer.get('contact').get('name')
      customer_contact_phone = self.customer.get('contact').get('phone')
      customer_contact_email = self.customer.get('contact').get('email')
      customer_taxpayer_id = self.customer.get('contact').get('taxpayer_id')
      customer_legal_name = self.customer.get('legal_info').get('name')
      #customer_legal_company = self.customer.get('legal_info').get('company')


      tag_banking = Paragraph('<b>Banking Reference: </b>', self.style_content_header)
      tag_tax = Paragraph('<b>Tax Identification: </b>', self.style_content_header)
      tag_tech = Paragraph('<b>Technical Address: </b>', self.style_content_header)

      tag_id = Paragraph('<b>Identifier: </b>', self.style_content_header)
      tag_buyer = Paragraph('<b>Buyer Refernece: </b>', self.style_content_header)
      tag_issue = Paragraph('<b>Issue Date: </b>', self.style_content_header)
      tag_due = Paragraph('<b>Due Date: </b>', self.style_content_header)
      # tag_acc = Paragraph('<b>Accounting Cost: </b>', self.style_content_header)
      tag_curr = Paragraph('<b>Currency: </b>', self.style_content_header)

      p_name = Paragraph('<b>{}</b>'.format(supplier_name), self.style_content_header)
      p_street = Paragraph(supplier_street, self.style_content_header)
      p_extra = Paragraph(supplier_extra, self.style_content_header)
      p_postal_and_city = Paragraph('{} {}'.format(supplier_postal, supplier_city), self.style_content_header)
      p_country = Paragraph(supplier_country, self.style_content_header)

      p_id = Paragraph(metadata_id, self.style_content_header)
      p_buyer = Paragraph(metadata_buyer, self.style_content_header)
      p_issue = Paragraph(metadata_issue, self.style_content_header)
      p_due = Paragraph(metadata_due, self.style_content_header)
      # p_acc = Paragraph(metadata_acc, self.style_content_header)
      p_curr = Paragraph(metadata_curr, self.style_content_header)

      #p_cust_name = Paragraph('<b>{}</b>'.format(customer_name), self.style_content_header)
      p_cust_street = Paragraph(customer_street, self.style_content_header)
      #p_cust_extra = Paragraph(customer_extra, self.style_content_header)
      p_cust_postal_and_city = Paragraph('{} {}'.format(customer_postal, customer_city), self.style_content_header)
      p_cust_country = Paragraph(customer_country, self.style_content_header)
      p_contact_name = Paragraph(customer_contact_name, self.style_content_header)
      p_contact_phone = Paragraph(customer_contact_phone, self.style_content_header)
      p_contact_email = Paragraph(customer_contact_email, self.style_content_header)
      p_legal_name = Paragraph(customer_legal_name, self.style_content_header)
      p_taxpayer_id = Paragraph(customer_taxpayer_id, self.style_content_header)
      #p_legal_comp = Paragraph(customer_legal_company, self.style_content_header)

      header_data.append([[
          Paragraph('<b>SUPPLIER</b>', self.style_title),
        ],[
          Paragraph('<b>METADATA</b>', self.style_title)
          ]
        ])
      header_data.append([
         [
          p_name,
          Paragraph('<b>{}</b>'.format(self.supplier.get('supplier_taxpayer_id')), self.style_content_header),
          p_street,
          # p_extra,#Chido
          p_postal_and_city,
          p_country,
          Paragraph('<b>&nbsp;</b>', self.style_content_header),
          Paragraph('<b>&nbsp;</b>', self.style_content_header),
        ], [
          tag_id,
          tag_buyer,
          tag_issue,
          tag_curr,
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
        ], [
          p_id,
          # p_buyer,
          p_issue,
          p_due,
          # p_acc,
          p_curr,
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
        ],
      ])

      customer_data.append([[
        Paragraph('<b>CONTACT</b>', self.style_title),
      ],[
        Paragraph('<b>&nbsp;</b>', self.style_title)
        ], [
        Paragraph('<b>CUSTOMER</b>', self.style_title)
      ]
      ])

      customer_data.append([
        [
          #p_cust_name,
          p_cust_street,
          #p_cust_extra,
          p_cust_postal_and_city,
          p_cust_country,
          Paragraph('<b>&nbsp;</b>', self.style_content_header),
        ], [
          p_legal_name,
          #p_legal_comp,
          Paragraph('<b>&nbsp;</b>', self.style_content_header),
          Paragraph('<b>&nbsp;</b>', self.style_content_header),
          Paragraph('<b>&nbsp;</b>', self.style_content_header),
        ], [
          p_contact_name,
          p_taxpayer_id,
          # p_contact_phone,
          # p_contact_email,
          Paragraph('<b>&nbsp;</b>', self.style_content_header),
          Paragraph('<b>&nbsp;</b>', self.style_content_header),
        ]
      ])

      table_header = Table(
        header_data,
        colWidths=[4*inch, 2.1*inch, 2.1*inch],
        style=[
          ('BACKGROUND', (0,0), (-1,0), self.bg_color),
          ('LINEBELOW', (0,0), (-1,0), 1.5, colors.lightgrey),
        ]
      )

      table_customer = Table(
        customer_data,
        colWidths=[4*inch, 2.1*inch, 2.1*inch],
        style=[
          ('BACKGROUND', (0,0), (-1,0), self.bg_color),
          ('LINEBELOW', (0,0), (-1,0), 1.5, colors.lightgrey),
        ]
      )

      
      # table_header.wrapOn(canvas, 0*inch, 0*inch)
      # table_header.drawOn(canvas, 0.15*inch, 9.2*inch)

      # table_customer.wrapOn(canvas, 0*inch, 0*inch)
      # table_customer.drawOn(canvas, 0.15*inch, 8*inch)
      
      # table_invoice.wrapOn(canvas, 0*inch, 0*inch)
      # table_invoice.drawOn(canvas, 0.15*inch, 10.5*inch)
      return table_header, table_customer
    except Exception as e:
      print(f'Exception in header_info => {e}')

  def header(self, canvas):
    try:
      table_invoice = Table(
        [[Paragraph('<b>UBL2.1</b>', ParagraphStyle('Caption', fontSize=12, alignment=TA_LEFT, leading=15)), Paragraph('<b>&nbsp;</b>', self.style_content), Paragraph('<b>COMMERCIAL INVOICE</b>', ParagraphStyle('Caption', fontSize=12, alignment=TA_CENTER, leading=15, textColor=colors.white))]],
        colWidths=[1.5*inch, 4.5*inch, 2.2*inch],
        style=[
        ('BACKGROUND', (2,0), (-1,-1), HexColor('#949191')),
        #('BACKGROUND', (0,0), (0,0), HexColor('#949191'))
        ]
      )
      table_invoice.wrapOn(canvas, 0*inch, 0*inch)
      table_invoice.drawOn(canvas, 0.15*inch, 10.5*inch)
    except Exception as e:
      print(f'Exception in header | {e}')

  def totals_data(self):
    try:
      totals_data = []
      charges_tags = []
      charges_p = []
      tag_tax = Paragraph('<b>Tax Total</b>', self.style_totals)
      #tag_charge = Paragraph('<b>Charge Total</b>', self.style_totals)
      tag_total = Paragraph('<b>Line Total</b>', self.style_totals)
      tag_discount = Paragraph('<b> Discount</b>', self.style_totals)
      tag_exclu = Paragraph('<b>Tax Exclusive</b>', self.style_totals)
      tag_inclu = Paragraph('<b>Tax Inclusive</b>', self.style_totals)
      tag_payable = Paragraph('<b>Payable</b>', self.style_total)
      tag_prepaid = Paragraph('<b>Prepaid</b>', self.style_totals)
      tag_terms = Paragraph('<b>Terms</b>', self.style_total)

      for charge in self.details:
        charges_tags.append(
          Paragraph('<b>{}</b>'.format(charge.get('reason')), self.style_totals)
        )
        charges_p.append(
          Paragraph(('-' if charge.get('reason') == 'Discount' else '+') + charge.get('amount'), self.style_totals)
        )

      # set_trace()
      p_tax = Paragraph('+{}'.format(self.tax.get('tax_amount')), self.style_totals)
      
      p_charge = Paragraph(self.totals.get('charge'), self.style_totals)
      p_total = Paragraph(self.totals.get('line_extension'), self.style_totals)
      p_exclu = Paragraph(self.totals.get('tax_exclusive'), self.style_totals)
      p_inclu = Paragraph(self.totals.get('tax_inclusive'), self.style_totals)
      p_discount = Paragraph(self.totals.get('discount_total'), self.style_totals)
      
      p_prepaid = Paragraph('-{}'.format(self.totals.get('prepaid')), self.style_totals)
      p_payable = Paragraph(self.totals.get('payable'), self.style_total)
      terms = Paragraph(self.totals.get('terms'), self.style_totals)
      p_note = Paragraph(self.totals.get('note'), self.style_signature)
      tag_note = Paragraph('<p><strong>Notes:&nbsp</strong></p><br/>\n<p>{}</p>'.format(self.totals.get('note')), self.style_sign_tittle) if self.totals.get('note') != '' else Paragraph('', self.style_sign_tittle)

      print(self.totals.get('signature'))
      totals_data.append([
        [], [
          Paragraph('<b>&nbsp;</b>', self.style_content),
          tag_total,
          tag_tax,
          tag_discount,
          charges_tags,
          tag_prepaid if self.totals.get('prepaid').split()[0] != '0.00' else Paragraph('<b></b>', self.style_content),
          tag_inclu,
        ], [
          Paragraph('<b>&nbsp;</b>', self.style_content),
          p_total,
          p_tax,
          p_discount,
          charges_p,
          p_prepaid if self.totals.get('prepaid').split()[0] != '0.00' else Paragraph('<b></b>', self.style_content),
          #p_charge,
          p_inclu,
        ], [],
      ])
      

      table_totals = Table(
        totals_data,
        colWidths=[5.2*inch,1.5*inch, 1.3*inch, 0.2*inch],
        style=[
          ('LINEBELOW', (1,0),(-1,-1), 1.5, colors.lightgrey),
          ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
          ('VALIGN', (1,-1),(-1,-1), 'TOP'),
          ('TOPPADDING', (0,1),(-1,-1), 1.5),
          ('LEFTPADDING', (0,0),(-1,-1), 0),
          ('RIGHTPADDING', (0,0),(-1,-1), 0),
        ],
      )
      table_payable = Table(
        [[], [tag_payable,p_payable], []],
        colWidths=[6.6*inch,1.5*inch, 0.2*inch],
        style=[
          ('TOPPADDING', (0,1),(-1,-1),-50),
        ]
      )

      table_terms = Table(
        [[tag_terms,terms]],
        colWidths=[6.6*inch,1.5*inch],
        style=[
          ('TOPPADDING', (0,9),(-1,-1),-50),
        ]
      )

      signature_Data = []
      signature_Data.append(
        [
          [
            Paragraph('<b>&nbsp;</b>', self.style_content), 
          ], 
          [
            Paragraph('<p><strong>Signature:&nbsp<br/>\n</strong>{}</p>'.format(self.totals.get('signature')), self.style_sign_tittle),
          ],
        ]
      )

      if self.totals.get('note') != '':
        signature_Data.append([
            [
                Paragraph('<b>&nbsp;</b>', self.style_content),
            ],
            [
                tag_note
            ]
        ])

      table_signature = Table(
        signature_Data,
        colWidths=[0.3*inch, 7.6*inch, 0.3*inch],
        style=[
          ('TOPPADDING', (0,9),(-1,-1),-50),
        ]
      )

      return table_terms, table_totals, table_payable, table_signature

    except Exception as e:
      print(f'Exception in totals_data => {e}')

  def delivery_payment_data(self):
    try:
      delivery_data = []
      tag_date = Paragraph('<b>Date</b>', self.style_content)
      tag_location = Paragraph('<b>Location</b>', self.style_content)
      tag_address = Paragraph('<b>Address</b>', self.style_content)

      tag_paymentid = Paragraph('<b>PaymentID</b>', self.style_content)
      tag_account = Paragraph('<b>Account</b>', self.style_content)

      p_date = Paragraph(self.delivery.get('date'), self.style_content)
      p_location = Paragraph(self.delivery.get('location'), self.style_content)
      p_street = Paragraph(self.delivery.get('address').get('street'), self.style_content)
      p_extra = Paragraph(self.delivery.get('address').get('extra'), self.style_content)
      p_postal_and_city = Paragraph('{} {}'.format(self.delivery.get('address').get('postal'), self.delivery.get('address').get('city')), self.style_content)
      p_country = Paragraph(self.delivery.get('address').get('country'), self.style_content)

      p_code = Paragraph(self.payment.get('code'), self.style_content)
      p_paymentid = Paragraph(self.payment.get('id'), self.style_content)
      p_account = Paragraph('{} ({})'.format(self.payment.get('account').get('id'), self.payment.get('financial')), self.style_content)
      p_terms = Paragraph('<i>{}</i>'.format(self.payment.get('terms')), self.style_content)

      delivery_data.append([
          [Paragraph('<b>DELIVERY</b>', self.style_title),],
          [Paragraph('<b>&nbsp;</b>', self.style_title),], 
          [Paragraph('<b>PAYMENT</b>', self.style_title),], 
      ])

      delivery_data.append([
        [
          tag_date,
          tag_location,
          tag_address,
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
        ], [
          p_date,
          p_location,
          p_street,
          p_extra,
          p_postal_and_city,
          p_country,
        ], [
          p_code,
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
        ], [
          tag_paymentid, 
          tag_account,
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
        ], [
          p_paymentid,
          p_account,
          p_terms,
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
          Paragraph('<b>&nbsp;</b>', self.style_content),
        ]
      ])

      delivery_data.append([[], [], [p_terms]])

      table_delivery = Table(
        delivery_data,
        colWidths=[1.5*inch, 2.5*inch, 1*inch, 1.2*inch, 2*inch],
        style=[
          ('SPAN', (2,-1), (-1,-1,)),
          ('TOPPADDING', (2,-1), (-1,-1), -100),
          ('BACKGROUND', (0,0), (-1,0), self.bg_color),
          ('TOPPADDING', (0,1), (-1,1), 10)
        ]
      )

      return table_delivery

    except Exception as e:
      print(f'Exception in delivery_data => {e}')

  def concepts(self):
    try:
      style_number = ParagraphStyle('Caption', fontSize=7, alignment=TA_CENTER)
      basic_center = ParagraphStyle('Caption', fontSize=7, alignment=TA_CENTER)
      NullParagraph = Paragraph('<b></b>', basic_center)

      concepts_data = []
      style_content = self.style_content
      style_price = ParagraphStyle('Caption', fontSize=7, alignment=TA_LEFT)
      
      tag_order_line = Paragraph('<b>Order Line: </b>', style_content)
      tag_id = Paragraph('<b>Standard Item Identification: </b>', style_content)
      tag_country = Paragraph('<b>Origin Country: </b>', style_content)
      tag_commodity = Paragraph('<b>Commodity Classification: </b>', style_content)
      tag_price = Paragraph('<b>Price: </b>', style_content)
      tag_discount = Paragraph('<b>Discount: </b>', style_content)
      tag_day = Paragraph('<b>Quantity/Unit Code</b>', style_content)
      tag_taxes = Paragraph('<b>Taxes: </b>', style_content)

      concepts_data.append([Paragraph('<b>DETAILS</b>', self.style_title)])

      for item in self.items_list:
        # set_trace()
        item_number = Paragraph('<b>{}</b>'.format(item.get('inv_id')), style_number)
        item_name = Paragraph('<b>{}</b>'.format(item.get('item').get('item_name')), style_content)
        item_desc = Paragraph('{}'.format(item.get('item').get('item_desc')), style_content)
        item_order_line = Paragraph('{}'.format(item.get('inv_order_line')), style_content)
        item_id = Paragraph('{}'.format(item.get('item').get('item_id') if item.get('item').get('item_id') and item.get('item').get('item_id') != ':' else ''), style_content)
        # item_country = Paragraph('{}'.format(item.get('item').get('item_country') if item.get('item').get('item_country') and item.get('item').get('item_country') != 'NO' else 'Norway'), style_content)
        item_commodity = Paragraph('{}'.format(item.get('item').get('item_commodity')), style_content)
        item_price = Paragraph('<b>{}</b>'.format(item.get('price')), style_price)
        item_day = Paragraph('<b>{}</b>'.format(item.get('inv_day')), style_content)
        item_cost = Paragraph('<b>{}</b>'.format(item.get('inv_accounting_cost')), style_content)
        item_tax = Paragraph('<b>{}</b>'.format(item.get('item').get('item_tax')), style_price)
        item_amount = Paragraph('<b>{}</b>'.format(item.get('inv_amount')), style_price)
        item_discount = Paragraph('<b>{}</b>'.format(item.get('item').get('item_discount')), style_price)
        

        concepts_data.append([
          [
            item_number,
            Paragraph('&nbsp;', style_content),
            Paragraph('&nbsp;', style_content),
            Paragraph('&nbsp;', style_content),
          ], 
          [
            item_name,
            item_desc,
            tag_order_line,
            tag_price,
            tag_discount,
            tag_taxes,
            # item_day,
            tag_day,
          ], [
            item_order_line,
            item_price,
            # item_discount,
            Paragraph('&nbsp;', style_content),
            Paragraph('&nbsp;', style_content),
            item_day,
          ], 
          [
            Paragraph('&nbsp;', style_content),
            Paragraph('&nbsp;', style_content),
            item_cost,
            Paragraph('&nbsp;', style_content),
          ], 
          [
            tag_id,
            # tag_country,
            tag_commodity,
            Paragraph('&nbsp;', style_content),
            Paragraph('&nbsp;', style_content),
            Paragraph('&nbsp;', style_content),
          ], [
            item_id,
            # item_country,
            item_commodity,
            Paragraph('&nbsp;', style_content),
            Paragraph('&nbsp;', style_content),
            Paragraph('&nbsp;', style_content),
            #item_price,
          ], [
            Paragraph('&nbsp;', style_content),
            # item_price,
            Paragraph('&nbsp;', style_content),
            item_discount,
            item_tax,
            Paragraph('&nbsp;', style_content),
          ],
          [
            Paragraph('&nbsp;', style_content),
            item_amount,
          ],
        ])

      table_concepts = Table(
        concepts_data, 
        colWidths=[0.3*inch, 1.5*inch, 1.1*inch, 0.2*inch, 1.7*inch, 1.0*inch, 1.1*inch, 1.2*inch],
        style=[
          ('SPAN', (0,0), (-1,0)),
          ('LINEBELOW',(0,0),(-1,-1),1,colors.gray),
          ('BACKGROUND', (0,0), (-1,0), self.bg_color),
          # ('GRID', (0,1), (-1,-1),2, colors.black)
          #('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]
      )
      return table_concepts
    except Exception as e:
      print(f'Exception in concepts => {e}')

  def truncate(self, f, n):
    s = '{:,}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

class NumberedCanvas(canvas.Canvas):
  def __init__(self, *args, **kwargs):
    canvas.Canvas.__init__(self, *args, **kwargs)
    self.__saved_page_states = []

  def showPage(self):
    self.__saved_page_states.append(dict(self.__dict__))
    self._startPage()

  def save(self):
    num_pages = len(self.__saved_page_states)
    for state in self.__saved_page_states:
      self.__dict__.update(state)
      self.draw_page_number(num_pages)
      canvas.Canvas.showPage(self)
    canvas.Canvas.save(self)

  def draw_page_number(self, page_count):
    self.setFont('Helvetica-Bold', 8)
    self.setFillColor(HexColor('#555759'))
    self.drawRightString(7.85*inch, 0.2*inch, 'Page %d of %d' % (self._pageNumber, page_count))

# xml_path = open('/home/jroque/Downloads/jannet.xml', 'r')
# creator = CreatePDF(xml_path)
