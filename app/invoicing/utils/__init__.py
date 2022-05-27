# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from app.cfdi.utils.controller import CFDIValidator
from app.core.models import Business
import json


class SatProcess(object):
  def __init__(self, xml_string, user):
    self.uuid = None
    self.is_valid = False
    self.xml_string = xml_string
    self.error_code = ''
    self.xml_signed = ''
    self.user_obj = user

  def timbrado(self):
    try:
      cfdi_validator = CFDIValidator(self.xml_string, self.user_obj)
      cfdi_validator.validar()
      self.error_code = cfdi_validator.error
      self.is_valid = cfdi_validator.is_valid
      if self.is_valid:
        cfdi_validator.generar_tfd()
        self.xml_signed = cfdi_validator.xml_string_tfd
        self.uuid = cfdi_validator.uuid
    except Exception as e:
      print(f'Exception on stamp_process {e}')


def create_json_asp(taxpayer_id):
  asp_json = {}
  try:
    business_obj = Business.objects.get(taxpayer_id=taxpayer_id)
    asp_json = {
        "AccountingSupplierParty": {
            "Party": {
                # "EndpointID": {
                #     "value": business_obj.taxpayer_id,
                #     "schemeID": business_obj.schemeid
                # },
                "PartyIdentification": [
                    {
                        "ID": {
                            "value": business_obj.taxpayer_id,
                            "schemeID": business_obj.schemeid
                        }
                    }
                ],
                "PartyName": {
                    "Name": business_obj.name
                },
                "PostalAddress": {
                    "StreetName": business_obj.address.street,
                    "AdditionalStreetName": business_obj.address.street,
                    "CityName": business_obj.address.city,
                    "PostalZone": business_obj.address.zipcode,
                    "Country": {
                        "IdentificationCode": business_obj.address.country
                    }
                },
                "PartyTaxScheme": [
                    {
                        "CompanyID": business_obj.organization_id,
                        "TaxScheme": {
                            "ID": "VAT"
                        }
                    }
                ],
                # "PartyLegalEntity":{
                #     "RegistrationName": business_obj.name,
                #     "CompanyID": {
                #         "value": business_obj.organization_id,
                #         "schemeID": business_obj.schemeid,
                #     },
                # },
            }
        }
    }
  except Exception as e:
    print(f'Exception in create_json_asp => {str(e)}')
  #return json.dumps(asp_json)
  return asp_json


def create_json_acp(taxpayer_id, rtaxpayer_id, customer_country):
  from app.invoicing.models import Buyer
  acp_json = {}
  try:
    business_obj = Business.objects.get(taxpayer_id=taxpayer_id)
    buyer_obj = Buyer.objects.get(
        business_id=business_obj.id, tax_idenfier_number=rtaxpayer_id)
    country_acp = {}
    if customer_country:
      country_acp = {
          # "IdentificationCode": buyer_obj.country
          "IdentificationCode": customer_country
      }
    acp_json = {
        "AccountingCustomerParty": {
            "Party": {
                # "EndpointID": {
                #     "value": buyer_obj.tax_idenfier_number,
                #     "schemeID": "0002"
                # },
                "PartyIdentification": [
                    {
                        "ID": {
                            "value": buyer_obj.tax_idenfier_number,
                        }
                    }
                ],
                "PartyName": {
                    "Name": buyer_obj.company_name
                },
                "PostalAddress": {
                    "StreetName": buyer_obj.address_name,
                    "AdditionalStreetName": buyer_obj.address_name,
                    "CityName": buyer_obj.city_name,
                    "PostalZone": buyer_obj.postal_zone,
                    "Country": country_acp,
                },
                # "PartyTaxScheme": [
                #     {
                #     "CompanyID": buyer_obj.tax_idenfier_number,
                #     "TaxScheme": {
                #         "ID": "VAT"
                #     }
                #     }
                # ],
                # "PartyLegalEntity":{
                #     "RegistrationName": buyer_obj.organization_id,
                #     "CompanyID": {
                #         "value": buyer_obj.tax_idenfier_number,
                #         "schemeID": "0183",
                #     },
                # },
                # "Contact": {
                #     "Name": buyer_obj.company_name,
                #     "Telephone": buyer_obj.telephone_contact,
                #     "ElectronicMail": buyer_obj.email_contact
                # }
            }
        }
    }
  except Exception as e:
    print(f'Exception in create_json_acp => {str(e)}')
  #return json.dumps(acp_json)
  return acp_json


