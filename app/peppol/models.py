from django.db import models
class ICD(models.Model):
	'''
	Identifier 		ICD
	Agency 			The International Organization for Standardization (ISO)
	Version 		
	Usage 			/ ubl:Invoice / cac:AccountingSupplierParty / cac:Party / cac:PartyIdentification / cbc:ID / @schemeID
					/ ubl:Invoice / cac:AccountingSupplierParty / cac:Party / cac:PartyLegalEntity / cbc:CompanyID / @schemeID
					/ ubl:Invoice / cac:AccountingCustomerParty / cac:Party / cac:PartyIdentification / cbc:ID / @schemeID
					/ ubl:Invoice / cac:AccountingCustomerParty / cac:Party / cac:PartyLegalEntity / cbc:CompanyID / @schemeID
					/ ubl:Invoice / cac:PayeeParty / cac:PartyIdentification / cbc:ID / @schemeID
					/ ubl:Invoice / cac:PayeeParty / cac:PartyLegalEntity / cbc:CompanyID / @schemeID
					/ ubl:Invoice / cac:Delivery / cac:DeliveryLocation / cbc:ID / @schemeID
					/ ubl:Invoice / cac:InvoiceLine / cac:Item / cac:StandardItemIdentification / cbc:ID / @schemeID
					/ ubl:CreditNote / cac:AccountingSupplierParty / cac:Party / cac:PartyIdentification / cbc:ID / @schemeID
					/ ubl:CreditNote / cac:AccountingSupplierParty / cac:Party / cac:PartyLegalEntity / cbc:CompanyID / @schemeID
					/ ubl:CreditNote / cac:AccountingCustomerParty / cac:Party / cac:PartyIdentification / cbc:ID / @schemeID
					/ ubl:CreditNote / cac:AccountingCustomerParty / cac:Party / cac:PartyLegalEntity / cbc:CompanyID / @schemeID
					/ ubl:CreditNote / cac:PayeeParty / cac:PartyIdentification / cbc:ID / @schemeID
					/ ubl:CreditNote / cac:PayeeParty / cac:PartyLegalEntity / cbc:CompanyID / @schemeID
					/ ubl:CreditNote / cac:Delivery / cac:DeliveryLocation / cbc:ID / @schemeID
					/ ubl:CreditNote / cac:CreditNoteLine / cac:Item / cac:StandardItemIdentification / cbc:ID / @schemeID
	'''
	code = models.CharField(max_length=4, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=1500, null=True, blank=True)


class EAS(models.Model):
	'''
	Identifier 		eas
	Agency 			CEF
	Version 		
	Usage 			/ ubl:Invoice / cac:AccountingSupplierParty / cac:Party / cbc:EndpointID / @schemeID
					/ ubl:Invoice / cac:AccountingCustomerParty / cac:Party / cbc:EndpointID / @schemeID
					/ ubl:CreditNote / cac:AccountingSupplierParty / cac:Party / cbc:EndpointID / @schemeID
					/ ubl:CreditNote / cac:AccountingCustomerParty / cac:Party / cbc:EndpointID / @schemeID
	'''
	code = models.CharField(max_length=4, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)


