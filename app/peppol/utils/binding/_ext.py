# ./_ext.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d82937bf083ca454ba5857f319e6717eabb00597
# Generated 2020-05-26 15:40:38.331300 by PyXB version 1.2.6 using Python 3.7.5.final.0
# Namespace urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2 [xmlns:ext]

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
from . import _cbc as _ImportedBinding__cbc
from . import _udt as _ImportedBinding__udt

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cbc = _ImportedBinding__cbc.Namespace
_Namespace_cbc.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}UBLExtensionsType with content type ELEMENT_ONLY
class UBLExtensionsType (pyxb.binding.basis.complexTypeDefinition):
    """
        A container for all extensions present in the document.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UBLExtensionsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 15, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}UBLExtension uses Python identifier UBLExtension
    __UBLExtension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UBLExtension'), 'UBLExtension', '__urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2_UBLExtensionsType_urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2UBLExtension', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 31, 2), )

    
    UBLExtension = property(__UBLExtension.value, __UBLExtension.set, None, '\n        A single extension for private use.\n      ')

    _ElementMap.update({
        __UBLExtension.name() : __UBLExtension
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UBLExtensionsType = UBLExtensionsType
Namespace.addCategoryObject('typeBinding', 'UBLExtensionsType', UBLExtensionsType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}UBLExtensionType with content type ELEMENT_ONLY
class UBLExtensionType (pyxb.binding.basis.complexTypeDefinition):
    """
        A single extension for private use.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UBLExtensionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 38, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ID'), 'ID', '__urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2_UBLExtensionType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2ID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 327, 3), )

    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'Name'), 'Name', '__urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2_UBLExtensionType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2Name', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 459, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionAgencyID uses Python identifier ExtensionAgencyID
    __ExtensionAgencyID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyID'), 'ExtensionAgencyID', '__urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2_UBLExtensionType_urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2ExtensionAgencyID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 118, 2), )

    
    ExtensionAgencyID = property(__ExtensionAgencyID.value, __ExtensionAgencyID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionAgencyName uses Python identifier ExtensionAgencyName
    __ExtensionAgencyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyName'), 'ExtensionAgencyName', '__urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2_UBLExtensionType_urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2ExtensionAgencyName', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 119, 2), )

    
    ExtensionAgencyName = property(__ExtensionAgencyName.value, __ExtensionAgencyName.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionAgencyURI uses Python identifier ExtensionAgencyURI
    __ExtensionAgencyURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyURI'), 'ExtensionAgencyURI', '__urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2_UBLExtensionType_urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2ExtensionAgencyURI', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 120, 2), )

    
    ExtensionAgencyURI = property(__ExtensionAgencyURI.value, __ExtensionAgencyURI.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionContent uses Python identifier ExtensionContent
    __ExtensionContent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtensionContent'), 'ExtensionContent', '__urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2_UBLExtensionType_urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2ExtensionContent', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 121, 2), )

    
    ExtensionContent = property(__ExtensionContent.value, __ExtensionContent.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionReason uses Python identifier ExtensionReason
    __ExtensionReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtensionReason'), 'ExtensionReason', '__urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2_UBLExtensionType_urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2ExtensionReason', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 122, 2), )

    
    ExtensionReason = property(__ExtensionReason.value, __ExtensionReason.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionReasonCode uses Python identifier ExtensionReasonCode
    __ExtensionReasonCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtensionReasonCode'), 'ExtensionReasonCode', '__urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2_UBLExtensionType_urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2ExtensionReasonCode', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 123, 2), )

    
    ExtensionReasonCode = property(__ExtensionReasonCode.value, __ExtensionReasonCode.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionURI uses Python identifier ExtensionURI
    __ExtensionURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtensionURI'), 'ExtensionURI', '__urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2_UBLExtensionType_urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2ExtensionURI', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 124, 2), )

    
    ExtensionURI = property(__ExtensionURI.value, __ExtensionURI.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionVersionID uses Python identifier ExtensionVersionID
    __ExtensionVersionID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtensionVersionID'), 'ExtensionVersionID', '__urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2_UBLExtensionType_urnoasisnamesspecificationublschemaxsdCommonExtensionComponents_2ExtensionVersionID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 125, 2), )

    
    ExtensionVersionID = property(__ExtensionVersionID.value, __ExtensionVersionID.set, None, None)

    _ElementMap.update({
        __ID.name() : __ID,
        __Name.name() : __Name,
        __ExtensionAgencyID.name() : __ExtensionAgencyID,
        __ExtensionAgencyName.name() : __ExtensionAgencyName,
        __ExtensionAgencyURI.name() : __ExtensionAgencyURI,
        __ExtensionContent.name() : __ExtensionContent,
        __ExtensionReason.name() : __ExtensionReason,
        __ExtensionReasonCode.name() : __ExtensionReasonCode,
        __ExtensionURI.name() : __ExtensionURI,
        __ExtensionVersionID.name() : __ExtensionVersionID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UBLExtensionType = UBLExtensionType
Namespace.addCategoryObject('typeBinding', 'UBLExtensionType', UBLExtensionType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionContentType with content type ELEMENT_ONLY
class ExtensionContentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionContentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionContentType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-ExtensionContentDataType-2.1.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExtensionContentType = ExtensionContentType
Namespace.addCategoryObject('typeBinding', 'ExtensionContentType', ExtensionContentType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionAgencyIDType with content type SIMPLE
class ExtensionAgencyIDType (_ImportedBinding__udt.IdentifierType):
    """Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionAgencyIDType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 126, 2)
    _ElementMap = _ImportedBinding__udt.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.IdentifierType
    
    # Attribute schemeID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeAgencyID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeAgencyName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeVersionID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeDataURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExtensionAgencyIDType = ExtensionAgencyIDType
Namespace.addCategoryObject('typeBinding', 'ExtensionAgencyIDType', ExtensionAgencyIDType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionAgencyNameType with content type SIMPLE
class ExtensionAgencyNameType (_ImportedBinding__udt.TextType):
    """Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionAgencyNameType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 131, 2)
    _ElementMap = _ImportedBinding__udt.TextType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.TextType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.TextType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    
    # Attribute languageLocaleID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExtensionAgencyNameType = ExtensionAgencyNameType
Namespace.addCategoryObject('typeBinding', 'ExtensionAgencyNameType', ExtensionAgencyNameType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionAgencyURIType with content type SIMPLE
class ExtensionAgencyURIType (_ImportedBinding__udt.IdentifierType):
    """Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionAgencyURIType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyURIType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 136, 2)
    _ElementMap = _ImportedBinding__udt.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.IdentifierType
    
    # Attribute schemeID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeAgencyID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeAgencyName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeVersionID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeDataURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExtensionAgencyURIType = ExtensionAgencyURIType
Namespace.addCategoryObject('typeBinding', 'ExtensionAgencyURIType', ExtensionAgencyURIType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionReasonType with content type SIMPLE
class ExtensionReasonType (_ImportedBinding__udt.TextType):
    """Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionReasonType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionReasonType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 141, 2)
    _ElementMap = _ImportedBinding__udt.TextType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.TextType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.TextType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    
    # Attribute languageLocaleID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExtensionReasonType = ExtensionReasonType
Namespace.addCategoryObject('typeBinding', 'ExtensionReasonType', ExtensionReasonType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionReasonCodeType with content type SIMPLE
class ExtensionReasonCodeType (_ImportedBinding__udt.CodeType):
    """Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionReasonCodeType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionReasonCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 146, 2)
    _ElementMap = _ImportedBinding__udt.CodeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.CodeType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.CodeType
    
    # Attribute listID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listAgencyID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listAgencyName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listVersionID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute name inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    
    # Attribute listSchemeURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExtensionReasonCodeType = ExtensionReasonCodeType
Namespace.addCategoryObject('typeBinding', 'ExtensionReasonCodeType', ExtensionReasonCodeType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionURIType with content type SIMPLE
class ExtensionURIType (_ImportedBinding__udt.IdentifierType):
    """Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionURIType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionURIType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 151, 2)
    _ElementMap = _ImportedBinding__udt.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.IdentifierType
    
    # Attribute schemeID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeAgencyID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeAgencyName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeVersionID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeDataURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExtensionURIType = ExtensionURIType
Namespace.addCategoryObject('typeBinding', 'ExtensionURIType', ExtensionURIType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionVersionIDType with content type SIMPLE
class ExtensionVersionIDType (_ImportedBinding__udt.IdentifierType):
    """Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionVersionIDType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionVersionIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 156, 2)
    _ElementMap = _ImportedBinding__udt.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__udt.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__udt.IdentifierType
    
    # Attribute schemeID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeAgencyID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeAgencyName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeVersionID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeDataURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    
    # Attribute schemeURI inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExtensionVersionIDType = ExtensionVersionIDType
Namespace.addCategoryObject('typeBinding', 'ExtensionVersionIDType', ExtensionVersionIDType)


UBLExtensions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UBLExtensions'), UBLExtensionsType, documentation='\n        A container for all extensions present in the document.\n      ', location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 8, 2))
Namespace.addCategoryObject('elementBinding', UBLExtensions.name().localName(), UBLExtensions)

UBLExtension = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UBLExtension'), UBLExtensionType, documentation='\n        A single extension for private use.\n      ', location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 31, 2))
Namespace.addCategoryObject('elementBinding', UBLExtension.name().localName(), UBLExtension)

ExtensionContent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionContent'), ExtensionContentType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 121, 2))
Namespace.addCategoryObject('elementBinding', ExtensionContent.name().localName(), ExtensionContent)

ExtensionAgencyID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyID'), ExtensionAgencyIDType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 118, 2))
Namespace.addCategoryObject('elementBinding', ExtensionAgencyID.name().localName(), ExtensionAgencyID)

ExtensionAgencyName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyName'), ExtensionAgencyNameType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 119, 2))
Namespace.addCategoryObject('elementBinding', ExtensionAgencyName.name().localName(), ExtensionAgencyName)

ExtensionAgencyURI = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyURI'), ExtensionAgencyURIType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 120, 2))
Namespace.addCategoryObject('elementBinding', ExtensionAgencyURI.name().localName(), ExtensionAgencyURI)

ExtensionReason = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionReason'), ExtensionReasonType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 122, 2))
Namespace.addCategoryObject('elementBinding', ExtensionReason.name().localName(), ExtensionReason)

ExtensionReasonCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionReasonCode'), ExtensionReasonCodeType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 123, 2))
Namespace.addCategoryObject('elementBinding', ExtensionReasonCode.name().localName(), ExtensionReasonCode)

ExtensionURI = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionURI'), ExtensionURIType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 124, 2))
Namespace.addCategoryObject('elementBinding', ExtensionURI.name().localName(), ExtensionURI)

ExtensionVersionID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionVersionID'), ExtensionVersionIDType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 125, 2))
Namespace.addCategoryObject('elementBinding', ExtensionVersionID.name().localName(), ExtensionVersionID)



UBLExtensionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UBLExtension'), UBLExtensionType, scope=UBLExtensionsType, documentation='\n        A single extension for private use.\n      ', location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 31, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UBLExtensionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UBLExtension')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 22, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UBLExtensionsType._Automaton = _BuildAutomaton()




UBLExtensionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ID'), _ImportedBinding__cbc.IDType, scope=UBLExtensionType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 327, 3)))

UBLExtensionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'Name'), _ImportedBinding__cbc.NameType, scope=UBLExtensionType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 459, 3)))

UBLExtensionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyID'), ExtensionAgencyIDType, scope=UBLExtensionType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 118, 2)))

UBLExtensionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyName'), ExtensionAgencyNameType, scope=UBLExtensionType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 119, 2)))

UBLExtensionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyURI'), ExtensionAgencyURIType, scope=UBLExtensionType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 120, 2)))

UBLExtensionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionContent'), ExtensionContentType, scope=UBLExtensionType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 121, 2)))

UBLExtensionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionReason'), ExtensionReasonType, scope=UBLExtensionType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 122, 2)))

UBLExtensionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionReasonCode'), ExtensionReasonCodeType, scope=UBLExtensionType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 123, 2)))

UBLExtensionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionURI'), ExtensionURIType, scope=UBLExtensionType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 124, 2)))

UBLExtensionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionVersionID'), ExtensionVersionIDType, scope=UBLExtensionType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 125, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 45, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 52, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 59, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 66, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 73, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 80, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 87, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 94, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 101, 6))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UBLExtensionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 45, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UBLExtensionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'Name')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 52, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UBLExtensionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 59, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UBLExtensionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyName')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 66, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UBLExtensionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtensionVersionID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 73, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UBLExtensionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtensionAgencyURI')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 80, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UBLExtensionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtensionURI')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 87, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UBLExtensionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtensionReasonCode')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 94, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UBLExtensionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtensionReason')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 101, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UBLExtensionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtensionContent')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonExtensionComponents-2.1.xsd', 108, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UBLExtensionType._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-ExtensionContentDataType-2.1.xsd', 9, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ExtensionContentType._Automaton = _BuildAutomaton_2()

