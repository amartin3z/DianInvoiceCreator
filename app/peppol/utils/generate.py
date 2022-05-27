import pyxb
import pyxb.utils.domutils
import pyxb.binding.datatypes as xs

from .binding import ublinvoice

from .binding import _cac 
from .binding import _cbc 
from .binding import _ext
from .binding import _qdt
from .binding import _udt
from .binding import _ccts_cct
from .binding import _ds

from uuid import uuid4
from lxml import etree
from datetime import date
from pdb import set_trace


class UBLInvoice12(object):

  '''
    XSD was downloaded recursiverly with xsd_download (https://github.com/n-a-t-e/xsd_download)

    usage:
      python xsd_download.py http://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd

    XSD binding classes was generated with pyxbgen

    usage:
      pyxbgen -u UBL-Invoice-2.1.xsd 

  '''

  def __init__(self, invoice_json, asp, acp, delivery={}, payment_means={}, payment_terms={}, allowance_charge={}, tax_total={}, legal_monetary_total={}, invoice_line={}, ubl_extensions_json={}):
    
    self.invoice_json = invoice_json
    self.accouting_supplier_party = asp.get('AccountingSupplierParty', {})
    self.accouting_customer_party = acp.get('AccountingCustomerParty', {})
    self.delivery = delivery.get('Delivery', {})
    self.payment_means = payment_means.get('PaymentMeans', {})
    self.payment_terms = payment_terms.get('PaymentTerms', {})
    self.allowance_charge = allowance_charge.get('AllowanceCharge', [])
    self.tax_total = tax_total.get('TaxTotal', [])
    self.legal_monetary_total = legal_monetary_total.get('LegalMonetaryTotal', {})
    self.invoice_lines = invoice_line.get('InvoiceLine', [])
    self.ubl_extensions_json = ubl_extensions_json

    self.CUSTOMIZATION_ID = 'urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0'
    self.PROFILE_ID = 'urn:fdc:peppol.eu:2017:poacc:billing:01:1.0'

    self.__set_namespaces()
    self.invoice_obj = ublinvoice.Invoice()

    # self.ubl_extensions_json = ubl_extensions_json

  def __proccess_invoice(self):
    '''
      @invoice_json must contain the following structure:
      {
        "CustomizationID": "urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0".
        "ProfileID": "urn:fdc:peppol.eu:2017:poacc:billing:01:1.0",
        "ID": "Snippet1",
        "IssueDate": "2017-11-13",
        "IssueDate": "2017-12-01",
        "InvoiceTypeCode": 380,
        "DocumentCurrencyCode": "EUR",
        "AccountingCost": "4025:123:4343",
        "BuyerReference": "0150abc"
      }
    '''
    print(self.invoice_json)
    self.invoice_obj.UBLVersionID = _cbc.UBLVersionID(2.1)

    if self.__element_exists('CustomizationID', self.invoice_json):
      self.invoice_obj.CustomizationID = _cbc.CustomizationID(
        self.invoice_json.get('CustomizationID', self.CUSTOMIZATION_ID)
      )

    if self.__element_exists('ProfileID', self.invoice_json):
      self.invoice_obj.ProfileID = _cbc.ProfileID(
        self.invoice_json.get('ProfileID', self.PROFILE_ID)
      )

    if self.__element_exists('ID', self.invoice_json):
      self.invoice_obj.ID = _cbc.ID(
        self.invoice_json.get('ID')
      )

    if self.__element_exists('IssueDate', self.invoice_json):
      self.invoice_obj.IssueDate = _cbc.IssueDate(
        self.invoice_json.get('IssueDate')
      )

    if self.__element_exists('IssueTime', self.invoice_json):
      self.invoice_obj.IssueTime = _cbc.IssueTime(
        self.invoice_json.get('IssueTime')
      )

    if self.__element_exists('DueDate', self.invoice_json):
      self.invoice_obj.DueDate = _cbc.DueDate(
        self.invoice_json.get('DueDate')
      )

    if self.__element_exists('InvoiceTypeCode', self.invoice_json):
      self.invoice_obj.InvoiceTypeCode = _cbc.InvoiceTypeCode(
        self.invoice_json.get('InvoiceTypeCode'),
      )

    if self.__element_exists('Note', self.invoice_json):
      self.invoice_obj.Note.append(self.invoice_json.get("Note"))

    if self.__element_exists('TaxPointDate', self.invoice_json):
      self.invoice_obj.TaxPointDate = _cbc.TaxPointDate(
        self.invoice_json.get('TaxPointDate')
      )

    if self.__element_exists('DocumentCurrencyCode', self.invoice_json):
      self.invoice_obj.DocumentCurrencyCode = _cbc.DocumentCurrencyCode(
        self.invoice_json.get('DocumentCurrencyCode')
      )

    if self.__element_exists('TaxCurrencyCode', self.invoice_json):
      self.invoice_obj.TaxCurrencyCode = _cbc.TaxCurrencyCode(
        self.invoice_json.get('TaxCurrencyCode')
      )

    if self.__element_exists('AccountingCost', self.invoice_json):
      self.invoice_obj.AccountingCost = _cbc.AccountingCost(
        self.invoice_json.get('AccountingCost')
      )

    if self.__element_exists('BuyerReference', self.invoice_json):
      self.invoice_obj.BuyerReference = _cbc.BuyerReference(
        self.invoice_json.get('BuyerReference')
      )

  def __proccess_accouting_party(self, _type="supplier"):
    """
    @accouting_supplier_party
    @accouting_customer_party must contain the following structure:
      Note: AccountingSupplierParty key can change depending on _type ('supplier', 'customer') value
    {
      "AccountingSupplierParty": {
        "Party":{
          "EndpointID" {
            "value": "9482348239847239874",
            "schemeID": "0088"
          },
          "PartyIdentification": [
            {
              "ID": "99887766",
              "schemeID": "0088"
            }
          ], 
          "PartyName": {
            "Name": "Seller Business Name AS"
          },
          "PostalAddress": {
            "StreetName": "Main Street 1",
            "AddressLine": {
              "Line": "Building 23"
            }
            "Country": {
              "IdentificationCode": "GB"
            }
          },
          "PartyTaxScheme": [
            {
              "CompanyID": "NO999888777",
              "TaxScheme": {
                "ID": "VAT"
              }
            }
          ],
          "PartyLegalEntity":{
            "RegistrationName": "Full Formal Seller Name LTD.",
            "CompanyID": {
              "value": "987654321",
              "schemeID": "0002"
            },
            "CompanyLegalForm": "CompanyLegalForm",
          },
          "Contact": {
            "Name": "xyz123",
            "Telephone": "887 654 321",
            "ElectronicMail": "test.name@foo.bar"
          } 
        }
      }
    }
    """

    assert _type in ("supplier", "customer")

    if _type == "supplier":
      party_json = self.accouting_supplier_party.pop('Party', {})
    elif _type == "customer":
      party_json = self.accouting_customer_party.pop('Party', {})


    if party_json:
      if _type == "supplier":
        ### cac:AccountingSupplierParty
        accounting_party_obj = _cac.SupplierParty()
        ### cac:AccountingSupplierParty
      else:
        ### cac:AccountingCustomerParty
        accounting_party_obj = _cac.CustomerParty()
        ### cac:AccountingCustomerParty
    
      ### cac:Party
      ac_pa_party_obj = self.__proccess_party(party_json)

      accounting_party_obj.Party = ac_pa_party_obj

      # set_trace()
      # print(accounting_party_obj.toxml('utf-8'))

      if _type == "supplier":
        self.invoice_obj.AccountingSupplierParty = accounting_party_obj
      else:
        self.invoice_obj.AccountingCustomerParty = accounting_party_obj
      
      del accounting_party_obj
      del ac_pa_party_obj

  def __proccess_address(self, postaladdress_json):
    '''
      {
        "PostalAddress": {
          "StreetName": "Main Street 1",
          "AddressLine": {
            "Line": "Building 23"
          }
          "Country": {
            "IdentificationCode": "GB"
          }
        }
      }
    '''
    postaladdress_obj = _cac.Address()
    if postaladdress_json.get("StreetName", False):
      postaladdress_obj.StreetName = _cbc.StreetName(
        postaladdress_json.get("StreetName")
      )
    
    if postaladdress_json.get("AdditionalStreetName", False):
      postaladdress_obj.AdditionalStreetName = _cbc.AdditionalStreetName(
        postaladdress_json.get("AdditionalStreetName")
      )
    
    if postaladdress_json.get("CityName", False):
      postaladdress_obj.CityName = _cbc.CityName(
        postaladdress_json.get("CityName")
      )

    if postaladdress_json.get("PostalZone", False):
      postaladdress_obj.PostalZone = _cbc.PostalZone(
        postaladdress_json.get("PostalZone")
      )

    if postaladdress_json.get("CountrySubentity", False):
      postaladdress_obj.CountrySubentity = _cbc.CountrySubentity(
        postaladdress_json.get("CountrySubentity")
      )

    if postaladdress_json.get("AddressLine", False):
      address_line_json = postaladdress_json.get("AddressLine")
      addressline_obj = _cac.AddressLine()
      addressline_obj.Line = _cbc.Line(
        address_line_json.get("Line")
      )
      postaladdress_obj.AddressLine.append(addressline_obj)

    if postaladdress_json.get("Country", False):
      country_json = postaladdress_json.get("Country")
      country_obj = _cac.Country()
      country_obj.IdentificationCode = _cbc.IdentificationCode(
        country_json.get("IdentificationCode")
      )
      postaladdress_obj.Country = country_obj

    return postaladdress_obj

  def __proccess_party(self, party_json):
    party_obj = _cac.Party()
    ### cac:Party

    ### cbc:EndpointID
    '''
      {
        "EndpointID": {
          "value": "7300010000001",
          "schemeID": "0088"
      }
    '''
    endpointid_json = party_json.pop("EndpointID", {})
    if endpointid_json:
      endpointid_obj = _cbc.EndpointID(
        endpointid_json.get('value'), 
      )
      if endpointid_json.get('schemeID', False):
        endpointid_obj.schemeID = endpointid_json.get('schemeID')
      
      party_obj.EndpointID = endpointid_obj
    ### cbc:EndpointID

    ### cac:PartyIdentification
    '''
      {
        "PartyIdentification": [
          {
            "ID": {
              "99887766",
              "schemeID": "0088"
            }
          }
        ]
      }
    '''
    partyidentification_list = party_json.pop("PartyIdentification", [])
    for partyidentification_json in partyidentification_list:
      partyidentification_obj = _cac.PartyIdentification()
      
      id_json = partyidentification_json.get('ID', {})
      if id_json:
        partyidentification_id_obj = _cbc.ID(
          id_json.get('value')
        )
        if 'schemeID' in id_json:
          partyidentification_id_obj.schemeID = id_json.get('schemeID')
      
        partyidentification_obj.ID = partyidentification_id_obj
      party_obj.PartyIdentification.append(partyidentification_obj)
    ### cac:PartyIdentification

    ### cac:PartyName
    '''
      {
        "PartyName": {
          "Name": "Seller Business Name AS"
        }
      }
    '''
    partyname_json = party_json.pop("PartyName", {})
    if partyname_json:
      partyname_obj = _cac.PartyName(
        _cbc.Name( partyname_json.get("Name") )
      )

      party_obj.PartyName.append(partyname_obj)
    ### cac:PartyName

    ### cac:PostalAddress
    '''
      {
        "PostalAddress": {
          "StreetName": "Main Street 1",
          "AddressLine": {
            "Line": "Building 23"
          }
          "Country": {
            "IdentificationCode": "GB"
          }
        }
      }
    '''
    postaladdress_json = party_json.pop("PostalAddress", [])
    if postaladdress_json:
      #postaladdress_obj = _cac.PostalAddress()
      postaladdress_obj = self.__proccess_address(postaladdress_json)
      party_obj.PostalAddress = postaladdress_obj
    ### cac:PostalAddress

    ### cac:PartyTaxScheme
    '''
      {
        "PartyTaxScheme": [
          {
            "CompanyID": "NO999888777",
            "TaxScheme": {
              "ID": "VAT"
            }
          }
        ]
      }
    '''
    partytaxscheme_list = party_json.pop("PartyTaxScheme", [])
    for partytaxscheme_json in partytaxscheme_list:
      partyscheme_obj = _cac.PartyTaxScheme()

      if partytaxscheme_json.get('CompanyID') != '':
        partyscheme_obj.CompanyID = _cbc.CompanyID(
          partytaxscheme_json.get('CompanyID')
        )
      
      pts_taxscheme_json = partytaxscheme_json.get('TaxScheme')
      pts_taxscheme_obj = _cac.TaxScheme()
      pts_taxscheme_obj.ID = _cbc.ID(
        pts_taxscheme_json.get("ID")
      )

      partyscheme_obj.TaxScheme = pts_taxscheme_obj
      
      party_obj.PartyTaxScheme.append(partyscheme_obj)
    ### cac:PartyTaxScheme

    ### cac:PartyLegalEntity
    '''
      {
        "PartyLegalEntity":{
          "RegistrationName": "Full Formal Seller Name LTD.",
          "CompanyID": {
            "value": "987654321",
            "schemeID": "0002"
          },
          "CompanyLegalForm": "CompanyLegalForm",
        }
      }
    '''
    partylegalentity_json = party_json.pop("PartyLegalEntity", {})
    if partylegalentity_json:
      partylegalentity_obj = _cac.PartyLegalEntity()

      if partylegalentity_json.get("RegistrationName", False):
        partylegalentity_obj.RegistrationName = _cbc.RegistrationName(
          partylegalentity_json.get("RegistrationName")
        )

      if partylegalentity_json.get("CompanyID", False):
        ple_companyid_json = partylegalentity_json.get("CompanyID")

        partylegalentity_obj.CompanyID = _cbc.CompanyID(
          ple_companyid_json.get("value")
        )
        if ple_companyid_json.get("schemeID", False):
          partylegalentity_obj.CompanyID.schemeID = ple_companyid_json.get("schemeID")
      
      if partylegalentity_json.get("CompanyLegalForm", False) and _type == "supplier":
        partylegalentity_obj.CompanyLegalForm = _cbc.CompanyLegalForm(
          partylegalentity_json.get("CompanyLegalForm")
        )
      party_obj.PartyLegalEntity.append(
        partylegalentity_obj
      )
    ### cac:PartyLegalEntity

    ### cac:Contact
    '''
      {
        "Contact": {
          "Name": "xyz123",
          "Telephone": "887 654 321",
          "ElectronicMail": "test.name@foo.bar"
        }
      }
    '''
    contact_json = party_json.pop("Contact", {})
    if contact_json:
      contact_obj = _cac.Contact()
      
      if contact_json.get("Name", False):
        contact_obj.Name = _cbc.Name(
          contact_json.get("Name")
        )

      if contact_json.get("Telephone", False):
        contact_obj.Telephone = _cbc.Telephone(
          contact_json.get("Telephone")
        )

      if contact_json.get("ElectronicMail", False):
        contact_obj.ElectronicMail = _cbc.ElectronicMail(
          contact_json.get("ElectronicMail")
        )
      party_obj.Contact = contact_obj
    ### cac:Contact
    return party_obj

  def __proccess_delivery(self):
    '''
    {
      "Delivery": {
        "ActualDeliveryDate": "2017-12-01",
        "DeliveryLocation": {
          "ID":{
            "value": "83745498753497",
            "schemeID": "0088",
          },
          "Address": {
            "StreetName": "Main Street 1",
            "AddressLine": {
              "Line": "Building 23"
            }
            "Country": {
              "IdentificationCode": "GB"
            }
          }
        },
        "DeliveryParty": {
          "PartyName": {
            "Name": "Deliver name",
          }
        }
      }
    }
    '''

    '''
    {
      "ActualDeliveryDate": "2017-12-01"
    }
    '''
    delivery_obj = _cac.Delivery()
    if self.delivery.get('ActualDeliveryDate', False):
      delivery_obj.ActualDeliveryDate = _cbc.ActualDeliveryDate(
        self.delivery.get('ActualDeliveryDate')
      )
    
    '''
    '''
    deliverylocation_json = self.delivery.get('DeliveryLocation', {})
    if deliverylocation_json:
      deliverylocation_obj = _cac.DeliveryLocation()

      if deliverylocation_json.get('ID', False):
        deliverylocation_id_json = deliverylocation_json.get('ID')

        deliverylocation_obj.ID = _cbc.ID(
          deliverylocation_id_json.get('value')
        )
        if deliverylocation_id_json.get('schemeID', False):
          deliverylocation_obj.ID.schemeID = deliverylocation_id_json.get('schemeID')

      if deliverylocation_json.get('Address', False):
        deliverylocation_address_obj = self.__proccess_address(
          deliverylocation_json.get('Address')
        )
        deliverylocation_obj.Address = deliverylocation_address_obj
      
      delivery_obj.DeliveryLocation = deliverylocation_obj

    deliveryparty_json = self.delivery.get('DeliveryParty', {})
    if deliveryparty_json:
      deliveryparty_obj = self.__proccess_party(deliveryparty_json)
      delivery_obj.DeliveryParty = deliveryparty_obj
    
    # set_trace()
    # print(delivery_obj.toxml('utf-8'))

    self.invoice_obj.Delivery.append(delivery_obj)

  def __proccess_payment_means(self):
    '''
      {
        "PaymentMeans": {
          "PaymentMeansCode":{
            "value": "30",
            "name": "Credit transfer"
          },
          "PaymentID": "432948234234234",
          "CardAccount": {
            "PrimaryAccountNumberID": "1234"
            "NetworkID": "VISA",
            "HolderName": "John Doe"
          },
          "PayeeFinancialAccount": {
            "ID": "NO99991122222",
            "Name": "Payment Account",
            "FinancialInstitutionBranch":{
              "ID": "9999"
            }
          },
          "PaymentMandate": {
            "ID": "123456",
            "PayerFinancialAccount": {
              "ID": "12345676543"
            }
          }
        }
      }
    '''
    payment_means_obj = _cac.PaymentMeans()
    
    payment_means_code_json = self.payment_means.get('PaymentMeansCode', {})
    if payment_means_code_json:
      payment_means_code_obj = _cbc.PaymentMeansCode(
        payment_means_code_json.get('value')
      )

      if payment_means_code_json.get('name', False):
        payment_means_code_obj.name = payment_means_code_json.get('name')
      
      payment_means_obj.PaymentMeansCode = payment_means_code_obj
    
    
    if self.payment_means.get('PaymentID', False):
      payment_means_obj.PaymentID.append(_cbc.PaymentID(
        self.payment_means.get('PaymentID')
      ))
    
    card_account_json = self.payment_means.get('CardAccount', {})
    if card_account_json:
      card_account_obj = _cac.CardAccount()

      if card_account_json.get('PrimaryAccountNumberID', False):
        card_account_obj.PrimaryAccountNumberID = _cbc.PrimaryAccountNumberID(
          card_account_json.get('PrimaryAccountNumberID')
        )
      
      if card_account_json.get('NetworkID', False):
        card_account_obj.NetworkID = _cbc.NetworkID(
          card_account_json.get('NetworkID')
        )

      if card_account_json.get('HolderName', False):
        card_account_obj.HolderName = _cbc.HolderName(
          card_account_json.get('HolderName')
        )
      
      payment_means_obj.CardAccount = card_account_obj
    
    payee_financial_account_json = self.payment_means.get('PayeeFinancialAccount', {})
    if payee_financial_account_json:
      payee_financial_account_obj = _cac.PayeeFinancialAccount()

      if payee_financial_account_json.get('ID', False):
        payee_financial_account_obj.ID = _cbc.ID(
          payee_financial_account_json.get('ID')
        )

      if payee_financial_account_json.get('Name', False):
        payee_financial_account_obj.Name = _cbc.Name(
          payee_financial_account_json.get('Name')
        )
        
      financial_institution_branch_json = payee_financial_account_json.get('FinancialInstitutionBranch', {})
      if financial_institution_branch_json:
        financial_institution_branch_obj = _cac.FinancialInstitutionBranch()
        financial_institution_branch_obj.ID = _cbc.ID(
          financial_institution_branch_json.get('ID')
        )
        payee_financial_account_obj.FinancialInstitutionBranch = financial_institution_branch_obj


      payment_means_obj.PayeeFinancialAccount = payee_financial_account_obj

    payment_mandate_json = self.payment_means.get('PaymentMandate', {})
    if payment_mandate_json:
      payment_mandate_obj = _cac.PaymentMandate()

      if payment_mandate_json.get('ID', False):
        payment_mandate_obj.ID = _cbc.ID(
          payment_mandate_json.get('ID')
        )
      
      payer_financial_account_json = payment_mandate_json.get('PayerFinancialAccount', {})
      if payer_financial_account_json:

        payer_financial_account_obj = _cac.PayerFinancialAccount()
        payer_financial_account_obj.ID = _cbc.ID(
          payer_financial_account_json.get('ID')
        )
        payment_mandate_obj.PayerFinancialAccount = payer_financial_account_obj
      
      payment_means_obj.PaymentMandate = payment_mandate_obj
    
    # set_trace()
    # print(payment_means_obj.toxml('utf-8'))

    self.invoice_obj.PaymentMeans.append(payment_means_obj)

  def __proccess_payment_terms(self):
    '''
      {
        "PaymentTerms": {
          "Note": "Payment within 10 days, 2% discount"
        }
      }
    '''
    note_str = self.payment_terms.get('Note', False)
    
    if note_str:
      payment_terms_obj = _cac.PaymentTerms()
      payment_terms_obj.Note.append(
          _cbc.Note(
          note_str.strip()
        )
      )
      
      # print(payment_terms_obj.toxml('utf-8'))

      self.invoice_obj.PaymentTerms.append(
        payment_terms_obj
      )
    
  def __proccess_legal_monetary_total(self):
    '''
      {
        "LegalMonetaryTotal":{
          "LineExtensionAmount":{
            "value": 3800.0,
            "currencyID": "EUR"
          },
          "TaxExclusiveAmount": {
            "value": 3600.0,
            "currencyID": "EUR"
          },
          "TaxInclusiveAmount": {
            "value": 4500.0,
            "currencyID": "EUR"
          },
          "AllowanceTotalAmount":{
            "value": 200.0,
            "currencyID": "EUR"
          },
          "ChargeTotalAmount": {
            "value": 0.0,
            "currencyID": "EUR"
          },
          "PrepaidAmount": {
            "value": 1000.0,
            "currencyID": "EUR"
          },
          "PayableRoundingAmount": {
            "value": 1000.0,
            "currencyID": "EUR"
          },
          "PayableAmount": {
            "value": 1000.0,
            "currencyID": "EUR"
          },
        }
      }
    '''
    # set_trace()
    legal_monetary_total = _cac.LegalMonetaryTotal()

    line_extension_amount_json = self.legal_monetary_total.get("LineExtensionAmount", {})
    if line_extension_amount_json:

      lea_currency_id = line_extension_amount_json.pop("currencyID", None)
      
      line_extension_amount_obj = _cbc.LineExtensionAmount(
        line_extension_amount_json.get("value"),
        currencyID=lea_currency_id
      )

      legal_monetary_total.LineExtensionAmount = line_extension_amount_obj


    tax_exclusive_amount_json = self.legal_monetary_total.get("TaxExclusiveAmount", {})
    if tax_exclusive_amount_json:

      tea_currency_id = None
      if "currencyID" in tax_exclusive_amount_json:
        tea_currency_id = tax_exclusive_amount_json.pop("currencyID")
      
      tax_exclusive_amount_obj = _cbc.TaxExclusiveAmount(
        tax_exclusive_amount_json.get("value"),
        currencyID=tea_currency_id
      )

      legal_monetary_total.TaxExclusiveAmount = tax_exclusive_amount_obj

    tax_inclusive_amount_json = self.legal_monetary_total.get("TaxInclusiveAmount", {})
    if tax_inclusive_amount_json:

      tia_currency_id = None
      if "currencyID" in tax_inclusive_amount_json:
        tia_currency_id = tax_inclusive_amount_json.pop("currencyID")
      
      tax_inclusive_amount_obj = _cbc.TaxInclusiveAmount(
        tax_inclusive_amount_json.get("value"),
        currencyID=tia_currency_id
      )

      legal_monetary_total.TaxInclusiveAmount = tax_inclusive_amount_obj

    allowance_total_amount_json = self.legal_monetary_total.get("AllowanceTotalAmount", {})
    if allowance_total_amount_json:

      ata_currency_id = None
      if "currencyID" in allowance_total_amount_json:
        ata_currency_id = allowance_total_amount_json.pop("currencyID")
      
      allowance_total_amount_obj = _cbc.AllowanceTotalAmount(
        allowance_total_amount_json.get("value"),
        currencyID=ata_currency_id
      )

      legal_monetary_total.AllowanceTotalAmount = allowance_total_amount_obj

    carge_total_amount_json = self.legal_monetary_total.get("ChargeTotalAmount", {})
    if carge_total_amount_json:

      cta_currency_id = None
      if "currencyID" in carge_total_amount_json:
        cta_currency_id = carge_total_amount_json.pop("currencyID")
      
      carge_total_amount_obj = _cbc.ChargeTotalAmount(
        carge_total_amount_json.get("value"),
        currencyID=cta_currency_id
      )

      legal_monetary_total.ChargeTotalAmount = carge_total_amount_obj

    prepaid_amount_json = self.legal_monetary_total.get("PrepaidAmount", {})
    if prepaid_amount_json:

      pa_currency_id = None
      if "currencyID" in prepaid_amount_json:
        pa_currency_id = prepaid_amount_json.pop("currencyID")
      
      prepaid_amount_obj = _cbc.PrepaidAmount(
        prepaid_amount_json.get("value"),
        currencyID=pa_currency_id
      )

      legal_monetary_total.PrepaidAmount = prepaid_amount_obj

    payable_rounding_amount_json = self.legal_monetary_total.get("PayableRoundingAmount", {})
    if payable_rounding_amount_json:

      pra_currency_id = None
      if "currencyID" in payable_rounding_amount_json:
        pra_currency_id = payable_rounding_amount_json.pop("currencyID")
      
      payable_rounding_amount_obj = _cbc.PayableRoundingAmount(
        payable_rounding_amount_json.get("value"),
        currencyID=pra_currency_id
      )

      legal_monetary_total.PayableRoundingAmount = payable_rounding_amount_obj

    payable_amount_json = self.legal_monetary_total.get("PayableAmount", {})
    if payable_amount_json:

      pya_currency_id = None
      if "currencyID" in payable_amount_json:
        pya_currency_id = payable_amount_json.pop("currencyID")
      
      payable_amount_obj = _cbc.PayableAmount(
        payable_amount_json.get("value"),
        currencyID=pya_currency_id
      )

      legal_monetary_total.PayableAmount = payable_amount_obj

    self.invoice_obj.LegalMonetaryTotal = legal_monetary_total

  def __proccess_individial_allowance_charge(self, allowance_charge_json):
    allowance_charge_obj = _cac.AllowanceCharge()

    charge_indicator_str = allowance_charge_json.get('ChargeIndicator', False)
    if charge_indicator_str:
      allowance_charge_obj.ChargeIndicator = _cbc.ChargeIndicator(
        charge_indicator_str
      )

    allowance_charge_reason_str = allowance_charge_json.get('AllowanceChargeReasonCode', False)
    if allowance_charge_reason_str:
      allowance_charge_obj.AllowanceChargeReasonCode = _cbc.AllowanceChargeReasonCode(
        allowance_charge_reason_str
      )
        
    allowance_charge_reason_str = allowance_charge_json.get('AllowanceChargeReason', False)
    if allowance_charge_reason_str:
      allowance_charge_obj.AllowanceChargeReason.append(
        _cbc.AllowanceChargeReason(
          allowance_charge_reason_str
        )
      )
        
    multiplier_factor_numeric_str = allowance_charge_json.get('MultiplierFactorNumeric', False)
    if multiplier_factor_numeric_str:
      allowance_charge_obj.MultiplierFactorNumeric = _cbc.MultiplierFactorNumeric(
        multiplier_factor_numeric_str
      )
        
    amount_json = allowance_charge_json.get('Amount', False)
    if amount_json:
      allowance_charge_obj.Amount = _cbc.Amount(
        amount_json.get('value'),
        currencyID = amount_json.get('currencyID')
      )
        
    base_amount_json = allowance_charge_json.get('BaseAmount', False)
    if base_amount_json:
      allowance_charge_obj.BaseAmount = _cbc.BaseAmount(
        base_amount_json.get('value'),
        currencyID = base_amount_json.get('currencyID'),
      )
    
    tax_category_json = allowance_charge_json.get('TaxCategory', {})
    if tax_category_json:
      tax_category_obj = _cac.TaxCategory()

      id_str = tax_category_json.get('ID', False)
      if id_str:
        tax_category_obj.ID = _cbc.ID(
          id_str
        )
      
      percent_str = tax_category_json.get('Percent', False)
      if percent_str:
        tax_category_obj.Percent = _cbc.Percent(
          percent_str
        )

      tax_scheme_json = tax_category_json.get('TaxScheme', {})
      if tax_scheme_json:
        tax_category_obj.TaxScheme = _cac.TaxScheme(
          _cbc.ID(
            tax_scheme_json.get('ID')
          )
        )
      
      allowance_charge_obj.TaxCategory.append(
        tax_category_obj
      )
    
    return allowance_charge_obj
  
  def __proccess_tax_total(self):
    for tax_total_json in self.tax_total:
      tax_total_obj = _cac.TaxTotal()

      tax_amount_json = tax_total_json.get('TaxAmount', {})
      if tax_amount_json:
        tax_total_obj.TaxAmount = _cbc.TaxAmount(
          tax_amount_json.get('value'),
          currencyID=tax_amount_json.get('currencyID')
        )
      
      for tax_subtotal_json in tax_total_json.get('TaxSubtotal', []):
        tax_subtotal_obj = _cac.TaxSubtotal()

        taxable_amount_json = tax_subtotal_json.get('TaxableAmount', {})
        if taxable_amount_json:
          tax_subtotal_obj.TaxableAmount = _cbc.TaxableAmount(
            taxable_amount_json.get('value'),
            currencyID=taxable_amount_json.get('currencyID')
          )
        
        ts_tax_amount_json = tax_subtotal_json.get('TaxAmount', {})
        if ts_tax_amount_json:
          tax_subtotal_obj.TaxAmount = _cbc.TaxAmount(
            ts_tax_amount_json.get('value'),
            currencyID=ts_tax_amount_json.get('currencyID')
          )
        
        tax_category_json = tax_subtotal_json.get('TaxCategory', {})
        if tax_category_json:
          tax_category_obj = _cac.TaxCategory()

          id_str = tax_category_json.get('ID', False)
          if id_str:
            tax_category_obj.ID = _cbc.ID(
              id_str
            )
          percent_str = tax_category_json.get('Percent', False)
          if percent_str:
            tax_category_obj.Percent = _cbc.Percent(
              percent_str
            )
          
          tax_exeption_reason_code_str = tax_category_json.get('TaxExemptionReasonCode', False)
          if tax_exeption_reason_code_str:
            tax_category_obj.TaxExemptionReasonCode = _cbc.TaxExemptionReasonCode(
              tax_exeption_reason_code_str
            )

          tax_exeption_reason_str = tax_category_json.get('TaxExemptionReason', False)
          if tax_exeption_reason_str:
            tax_category_obj.TaxExemptionReason = _cbc.TaxExemptionReason(
              tax_exeption_reason_str
            )
          
          tax_scheme_json = tax_category_json.get('TaxScheme', {})
          if tax_scheme_json:
            tax_category_obj.TaxScheme = _cac.TaxScheme(
              ID = _cbc.ID(
                tax_scheme_json.get('ID')
              )
            )
          
          tax_subtotal_obj.TaxCategory = tax_category_obj
        
        tax_total_obj.TaxSubtotal.append(
          tax_subtotal_obj
        )
      
      self.invoice_obj.TaxTotal.append(
        tax_total_obj
      )

  def __proccess_allowance_charge(self):
    for allowance_charge_json in self.allowance_charge:
      self.invoice_obj.AllowanceCharge.append(
        self.__proccess_individial_allowance_charge(allowance_charge_json)
      )

  def __ubl_extension(self):
    # set_trace()
    import base64
    from app.core.models import SatFile, Business

    ubl_extension_obj = _ext.UBLExtensions()
    ds_key_info = _ds.KeyInfo()
    ds_signed_info = _ds.SignedInfo()

    reference = _ds.Reference(
      URI=""
    )
    ds_509_data = _ds.X509Data()

    signature_obj = _ds.Signature(
      Id="signatureKG"
    )

    ds_signed_info.append(_ds.CanonicalizationMethod(
      Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"
    ))

    ds_signed_info.append(_ds.SignatureMethod(
      Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"
    ))

    ds_transform = _ds.Transforms()
    ds_transform.append(_ds.Transform(
      Algorithm="http://www.w3.org/2000/09/xmldsig#envelopedsignature"
    ))
    
    reference.append(ds_transform)
    digest_method = _ds.DigestMethod(
      Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"  
    )
    digest_val = _ds.DigestValue(
        self.ubl_extensions_json.get("Reference").get("DigestValue"), "UTF-8"
      )

    reference.append(digest_method)
    reference.append(digest_val)
    ds_signed_info.append(reference)

    ds_signature_val = _ds.SignatureValue(base64.b64encode(bytes(self.ubl_extensions_json.get("SignatureValue"), "utf-8")))
    ds_509_data.X509Certificate.append(b"MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==")
    # ds_509_data.X509Certificate.append(base64.b64encode(self.ubl_extensions_json.get("X509Data").get("X509Certificate")))
    # ds_509_data.X509SubjectName.append('1.2.840.113549.1.9.1=#161a4253554c434140534f55544845524e504552552e434f4d2e5045,CN=Juan Robles,OU=20889666312,O= SOPORTE TECNOLOGICO EIRL,L=LIMA,ST=LIMA,C=PE')
    ds_key_info.append(ds_509_data)

    signature_obj.append(ds_signed_info)
    signature_obj.append(ds_signature_val)
    signature_obj.append(ds_key_info)

    extention_content = _ext.ExtensionContent()
    extention_content.append(signature_obj)

    ubl_extension = _ext.UBLExtension()
    ubl_extension.append(extention_content)

    ubl_extension_obj.append(ubl_extension)

    # self.invoice_obj.UBLExtensions = ubl_extension_obj
    return etree.fromstring(ubl_extension_obj.toxml('utf-8'))


  def __proccess_invoice_line(self):
    '''
      {
        "InvoiceLine": {
          "ID": 12,
          "Note": "New article number 12345",
          "InvoicedQuantity": {
            "value": "100",
            "unitCode": "C62"
          },
          "LineExtensionAmount": {
            "value": 2145.00,
            "currencyID": "EUR"
          },
          "AccountingCost": "1287:65464",
          "InvoicePeriod": {
            "StartDate": "2017-10-05",
            "EndDate": "2017-10-15"
          },
          "OrderLineReference": {
            "LineID": "3"
          },
          "DocumentReference": {
            "ID": {
              "value": AB12345,
              "schemeID": "ABZ"
            }
          },
          "AllowanceCharge": [{
            "ChargeIndicator": false,
            "AllowanceChargeReasonCode": "95",
            "AllowanceChargeReason": "Discount",
            "MultiplierFactorNumeric": "20",
            "Amount": {
              "value": "200",
              "currencyID": "EUR"
            },
            "BaseAmount": {
              "value": "1000",
              "currencyID": "EUR"
            }
          }],
          "Item": {
            "Description": "Long description of the item on the invoice line",
            "Name": "Item name",
            "BuyersItemIdentification": {
              "ID": "123455"
            },
            "SellersItemIdentification": {
              "ID": "9873242"
            },
            "StandardItemIdentification": {
              "ID": {
                "value": "10986700",
                "schemeID": "0160"
              }
            },
            "OriginCountry": {
              "IdentificationCode": "CN"
            },
            "CommodityClassification": [{
              "ItemClassificationCode": {
                "value": 9873242,
                "listID": "STI",
                "listVersionID": "-"
              }
            }],
            "ClassifiedTaxCategory": {
              "ID": "S",
              "Percent": "25",
              "TaxScheme": {
                "ID": "VAT"
              }
            },
            "AdditionalItemProperty": [{
              "Name": "Color",
              "Value": "Black"
            }],
          },
          "Price": {
            "PriceAmount": {
              "value": 23.45,
              "currencyID": "EUR"
            },
            "BaseQuantity": {
              "value": 1,
              "unitCode": "C62"
            },
            "AllowanceCharge": {
              "ChargeIndicator": false,
              "Amount": {
                "value": 100,
                "currencyID": "EUR",
              }
            },
            "BaseAmount": {
              "value": 123.45,
              "currencyID": "EUR"
            }
          }
        }
      }
    '''

    for invoice_line_json in self.invoice_lines:

      invoice_line_obj = _cac.InvoiceLine()

      id_str = invoice_line_json.get('ID', False)
      if id_str:
        invoice_line_obj.ID = _cbc.ID(
          id_str
        )
      
      note_str = invoice_line_json.get('Note', False)
      if note_str:
        invoice_line_obj.Note.append(
          _cbc.Note(
            note_str
          )
        )
      
      invoiced_quantity_json = invoice_line_json.get('InvoicedQuantity', {})
      if invoiced_quantity_json:

        invoice_line_obj.InvoicedQuantity = _cbc.InvoicedQuantity(
          invoiced_quantity_json.get('value'),
          unitCode=invoiced_quantity_json.get('unitCode', None)
        )
      
      line_extension_amount_json = invoice_line_json.get('LineExtensionAmount', {})
      if line_extension_amount_json:
        invoice_line_obj.LineExtensionAmount = _cbc.LineExtensionAmount(
          line_extension_amount_json.get('value'),
          currencyID=line_extension_amount_json.get('currencyID', None)
        )
      
      accounting_cost_str = invoice_line_json.get('AccountingCost', False)
      if accounting_cost_str:
        invoice_line_obj.AccountingCost = _cbc.AccountingCost(
          accounting_cost_str
        )
      
      invoice_period_json = invoice_line_json.get('InvoicePeriod', {})
      if invoice_period_json:
        invoice_period_obj = _cac.InvoicePeriod()

        start_date_str = invoice_period_json.get('StartDate', False)
        if start_date_str:
          invoice_period_obj.StartDate = _cbc.StartDate(
            start_date_str
          )
        
        end_date_str = invoice_period_json.get('EndDate', False)
        if end_date_str:
          invoice_period_obj.EndDate = _cbc.EndDate(
            end_date_str
          )
        
        invoice_line_obj.InvoicePeriod.append(invoice_period_obj)
      
      order_line_reference_json = invoice_line_json.get('OrderLineReference', {})
      if order_line_reference_json:

        invoice_line_obj.OrderLineReference.append(_cac.OrderLineReference(
            LineID = _cbc.LineID(
              order_line_reference_json.get('LineID')
            )
          )
        )
      
      document_reference_json = invoice_line_json.get('DocumentReference', {})
      if document_reference_json:
        document_reference_obj = _cac.DocumentReference()

        id_json = document_reference_json.get('ID', {})
        if id_json:
          document_reference_obj.ID = _cbc.ID(
            id_json.get('value'),
            schemeID=id_json.get('schemeID')
          )
        
        document_type_code_str = document_reference_json.get('DocumentTypeCode', False)
        if document_type_code_str:
          document_reference_obj.DocumentTypeCode = _cbc.DocumentTypeCode(
            document_type_code_str
          )
        
        invoice_line_obj.DocumentReference.append(
          document_reference_obj
        )
      
      # set_trace()
      # for allowance_charge_json in document_reference_json.get('AllowanceCharge', []):
      for allowance_charge_json in invoice_line_json.get('AllowanceCharge', []):
        allowance_charge_obj = self.__proccess_individial_allowance_charge(allowance_charge_json)

        invoice_line_obj.AllowanceCharge.append(
          allowance_charge_obj
        )
  
      item_json = invoice_line_json.get('Item', {})
      if item_json:
        item_obj = _cac.Item()

        description_str = item_json.get('Description', False)
        if description_str:
          item_obj.Description.append(
            _cbc.Description(
              description_str
            )
          )
        
        name_str = item_json.get('Name', False)
        if name_str:
          item_obj.Name = _cbc.Name(
            name_str
          )
        
        buyers_item_identification_json = item_json.get('BuyersItemIdentification', {})
        if buyers_item_identification_json:
          item_obj.BuyersItemIdentification = _cac.BuyersItemIdentification(
            _cbc.ID(
              buyers_item_identification_json.get('ID')
            )
          )

        sellers_item_identification_json = item_json.get('SellersItemIdentification', {})
        if sellers_item_identification_json:
          item_obj.SellersItemIdentification = _cac.SellersItemIdentification(
            _cbc.ID(
              sellers_item_identification_json.get('ID')
            )
          )
        
        standard_item_identification_json = item_json.get('StandardItemIdentification', {})
        if standard_item_identification_json:
          id_json = standard_item_identification_json.get('ID')
          item_obj.StandardItemIdentification = _cac.StandardItemIdentification(
            ID = _cbc.ID(
              id_json.get('value'),
              schemeID=id_json.get('schemeID', None)
            )
          )

        origin_country_json = item_json.get('OriginCountry', {})
        if origin_country_json:
          item_obj.OriginCountry = _cac.OriginCountry(
            IdentificationCode=_cbc.IdentificationCode(
              origin_country_json.get("IdentificationCode")
            )
          )
        
        for commodity_classification_json in item_json.get('CommodityClassification', []):
          item_cassification_json = commodity_classification_json.get('ItemClassificationCode')
          item_obj.CommodityClassification.append(_cac.CommodityClassification(
            _cbc.ItemClassificationCode(
                item_cassification_json.get('value'),
                listID=item_cassification_json.get('listID', None),
                listVersionID=item_cassification_json.get('listVersionID', None)
              )
            )
          )
        
        classified_tax_category_json = item_json.get('ClassifiedTaxCategory', {})
        if classified_tax_category_json:
          classified_tax_category_obj = _cac.ClassifiedTaxCategory()
          
          id_str = classified_tax_category_json.get('ID', False)
          if id_str:
            classified_tax_category_obj.ID = _cbc.ID(
              id_str
            )
          
          percent_str = classified_tax_category_json.get('Percent', False)
          if percent_str:
            classified_tax_category_obj.Percent = _cbc.Percent(
              percent_str
            )
          
          tax_scheme_json =  classified_tax_category_json.get('TaxScheme', {})
          if tax_scheme_json:
            classified_tax_category_obj.TaxScheme = _cac.TaxScheme(
              ID=_cbc.ID(
                tax_scheme_json.get('ID')
              )
            )
          
          item_obj.ClassifiedTaxCategory.append(
            classified_tax_category_obj
          )

        
        for additional_item_property_json in item_json.get('AdditionalItemProperty', []):
          additional_item_property_obj = _cac.AdditionalItemProperty(
            Name=_cbc.Name(
              additional_item_property_json.get('Name')
            ),
            Value=_cbc.Value(
              additional_item_property_json.get('Value')
            )
          )

          item_obj.AdditionalItemProperty.append(
            additional_item_property_obj
          )

        invoice_line_obj.Item = item_obj
        
      price_json = invoice_line_json.get('Price', {})
      if price_json:
        price_obj = _cac.Price()

        price_amount_json = price_json.get('PriceAmount', {})
        if price_amount_json:
          price_obj.PriceAmount = _cbc.PriceAmount(
            price_amount_json.get('value'),
            currencyID=price_amount_json.get('currencyID')
          )
        
        base_quantity_json = price_json.get('BaseQuantity', {})
        if base_quantity_json:
          price_obj.BaseQuantity = _cbc.BaseQuantity(
            base_quantity_json.get('value'),
            unitCode=base_quantity_json.get('unitCode')
          )
        
        price_allowance_charge_json = price_json.get('AllowanceCharge')
        if price_allowance_charge_json:
          allowance_charge_obj = self.__proccess_individial_allowance_charge(price_allowance_charge_json)
          
          price_obj.AllowanceCharge.append(allowance_charge_obj)
        
        invoice_line_obj.Price = price_obj
      
      #   print('InvoiceLine')
      #   print(invoice_line_obj.toxml('utf-8'))
      self.invoice_obj.InvoiceLine.append(
        invoice_line_obj
      )
  
  def __element_exists(self, attribute, json):
    return attribute in json and json.get(attribute, False)

  def __set_namespaces(self):
    pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(ublinvoice.Namespace)
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_cac.Namespace, 'cac')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_cbc.Namespace, 'cbc')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_ext.Namespace, 'ext')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_ext.Namespace, 'ext')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_ds.Namespace, 'ds')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_udt.Namespace, 'udt')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_ccts_cct.Namespace, 'ccts')

  def get_invoice(self):
    

    if self.accouting_supplier_party:
      self.__proccess_accouting_party("supplier")
    
    if self.accouting_customer_party:
      self.__proccess_accouting_party("customer")
    
    if self.delivery:
      self.__proccess_delivery()
    
    if self.payment_means:
      self.__proccess_payment_means()

    if self.payment_terms:
      self.__proccess_payment_terms()

    if self.tax_total:
      self.__proccess_tax_total()

    if self.allowance_charge:
      self.__proccess_allowance_charge()
    
    if self.legal_monetary_total:
      self.__proccess_legal_monetary_total()
    
    if self.invoice_lines:
      self.__proccess_invoice_line()

    self.__proccess_invoice()

    # self.__ubl_extension()

    ubl_string = self.invoice_obj.toxml('UTF-8')
    ubl_etree = etree.fromstring(ubl_string)

    return ubl_string, ubl_etree
    # ubl_rootree =  ubl_etree.getroottree()
    # ubl_rootree.write('prueba_generacion.xml', encoding='utf-8')