class ISO3166(models.Model):
	'''
	Identifier 		ISO3166
	Agency 			ISO
	Version 		2013
	Usage 			/ ubl:Invoice / cac:AccountingSupplierParty / cac:Party / cac:PostalAddress / cac:Country / cbc:IdentificationCode
					/ ubl:Invoice / cac:AccountingCustomerParty / cac:Party / cac:PostalAddress / cac:Country / cbc:IdentificationCode
					/ ubl:Invoice / cac:TaxRepresentativeParty / cac:PostalAddress / cac:Country / cbc:IdentificationCode
					/ ubl:Invoice / cac:Delivery / cac:DeliveryLocation / cac:Address / cac:Country / cbc:IdentificationCode
					/ ubl:Invoice / cac:InvoiceLine / cac:Item / cac:OriginCountry / cbc:IdentificationCode
					/ ubl:CreditNote / cac:AccountingSupplierParty / cac:Party / cac:PostalAddress / cac:Country / cbc:IdentificationCode
					/ ubl:CreditNote / cac:AccountingCustomerParty / cac:Party / cac:PostalAddress / cac:Country / cbc:IdentificationCode
					/ ubl:CreditNote / cac:TaxRepresentativeParty / cac:PostalAddress / cac:Country / cbc:IdentificationCode
					/ ubl:CreditNote / cac:Delivery / cac:DeliveryLocation / cac:Address / cac:Country / cbc:IdentificationCode
					/ ubl:CreditNote / cac:CreditNoteLine / cac:Item / cac:OriginCountry / cbc:IdentificationCode
	'''
	code = models.CharField(max_length=2, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return f'{self.code} - {self.name}'


class ISO4217(models.Model):
	'''
	Identifier 		ISO4217
	Agency 			ISO
	Version 		2018-01-01
	Usage 			/ ubl:Invoice / cbc:DocumentCurrencyCode
					/ ubl:Invoice / cbc:TaxCurrencyCode
					/ ubl:Invoice / cac:AllowanceCharge / cbc:Amount / @currencyID
					/ ubl:Invoice / cac:AllowanceCharge / cbc:BaseAmount / @currencyID
					/ ubl:Invoice / cac:TaxTotal / cbc:TaxAmount / @currencyID
					/ ubl:Invoice / cac:TaxTotal / cac:TaxSubtotal / cbc:TaxableAmount / @currencyID
					/ ubl:Invoice / cac:TaxTotal / cac:TaxSubtotal / cbc:TaxAmount / @currencyID
					/ ubl:Invoice / cac:LegalMonetaryTotal / cbc:LineExtensionAmount / @currencyID
					/ ubl:Invoice / cac:LegalMonetaryTotal / cbc:TaxExclusiveAmount / @currencyID
					/ ubl:Invoice / cac:LegalMonetaryTotal / cbc:TaxInclusiveAmount / @currencyID
					/ ubl:Invoice / cac:LegalMonetaryTotal / cbc:AllowanceTotalAmount / @currencyID
					/ ubl:Invoice / cac:LegalMonetaryTotal / cbc:ChargeTotalAmount / @currencyID
					/ ubl:Invoice / cac:LegalMonetaryTotal / cbc:PrepaidAmount / @currencyID
					/ ubl:Invoice / cac:LegalMonetaryTotal / cbc:PayableRoundingAmount / @currencyID
					/ ubl:Invoice / cac:LegalMonetaryTotal / cbc:PayableAmount / @currencyID
					/ ubl:Invoice / cac:InvoiceLine / cbc:LineExtensionAmount / @currencyID
					/ ubl:Invoice / cac:InvoiceLine / cac:AllowanceCharge / cbc:Amount / @currencyID
					/ ubl:Invoice / cac:InvoiceLine / cac:AllowanceCharge / cbc:BaseAmount / @currencyID
					/ ubl:Invoice / cac:InvoiceLine / cac:Price / cbc:PriceAmount / @currencyID
					/ ubl:Invoice / cac:InvoiceLine / cac:Price / cac:AllowanceCharge / cbc:Amount / @currencyID
					/ ubl:Invoice / cac:InvoiceLine / cac:Price / cac:AllowanceCharge / cbc:BaseAmount / @currencyID
					/ ubl:CreditNote / cbc:DocumentCurrencyCode
					/ ubl:CreditNote / cbc:TaxCurrencyCode
					/ ubl:CreditNote / cac:AllowanceCharge / cbc:Amount / @currencyID
					/ ubl:CreditNote / cac:AllowanceCharge / cbc:BaseAmount / @currencyID
					/ ubl:CreditNote / cac:TaxTotal / cbc:TaxAmount / @currencyID
					/ ubl:CreditNote / cac:TaxTotal / cac:TaxSubtotal / cbc:TaxableAmount / @currencyID
					/ ubl:CreditNote / cac:TaxTotal / cac:TaxSubtotal / cbc:TaxAmount / @currencyID
					/ ubl:CreditNote / cac:LegalMonetaryTotal / cbc:LineExtensionAmount / @currencyID
					/ ubl:CreditNote / cac:LegalMonetaryTotal / cbc:TaxExclusiveAmount / @currencyID
					/ ubl:CreditNote / cac:LegalMonetaryTotal / cbc:TaxInclusiveAmount / @currencyID
					/ ubl:CreditNote / cac:LegalMonetaryTotal / cbc:AllowanceTotalAmount / @currencyID
					/ ubl:CreditNote / cac:LegalMonetaryTotal / cbc:ChargeTotalAmount / @currencyID
					/ ubl:CreditNote / cac:LegalMonetaryTotal / cbc:PrepaidAmount / @currencyID
					/ ubl:CreditNote / cac:LegalMonetaryTotal / cbc:PayableRoundingAmount / @currencyID
					/ ubl:CreditNote / cac:LegalMonetaryTotal / cbc:PayableAmount / @currencyID
					/ ubl:CreditNote / cac:CreditNoteLine / cbc:LineExtensionAmount / @currencyID
					/ ubl:CreditNote / cac:CreditNoteLine / cac:AllowanceCharge / cbc:Amount / @currencyID
					/ ubl:CreditNote / cac:CreditNoteLine / cac:AllowanceCharge / cbc:BaseAmount / @currencyID
					/ ubl:CreditNote / cac:CreditNoteLine / cac:Price / cbc:PriceAmount / @currencyID
					/ ubl:CreditNote / cac:CreditNoteLine / cac:Price / cac:AllowanceCharge / cbc:Amount / @currencyID
					/ ubl:CreditNote / cac:CreditNoteLine / cac:Price / cac:AllowanceCharge / cbc:BaseAmount / @currencyID
	'''
	code = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return f'{self.code} - {self.name}'


class UNECEREC20(models.Model):
	'''
	Identifier 		UNECERec20
	Agency 			UN/ECE
	Version 		Revision 11e
	Usage 			/ ubl:Invoice / cac:InvoiceLine / cbc:InvoicedQuantity / @unitCode
					/ ubl:Invoice / cac:InvoiceLine / cac:Price / cbc:BaseQuantity / @unitCode
					/ ubl:CreditNote / cac:CreditNoteLine / cbc:CreditedQuantity / @unitCode
					/ ubl:CreditNote / cac:CreditNoteLine / cac:Price / cbc:BaseQuantity / @unitCode
	'''
	code = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=300, null=True, blank=True)