def create_json_delivery(invoice_json, taxpayer_id):
  delivery_json = {}
  try:
    business_obj = Business.objects.get(taxpayer_id=taxpayer_id)
    delivery_json = {
        "Delivery": {
            "ActualDeliveryDate": invoice_json['IssueDate'],
            "DeliveryLocation": {
                "ID": {
                    "value": invoice_json['ID'],
                    "schemeID": business_obj.schemeid,
                },
                "Address": {
                    "StreetName": business_obj.address.street,
                    "AdditionalStreetName": business_obj.address.street,
                    "CityName": business_obj.address.city,
                    "PostalZone": business_obj.address.zipcode,
                    "Country": {
                        "IdentificationCode": business_obj.address.country
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
  except Exception as e:
    print(f'Exception in create_json_delivery => {str(e)}')
  #return json.dumps(delivery_json)
  return delivery_json


def create_json_payment_means(code, name):
  payment_means_json = {}
  try:
    payment_means_json = {
        "PaymentMeans": {
            "PaymentMeansCode": {
                "value": code,
                "name": name
            },
            # "PaymentID": "Snippet1",
            # "PayeeFinancialAccount": {
            #     "ID": "NO99991122222",
            #     "Name": "Payment Account",
            #     "FinancialInstitutionBranch":{
            #         "ID": "BIC324098"
            #     }
            # },
        }
    }
  except Exception as e:
    print(f'Exception in create_json_payment_means => {str(e)}')
  #return json.dumps(payment_means_json)
  return payment_means_json


def create_json_payment_terms(notes):
  payment_terms_json = {}
  try:
    payment_terms_json = {
        "PaymentTerms": {
            "Note": notes
        }
    }
  except Exception as e:
    print(f'Exception in create_json_payment_terms => {str(e)}')
  #return json.dumps(payment_terms_json)
  return payment_terms_json


def create_json_allowance_charge():
  allowance_charge_json = {}
  try:
    if False:
      allowance_charge_json = {
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
  except Exception as e:
    print(f'Exception in create_json_allowance_charge => {str(e)}')
  #return json.dumps(allowance_charge_json)
  return allowance_charge_json


def create_json_tax_total(json_, document_currency):
  tax_total_json = {}
  #{'TaxSubtotal': [{'value': '20', 'ID': 'S', 'Percent': '20'}, {'value': '10', 'ID': 'AE', 'Percent': '10'}]}
  print(json_)
  try:
    tax_total_json = {
        "TaxTotal": [
            {
                "TaxAmount": {
                    "value": json_['total_taxes'],
                    "currencyID": document_currency
                }
            }
        ]
    }
    taxes_dic = json_['TaxSubtotal']
    if len(taxes_dic):
      dict_new_taxes = []
      for taxes in taxes_dic:
        if len(dict_new_taxes):
          duplicate = False
          pos = 0
          for new_taxes in dict_new_taxes:
            if new_taxes['TaxCategory']['Percent'] == taxes['value'] and new_taxes['TaxCategory']['ID'] == taxes['ID']:
              duplicate = True
              break
            pos += 1
          if duplicate:
            dict_new_taxes[pos]['TaxAmount']['value'] = dict_new_taxes[pos]['TaxAmount']['value'] + \
                float(taxes['value'])
          else:
            dict_new_taxes.append({
                "TaxableAmount": {
                    "value": json_['total_invoice'],
                    "currencyID": json_['currency']
                },
                "TaxAmount": {
                    "value": float(taxes['value']),
                    "currencyID": json_['currency']
                },
                "TaxCategory": {
                    "ID": taxes['ID'],
                    "Percent": taxes['Percent'],
                    "TaxScheme": {
                        # "ID": json_['currency']
                        "ID": "VAT"
                    }
                }
            })
        else:
          dict_new_taxes.append({
              "TaxableAmount": {
                  "value": json_['total_invoice'],
                  "currencyID": json_['currency']
              },
              "TaxAmount": {
                  "value": float(taxes['value']),
                  "currencyID": json_['currency']
              },
              "TaxCategory": {
                  "ID": taxes['ID'],
                  "Percent": taxes['value'],
                  "TaxScheme": {
                    #   "ID": json_['currency']
                    "ID": "VAT"
                  }
              }
          })
      tax_total_json['TaxTotal'][0]['TaxSubtotal'] = dict_new_taxes
  except Exception as e:
    print(f'Exception in create_json_tax_total => {str(e)}')
  #return json.dumps(tax_total_json)
  return tax_total_json


def create_json_legal_monetary_total(json_):
  legal_monetary_total_json = {}
  # set_trace()
  try:
    legal_monetary_total_json = {
        "LegalMonetaryTotal": {
            "LineExtensionAmount": {
                "value": float(json_['SubTotal']),
                "currencyID": json_['currency']
            },
            "TaxExclusiveAmount": {
                "value": float(json_['SubTotal']),
                "currencyID": json_['currency']
            },
            "TaxInclusiveAmount": {
                "value": float(json_['total']),
                "currencyID": json_['currency']
            },
            "ChargeTotalAmount": {
                "value": float(json_['total_taxes']),
                "currencyID": json_['currency']
            },
            "PayableAmount": {
                "value": json_['total'],
                "currencyID": json_['currency']
            },
            "AllowanceTotalAmount": {
                "value": json_['discountInvoice'],
                "currencyID": json_['currency']
            },
        }
    }
  except Exception as e:
    print(f'Exception in create_json_legal_monetary_total => {str(e)}')
  #return json.dumps(legal_monetary_total_json)
  return legal_monetary_total_json


def create_json_invoice_lines(json_, taxpayer_id):
  from app.invoicing.models import ProdServ
  from pdb import set_trace

  invoice_lines_json = {}
  try:
    invoice_line = []
    business_obj = Business.objects.get(taxpayer_id=taxpayer_id)
    item_ = 1
    price_amount = 0
    # set_trace()
    for item in json_:
      #{'item_id': '1234', 'quantity': '1.0', 'discount': '0.0', 'amount': '100'}
      new_item = ProdServ.objects.get(
          standard_item_identifier=item['item_id'], business_id=business_obj.id)
      price_amount = float(item['amount'])-float(item['discount']) if float(item['discount']) > 0.0 and float(item['discount']) < float(item['amount']) else new_item.unit_price
      invoice_line.append({
          "ID": item_,
          "InvoicedQuantity": {
              "value": item['quantity'],
              "unitCode": new_item.unit_code
          },
          "LineExtensionAmount": {
              "value": float(item['amount']),
              "currencyID": item['currency']
          },
          # "AccountingCost": item['accounting_cost'],
          "OrderLineReference": {
              "LineID": new_item.item_classification_code
          },
          # "AllowanceCharge":{
          #   "Amount": item['amount'],
          #   "currencyID": item['currency']
          # }
          "Item": {
              "Description": new_item.description,
              "Name": new_item.name,
              "StandardItemIdentification": {
                  "ID": {
                      "value": new_item.standard_item_identifier,
                      "schemeID": new_item.standard_item_scheme
                  }
              },
              # "OriginCountry": {
              #     "IdentificationCode": item['country']
              # },
              "CommodityClassification": [{
                  "ItemClassificationCode": {
                      "value": new_item.item_classification_code,
                      "listID": new_item.list_id,
                  }
              }],
              "ClassifiedTaxCategory": {
                  "ID": item['tax_type'],
                  "Percent": item['tax_percent'],
                  "TaxScheme": {
                      "ID": "VAT"
                  }
              },
          },
          "Price": {
              "PriceAmount": {
                  # "value": new_item.unit_price,
                  "value": price_amount,
                  "currencyID": item['currency']
              },
          },
          "AllowanceCharge": [{
              "ChargeIndicator": "false",
              "Amount": {
                  "value": float(item['discount']),
                  "currencyID": item['currency'],
              }
          }],
          # "AllowanceCharge": [{
          #   "ChargeIndicator": "false",
          #   "AllowanceChargeReasonCode": "95",
          #   "AllowanceChargeReason": "Discount",
          #   "MultiplierFactorNumeric": "20",
          #   "Amount": {
          #     "value": float(item['discount']),
          #     "currencyID": item['currency'],
          #   },
          #   "BaseAmount": {
          #     "value": "1000",
          #     "currencyID": "EUR"
          #   }
          # }],
      })
      item_ += 1
    invoice_lines_json["InvoiceLine"] = invoice_line
  except Exception as e:
    print(f'Exception in create_json_legal_monetary_total => {str(e)}')
  #return json.dumps(invoice_lines_json)
  return invoice_lines_json


def create_ubl_extensions_json(taxpayer_id):
    import base64
    from app.core.models import SatFile, Business
    from pdb import set_trace
    ubl_extensions_json = {}
    # set_trace()
    try:
        business = Business.objects.get(taxpayer_id=taxpayer_id)
        # sat_file = SatFile.objects.filter(business_id=business.id, default=True).last()
        ubl_extensions_json = {
            "Reference":{
                "DigestValue": "+pruib33lOapq6GSw58GgQLR8VGIGqANloj4EqB1cb4=",
            },
            "SignatureValue": "Oatv5xMfFInuGqiX9SoLDTy2yuLf0tTlMFkWtkdw1z/Ss6kiDz+vIgZhgKfIaxp+JbVy57GT50VLMLatdwPVRbrWmz1/NIy5CWp1xWMaM6fC/9SXV0O1Lqopk0UeX2I2yuf05QhmVfjgUu6GnS3m6o6zM9J36iDvMVZyj7vbJTwI8SfWjTSNqxXlqPQ==",
            "X509Data":{
                "X509SubjectName": "1.2.840.113549.1.9.1=#161a4253554c434140534f55544845524e504552552e434f4d2e5045,CN=Juan Robles,OU=20889666312,O= SOPORTE TECNOLOGICO EIRL,L=LIMA,ST=LIMA,C=PE",
                # "X509Certificate": sat_file.cer
                "X509Certificate": ""
            }
        }
    except Exception as e:
        print(f"Exception in create_ubl_extensions_json | {e}")
    
    return ubl_extensions_json