'''
from generate import UBLInvoice12

invoice_json = {
    "CustomizationID": "urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0",
    "ProfileID": "urn:fdc:peppol.eu:2017:poacc:billing:01:1.0",
    "ID": "Snippet1",
    "IssueDate": "2017-11-13",
    "DueDate": "2017-12-01",
    "InvoiceTypeCode": "380",
    "DocumentCurrencyCode": "EUR",
    "AccountingCost": "4025:123:4343",
    "BuyerReference": "0150abc"
}


asp = {
    "AccountingSupplierParty": {
        "Party": {
            "EndpointID": {
                "value": "9482348239847239874",
                "schemeID": "0088"
            },
            "PartyIdentification": [
                {
                    "ID": { 
                        "value": "99887766",
                        "schemeID": "0088"
                    }
                }
            ], 
            "PartyName": {
                "Name": "Seller Business Name AS"
            },
            "PostalAddress": {
                "StreetName": "Main Street 1",
                "AdditionalStreetName": "Postbox 123",
                "CityName": "London",
                "PostalZone": "GB 123 EW",
                "Country": {
                    "IdentificationCode": "GB"
                }
            },
            "PartyTaxScheme": [
                {
                "CompanyID": "GB1232434",
                "TaxScheme": {
                    "ID": "VAT"
                }
                }
            ],
            "PartyLegalEntity":{
                "RegistrationName": "Full Formal Seller Name LTD.",
                "CompanyID": {
                    "value": "987654321",
                },
            },
        }
    }
}

acp = {
    "AccountingCustomerParty": {
        "Party": {
            "EndpointID": {
                "value": "FR23342",
                "schemeID": "0002"
            },
            "PartyIdentification": [
                {
                    "ID": {
                        "value": "FR23342",
                        "schemeID": "0002"
                    }
                }
            ], 
            "PartyName": {
                "Name": "BuyerTradingName AS"
            },
            "PostalAddress": {
                "StreetName": "Hovedgatan 32",
                "AdditionalStreetName": "Po box 878",
                "CityName": "Stockholm",
                "PostalZone": "456 34",
                "Country": {
                    "IdentificationCode": "SE"
                }
            },
            "PartyTaxScheme": [
                {
                "CompanyID": "SE4598375937",
                "TaxScheme": {
                    "ID": "VAT"
                }
                }
            ],
            "PartyLegalEntity":{
                "RegistrationName": "Buyer Official Name",
                "CompanyID": {
                    "value": "39937423947",
                    "schemeID": "0183",
                },
            },
            "Contact": {
                "Name": "Lisa Johnson",
                "Telephone": "23434234",
                "ElectronicMail": "lj@buyer.se"
            }
        }
    }
}

delivery = {
    "Delivery": {
        "ActualDeliveryDate": "2017-11-01",
        "DeliveryLocation": {
            "ID":{
                "value": "9483759475923478",
                "schemeID": "0088",
          },
          "Address": {
                "StreetName": "Delivery street 2",
                "AdditionalStreetName": "Building 56",
                "CityName": "Stockholm",
                "PostalZone": "21234",
                "Country": {
                    "IdentificationCode": "SE"
                }
            }
        },
        "DeliveryParty": {
            "PartyName": {
                "Name": "Delivery party Name",
            }
        }
    }
}

payment_means = {
    "PaymentMeans": {
        "PaymentMeansCode":{
            "value": "30",
            "name": "Credit transfer"
        },
        "PaymentID": "Snippet1",
        "PayeeFinancialAccount": {
            "ID": "NO99991122222",
            "Name": "Payment Account",
            "FinancialInstitutionBranch":{
                "ID": "BIC324098"
            }
        },
    }
}

payment_terms = {
    "PaymentTerms": {
        "Note": "Payment within 10 days, 2% discount"
    }
}

allowance_charge = {
    "AllowanceCharge": [
    {
        "ChargeIndicator": "true",
        "AllowanceChargeReason": "Insurance",
        "Amount": {
            "value": 25,
            "currencyID": "EUR"
        },
        "TaxCategory": {
            "ID": "S",
            "Percent": "25.0",
            "TaxScheme": {
                "ID": "VAT"
            }
        }
    }
]}

tax_total = {    
    "TaxTotal": [
        {
            "TaxAmount": {
                "value": 331.25,
                "currencyID": "EUR"
            },
            "TaxSubtotal": [{
                "TaxableAmount": {
                    "value": 1325,
                    "currencyID": "EUR"
                },
                "TaxAmount": {
                    "value": 331.25,
                    "currencyID": "EUR"
                },
                "TaxCategory": {
                    "ID": "S",
                    "Percent": 25.0,
                    "TaxScheme": {
                        "ID": "VAT"
                    }
                }
            }]
        }
    ]
}

legal_monetary_total = {
    "LegalMonetaryTotal":{
        "LineExtensionAmount":{
            "value": 1300,
            "currencyID": "EUR"
        },
        "TaxExclusiveAmount": {
            "value": 1325,
            "currencyID": "EUR"
        },
        "TaxInclusiveAmount": {
            "value": 1656.25,
            "currencyID": "EUR"
        },
        "ChargeTotalAmount": {
            "value": 25,
            "currencyID": "EUR"
        },
        "PayableAmount": {
            "value": 1656.25,
            "currencyID": "EUR"
        },
    }
}

invoice_lines = {
    "InvoiceLine": [
        {
            "ID": 1,
            "InvoicedQuantity": {
                "value": "7",
                "unitCode": "DAY"
            },
            "LineExtensionAmount": {
                "value": 2800,
                "currencyID": "EUR"
            },
            "AccountingCost": "Konteringsstreng",
            "OrderLineReference": {
                "LineID": "123"
            },
            "Item": {
                "Description": "Description of item",
                "Name": "Item name",
                "StandardItemIdentification": {
                    "ID": {
                        "value": "21382183120983",
                        "schemeID": "0088"
                    }
                },
                "OriginCountry": {
                    "IdentificationCode": "NO"
                },
                "CommodityClassification": [{
                    "ItemClassificationCode": {
                        "value": "09348023",
                        "listID": "SRV",
                    }
                }],
                "ClassifiedTaxCategory": {
                    "ID": "S",
                    "Percent": 25.0,
                    "TaxScheme": {
                        "ID": "VAT"
                    }
                },
            },
          "Price": {
            "PriceAmount": {
              "value": 400,
              "currencyID": "EUR"
            },
          }
        },{
            "ID": 2,
            "InvoicedQuantity": {
                "value": "-3",
                "unitCode": "DAY"
            },
            "LineExtensionAmount": {
                "value": "-1500",
                "currencyID": "EUR"
            },
            "AccountingCost": "Konteringsstreng",
            "OrderLineReference": {
                "LineID": "123"
            },
            "Item": {
                "Description": "Description 2",
                "Name": "Item name 2",
                "StandardItemIdentification": {
                    "ID": {
                        "value": "21382183120983",
                        "schemeID": "0088"
                    }
                },
                "OriginCountry": {
                    "IdentificationCode": "NO"
                },
                "CommodityClassification": [{
                    "ItemClassificationCode": {
                        "value": "09348023",
                        "listID": "SRV",
                    }
                }],
                "ClassifiedTaxCategory": {
                    "ID": "S",
                    "Percent": 25.0,
                    "TaxScheme": {
                        "ID": "VAT"
                    }
                },
            },
          "Price": {
            "PriceAmount": {
              "value": 500,
              "currencyID": "EUR"
            },
          }
        }
    ]
}

ubl_invoice_12 = UBLInvoice12(
    invoice_json,
    asp,
    acp,
    delivery,
    payment_means,
    payment_terms,
    allowance_charge,
    tax_total,
    legal_monetary_total,
    invoice_lines,
)

ubl_string, ubl_etree = ubl_invoice_12.get_invoice()

ubl_rootree =  ubl_etree.getroottree()
from datetime import datetime

timestamp = datetime.timestamp(datetime.now())

ubl_rootree.write(f'prueba_generacion_{timestamp}.xml', encoding='utf-8')
'''