class UNECEREC21(models.Model):
	'''
	Identifier 		UNECERec21
	Agency 			UN/ECE
	Version 		Revision 9e-2012
	Usage 			/ ubl:Invoice / cac:InvoiceLine / cbc:InvoicedQuantity / @unitCode
					/ ubl:Invoice / cac:InvoiceLine / cac:Price / cbc:BaseQuantity / @unitCode
					/ ubl:CreditNote / cac:CreditNoteLine / cbc:CreditedQuantity / @unitCode
					/ ubl:CreditNote / cac:CreditNoteLine / cac:Price / cbc:BaseQuantity / @unitCode
	'''
	code = models.CharField(max_length=2, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=300, null=True, blank=True)


class UNCL5305(models.Model):
	'''
	Identifier 		UNCL5305
	Agency 			UN/CEFACT
	Version 		D.16B
	Usage 			/ ubl:Invoice / cac:AllowanceCharge / cac:TaxCategory / cbc:ID
					/ ubl:Invoice / cac:TaxTotal / cac:TaxSubtotal / cac:TaxCategory / cbc:ID
					/ ubl:Invoice / cac:InvoiceLine / cac:Item / cac:ClassifiedTaxCategory / cbc:ID
					/ ubl:CreditNote / cac:AllowanceCharge / cac:TaxCategory / cbc:ID
					/ ubl:CreditNote / cac:TaxTotal / cac:TaxSubtotal / cac:TaxCategory / cbc:ID
					/ ubl:CreditNote / cac:CreditNoteLine / cac:Item / cac:ClassifiedTaxCategory / cbc:ID
	'''
	code = models.CharField(max_length=2, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=300, null=True, blank=True)


class UNCL7143(models.Model):
	'''
	Identifier 		UNCL7143
	Agency 			UN/CEFACT
	Version 		D.19A
	Usage 			/ ubl:Invoice / cac:InvoiceLine / cac:Item / cac:CommodityClassification / cbc:ItemClassificationCode / @listID
					/ ubl:CreditNote / cac:CreditNoteLine / cac:Item / cac:CommodityClassification / cbc:ItemClassificationCode / @listID
	'''
	code = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=500, null=True, blank=True)


class UNCL1001INV(models.Model):
	'''
	Identifier 		UNCL1001-inv
	Agency 			UN/CEFACT
	Version 		D.16B
	Usage 			/ ubl:Invoice / cbc:InvoiceTypeCode
	'''
	code = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return f'{self.code} - {self.name}'


class UNCL1001CN(models.Model):
	'''
	Identifier 		UNCL1001-cn
	Agency 			UN/CEFACT
	Version 		D.16B
	Usage 			/ ubl:CreditNote / cbc:CreditNoteTypeCode
	'''
	code = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=200, null=True, blank=True)


class UNCL1153(models.Model):
	'''
	Identifier 		UNCL1153
	Agency 			UN/CEFACT
	Version 		D.16B
	Usage 			/ ubl:Invoice / cac:AdditionalDocumentReference / cbc:ID / @schemeID
					/ ubl:Invoice / cac:InvoiceLine / cac:DocumentReference / cbc:ID / @schemeID
					/ ubl:CreditNote / cac:AdditionalDocumentReference / cbc:ID / @schemeID
					/ ubl:CreditNote / cac:CreditNoteLine / cac:DocumentReference / cbc:ID / @schemeID
	'''
	code = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=500, null=True, blank=True)


