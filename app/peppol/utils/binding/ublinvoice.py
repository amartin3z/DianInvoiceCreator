# ./ublinvoice.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a2b8949e26b759117ed16c657925d1ffae948838
# Generated 2020-05-26 15:40:38.331423 by PyXB version 1.2.6 using Python 3.7.5.final.0
# Namespace urn:oasis:names:specification:ubl:schema:xsd:Invoice-2

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:264924c2-9f91-11ea-91c2-ab4d45d74940')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
from . import _cac as _ImportedBinding__cac
from . import _cbc as _ImportedBinding__cbc
from . import _ext as _ImportedBinding__ext

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:oasis:names:specification:ubl:schema:xsd:Invoice-2', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cac = _ImportedBinding__cac.Namespace
_Namespace_cac.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cbc = _ImportedBinding__cbc.Namespace
_Namespace_cbc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ext = _ImportedBinding__ext.Namespace
_Namespace_ext.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:Invoice-2}InvoiceType with content type ELEMENT_ONLY
class InvoiceType (pyxb.binding.basis.complexTypeDefinition):
    """
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 14, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AccountingCustomerParty uses Python identifier AccountingCustomerParty
    __AccountingCustomerParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'AccountingCustomerParty'), 'AccountingCustomerParty', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2AccountingCustomerParty', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 8, 3), )

    
    AccountingCustomerParty = property(__AccountingCustomerParty.value, __AccountingCustomerParty.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AccountingSupplierParty uses Python identifier AccountingSupplierParty
    __AccountingSupplierParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'AccountingSupplierParty'), 'AccountingSupplierParty', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2AccountingSupplierParty', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 9, 3), )

    
    AccountingSupplierParty = property(__AccountingSupplierParty.value, __AccountingSupplierParty.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AdditionalDocumentReference uses Python identifier AdditionalDocumentReference
    __AdditionalDocumentReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'AdditionalDocumentReference'), 'AdditionalDocumentReference', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2AdditionalDocumentReference', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 21, 3), )

    
    AdditionalDocumentReference = property(__AdditionalDocumentReference.value, __AdditionalDocumentReference.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AllowanceCharge uses Python identifier AllowanceCharge
    __AllowanceCharge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'AllowanceCharge'), 'AllowanceCharge', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2AllowanceCharge', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 33, 3), )

    
    AllowanceCharge = property(__AllowanceCharge.value, __AllowanceCharge.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}BillingReference uses Python identifier BillingReference
    __BillingReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'BillingReference'), 'BillingReference', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2BillingReference', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 60, 3), )

    
    BillingReference = property(__BillingReference.value, __BillingReference.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}BuyerCustomerParty uses Python identifier BuyerCustomerParty
    __BuyerCustomerParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'BuyerCustomerParty'), 'BuyerCustomerParty', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2BuyerCustomerParty', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 68, 3), )

    
    BuyerCustomerParty = property(__BuyerCustomerParty.value, __BuyerCustomerParty.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}ContractDocumentReference uses Python identifier ContractDocumentReference
    __ContractDocumentReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'ContractDocumentReference'), 'ContractDocumentReference', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2ContractDocumentReference', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 124, 3), )

    
    ContractDocumentReference = property(__ContractDocumentReference.value, __ContractDocumentReference.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Delivery uses Python identifier Delivery
    __Delivery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'Delivery'), 'Delivery', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2Delivery', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 150, 3), )

    
    Delivery = property(__Delivery.value, __Delivery.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}DeliveryTerms uses Python identifier DeliveryTerms
    __DeliveryTerms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'DeliveryTerms'), 'DeliveryTerms', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2DeliveryTerms', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 157, 3), )

    
    DeliveryTerms = property(__DeliveryTerms.value, __DeliveryTerms.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}DespatchDocumentReference uses Python identifier DespatchDocumentReference
    __DespatchDocumentReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'DespatchDocumentReference'), 'DespatchDocumentReference', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2DespatchDocumentReference', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 165, 3), )

    
    DespatchDocumentReference = property(__DespatchDocumentReference.value, __DespatchDocumentReference.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}InvoiceLine uses Python identifier InvoiceLine
    __InvoiceLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'InvoiceLine'), 'InvoiceLine', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2InvoiceLine', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 283, 3), )

    
    InvoiceLine = property(__InvoiceLine.value, __InvoiceLine.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}InvoicePeriod uses Python identifier InvoicePeriod
    __InvoicePeriod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'InvoicePeriod'), 'InvoicePeriod', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2InvoicePeriod', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 284, 3), )

    
    InvoicePeriod = property(__InvoicePeriod.value, __InvoicePeriod.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}LegalMonetaryTotal uses Python identifier LegalMonetaryTotal
    __LegalMonetaryTotal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'LegalMonetaryTotal'), 'LegalMonetaryTotal', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2LegalMonetaryTotal', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 305, 3), )

    
    LegalMonetaryTotal = property(__LegalMonetaryTotal.value, __LegalMonetaryTotal.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}OrderReference uses Python identifier OrderReference
    __OrderReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'OrderReference'), 'OrderReference', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2OrderReference', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 363, 3), )

    
    OrderReference = property(__OrderReference.value, __OrderReference.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}OriginatorDocumentReference uses Python identifier OriginatorDocumentReference
    __OriginatorDocumentReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'OriginatorDocumentReference'), 'OriginatorDocumentReference', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2OriginatorDocumentReference', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 373, 3), )

    
    OriginatorDocumentReference = property(__OriginatorDocumentReference.value, __OriginatorDocumentReference.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PayeeParty uses Python identifier PayeeParty
    __PayeeParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'PayeeParty'), 'PayeeParty', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2PayeeParty', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 391, 3), )

    
    PayeeParty = property(__PayeeParty.value, __PayeeParty.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PaymentAlternativeExchangeRate uses Python identifier PaymentAlternativeExchangeRate
    __PaymentAlternativeExchangeRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentAlternativeExchangeRate'), 'PaymentAlternativeExchangeRate', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2PaymentAlternativeExchangeRate', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 395, 3), )

    
    PaymentAlternativeExchangeRate = property(__PaymentAlternativeExchangeRate.value, __PaymentAlternativeExchangeRate.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PaymentExchangeRate uses Python identifier PaymentExchangeRate
    __PaymentExchangeRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentExchangeRate'), 'PaymentExchangeRate', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2PaymentExchangeRate', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 396, 3), )

    
    PaymentExchangeRate = property(__PaymentExchangeRate.value, __PaymentExchangeRate.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PaymentMeans uses Python identifier PaymentMeans
    __PaymentMeans = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentMeans'), 'PaymentMeans', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2PaymentMeans', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 398, 3), )

    
    PaymentMeans = property(__PaymentMeans.value, __PaymentMeans.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PaymentTerms uses Python identifier PaymentTerms
    __PaymentTerms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentTerms'), 'PaymentTerms', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2PaymentTerms', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 400, 3), )

    
    PaymentTerms = property(__PaymentTerms.value, __PaymentTerms.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PrepaidPayment uses Python identifier PrepaidPayment
    __PrepaidPayment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'PrepaidPayment'), 'PrepaidPayment', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2PrepaidPayment', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 425, 3), )

    
    PrepaidPayment = property(__PrepaidPayment.value, __PrepaidPayment.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PricingExchangeRate uses Python identifier PricingExchangeRate
    __PricingExchangeRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'PricingExchangeRate'), 'PricingExchangeRate', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2PricingExchangeRate', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 434, 3), )

    
    PricingExchangeRate = property(__PricingExchangeRate.value, __PricingExchangeRate.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}ProjectReference uses Python identifier ProjectReference
    __ProjectReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'ProjectReference'), 'ProjectReference', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2ProjectReference', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 440, 3), )

    
    ProjectReference = property(__ProjectReference.value, __ProjectReference.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}ReceiptDocumentReference uses Python identifier ReceiptDocumentReference
    __ReceiptDocumentReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'ReceiptDocumentReference'), 'ReceiptDocumentReference', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2ReceiptDocumentReference', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 456, 3), )

    
    ReceiptDocumentReference = property(__ReceiptDocumentReference.value, __ReceiptDocumentReference.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}SellerSupplierParty uses Python identifier SellerSupplierParty
    __SellerSupplierParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'SellerSupplierParty'), 'SellerSupplierParty', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2SellerSupplierParty', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 529, 3), )

    
    SellerSupplierParty = property(__SellerSupplierParty.value, __SellerSupplierParty.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'Signature'), 'Signature', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2Signature', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 546, 3), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}StatementDocumentReference uses Python identifier StatementDocumentReference
    __StatementDocumentReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'StatementDocumentReference'), 'StatementDocumentReference', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2StatementDocumentReference', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 551, 3), )

    
    StatementDocumentReference = property(__StatementDocumentReference.value, __StatementDocumentReference.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxExchangeRate uses Python identifier TaxExchangeRate
    __TaxExchangeRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'TaxExchangeRate'), 'TaxExchangeRate', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2TaxExchangeRate', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 586, 3), )

    
    TaxExchangeRate = property(__TaxExchangeRate.value, __TaxExchangeRate.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxRepresentativeParty uses Python identifier TaxRepresentativeParty
    __TaxRepresentativeParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'TaxRepresentativeParty'), 'TaxRepresentativeParty', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2TaxRepresentativeParty', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 589, 3), )

    
    TaxRepresentativeParty = property(__TaxRepresentativeParty.value, __TaxRepresentativeParty.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxTotal uses Python identifier TaxTotal
    __TaxTotal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'TaxTotal'), 'TaxTotal', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2TaxTotal', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 592, 3), )

    
    TaxTotal = property(__TaxTotal.value, __TaxTotal.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}WithholdingTaxTotal uses Python identifier WithholdingTaxTotal
    __WithholdingTaxTotal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cac, 'WithholdingTaxTotal'), 'WithholdingTaxTotal', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonAggregateComponents_2WithholdingTaxTotal', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 670, 3), )

    
    WithholdingTaxTotal = property(__WithholdingTaxTotal.value, __WithholdingTaxTotal.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}AccountingCost uses Python identifier AccountingCost
    __AccountingCost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'AccountingCost'), 'AccountingCost', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2AccountingCost', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 11, 3), )

    
    AccountingCost = property(__AccountingCost.value, __AccountingCost.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}AccountingCostCode uses Python identifier AccountingCostCode
    __AccountingCostCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'AccountingCostCode'), 'AccountingCostCode', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2AccountingCostCode', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 12, 3), )

    
    AccountingCostCode = property(__AccountingCostCode.value, __AccountingCostCode.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}BuyerReference uses Python identifier BuyerReference
    __BuyerReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'BuyerReference'), 'BuyerReference', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2BuyerReference', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 90, 3), )

    
    BuyerReference = property(__BuyerReference.value, __BuyerReference.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CopyIndicator uses Python identifier CopyIndicator
    __CopyIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'CopyIndicator'), 'CopyIndicator', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2CopyIndicator', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 174, 3), )

    
    CopyIndicator = property(__CopyIndicator.value, __CopyIndicator.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CustomizationID uses Python identifier CustomizationID
    __CustomizationID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'CustomizationID'), 'CustomizationID', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2CustomizationID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 192, 3), )

    
    CustomizationID = property(__CustomizationID.value, __CustomizationID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}DocumentCurrencyCode uses Python identifier DocumentCurrencyCode
    __DocumentCurrencyCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'DocumentCurrencyCode'), 'DocumentCurrencyCode', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2DocumentCurrencyCode', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 221, 3), )

    
    DocumentCurrencyCode = property(__DocumentCurrencyCode.value, __DocumentCurrencyCode.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}DueDate uses Python identifier DueDate
    __DueDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'DueDate'), 'DueDate', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2DueDate', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 231, 3), )

    
    DueDate = property(__DueDate.value, __DueDate.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ID'), 'ID', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2ID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 327, 3), )

    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}InvoiceTypeCode uses Python identifier InvoiceTypeCode
    __InvoiceTypeCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'InvoiceTypeCode'), 'InvoiceTypeCode', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2InvoiceTypeCode', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 346, 3), )

    
    InvoiceTypeCode = property(__InvoiceTypeCode.value, __InvoiceTypeCode.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IssueDate uses Python identifier IssueDate
    __IssueDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'IssueDate'), 'IssueDate', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2IssueDate', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 349, 3), )

    
    IssueDate = property(__IssueDate.value, __IssueDate.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IssueTime uses Python identifier IssueTime
    __IssueTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'IssueTime'), 'IssueTime', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2IssueTime', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 351, 3), )

    
    IssueTime = property(__IssueTime.value, __IssueTime.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}LineCountNumeric uses Python identifier LineCountNumeric
    __LineCountNumeric = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'LineCountNumeric'), 'LineCountNumeric', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2LineCountNumeric', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 384, 3), )

    
    LineCountNumeric = property(__LineCountNumeric.value, __LineCountNumeric.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Note uses Python identifier Note
    __Note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'Note'), 'Note', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2Note', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 473, 3), )

    
    Note = property(__Note.value, __Note.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PaymentAlternativeCurrencyCode uses Python identifier PaymentAlternativeCurrencyCode
    __PaymentAlternativeCurrencyCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'PaymentAlternativeCurrencyCode'), 'PaymentAlternativeCurrencyCode', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2PaymentAlternativeCurrencyCode', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 530, 3), )

    
    PaymentAlternativeCurrencyCode = property(__PaymentAlternativeCurrencyCode.value, __PaymentAlternativeCurrencyCode.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PaymentCurrencyCode uses Python identifier PaymentCurrencyCode
    __PaymentCurrencyCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'PaymentCurrencyCode'), 'PaymentCurrencyCode', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2PaymentCurrencyCode', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 532, 3), )

    
    PaymentCurrencyCode = property(__PaymentCurrencyCode.value, __PaymentCurrencyCode.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PricingCurrencyCode uses Python identifier PricingCurrencyCode
    __PricingCurrencyCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'PricingCurrencyCode'), 'PricingCurrencyCode', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2PricingCurrencyCode', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 581, 3), )

    
    PricingCurrencyCode = property(__PricingCurrencyCode.value, __PricingCurrencyCode.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ProfileExecutionID uses Python identifier ProfileExecutionID
    __ProfileExecutionID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileExecutionID'), 'ProfileExecutionID', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2ProfileExecutionID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 596, 3), )

    
    ProfileExecutionID = property(__ProfileExecutionID.value, __ProfileExecutionID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ProfileID uses Python identifier ProfileID
    __ProfileID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileID'), 'ProfileID', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2ProfileID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 597, 3), )

    
    ProfileID = property(__ProfileID.value, __ProfileID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxCurrencyCode uses Python identifier TaxCurrencyCode
    __TaxCurrencyCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'TaxCurrencyCode'), 'TaxCurrencyCode', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2TaxCurrencyCode', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 755, 3), )

    
    TaxCurrencyCode = property(__TaxCurrencyCode.value, __TaxCurrencyCode.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxPointDate uses Python identifier TaxPointDate
    __TaxPointDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'TaxPointDate'), 'TaxPointDate', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2TaxPointDate', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 766, 3), )

    
    TaxPointDate = property(__TaxPointDate.value, __TaxPointDate.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UBLVersionID uses Python identifier UBLVersionID
    __UBLVersionID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'UBLVersionID'), 'UBLVersionID', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2UBLVersionID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 843, 3), )

    
    UBLVersionID = property(__UBLVersionID.value, __UBLVersionID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UUID uses Python identifier UUID
    __UUID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'UUID'), 'UUID', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2UUID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 846, 3), )

    
    UUID = property(__UUID.value, __UUID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}UBLExtensions uses Python identifier UBLExtensions
    __UBLExtensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ext, 'UBLExtensions'), 'UBLExtensions', '__urnoasisnamesspecificationublschemaxsdInvoice_2_InvoiceType_urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2UBLExtensions', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 8, 2), )

    
    UBLExtensions = property(__UBLExtensions.value, __UBLExtensions.set, None, '\n        A container for all extensions present in the document.\n      ')

    _ElementMap.update({
        __AccountingCustomerParty.name() : __AccountingCustomerParty,
        __AccountingSupplierParty.name() : __AccountingSupplierParty,
        __AdditionalDocumentReference.name() : __AdditionalDocumentReference,
        __AllowanceCharge.name() : __AllowanceCharge,
        __BillingReference.name() : __BillingReference,
        __BuyerCustomerParty.name() : __BuyerCustomerParty,
        __ContractDocumentReference.name() : __ContractDocumentReference,
        __Delivery.name() : __Delivery,
        __DeliveryTerms.name() : __DeliveryTerms,
        __DespatchDocumentReference.name() : __DespatchDocumentReference,
        __InvoiceLine.name() : __InvoiceLine,
        __InvoicePeriod.name() : __InvoicePeriod,
        __LegalMonetaryTotal.name() : __LegalMonetaryTotal,
        __OrderReference.name() : __OrderReference,
        __OriginatorDocumentReference.name() : __OriginatorDocumentReference,
        __PayeeParty.name() : __PayeeParty,
        __PaymentAlternativeExchangeRate.name() : __PaymentAlternativeExchangeRate,
        __PaymentExchangeRate.name() : __PaymentExchangeRate,
        __PaymentMeans.name() : __PaymentMeans,
        __PaymentTerms.name() : __PaymentTerms,
        __PrepaidPayment.name() : __PrepaidPayment,
        __PricingExchangeRate.name() : __PricingExchangeRate,
        __ProjectReference.name() : __ProjectReference,
        __ReceiptDocumentReference.name() : __ReceiptDocumentReference,
        __SellerSupplierParty.name() : __SellerSupplierParty,
        __Signature.name() : __Signature,
        __StatementDocumentReference.name() : __StatementDocumentReference,
        __TaxExchangeRate.name() : __TaxExchangeRate,
        __TaxRepresentativeParty.name() : __TaxRepresentativeParty,
        __TaxTotal.name() : __TaxTotal,
        __WithholdingTaxTotal.name() : __WithholdingTaxTotal,
        __AccountingCost.name() : __AccountingCost,
        __AccountingCostCode.name() : __AccountingCostCode,
        __BuyerReference.name() : __BuyerReference,
        __CopyIndicator.name() : __CopyIndicator,
        __CustomizationID.name() : __CustomizationID,
        __DocumentCurrencyCode.name() : __DocumentCurrencyCode,
        __DueDate.name() : __DueDate,
        __ID.name() : __ID,
        __InvoiceTypeCode.name() : __InvoiceTypeCode,
        __IssueDate.name() : __IssueDate,
        __IssueTime.name() : __IssueTime,
        __LineCountNumeric.name() : __LineCountNumeric,
        __Note.name() : __Note,
        __PaymentAlternativeCurrencyCode.name() : __PaymentAlternativeCurrencyCode,
        __PaymentCurrencyCode.name() : __PaymentCurrencyCode,
        __PricingCurrencyCode.name() : __PricingCurrencyCode,
        __ProfileExecutionID.name() : __ProfileExecutionID,
        __ProfileID.name() : __ProfileID,
        __TaxCurrencyCode.name() : __TaxCurrencyCode,
        __TaxPointDate.name() : __TaxPointDate,
        __UBLVersionID.name() : __UBLVersionID,
        __UUID.name() : __UUID,
        __UBLExtensions.name() : __UBLExtensions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InvoiceType = InvoiceType
Namespace.addCategoryObject('typeBinding', 'InvoiceType', InvoiceType)


Invoice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Invoice'), InvoiceType, documentation='This element MUST be conveyed as the root element in any instance document based on this Schema expression', location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 7, 3))
Namespace.addCategoryObject('elementBinding', Invoice.name().localName(), Invoice)



InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'AccountingCustomerParty'), _ImportedBinding__cac.CustomerPartyType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 8, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'AccountingSupplierParty'), _ImportedBinding__cac.SupplierPartyType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 9, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'AdditionalDocumentReference'), _ImportedBinding__cac.DocumentReferenceType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 21, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'AllowanceCharge'), _ImportedBinding__cac.AllowanceChargeType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 33, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'BillingReference'), _ImportedBinding__cac.BillingReferenceType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 60, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'BuyerCustomerParty'), _ImportedBinding__cac.CustomerPartyType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 68, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'ContractDocumentReference'), _ImportedBinding__cac.DocumentReferenceType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 124, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'Delivery'), _ImportedBinding__cac.DeliveryType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 150, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'DeliveryTerms'), _ImportedBinding__cac.DeliveryTermsType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 157, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'DespatchDocumentReference'), _ImportedBinding__cac.DocumentReferenceType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 165, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'InvoiceLine'), _ImportedBinding__cac.InvoiceLineType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 283, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'InvoicePeriod'), _ImportedBinding__cac.PeriodType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 284, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'LegalMonetaryTotal'), _ImportedBinding__cac.MonetaryTotalType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 305, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'OrderReference'), _ImportedBinding__cac.OrderReferenceType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 363, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'OriginatorDocumentReference'), _ImportedBinding__cac.DocumentReferenceType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 373, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'PayeeParty'), _ImportedBinding__cac.PartyType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 391, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentAlternativeExchangeRate'), _ImportedBinding__cac.ExchangeRateType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 395, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentExchangeRate'), _ImportedBinding__cac.ExchangeRateType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 396, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentMeans'), _ImportedBinding__cac.PaymentMeansType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 398, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentTerms'), _ImportedBinding__cac.PaymentTermsType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 400, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'PrepaidPayment'), _ImportedBinding__cac.PaymentType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 425, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'PricingExchangeRate'), _ImportedBinding__cac.ExchangeRateType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 434, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'ProjectReference'), _ImportedBinding__cac.ProjectReferenceType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 440, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'ReceiptDocumentReference'), _ImportedBinding__cac.DocumentReferenceType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 456, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'SellerSupplierParty'), _ImportedBinding__cac.SupplierPartyType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 529, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'Signature'), _ImportedBinding__cac.SignatureType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 546, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'StatementDocumentReference'), _ImportedBinding__cac.DocumentReferenceType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 551, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'TaxExchangeRate'), _ImportedBinding__cac.ExchangeRateType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 586, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'TaxRepresentativeParty'), _ImportedBinding__cac.PartyType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 589, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'TaxTotal'), _ImportedBinding__cac.TaxTotalType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 592, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cac, 'WithholdingTaxTotal'), _ImportedBinding__cac.TaxTotalType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd', 670, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'AccountingCost'), _ImportedBinding__cbc.AccountingCostType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 11, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'AccountingCostCode'), _ImportedBinding__cbc.AccountingCostCodeType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 12, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'BuyerReference'), _ImportedBinding__cbc.BuyerReferenceType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 90, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'CopyIndicator'), _ImportedBinding__cbc.CopyIndicatorType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 174, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'CustomizationID'), _ImportedBinding__cbc.CustomizationIDType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 192, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'DocumentCurrencyCode'), _ImportedBinding__cbc.DocumentCurrencyCodeType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 221, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'DueDate'), _ImportedBinding__cbc.DueDateType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 231, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ID'), _ImportedBinding__cbc.IDType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 327, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'InvoiceTypeCode'), _ImportedBinding__cbc.InvoiceTypeCodeType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 346, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'IssueDate'), _ImportedBinding__cbc.IssueDateType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 349, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'IssueTime'), _ImportedBinding__cbc.IssueTimeType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 351, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'LineCountNumeric'), _ImportedBinding__cbc.LineCountNumericType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 384, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'Note'), _ImportedBinding__cbc.NoteType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 473, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'PaymentAlternativeCurrencyCode'), _ImportedBinding__cbc.PaymentAlternativeCurrencyCodeType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 530, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'PaymentCurrencyCode'), _ImportedBinding__cbc.PaymentCurrencyCodeType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 532, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'PricingCurrencyCode'), _ImportedBinding__cbc.PricingCurrencyCodeType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 581, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileExecutionID'), _ImportedBinding__cbc.ProfileExecutionIDType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 596, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileID'), _ImportedBinding__cbc.ProfileIDType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 597, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'TaxCurrencyCode'), _ImportedBinding__cbc.TaxCurrencyCodeType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 755, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'TaxPointDate'), _ImportedBinding__cbc.TaxPointDateType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 766, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'UBLVersionID'), _ImportedBinding__cbc.UBLVersionIDType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 843, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'UUID'), _ImportedBinding__cbc.UUIDType, scope=InvoiceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 846, 3)))

InvoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ext, 'UBLExtensions'), _ImportedBinding__ext.UBLExtensionsType, scope=InvoiceType, documentation='\n        A container for all extensions present in the document.\n      ', location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 8, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 26, 11))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 31, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 48, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 65, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 82, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 116, 9))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 133, 9))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 166, 9))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 182, 9))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 198, 9))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 214, 9))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 230, 9))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 246, 9))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 264, 9))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 282, 9))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 300, 9))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 318, 9))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 336, 9))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 352, 9))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 368, 9))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 384, 9))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 401, 9))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 418, 9))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 434, 9))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 450, 9))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 467, 9))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 484, 9))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 501, 9))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 518, 9))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 535, 9))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 552, 9))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 568, 9))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 618, 9))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 635, 9))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 652, 9))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 669, 9))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 686, 9))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 702, 9))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 718, 9))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 734, 9))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 750, 9))
    counters.add(cc_40)
    cc_41 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 767, 9))
    counters.add(cc_41)
    cc_42 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 783, 9))
    counters.add(cc_42)
    cc_43 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 800, 9))
    counters.add(cc_43)
    cc_44 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 817, 9))
    counters.add(cc_44)
    cc_45 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 834, 9))
    counters.add(cc_45)
    cc_46 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 851, 9))
    counters.add(cc_46)
    cc_47 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 867, 9))
    counters.add(cc_47)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ext, 'UBLExtensions')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 26, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'UBLVersionID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 31, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'CustomizationID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 48, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 65, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ProfileExecutionID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 82, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 99, 9))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'CopyIndicator')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 116, 9))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'UUID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 133, 9))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'IssueDate')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 149, 9))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'IssueTime')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 166, 9))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'DueDate')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 182, 9))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'InvoiceTypeCode')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 198, 9))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'Note')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 214, 9))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'TaxPointDate')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 230, 9))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'DocumentCurrencyCode')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 246, 9))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'TaxCurrencyCode')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 264, 9))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'PricingCurrencyCode')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 282, 9))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'PaymentCurrencyCode')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 300, 9))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'PaymentAlternativeCurrencyCode')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 318, 9))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'AccountingCostCode')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 336, 9))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'AccountingCost')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 352, 9))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'LineCountNumeric')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 368, 9))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'BuyerReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 384, 9))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'InvoicePeriod')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 401, 9))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'OrderReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 418, 9))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'BillingReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 434, 9))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'DespatchDocumentReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 450, 9))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'ReceiptDocumentReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 467, 9))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'StatementDocumentReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 484, 9))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'OriginatorDocumentReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 501, 9))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'ContractDocumentReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 518, 9))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'AdditionalDocumentReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 535, 9))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'ProjectReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 552, 9))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'Signature')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 568, 9))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'AccountingSupplierParty')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 584, 9))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'AccountingCustomerParty')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 601, 9))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'PayeeParty')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 618, 9))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'BuyerCustomerParty')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 635, 9))
    st_37 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'SellerSupplierParty')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 652, 9))
    st_38 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'TaxRepresentativeParty')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 669, 9))
    st_39 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'Delivery')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 686, 9))
    st_40 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'DeliveryTerms')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 702, 9))
    st_41 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentMeans')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 718, 9))
    st_42 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentTerms')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 734, 9))
    st_43 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'PrepaidPayment')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 750, 9))
    st_44 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'AllowanceCharge')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 767, 9))
    st_45 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_45)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'TaxExchangeRate')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 783, 9))
    st_46 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_46)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'PricingExchangeRate')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 800, 9))
    st_47 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_47)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentExchangeRate')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 817, 9))
    st_48 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_48)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'PaymentAlternativeExchangeRate')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 834, 9))
    st_49 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_49)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'TaxTotal')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 851, 9))
    st_50 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_50)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'WithholdingTaxTotal')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 867, 9))
    st_51 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_51)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'LegalMonetaryTotal')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 884, 9))
    st_52 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_52)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InvoiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cac, 'InvoiceLine')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd', 901, 9))
    st_53 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_53)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    transitions.append(fac.Transition(st_34, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
         ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
         ]))
    transitions.append(fac.Transition(st_37, [
         ]))
    transitions.append(fac.Transition(st_38, [
         ]))
    transitions.append(fac.Transition(st_39, [
         ]))
    transitions.append(fac.Transition(st_40, [
         ]))
    transitions.append(fac.Transition(st_41, [
         ]))
    transitions.append(fac.Transition(st_42, [
         ]))
    transitions.append(fac.Transition(st_43, [
         ]))
    transitions.append(fac.Transition(st_44, [
         ]))
    transitions.append(fac.Transition(st_45, [
         ]))
    transitions.append(fac.Transition(st_46, [
         ]))
    transitions.append(fac.Transition(st_47, [
         ]))
    transitions.append(fac.Transition(st_48, [
         ]))
    transitions.append(fac.Transition(st_49, [
         ]))
    transitions.append(fac.Transition(st_50, [
         ]))
    transitions.append(fac.Transition(st_51, [
         ]))
    transitions.append(fac.Transition(st_52, [
         ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_39, True) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_39, False) ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_40, True) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_40, False) ]))
    st_44._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_41, True) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_41, False) ]))
    st_45._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_42, True) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_42, False) ]))
    st_46._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_43, True) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_43, False) ]))
    st_47._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_44, True) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_44, False) ]))
    st_48._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_45, True) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_45, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_45, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_45, False) ]))
    st_49._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_46, True) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_46, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_46, False) ]))
    st_50._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_47, True) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_47, False) ]))
    st_51._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_53, [
         ]))
    st_52._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_53, [
         ]))
    st_53._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InvoiceType._Automaton = _BuildAutomaton()