class UNCL2005(models.Model):
	'''
	Identifier 		UNCL2005
	Agency 			UN/CEFACT
	Version 		D.16B
	Usage 			/ ubl:Invoice / cac:InvoicePeriod / cbc:DescriptionCode
					/ ubl:CreditNote / cac:InvoicePeriod / cbc:DescriptionCode
	'''
	code = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=50, null=True, blank=True)


class UNCL4461(models.Model):
	'''
	Identifier 		UNCL4461
	Agency 			UN/CEFACT
	Version 		D.16B
	Usage 			/ ubl:Invoice / cac:PaymentMeans / cbc:PaymentMeansCode
					/ ubl:CreditNote / cac:PaymentMeans / cbc:PaymentMeansCode
	'''
	code = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=500, null=True, blank=True)


class UNCL5189(models.Model):
	'''
	Identifier 		UNCL5189
	Agency 			UN/CEFACT
	Version 		D.16B
	Usage 			/ ubl:Invoice / cac:AllowanceCharge / cbc:AllowanceChargeReasonCode
					/ ubl:Invoice / cac:InvoiceLine / cac:AllowanceCharge / cbc:AllowanceChargeReasonCode
					/ ubl:CreditNote / cac:AllowanceCharge / cbc:AllowanceChargeReasonCode
					/ ubl:CreditNote / cac:CreditNoteLine / cac:AllowanceCharge / cbc:AllowanceChargeReasonCode
	'''
	code = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=50, null=True, blank=True)


class UNCL7161(models.Model):
	'''
	Identifier 		UNCL7161
	Agency 			UN/CEFACT
	Version 		D.16B
	Usage 			/ ubl:Invoice / cac:AllowanceCharge / cbc:AllowanceChargeReasonCode
					/ ubl:Invoice / cac:InvoiceLine / cac:AllowanceCharge / cbc:AllowanceChargeReasonCode
					/ ubl:CreditNote / cac:AllowanceCharge / cbc:AllowanceChargeReasonCode
					/ ubl:CreditNote / cac:CreditNoteLine / cac:AllowanceCharge / cbc:AllowanceChargeReasonCode
	'''
	code = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=80, null=True, blank=True)
	description = models.CharField(max_length=200, null=True, blank=True)

class MIMECODE(models.Model):
	'''
	Identifier 		MimeCode
	Agency 			IANA
	Version 		1.0
	Usage 			/ ubl:Invoice / cac:AdditionalDocumentReference / cac:Attachment / cbc:EmbeddedDocumentBinaryObject / @mimeCode
					/ ubl:CreditNote / cac:AdditionalDocumentReference / cac:Attachment / cbc:EmbeddedDocumentBinaryObject / @mimeCode
	'''
	code = models.CharField(max_length=80, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)

class SEPA(models.Model):
	'''
	Identifier 		SEPA
	Agency 			OpenPEPPOL
	Version 		1.0
	Usage 			/ ubl:Invoice / cac:AccountingSupplierParty / cac:Party / cac:PartyIdentification / cbc:ID / @schemeID
					/ ubl:Invoice / cac:PayeeParty / cac:PartyIdentification / cbc:ID / @schemeID
					/ ubl:CreditNote / cac:AccountingSupplierParty / cac:Party / cac:PartyIdentification / cbc:ID / @schemeID
					/ ubl:CreditNote / cac:PayeeParty / cac:PartyIdentification / cbc:ID / @schemeID
	'''
	code = models.CharField(max_length=4, null=True, blank=True)
	name = models.CharField(max_length=50, null=True, blank=True)


class VATEX(models.Model):
	'''
	Identifier 		vatex
	Agency 			CEF
	Version 		
	Usage 			
	'''
	code = models.CharField(max_length=20, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=800, null=True, blank=True)


class AnnexI(models.Model):
	groupnumber = models.CharField(max_length=2, null=True, blank=True)
	sector = models.CharField(max_length=50, null=True, blank=True)
	groupid = models.CharField(max_length=3, null=True, blank=True)
	quantity = models.CharField(max_length=300, null=True, blank=True)
	levelcategory = models.CharField(max_length=2, null=True, blank=True)
	status = models.CharField(max_length=1, null=True, blank=True)
	commoncode = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	conversionfactor = models.CharField(max_length=50, null=True, blank=True)
	symbol = models.CharField(max_length=50, null=True, blank=True)
	description = models.CharField(max_length=500, null=True, blank=True)

class AnnexII_AnnexIII(models.Model):
	status = models.CharField(max_length=1, null=True, blank=True)
	commoncode = models.CharField(max_length=3, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=500, null=True, blank=True)
	levelcategory = models.CharField(max_length=10, null=True, blank=True)
	symbol = models.CharField(max_length=50, null=True, blank=True)
	conversionfactor = models.CharField(max_length=50, null=True, blank=True)