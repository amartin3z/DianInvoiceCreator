# ./_xades.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a9588716cb9fa3f5077fac32cb674acb7b7ef20a
# Generated 2020-05-26 15:40:38.330013 by PyXB version 1.2.6 using Python 3.7.5.final.0
# Namespace http://uri.etsi.org/01903/v1.3.2# [xmlns:xades]

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
import _ds as _ImportedBinding__ds

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://uri.etsi.org/01903/v1.3.2#', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ds = _ImportedBinding__ds.Namespace
_Namespace_ds.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://uri.etsi.org/01903/v1.3.2#}QualifierType
class QualifierType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QualifierType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 29, 1)
    _Documentation = None
QualifierType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=QualifierType, enum_prefix=None)
QualifierType.OIDAsURI = QualifierType._CF_enumeration.addEnumeration(unicode_value='OIDAsURI', tag='OIDAsURI')
QualifierType.OIDAsURN = QualifierType._CF_enumeration.addEnumeration(unicode_value='OIDAsURN', tag='OIDAsURN')
QualifierType._InitializeFacetMap(QualifierType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'QualifierType', QualifierType)
_module_typeBindings.QualifierType = QualifierType

# Complex type {http://uri.etsi.org/01903/v1.3.2#}AnyType with content type MIXED
class AnyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}AnyType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 6, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AnyType = AnyType
Namespace.addCategoryObject('typeBinding', 'AnyType', AnyType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}ObjectIdentifierType with content type ELEMENT_ONLY
class ObjectIdentifierType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}ObjectIdentifierType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObjectIdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 15, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__httpuri_etsi_org01903v1_3_2_ObjectIdentifierType_httpuri_etsi_org01903v1_3_2Identifier', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 17, 3), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Description'), 'Description', '__httpuri_etsi_org01903v1_3_2_ObjectIdentifierType_httpuri_etsi_org01903v1_3_2Description', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 18, 3), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}DocumentationReferences uses Python identifier DocumentationReferences
    __DocumentationReferences = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DocumentationReferences'), 'DocumentationReferences', '__httpuri_etsi_org01903v1_3_2_ObjectIdentifierType_httpuri_etsi_org01903v1_3_2DocumentationReferences', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 19, 3), )

    
    DocumentationReferences = property(__DocumentationReferences.value, __DocumentationReferences.set, None, None)

    _ElementMap.update({
        __Identifier.name() : __Identifier,
        __Description.name() : __Description,
        __DocumentationReferences.name() : __DocumentationReferences
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ObjectIdentifierType = ObjectIdentifierType
Namespace.addCategoryObject('typeBinding', 'ObjectIdentifierType', ObjectIdentifierType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}DocumentationReferencesType with content type ELEMENT_ONLY
class DocumentationReferencesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}DocumentationReferencesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentationReferencesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 35, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}DocumentationReference uses Python identifier DocumentationReference
    __DocumentationReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DocumentationReference'), 'DocumentationReference', '__httpuri_etsi_org01903v1_3_2_DocumentationReferencesType_httpuri_etsi_org01903v1_3_2DocumentationReference', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 37, 3), )

    
    DocumentationReference = property(__DocumentationReference.value, __DocumentationReference.set, None, None)

    _ElementMap.update({
        __DocumentationReference.name() : __DocumentationReference
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DocumentationReferencesType = DocumentationReferencesType
Namespace.addCategoryObject('typeBinding', 'DocumentationReferencesType', DocumentationReferencesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}EncapsulatedPKIDataType with content type SIMPLE
class EncapsulatedPKIDataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}EncapsulatedPKIDataType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedPKIDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 43, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.base64Binary
    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_EncapsulatedPKIDataType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 46, 4)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 46, 4)
    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Attribute Encoding uses Python identifier Encoding
    __Encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Encoding'), 'Encoding', '__httpuri_etsi_org01903v1_3_2_EncapsulatedPKIDataType_Encoding', pyxb.binding.datatypes.anyURI)
    __Encoding._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 47, 4)
    __Encoding._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 47, 4)
    
    Encoding = property(__Encoding.value, __Encoding.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id,
        __Encoding.name() : __Encoding
    })
_module_typeBindings.EncapsulatedPKIDataType = EncapsulatedPKIDataType
Namespace.addCategoryObject('typeBinding', 'EncapsulatedPKIDataType', EncapsulatedPKIDataType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}IncludeType with content type EMPTY
class IncludeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}IncludeType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IncludeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 55, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute URI uses Python identifier URI
    __URI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'URI'), 'URI', '__httpuri_etsi_org01903v1_3_2_IncludeType_URI', pyxb.binding.datatypes.anyURI, required=True)
    __URI._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 56, 2)
    __URI._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 56, 2)
    
    URI = property(__URI.value, __URI.set, None, None)

    
    # Attribute referencedData uses Python identifier referencedData
    __referencedData = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'referencedData'), 'referencedData', '__httpuri_etsi_org01903v1_3_2_IncludeType_referencedData', pyxb.binding.datatypes.boolean)
    __referencedData._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 57, 2)
    __referencedData._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 57, 2)
    
    referencedData = property(__referencedData.value, __referencedData.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __URI.name() : __URI,
        __referencedData.name() : __referencedData
    })
_module_typeBindings.IncludeType = IncludeType
Namespace.addCategoryObject('typeBinding', 'IncludeType', IncludeType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}ReferenceInfoType with content type ELEMENT_ONLY
class ReferenceInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}ReferenceInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 60, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}DigestMethod uses Python identifier DigestMethod
    __DigestMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestMethod'), 'DigestMethod', '__httpuri_etsi_org01903v1_3_2_ReferenceInfoType_httpwww_w3_org200009xmldsigDigestMethod', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 96, 0), )

    
    DigestMethod = property(__DigestMethod.value, __DigestMethod.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}DigestValue uses Python identifier DigestValue
    __DigestValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestValue'), 'DigestValue', '__httpuri_etsi_org01903v1_3_2_ReferenceInfoType_httpwww_w3_org200009xmldsigDigestValue', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 104, 0), )

    
    DigestValue = property(__DigestValue.value, __DigestValue.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_ReferenceInfoType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 65, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 65, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Attribute URI uses Python identifier URI
    __URI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'URI'), 'URI', '__httpuri_etsi_org01903v1_3_2_ReferenceInfoType_URI', pyxb.binding.datatypes.anyURI)
    __URI._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 66, 2)
    __URI._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 66, 2)
    
    URI = property(__URI.value, __URI.set, None, None)

    _ElementMap.update({
        __DigestMethod.name() : __DigestMethod,
        __DigestValue.name() : __DigestValue
    })
    _AttributeMap.update({
        __Id.name() : __Id,
        __URI.name() : __URI
    })
_module_typeBindings.ReferenceInfoType = ReferenceInfoType
Namespace.addCategoryObject('typeBinding', 'ReferenceInfoType', ReferenceInfoType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}GenericTimeStampType with content type ELEMENT_ONLY
class GenericTimeStampType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}GenericTimeStampType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericTimeStampType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 68, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}Include uses Python identifier Include
    __Include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Include'), 'Include', '__httpuri_etsi_org01903v1_3_2_GenericTimeStampType_httpuri_etsi_org01903v1_3_2Include', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 54, 1), )

    
    Include = property(__Include.value, __Include.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}ReferenceInfo uses Python identifier ReferenceInfo
    __ReferenceInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReferenceInfo'), 'ReferenceInfo', '__httpuri_etsi_org01903v1_3_2_GenericTimeStampType_httpuri_etsi_org01903v1_3_2ReferenceInfo', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 59, 1), )

    
    ReferenceInfo = property(__ReferenceInfo.value, __ReferenceInfo.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}EncapsulatedTimeStamp uses Python identifier EncapsulatedTimeStamp
    __EncapsulatedTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedTimeStamp'), 'EncapsulatedTimeStamp', '__httpuri_etsi_org01903v1_3_2_GenericTimeStampType_httpuri_etsi_org01903v1_3_2EncapsulatedTimeStamp', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 76, 4), )

    
    EncapsulatedTimeStamp = property(__EncapsulatedTimeStamp.value, __EncapsulatedTimeStamp.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}XMLTimeStamp uses Python identifier XMLTimeStamp
    __XMLTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'XMLTimeStamp'), 'XMLTimeStamp', '__httpuri_etsi_org01903v1_3_2_GenericTimeStampType_httpuri_etsi_org01903v1_3_2XMLTimeStamp', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 77, 4), )

    
    XMLTimeStamp = property(__XMLTimeStamp.value, __XMLTimeStamp.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}CanonicalizationMethod uses Python identifier CanonicalizationMethod
    __CanonicalizationMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'CanonicalizationMethod'), 'CanonicalizationMethod', '__httpuri_etsi_org01903v1_3_2_GenericTimeStampType_httpwww_w3_org200009xmldsigCanonicalizationMethod', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 44, 2), )

    
    CanonicalizationMethod = property(__CanonicalizationMethod.value, __CanonicalizationMethod.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_GenericTimeStampType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 80, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 80, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Include.name() : __Include,
        __ReferenceInfo.name() : __ReferenceInfo,
        __EncapsulatedTimeStamp.name() : __EncapsulatedTimeStamp,
        __XMLTimeStamp.name() : __XMLTimeStamp,
        __CanonicalizationMethod.name() : __CanonicalizationMethod
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.GenericTimeStampType = GenericTimeStampType
Namespace.addCategoryObject('typeBinding', 'GenericTimeStampType', GenericTimeStampType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}QualifyingPropertiesType with content type ELEMENT_ONLY
class QualifyingPropertiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}QualifyingPropertiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QualifyingPropertiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 124, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SignedProperties uses Python identifier SignedProperties
    __SignedProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignedProperties'), 'SignedProperties', '__httpuri_etsi_org01903v1_3_2_QualifyingPropertiesType_httpuri_etsi_org01903v1_3_2SignedProperties', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 126, 3), )

    
    SignedProperties = property(__SignedProperties.value, __SignedProperties.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}UnsignedProperties uses Python identifier UnsignedProperties
    __UnsignedProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UnsignedProperties'), 'UnsignedProperties', '__httpuri_etsi_org01903v1_3_2_QualifyingPropertiesType_httpuri_etsi_org01903v1_3_2UnsignedProperties', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 127, 3), )

    
    UnsignedProperties = property(__UnsignedProperties.value, __UnsignedProperties.set, None, None)

    
    # Attribute Target uses Python identifier Target
    __Target = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Target'), 'Target', '__httpuri_etsi_org01903v1_3_2_QualifyingPropertiesType_Target', pyxb.binding.datatypes.anyURI, required=True)
    __Target._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 129, 2)
    __Target._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 129, 2)
    
    Target = property(__Target.value, __Target.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_QualifyingPropertiesType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 130, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 130, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __SignedProperties.name() : __SignedProperties,
        __UnsignedProperties.name() : __UnsignedProperties
    })
    _AttributeMap.update({
        __Target.name() : __Target,
        __Id.name() : __Id
    })
_module_typeBindings.QualifyingPropertiesType = QualifyingPropertiesType
Namespace.addCategoryObject('typeBinding', 'QualifyingPropertiesType', QualifyingPropertiesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}SignedPropertiesType with content type ELEMENT_ONLY
class SignedPropertiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}SignedPropertiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignedPropertiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 135, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SignedSignatureProperties uses Python identifier SignedSignatureProperties
    __SignedSignatureProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignedSignatureProperties'), 'SignedSignatureProperties', '__httpuri_etsi_org01903v1_3_2_SignedPropertiesType_httpuri_etsi_org01903v1_3_2SignedSignatureProperties', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 137, 3), )

    
    SignedSignatureProperties = property(__SignedSignatureProperties.value, __SignedSignatureProperties.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SignedDataObjectProperties uses Python identifier SignedDataObjectProperties
    __SignedDataObjectProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignedDataObjectProperties'), 'SignedDataObjectProperties', '__httpuri_etsi_org01903v1_3_2_SignedPropertiesType_httpuri_etsi_org01903v1_3_2SignedDataObjectProperties', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 138, 3), )

    
    SignedDataObjectProperties = property(__SignedDataObjectProperties.value, __SignedDataObjectProperties.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_SignedPropertiesType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 140, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 140, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __SignedSignatureProperties.name() : __SignedSignatureProperties,
        __SignedDataObjectProperties.name() : __SignedDataObjectProperties
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.SignedPropertiesType = SignedPropertiesType
Namespace.addCategoryObject('typeBinding', 'SignedPropertiesType', SignedPropertiesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}UnsignedPropertiesType with content type ELEMENT_ONLY
class UnsignedPropertiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}UnsignedPropertiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnsignedPropertiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 145, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}UnsignedSignatureProperties uses Python identifier UnsignedSignatureProperties
    __UnsignedSignatureProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UnsignedSignatureProperties'), 'UnsignedSignatureProperties', '__httpuri_etsi_org01903v1_3_2_UnsignedPropertiesType_httpuri_etsi_org01903v1_3_2UnsignedSignatureProperties', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 147, 3), )

    
    UnsignedSignatureProperties = property(__UnsignedSignatureProperties.value, __UnsignedSignatureProperties.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}UnsignedDataObjectProperties uses Python identifier UnsignedDataObjectProperties
    __UnsignedDataObjectProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UnsignedDataObjectProperties'), 'UnsignedDataObjectProperties', '__httpuri_etsi_org01903v1_3_2_UnsignedPropertiesType_httpuri_etsi_org01903v1_3_2UnsignedDataObjectProperties', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 148, 3), )

    
    UnsignedDataObjectProperties = property(__UnsignedDataObjectProperties.value, __UnsignedDataObjectProperties.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_UnsignedPropertiesType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 150, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 150, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __UnsignedSignatureProperties.name() : __UnsignedSignatureProperties,
        __UnsignedDataObjectProperties.name() : __UnsignedDataObjectProperties
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.UnsignedPropertiesType = UnsignedPropertiesType
Namespace.addCategoryObject('typeBinding', 'UnsignedPropertiesType', UnsignedPropertiesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}SignedSignaturePropertiesType with content type ELEMENT_ONLY
class SignedSignaturePropertiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}SignedSignaturePropertiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignedSignaturePropertiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 155, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SigningTime uses Python identifier SigningTime
    __SigningTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SigningTime'), 'SigningTime', '__httpuri_etsi_org01903v1_3_2_SignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2SigningTime', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 157, 3), )

    
    SigningTime = property(__SigningTime.value, __SigningTime.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SigningCertificate uses Python identifier SigningCertificate
    __SigningCertificate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SigningCertificate'), 'SigningCertificate', '__httpuri_etsi_org01903v1_3_2_SignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2SigningCertificate', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 158, 3), )

    
    SigningCertificate = property(__SigningCertificate.value, __SigningCertificate.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SignaturePolicyIdentifier uses Python identifier SignaturePolicyIdentifier
    __SignaturePolicyIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyIdentifier'), 'SignaturePolicyIdentifier', '__httpuri_etsi_org01903v1_3_2_SignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2SignaturePolicyIdentifier', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 159, 3), )

    
    SignaturePolicyIdentifier = property(__SignaturePolicyIdentifier.value, __SignaturePolicyIdentifier.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SignatureProductionPlace uses Python identifier SignatureProductionPlace
    __SignatureProductionPlace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignatureProductionPlace'), 'SignatureProductionPlace', '__httpuri_etsi_org01903v1_3_2_SignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2SignatureProductionPlace', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 160, 3), )

    
    SignatureProductionPlace = property(__SignatureProductionPlace.value, __SignatureProductionPlace.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SignerRole uses Python identifier SignerRole
    __SignerRole = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignerRole'), 'SignerRole', '__httpuri_etsi_org01903v1_3_2_SignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2SignerRole', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 161, 3), )

    
    SignerRole = property(__SignerRole.value, __SignerRole.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_SignedSignaturePropertiesType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 163, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 163, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __SigningTime.name() : __SigningTime,
        __SigningCertificate.name() : __SigningCertificate,
        __SignaturePolicyIdentifier.name() : __SignaturePolicyIdentifier,
        __SignatureProductionPlace.name() : __SignatureProductionPlace,
        __SignerRole.name() : __SignerRole
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.SignedSignaturePropertiesType = SignedSignaturePropertiesType
Namespace.addCategoryObject('typeBinding', 'SignedSignaturePropertiesType', SignedSignaturePropertiesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}SignedDataObjectPropertiesType with content type ELEMENT_ONLY
class SignedDataObjectPropertiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}SignedDataObjectPropertiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignedDataObjectPropertiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 168, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}DataObjectFormat uses Python identifier DataObjectFormat
    __DataObjectFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataObjectFormat'), 'DataObjectFormat', '__httpuri_etsi_org01903v1_3_2_SignedDataObjectPropertiesType_httpuri_etsi_org01903v1_3_2DataObjectFormat', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 170, 3), )

    
    DataObjectFormat = property(__DataObjectFormat.value, __DataObjectFormat.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CommitmentTypeIndication uses Python identifier CommitmentTypeIndication
    __CommitmentTypeIndication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeIndication'), 'CommitmentTypeIndication', '__httpuri_etsi_org01903v1_3_2_SignedDataObjectPropertiesType_httpuri_etsi_org01903v1_3_2CommitmentTypeIndication', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 171, 3), )

    
    CommitmentTypeIndication = property(__CommitmentTypeIndication.value, __CommitmentTypeIndication.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}AllDataObjectsTimeStamp uses Python identifier AllDataObjectsTimeStamp
    __AllDataObjectsTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AllDataObjectsTimeStamp'), 'AllDataObjectsTimeStamp', '__httpuri_etsi_org01903v1_3_2_SignedDataObjectPropertiesType_httpuri_etsi_org01903v1_3_2AllDataObjectsTimeStamp', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 172, 3), )

    
    AllDataObjectsTimeStamp = property(__AllDataObjectsTimeStamp.value, __AllDataObjectsTimeStamp.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}IndividualDataObjectsTimeStamp uses Python identifier IndividualDataObjectsTimeStamp
    __IndividualDataObjectsTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IndividualDataObjectsTimeStamp'), 'IndividualDataObjectsTimeStamp', '__httpuri_etsi_org01903v1_3_2_SignedDataObjectPropertiesType_httpuri_etsi_org01903v1_3_2IndividualDataObjectsTimeStamp', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 173, 3), )

    
    IndividualDataObjectsTimeStamp = property(__IndividualDataObjectsTimeStamp.value, __IndividualDataObjectsTimeStamp.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_SignedDataObjectPropertiesType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 175, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 175, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __DataObjectFormat.name() : __DataObjectFormat,
        __CommitmentTypeIndication.name() : __CommitmentTypeIndication,
        __AllDataObjectsTimeStamp.name() : __AllDataObjectsTimeStamp,
        __IndividualDataObjectsTimeStamp.name() : __IndividualDataObjectsTimeStamp
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.SignedDataObjectPropertiesType = SignedDataObjectPropertiesType
Namespace.addCategoryObject('typeBinding', 'SignedDataObjectPropertiesType', SignedDataObjectPropertiesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}UnsignedSignaturePropertiesType with content type ELEMENT_ONLY
class UnsignedSignaturePropertiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}UnsignedSignaturePropertiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnsignedSignaturePropertiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 180, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CounterSignature uses Python identifier CounterSignature
    __CounterSignature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CounterSignature'), 'CounterSignature', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2CounterSignature', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 182, 3), )

    
    CounterSignature = property(__CounterSignature.value, __CounterSignature.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SignatureTimeStamp uses Python identifier SignatureTimeStamp
    __SignatureTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignatureTimeStamp'), 'SignatureTimeStamp', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2SignatureTimeStamp', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 183, 3), )

    
    SignatureTimeStamp = property(__SignatureTimeStamp.value, __SignatureTimeStamp.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CompleteCertificateRefs uses Python identifier CompleteCertificateRefs
    __CompleteCertificateRefs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompleteCertificateRefs'), 'CompleteCertificateRefs', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2CompleteCertificateRefs', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 184, 3), )

    
    CompleteCertificateRefs = property(__CompleteCertificateRefs.value, __CompleteCertificateRefs.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CompleteRevocationRefs uses Python identifier CompleteRevocationRefs
    __CompleteRevocationRefs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompleteRevocationRefs'), 'CompleteRevocationRefs', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2CompleteRevocationRefs', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 185, 3), )

    
    CompleteRevocationRefs = property(__CompleteRevocationRefs.value, __CompleteRevocationRefs.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}AttributeCertificateRefs uses Python identifier AttributeCertificateRefs
    __AttributeCertificateRefs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AttributeCertificateRefs'), 'AttributeCertificateRefs', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2AttributeCertificateRefs', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 186, 3), )

    
    AttributeCertificateRefs = property(__AttributeCertificateRefs.value, __AttributeCertificateRefs.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}AttributeRevocationRefs uses Python identifier AttributeRevocationRefs
    __AttributeRevocationRefs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AttributeRevocationRefs'), 'AttributeRevocationRefs', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2AttributeRevocationRefs', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 187, 3), )

    
    AttributeRevocationRefs = property(__AttributeRevocationRefs.value, __AttributeRevocationRefs.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SigAndRefsTimeStamp uses Python identifier SigAndRefsTimeStamp
    __SigAndRefsTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SigAndRefsTimeStamp'), 'SigAndRefsTimeStamp', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2SigAndRefsTimeStamp', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 188, 3), )

    
    SigAndRefsTimeStamp = property(__SigAndRefsTimeStamp.value, __SigAndRefsTimeStamp.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}RefsOnlyTimeStamp uses Python identifier RefsOnlyTimeStamp
    __RefsOnlyTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RefsOnlyTimeStamp'), 'RefsOnlyTimeStamp', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2RefsOnlyTimeStamp', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 189, 3), )

    
    RefsOnlyTimeStamp = property(__RefsOnlyTimeStamp.value, __RefsOnlyTimeStamp.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CertificateValues uses Python identifier CertificateValues
    __CertificateValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CertificateValues'), 'CertificateValues', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2CertificateValues', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 190, 3), )

    
    CertificateValues = property(__CertificateValues.value, __CertificateValues.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}RevocationValues uses Python identifier RevocationValues
    __RevocationValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RevocationValues'), 'RevocationValues', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2RevocationValues', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 191, 3), )

    
    RevocationValues = property(__RevocationValues.value, __RevocationValues.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}AttrAuthoritiesCertValues uses Python identifier AttrAuthoritiesCertValues
    __AttrAuthoritiesCertValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AttrAuthoritiesCertValues'), 'AttrAuthoritiesCertValues', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2AttrAuthoritiesCertValues', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 192, 3), )

    
    AttrAuthoritiesCertValues = property(__AttrAuthoritiesCertValues.value, __AttrAuthoritiesCertValues.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}AttributeRevocationValues uses Python identifier AttributeRevocationValues
    __AttributeRevocationValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AttributeRevocationValues'), 'AttributeRevocationValues', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2AttributeRevocationValues', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 193, 3), )

    
    AttributeRevocationValues = property(__AttributeRevocationValues.value, __AttributeRevocationValues.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}ArchiveTimeStamp uses Python identifier ArchiveTimeStamp
    __ArchiveTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ArchiveTimeStamp'), 'ArchiveTimeStamp', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_httpuri_etsi_org01903v1_3_2ArchiveTimeStamp', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 194, 3), )

    
    ArchiveTimeStamp = property(__ArchiveTimeStamp.value, __ArchiveTimeStamp.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_UnsignedSignaturePropertiesType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 197, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 197, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __CounterSignature.name() : __CounterSignature,
        __SignatureTimeStamp.name() : __SignatureTimeStamp,
        __CompleteCertificateRefs.name() : __CompleteCertificateRefs,
        __CompleteRevocationRefs.name() : __CompleteRevocationRefs,
        __AttributeCertificateRefs.name() : __AttributeCertificateRefs,
        __AttributeRevocationRefs.name() : __AttributeRevocationRefs,
        __SigAndRefsTimeStamp.name() : __SigAndRefsTimeStamp,
        __RefsOnlyTimeStamp.name() : __RefsOnlyTimeStamp,
        __CertificateValues.name() : __CertificateValues,
        __RevocationValues.name() : __RevocationValues,
        __AttrAuthoritiesCertValues.name() : __AttrAuthoritiesCertValues,
        __AttributeRevocationValues.name() : __AttributeRevocationValues,
        __ArchiveTimeStamp.name() : __ArchiveTimeStamp
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.UnsignedSignaturePropertiesType = UnsignedSignaturePropertiesType
Namespace.addCategoryObject('typeBinding', 'UnsignedSignaturePropertiesType', UnsignedSignaturePropertiesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}UnsignedDataObjectPropertiesType with content type ELEMENT_ONLY
class UnsignedDataObjectPropertiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}UnsignedDataObjectPropertiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnsignedDataObjectPropertiesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 202, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}UnsignedDataObjectProperty uses Python identifier UnsignedDataObjectProperty
    __UnsignedDataObjectProperty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UnsignedDataObjectProperty'), 'UnsignedDataObjectProperty', '__httpuri_etsi_org01903v1_3_2_UnsignedDataObjectPropertiesType_httpuri_etsi_org01903v1_3_2UnsignedDataObjectProperty', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 204, 3), )

    
    UnsignedDataObjectProperty = property(__UnsignedDataObjectProperty.value, __UnsignedDataObjectProperty.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_UnsignedDataObjectPropertiesType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 206, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 206, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __UnsignedDataObjectProperty.name() : __UnsignedDataObjectProperty
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.UnsignedDataObjectPropertiesType = UnsignedDataObjectPropertiesType
Namespace.addCategoryObject('typeBinding', 'UnsignedDataObjectPropertiesType', UnsignedDataObjectPropertiesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}QualifyingPropertiesReferenceType with content type EMPTY
class QualifyingPropertiesReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}QualifyingPropertiesReferenceType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QualifyingPropertiesReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 211, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute URI uses Python identifier URI
    __URI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'URI'), 'URI', '__httpuri_etsi_org01903v1_3_2_QualifyingPropertiesReferenceType_URI', pyxb.binding.datatypes.anyURI, required=True)
    __URI._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 212, 2)
    __URI._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 212, 2)
    
    URI = property(__URI.value, __URI.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_QualifyingPropertiesReferenceType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 213, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 213, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __URI.name() : __URI,
        __Id.name() : __Id
    })
_module_typeBindings.QualifyingPropertiesReferenceType = QualifyingPropertiesReferenceType
Namespace.addCategoryObject('typeBinding', 'QualifyingPropertiesReferenceType', QualifyingPropertiesReferenceType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CertIDListType with content type ELEMENT_ONLY
class CertIDListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CertIDListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CertIDListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 222, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}Cert uses Python identifier Cert
    __Cert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cert'), 'Cert', '__httpuri_etsi_org01903v1_3_2_CertIDListType_httpuri_etsi_org01903v1_3_2Cert', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 224, 3), )

    
    Cert = property(__Cert.value, __Cert.set, None, None)

    _ElementMap.update({
        __Cert.name() : __Cert
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CertIDListType = CertIDListType
Namespace.addCategoryObject('typeBinding', 'CertIDListType', CertIDListType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CertIDType with content type ELEMENT_ONLY
class CertIDType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CertIDType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CertIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 227, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CertDigest uses Python identifier CertDigest
    __CertDigest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CertDigest'), 'CertDigest', '__httpuri_etsi_org01903v1_3_2_CertIDType_httpuri_etsi_org01903v1_3_2CertDigest', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 229, 3), )

    
    CertDigest = property(__CertDigest.value, __CertDigest.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}IssuerSerial uses Python identifier IssuerSerial
    __IssuerSerial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IssuerSerial'), 'IssuerSerial', '__httpuri_etsi_org01903v1_3_2_CertIDType_httpuri_etsi_org01903v1_3_2IssuerSerial', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 230, 3), )

    
    IssuerSerial = property(__IssuerSerial.value, __IssuerSerial.set, None, None)

    
    # Attribute URI uses Python identifier URI
    __URI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'URI'), 'URI', '__httpuri_etsi_org01903v1_3_2_CertIDType_URI', pyxb.binding.datatypes.anyURI)
    __URI._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 232, 2)
    __URI._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 232, 2)
    
    URI = property(__URI.value, __URI.set, None, None)

    _ElementMap.update({
        __CertDigest.name() : __CertDigest,
        __IssuerSerial.name() : __IssuerSerial
    })
    _AttributeMap.update({
        __URI.name() : __URI
    })
_module_typeBindings.CertIDType = CertIDType
Namespace.addCategoryObject('typeBinding', 'CertIDType', CertIDType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}DigestAlgAndValueType with content type ELEMENT_ONLY
class DigestAlgAndValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}DigestAlgAndValueType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DigestAlgAndValueType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 234, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}DigestMethod uses Python identifier DigestMethod
    __DigestMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestMethod'), 'DigestMethod', '__httpuri_etsi_org01903v1_3_2_DigestAlgAndValueType_httpwww_w3_org200009xmldsigDigestMethod', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 96, 0), )

    
    DigestMethod = property(__DigestMethod.value, __DigestMethod.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}DigestValue uses Python identifier DigestValue
    __DigestValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestValue'), 'DigestValue', '__httpuri_etsi_org01903v1_3_2_DigestAlgAndValueType_httpwww_w3_org200009xmldsigDigestValue', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 104, 0), )

    
    DigestValue = property(__DigestValue.value, __DigestValue.set, None, None)

    _ElementMap.update({
        __DigestMethod.name() : __DigestMethod,
        __DigestValue.name() : __DigestValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DigestAlgAndValueType = DigestAlgAndValueType
Namespace.addCategoryObject('typeBinding', 'DigestAlgAndValueType', DigestAlgAndValueType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}SignaturePolicyIdentifierType with content type ELEMENT_ONLY
class SignaturePolicyIdentifierType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}SignaturePolicyIdentifierType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyIdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 243, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SignaturePolicyId uses Python identifier SignaturePolicyId
    __SignaturePolicyId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyId'), 'SignaturePolicyId', '__httpuri_etsi_org01903v1_3_2_SignaturePolicyIdentifierType_httpuri_etsi_org01903v1_3_2SignaturePolicyId', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 245, 3), )

    
    SignaturePolicyId = property(__SignaturePolicyId.value, __SignaturePolicyId.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SignaturePolicyImplied uses Python identifier SignaturePolicyImplied
    __SignaturePolicyImplied = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyImplied'), 'SignaturePolicyImplied', '__httpuri_etsi_org01903v1_3_2_SignaturePolicyIdentifierType_httpuri_etsi_org01903v1_3_2SignaturePolicyImplied', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 246, 3), )

    
    SignaturePolicyImplied = property(__SignaturePolicyImplied.value, __SignaturePolicyImplied.set, None, None)

    _ElementMap.update({
        __SignaturePolicyId.name() : __SignaturePolicyId,
        __SignaturePolicyImplied.name() : __SignaturePolicyImplied
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SignaturePolicyIdentifierType = SignaturePolicyIdentifierType
Namespace.addCategoryObject('typeBinding', 'SignaturePolicyIdentifierType', SignaturePolicyIdentifierType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}SignaturePolicyIdType with content type ELEMENT_ONLY
class SignaturePolicyIdType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}SignaturePolicyIdType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyIdType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 249, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SigPolicyId uses Python identifier SigPolicyId
    __SigPolicyId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyId'), 'SigPolicyId', '__httpuri_etsi_org01903v1_3_2_SignaturePolicyIdType_httpuri_etsi_org01903v1_3_2SigPolicyId', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 251, 3), )

    
    SigPolicyId = property(__SigPolicyId.value, __SigPolicyId.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SigPolicyHash uses Python identifier SigPolicyHash
    __SigPolicyHash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyHash'), 'SigPolicyHash', '__httpuri_etsi_org01903v1_3_2_SignaturePolicyIdType_httpuri_etsi_org01903v1_3_2SigPolicyHash', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 253, 3), )

    
    SigPolicyHash = property(__SigPolicyHash.value, __SigPolicyHash.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SigPolicyQualifiers uses Python identifier SigPolicyQualifiers
    __SigPolicyQualifiers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyQualifiers'), 'SigPolicyQualifiers', '__httpuri_etsi_org01903v1_3_2_SignaturePolicyIdType_httpuri_etsi_org01903v1_3_2SigPolicyQualifiers', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 254, 3), )

    
    SigPolicyQualifiers = property(__SigPolicyQualifiers.value, __SigPolicyQualifiers.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Transforms uses Python identifier Transforms
    __Transforms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Transforms'), 'Transforms', '__httpuri_etsi_org01903v1_3_2_SignaturePolicyIdType_httpwww_w3_org200009xmldsigTransforms', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 77, 2), )

    
    Transforms = property(__Transforms.value, __Transforms.set, None, None)

    _ElementMap.update({
        __SigPolicyId.name() : __SigPolicyId,
        __SigPolicyHash.name() : __SigPolicyHash,
        __SigPolicyQualifiers.name() : __SigPolicyQualifiers,
        __Transforms.name() : __Transforms
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SignaturePolicyIdType = SignaturePolicyIdType
Namespace.addCategoryObject('typeBinding', 'SignaturePolicyIdType', SignaturePolicyIdType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}SigPolicyQualifiersListType with content type ELEMENT_ONLY
class SigPolicyQualifiersListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}SigPolicyQualifiersListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SigPolicyQualifiersListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 257, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}SigPolicyQualifier uses Python identifier SigPolicyQualifier
    __SigPolicyQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyQualifier'), 'SigPolicyQualifier', '__httpuri_etsi_org01903v1_3_2_SigPolicyQualifiersListType_httpuri_etsi_org01903v1_3_2SigPolicyQualifier', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 259, 3), )

    
    SigPolicyQualifier = property(__SigPolicyQualifier.value, __SigPolicyQualifier.set, None, None)

    _ElementMap.update({
        __SigPolicyQualifier.name() : __SigPolicyQualifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SigPolicyQualifiersListType = SigPolicyQualifiersListType
Namespace.addCategoryObject('typeBinding', 'SigPolicyQualifiersListType', SigPolicyQualifiersListType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}SPUserNoticeType with content type ELEMENT_ONLY
class SPUserNoticeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}SPUserNoticeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SPUserNoticeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 264, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}NoticeRef uses Python identifier NoticeRef
    __NoticeRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NoticeRef'), 'NoticeRef', '__httpuri_etsi_org01903v1_3_2_SPUserNoticeType_httpuri_etsi_org01903v1_3_2NoticeRef', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 266, 3), )

    
    NoticeRef = property(__NoticeRef.value, __NoticeRef.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}ExplicitText uses Python identifier ExplicitText
    __ExplicitText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExplicitText'), 'ExplicitText', '__httpuri_etsi_org01903v1_3_2_SPUserNoticeType_httpuri_etsi_org01903v1_3_2ExplicitText', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 267, 3), )

    
    ExplicitText = property(__ExplicitText.value, __ExplicitText.set, None, None)

    _ElementMap.update({
        __NoticeRef.name() : __NoticeRef,
        __ExplicitText.name() : __ExplicitText
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SPUserNoticeType = SPUserNoticeType
Namespace.addCategoryObject('typeBinding', 'SPUserNoticeType', SPUserNoticeType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}NoticeReferenceType with content type ELEMENT_ONLY
class NoticeReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}NoticeReferenceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NoticeReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 270, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}Organization uses Python identifier Organization
    __Organization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organization'), 'Organization', '__httpuri_etsi_org01903v1_3_2_NoticeReferenceType_httpuri_etsi_org01903v1_3_2Organization', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 272, 3), )

    
    Organization = property(__Organization.value, __Organization.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}NoticeNumbers uses Python identifier NoticeNumbers
    __NoticeNumbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NoticeNumbers'), 'NoticeNumbers', '__httpuri_etsi_org01903v1_3_2_NoticeReferenceType_httpuri_etsi_org01903v1_3_2NoticeNumbers', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 273, 3), )

    
    NoticeNumbers = property(__NoticeNumbers.value, __NoticeNumbers.set, None, None)

    _ElementMap.update({
        __Organization.name() : __Organization,
        __NoticeNumbers.name() : __NoticeNumbers
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NoticeReferenceType = NoticeReferenceType
Namespace.addCategoryObject('typeBinding', 'NoticeReferenceType', NoticeReferenceType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}IntegerListType with content type ELEMENT_ONLY
class IntegerListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}IntegerListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IntegerListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 276, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}int uses Python identifier int
    __int = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'int'), 'int', '__httpuri_etsi_org01903v1_3_2_IntegerListType_httpuri_etsi_org01903v1_3_2int', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 278, 3), )

    
    int = property(__int.value, __int.set, None, None)

    _ElementMap.update({
        __int.name() : __int
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IntegerListType = IntegerListType
Namespace.addCategoryObject('typeBinding', 'IntegerListType', IntegerListType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CounterSignatureType with content type ELEMENT_ONLY
class CounterSignatureType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CounterSignatureType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CounterSignatureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 284, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__httpuri_etsi_org01903v1_3_2_CounterSignatureType_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 12, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CounterSignatureType = CounterSignatureType
Namespace.addCategoryObject('typeBinding', 'CounterSignatureType', CounterSignatureType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}DataObjectFormatType with content type ELEMENT_ONLY
class DataObjectFormatType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}DataObjectFormatType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataObjectFormatType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 292, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Description'), 'Description', '__httpuri_etsi_org01903v1_3_2_DataObjectFormatType_httpuri_etsi_org01903v1_3_2Description', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 294, 3), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}ObjectIdentifier uses Python identifier ObjectIdentifier
    __ObjectIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObjectIdentifier'), 'ObjectIdentifier', '__httpuri_etsi_org01903v1_3_2_DataObjectFormatType_httpuri_etsi_org01903v1_3_2ObjectIdentifier', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 295, 3), )

    
    ObjectIdentifier = property(__ObjectIdentifier.value, __ObjectIdentifier.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}MimeType uses Python identifier MimeType
    __MimeType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MimeType'), 'MimeType', '__httpuri_etsi_org01903v1_3_2_DataObjectFormatType_httpuri_etsi_org01903v1_3_2MimeType', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 296, 3), )

    
    MimeType = property(__MimeType.value, __MimeType.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}Encoding uses Python identifier Encoding
    __Encoding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Encoding'), 'Encoding', '__httpuri_etsi_org01903v1_3_2_DataObjectFormatType_httpuri_etsi_org01903v1_3_2Encoding', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 297, 3), )

    
    Encoding = property(__Encoding.value, __Encoding.set, None, None)

    
    # Attribute ObjectReference uses Python identifier ObjectReference
    __ObjectReference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ObjectReference'), 'ObjectReference', '__httpuri_etsi_org01903v1_3_2_DataObjectFormatType_ObjectReference', pyxb.binding.datatypes.anyURI, required=True)
    __ObjectReference._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 299, 2)
    __ObjectReference._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 299, 2)
    
    ObjectReference = property(__ObjectReference.value, __ObjectReference.set, None, None)

    _ElementMap.update({
        __Description.name() : __Description,
        __ObjectIdentifier.name() : __ObjectIdentifier,
        __MimeType.name() : __MimeType,
        __Encoding.name() : __Encoding
    })
    _AttributeMap.update({
        __ObjectReference.name() : __ObjectReference
    })
_module_typeBindings.DataObjectFormatType = DataObjectFormatType
Namespace.addCategoryObject('typeBinding', 'DataObjectFormatType', DataObjectFormatType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CommitmentTypeIndicationType with content type ELEMENT_ONLY
class CommitmentTypeIndicationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CommitmentTypeIndicationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeIndicationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 304, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CommitmentTypeId uses Python identifier CommitmentTypeId
    __CommitmentTypeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeId'), 'CommitmentTypeId', '__httpuri_etsi_org01903v1_3_2_CommitmentTypeIndicationType_httpuri_etsi_org01903v1_3_2CommitmentTypeId', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 306, 3), )

    
    CommitmentTypeId = property(__CommitmentTypeId.value, __CommitmentTypeId.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}ObjectReference uses Python identifier ObjectReference
    __ObjectReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ObjectReference'), 'ObjectReference', '__httpuri_etsi_org01903v1_3_2_CommitmentTypeIndicationType_httpuri_etsi_org01903v1_3_2ObjectReference', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 308, 4), )

    
    ObjectReference = property(__ObjectReference.value, __ObjectReference.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}AllSignedDataObjects uses Python identifier AllSignedDataObjects
    __AllSignedDataObjects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AllSignedDataObjects'), 'AllSignedDataObjects', '__httpuri_etsi_org01903v1_3_2_CommitmentTypeIndicationType_httpuri_etsi_org01903v1_3_2AllSignedDataObjects', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 309, 4), )

    
    AllSignedDataObjects = property(__AllSignedDataObjects.value, __AllSignedDataObjects.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CommitmentTypeQualifiers uses Python identifier CommitmentTypeQualifiers
    __CommitmentTypeQualifiers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeQualifiers'), 'CommitmentTypeQualifiers', '__httpuri_etsi_org01903v1_3_2_CommitmentTypeIndicationType_httpuri_etsi_org01903v1_3_2CommitmentTypeQualifiers', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 311, 3), )

    
    CommitmentTypeQualifiers = property(__CommitmentTypeQualifiers.value, __CommitmentTypeQualifiers.set, None, None)

    _ElementMap.update({
        __CommitmentTypeId.name() : __CommitmentTypeId,
        __ObjectReference.name() : __ObjectReference,
        __AllSignedDataObjects.name() : __AllSignedDataObjects,
        __CommitmentTypeQualifiers.name() : __CommitmentTypeQualifiers
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CommitmentTypeIndicationType = CommitmentTypeIndicationType
Namespace.addCategoryObject('typeBinding', 'CommitmentTypeIndicationType', CommitmentTypeIndicationType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CommitmentTypeQualifiersListType with content type ELEMENT_ONLY
class CommitmentTypeQualifiersListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CommitmentTypeQualifiersListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeQualifiersListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 314, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CommitmentTypeQualifier uses Python identifier CommitmentTypeQualifier
    __CommitmentTypeQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeQualifier'), 'CommitmentTypeQualifier', '__httpuri_etsi_org01903v1_3_2_CommitmentTypeQualifiersListType_httpuri_etsi_org01903v1_3_2CommitmentTypeQualifier', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 316, 3), )

    
    CommitmentTypeQualifier = property(__CommitmentTypeQualifier.value, __CommitmentTypeQualifier.set, None, None)

    _ElementMap.update({
        __CommitmentTypeQualifier.name() : __CommitmentTypeQualifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CommitmentTypeQualifiersListType = CommitmentTypeQualifiersListType
Namespace.addCategoryObject('typeBinding', 'CommitmentTypeQualifiersListType', CommitmentTypeQualifiersListType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}SignatureProductionPlaceType with content type ELEMENT_ONLY
class SignatureProductionPlaceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}SignatureProductionPlaceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignatureProductionPlaceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 322, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}City uses Python identifier City
    __City = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'City'), 'City', '__httpuri_etsi_org01903v1_3_2_SignatureProductionPlaceType_httpuri_etsi_org01903v1_3_2City', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 324, 3), )

    
    City = property(__City.value, __City.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}StateOrProvince uses Python identifier StateOrProvince
    __StateOrProvince = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StateOrProvince'), 'StateOrProvince', '__httpuri_etsi_org01903v1_3_2_SignatureProductionPlaceType_httpuri_etsi_org01903v1_3_2StateOrProvince', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 325, 3), )

    
    StateOrProvince = property(__StateOrProvince.value, __StateOrProvince.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__httpuri_etsi_org01903v1_3_2_SignatureProductionPlaceType_httpuri_etsi_org01903v1_3_2PostalCode', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 326, 3), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CountryName uses Python identifier CountryName
    __CountryName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CountryName'), 'CountryName', '__httpuri_etsi_org01903v1_3_2_SignatureProductionPlaceType_httpuri_etsi_org01903v1_3_2CountryName', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 327, 3), )

    
    CountryName = property(__CountryName.value, __CountryName.set, None, None)

    _ElementMap.update({
        __City.name() : __City,
        __StateOrProvince.name() : __StateOrProvince,
        __PostalCode.name() : __PostalCode,
        __CountryName.name() : __CountryName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SignatureProductionPlaceType = SignatureProductionPlaceType
Namespace.addCategoryObject('typeBinding', 'SignatureProductionPlaceType', SignatureProductionPlaceType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}SignerRoleType with content type ELEMENT_ONLY
class SignerRoleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}SignerRoleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignerRoleType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 333, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}ClaimedRoles uses Python identifier ClaimedRoles
    __ClaimedRoles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClaimedRoles'), 'ClaimedRoles', '__httpuri_etsi_org01903v1_3_2_SignerRoleType_httpuri_etsi_org01903v1_3_2ClaimedRoles', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 335, 3), )

    
    ClaimedRoles = property(__ClaimedRoles.value, __ClaimedRoles.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CertifiedRoles uses Python identifier CertifiedRoles
    __CertifiedRoles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CertifiedRoles'), 'CertifiedRoles', '__httpuri_etsi_org01903v1_3_2_SignerRoleType_httpuri_etsi_org01903v1_3_2CertifiedRoles', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 336, 3), )

    
    CertifiedRoles = property(__CertifiedRoles.value, __CertifiedRoles.set, None, None)

    _ElementMap.update({
        __ClaimedRoles.name() : __ClaimedRoles,
        __CertifiedRoles.name() : __CertifiedRoles
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SignerRoleType = SignerRoleType
Namespace.addCategoryObject('typeBinding', 'SignerRoleType', SignerRoleType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}ClaimedRolesListType with content type ELEMENT_ONLY
class ClaimedRolesListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}ClaimedRolesListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClaimedRolesListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 339, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}ClaimedRole uses Python identifier ClaimedRole
    __ClaimedRole = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClaimedRole'), 'ClaimedRole', '__httpuri_etsi_org01903v1_3_2_ClaimedRolesListType_httpuri_etsi_org01903v1_3_2ClaimedRole', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 341, 3), )

    
    ClaimedRole = property(__ClaimedRole.value, __ClaimedRole.set, None, None)

    _ElementMap.update({
        __ClaimedRole.name() : __ClaimedRole
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ClaimedRolesListType = ClaimedRolesListType
Namespace.addCategoryObject('typeBinding', 'ClaimedRolesListType', ClaimedRolesListType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CertifiedRolesListType with content type ELEMENT_ONLY
class CertifiedRolesListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CertifiedRolesListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CertifiedRolesListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 344, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CertifiedRole uses Python identifier CertifiedRole
    __CertifiedRole = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CertifiedRole'), 'CertifiedRole', '__httpuri_etsi_org01903v1_3_2_CertifiedRolesListType_httpuri_etsi_org01903v1_3_2CertifiedRole', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 346, 3), )

    
    CertifiedRole = property(__CertifiedRole.value, __CertifiedRole.set, None, None)

    _ElementMap.update({
        __CertifiedRole.name() : __CertifiedRole
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CertifiedRolesListType = CertifiedRolesListType
Namespace.addCategoryObject('typeBinding', 'CertifiedRolesListType', CertifiedRolesListType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CompleteCertificateRefsType with content type ELEMENT_ONLY
class CompleteCertificateRefsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CompleteCertificateRefsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompleteCertificateRefsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 355, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CertRefs uses Python identifier CertRefs
    __CertRefs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CertRefs'), 'CertRefs', '__httpuri_etsi_org01903v1_3_2_CompleteCertificateRefsType_httpuri_etsi_org01903v1_3_2CertRefs', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 357, 3), )

    
    CertRefs = property(__CertRefs.value, __CertRefs.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_CompleteCertificateRefsType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 359, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 359, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __CertRefs.name() : __CertRefs
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.CompleteCertificateRefsType = CompleteCertificateRefsType
Namespace.addCategoryObject('typeBinding', 'CompleteCertificateRefsType', CompleteCertificateRefsType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CompleteRevocationRefsType with content type ELEMENT_ONLY
class CompleteRevocationRefsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CompleteRevocationRefsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompleteRevocationRefsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 364, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CRLRefs uses Python identifier CRLRefs
    __CRLRefs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CRLRefs'), 'CRLRefs', '__httpuri_etsi_org01903v1_3_2_CompleteRevocationRefsType_httpuri_etsi_org01903v1_3_2CRLRefs', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 366, 3), )

    
    CRLRefs = property(__CRLRefs.value, __CRLRefs.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}OCSPRefs uses Python identifier OCSPRefs
    __OCSPRefs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OCSPRefs'), 'OCSPRefs', '__httpuri_etsi_org01903v1_3_2_CompleteRevocationRefsType_httpuri_etsi_org01903v1_3_2OCSPRefs', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 367, 3), )

    
    OCSPRefs = property(__OCSPRefs.value, __OCSPRefs.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}OtherRefs uses Python identifier OtherRefs
    __OtherRefs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OtherRefs'), 'OtherRefs', '__httpuri_etsi_org01903v1_3_2_CompleteRevocationRefsType_httpuri_etsi_org01903v1_3_2OtherRefs', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 368, 3), )

    
    OtherRefs = property(__OtherRefs.value, __OtherRefs.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_CompleteRevocationRefsType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 370, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 370, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __CRLRefs.name() : __CRLRefs,
        __OCSPRefs.name() : __OCSPRefs,
        __OtherRefs.name() : __OtherRefs
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.CompleteRevocationRefsType = CompleteRevocationRefsType
Namespace.addCategoryObject('typeBinding', 'CompleteRevocationRefsType', CompleteRevocationRefsType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CRLRefsType with content type ELEMENT_ONLY
class CRLRefsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CRLRefsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CRLRefsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 372, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CRLRef uses Python identifier CRLRef
    __CRLRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CRLRef'), 'CRLRef', '__httpuri_etsi_org01903v1_3_2_CRLRefsType_httpuri_etsi_org01903v1_3_2CRLRef', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 374, 3), )

    
    CRLRef = property(__CRLRef.value, __CRLRef.set, None, None)

    _ElementMap.update({
        __CRLRef.name() : __CRLRef
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CRLRefsType = CRLRefsType
Namespace.addCategoryObject('typeBinding', 'CRLRefsType', CRLRefsType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CRLRefType with content type ELEMENT_ONLY
class CRLRefType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CRLRefType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CRLRefType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 377, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}DigestAlgAndValue uses Python identifier DigestAlgAndValue
    __DigestAlgAndValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DigestAlgAndValue'), 'DigestAlgAndValue', '__httpuri_etsi_org01903v1_3_2_CRLRefType_httpuri_etsi_org01903v1_3_2DigestAlgAndValue', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 379, 3), )

    
    DigestAlgAndValue = property(__DigestAlgAndValue.value, __DigestAlgAndValue.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CRLIdentifier uses Python identifier CRLIdentifier
    __CRLIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CRLIdentifier'), 'CRLIdentifier', '__httpuri_etsi_org01903v1_3_2_CRLRefType_httpuri_etsi_org01903v1_3_2CRLIdentifier', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 380, 3), )

    
    CRLIdentifier = property(__CRLIdentifier.value, __CRLIdentifier.set, None, None)

    _ElementMap.update({
        __DigestAlgAndValue.name() : __DigestAlgAndValue,
        __CRLIdentifier.name() : __CRLIdentifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CRLRefType = CRLRefType
Namespace.addCategoryObject('typeBinding', 'CRLRefType', CRLRefType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CRLIdentifierType with content type ELEMENT_ONLY
class CRLIdentifierType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CRLIdentifierType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CRLIdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 383, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}Issuer uses Python identifier Issuer
    __Issuer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issuer'), 'Issuer', '__httpuri_etsi_org01903v1_3_2_CRLIdentifierType_httpuri_etsi_org01903v1_3_2Issuer', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 385, 3), )

    
    Issuer = property(__Issuer.value, __Issuer.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}IssueTime uses Python identifier IssueTime
    __IssueTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IssueTime'), 'IssueTime', '__httpuri_etsi_org01903v1_3_2_CRLIdentifierType_httpuri_etsi_org01903v1_3_2IssueTime', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 386, 3), )

    
    IssueTime = property(__IssueTime.value, __IssueTime.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}Number uses Python identifier Number
    __Number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Number'), 'Number', '__httpuri_etsi_org01903v1_3_2_CRLIdentifierType_httpuri_etsi_org01903v1_3_2Number', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 387, 3), )

    
    Number = property(__Number.value, __Number.set, None, None)

    
    # Attribute URI uses Python identifier URI
    __URI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'URI'), 'URI', '__httpuri_etsi_org01903v1_3_2_CRLIdentifierType_URI', pyxb.binding.datatypes.anyURI)
    __URI._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 389, 2)
    __URI._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 389, 2)
    
    URI = property(__URI.value, __URI.set, None, None)

    _ElementMap.update({
        __Issuer.name() : __Issuer,
        __IssueTime.name() : __IssueTime,
        __Number.name() : __Number
    })
    _AttributeMap.update({
        __URI.name() : __URI
    })
_module_typeBindings.CRLIdentifierType = CRLIdentifierType
Namespace.addCategoryObject('typeBinding', 'CRLIdentifierType', CRLIdentifierType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}OCSPRefsType with content type ELEMENT_ONLY
class OCSPRefsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}OCSPRefsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OCSPRefsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 391, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}OCSPRef uses Python identifier OCSPRef
    __OCSPRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OCSPRef'), 'OCSPRef', '__httpuri_etsi_org01903v1_3_2_OCSPRefsType_httpuri_etsi_org01903v1_3_2OCSPRef', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 393, 3), )

    
    OCSPRef = property(__OCSPRef.value, __OCSPRef.set, None, None)

    _ElementMap.update({
        __OCSPRef.name() : __OCSPRef
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OCSPRefsType = OCSPRefsType
Namespace.addCategoryObject('typeBinding', 'OCSPRefsType', OCSPRefsType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}OCSPRefType with content type ELEMENT_ONLY
class OCSPRefType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}OCSPRefType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OCSPRefType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 396, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}OCSPIdentifier uses Python identifier OCSPIdentifier
    __OCSPIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OCSPIdentifier'), 'OCSPIdentifier', '__httpuri_etsi_org01903v1_3_2_OCSPRefType_httpuri_etsi_org01903v1_3_2OCSPIdentifier', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 398, 3), )

    
    OCSPIdentifier = property(__OCSPIdentifier.value, __OCSPIdentifier.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}DigestAlgAndValue uses Python identifier DigestAlgAndValue
    __DigestAlgAndValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DigestAlgAndValue'), 'DigestAlgAndValue', '__httpuri_etsi_org01903v1_3_2_OCSPRefType_httpuri_etsi_org01903v1_3_2DigestAlgAndValue', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 399, 3), )

    
    DigestAlgAndValue = property(__DigestAlgAndValue.value, __DigestAlgAndValue.set, None, None)

    _ElementMap.update({
        __OCSPIdentifier.name() : __OCSPIdentifier,
        __DigestAlgAndValue.name() : __DigestAlgAndValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OCSPRefType = OCSPRefType
Namespace.addCategoryObject('typeBinding', 'OCSPRefType', OCSPRefType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}ResponderIDType with content type ELEMENT_ONLY
class ResponderIDType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}ResponderIDType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponderIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 402, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}ByName uses Python identifier ByName
    __ByName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ByName'), 'ByName', '__httpuri_etsi_org01903v1_3_2_ResponderIDType_httpuri_etsi_org01903v1_3_2ByName', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 404, 3), )

    
    ByName = property(__ByName.value, __ByName.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}ByKey uses Python identifier ByKey
    __ByKey = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ByKey'), 'ByKey', '__httpuri_etsi_org01903v1_3_2_ResponderIDType_httpuri_etsi_org01903v1_3_2ByKey', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 405, 3), )

    
    ByKey = property(__ByKey.value, __ByKey.set, None, None)

    _ElementMap.update({
        __ByName.name() : __ByName,
        __ByKey.name() : __ByKey
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ResponderIDType = ResponderIDType
Namespace.addCategoryObject('typeBinding', 'ResponderIDType', ResponderIDType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}OCSPIdentifierType with content type ELEMENT_ONLY
class OCSPIdentifierType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}OCSPIdentifierType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OCSPIdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 408, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}ResponderID uses Python identifier ResponderID
    __ResponderID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponderID'), 'ResponderID', '__httpuri_etsi_org01903v1_3_2_OCSPIdentifierType_httpuri_etsi_org01903v1_3_2ResponderID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 410, 3), )

    
    ResponderID = property(__ResponderID.value, __ResponderID.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}ProducedAt uses Python identifier ProducedAt
    __ProducedAt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProducedAt'), 'ProducedAt', '__httpuri_etsi_org01903v1_3_2_OCSPIdentifierType_httpuri_etsi_org01903v1_3_2ProducedAt', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 411, 3), )

    
    ProducedAt = property(__ProducedAt.value, __ProducedAt.set, None, None)

    
    # Attribute URI uses Python identifier URI
    __URI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'URI'), 'URI', '__httpuri_etsi_org01903v1_3_2_OCSPIdentifierType_URI', pyxb.binding.datatypes.anyURI)
    __URI._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 413, 2)
    __URI._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 413, 2)
    
    URI = property(__URI.value, __URI.set, None, None)

    _ElementMap.update({
        __ResponderID.name() : __ResponderID,
        __ProducedAt.name() : __ProducedAt
    })
    _AttributeMap.update({
        __URI.name() : __URI
    })
_module_typeBindings.OCSPIdentifierType = OCSPIdentifierType
Namespace.addCategoryObject('typeBinding', 'OCSPIdentifierType', OCSPIdentifierType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}OtherCertStatusRefsType with content type ELEMENT_ONLY
class OtherCertStatusRefsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}OtherCertStatusRefsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OtherCertStatusRefsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 415, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}OtherRef uses Python identifier OtherRef
    __OtherRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OtherRef'), 'OtherRef', '__httpuri_etsi_org01903v1_3_2_OtherCertStatusRefsType_httpuri_etsi_org01903v1_3_2OtherRef', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 417, 3), )

    
    OtherRef = property(__OtherRef.value, __OtherRef.set, None, None)

    _ElementMap.update({
        __OtherRef.name() : __OtherRef
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OtherCertStatusRefsType = OtherCertStatusRefsType
Namespace.addCategoryObject('typeBinding', 'OtherCertStatusRefsType', OtherCertStatusRefsType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CertificateValuesType with content type ELEMENT_ONLY
class CertificateValuesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CertificateValuesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CertificateValuesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 427, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}EncapsulatedX509Certificate uses Python identifier EncapsulatedX509Certificate
    __EncapsulatedX509Certificate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedX509Certificate'), 'EncapsulatedX509Certificate', '__httpuri_etsi_org01903v1_3_2_CertificateValuesType_httpuri_etsi_org01903v1_3_2EncapsulatedX509Certificate', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 429, 3), )

    
    EncapsulatedX509Certificate = property(__EncapsulatedX509Certificate.value, __EncapsulatedX509Certificate.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}OtherCertificate uses Python identifier OtherCertificate
    __OtherCertificate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OtherCertificate'), 'OtherCertificate', '__httpuri_etsi_org01903v1_3_2_CertificateValuesType_httpuri_etsi_org01903v1_3_2OtherCertificate', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 430, 3), )

    
    OtherCertificate = property(__OtherCertificate.value, __OtherCertificate.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_CertificateValuesType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 432, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 432, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __EncapsulatedX509Certificate.name() : __EncapsulatedX509Certificate,
        __OtherCertificate.name() : __OtherCertificate
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.CertificateValuesType = CertificateValuesType
Namespace.addCategoryObject('typeBinding', 'CertificateValuesType', CertificateValuesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}RevocationValuesType with content type ELEMENT_ONLY
class RevocationValuesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}RevocationValuesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RevocationValuesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 437, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CRLValues uses Python identifier CRLValues
    __CRLValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CRLValues'), 'CRLValues', '__httpuri_etsi_org01903v1_3_2_RevocationValuesType_httpuri_etsi_org01903v1_3_2CRLValues', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 439, 3), )

    
    CRLValues = property(__CRLValues.value, __CRLValues.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}OCSPValues uses Python identifier OCSPValues
    __OCSPValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OCSPValues'), 'OCSPValues', '__httpuri_etsi_org01903v1_3_2_RevocationValuesType_httpuri_etsi_org01903v1_3_2OCSPValues', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 440, 3), )

    
    OCSPValues = property(__OCSPValues.value, __OCSPValues.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}OtherValues uses Python identifier OtherValues
    __OtherValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OtherValues'), 'OtherValues', '__httpuri_etsi_org01903v1_3_2_RevocationValuesType_httpuri_etsi_org01903v1_3_2OtherValues', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 441, 3), )

    
    OtherValues = property(__OtherValues.value, __OtherValues.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_RevocationValuesType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 443, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 443, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __CRLValues.name() : __CRLValues,
        __OCSPValues.name() : __OCSPValues,
        __OtherValues.name() : __OtherValues
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.RevocationValuesType = RevocationValuesType
Namespace.addCategoryObject('typeBinding', 'RevocationValuesType', RevocationValuesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}CRLValuesType with content type ELEMENT_ONLY
class CRLValuesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}CRLValuesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CRLValuesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 445, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}EncapsulatedCRLValue uses Python identifier EncapsulatedCRLValue
    __EncapsulatedCRLValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedCRLValue'), 'EncapsulatedCRLValue', '__httpuri_etsi_org01903v1_3_2_CRLValuesType_httpuri_etsi_org01903v1_3_2EncapsulatedCRLValue', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 447, 3), )

    
    EncapsulatedCRLValue = property(__EncapsulatedCRLValue.value, __EncapsulatedCRLValue.set, None, None)

    _ElementMap.update({
        __EncapsulatedCRLValue.name() : __EncapsulatedCRLValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CRLValuesType = CRLValuesType
Namespace.addCategoryObject('typeBinding', 'CRLValuesType', CRLValuesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}OCSPValuesType with content type ELEMENT_ONLY
class OCSPValuesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}OCSPValuesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OCSPValuesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 450, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}EncapsulatedOCSPValue uses Python identifier EncapsulatedOCSPValue
    __EncapsulatedOCSPValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedOCSPValue'), 'EncapsulatedOCSPValue', '__httpuri_etsi_org01903v1_3_2_OCSPValuesType_httpuri_etsi_org01903v1_3_2EncapsulatedOCSPValue', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 452, 3), )

    
    EncapsulatedOCSPValue = property(__EncapsulatedOCSPValue.value, __EncapsulatedOCSPValue.set, None, None)

    _ElementMap.update({
        __EncapsulatedOCSPValue.name() : __EncapsulatedOCSPValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OCSPValuesType = OCSPValuesType
Namespace.addCategoryObject('typeBinding', 'OCSPValuesType', OCSPValuesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}OtherCertStatusValuesType with content type ELEMENT_ONLY
class OtherCertStatusValuesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}OtherCertStatusValuesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OtherCertStatusValuesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 455, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}OtherValue uses Python identifier OtherValue
    __OtherValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OtherValue'), 'OtherValue', '__httpuri_etsi_org01903v1_3_2_OtherCertStatusValuesType_httpuri_etsi_org01903v1_3_2OtherValue', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 457, 3), )

    
    OtherValue = property(__OtherValue.value, __OtherValue.set, None, None)

    _ElementMap.update({
        __OtherValue.name() : __OtherValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OtherCertStatusValuesType = OtherCertStatusValuesType
Namespace.addCategoryObject('typeBinding', 'OtherCertStatusValuesType', OtherCertStatusValuesType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}IdentifierType with content type SIMPLE
class IdentifierType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}IdentifierType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 22, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute Qualifier uses Python identifier Qualifier
    __Qualifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Qualifier'), 'Qualifier', '__httpuri_etsi_org01903v1_3_2_IdentifierType_Qualifier', _module_typeBindings.QualifierType)
    __Qualifier._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 25, 4)
    __Qualifier._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 25, 4)
    
    Qualifier = property(__Qualifier.value, __Qualifier.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Qualifier.name() : __Qualifier
    })
_module_typeBindings.IdentifierType = IdentifierType
Namespace.addCategoryObject('typeBinding', 'IdentifierType', IdentifierType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}XAdESTimeStampType with content type ELEMENT_ONLY
class XAdESTimeStampType (GenericTimeStampType):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}XAdESTimeStampType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'XAdESTimeStampType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 85, 1)
    _ElementMap = GenericTimeStampType._ElementMap.copy()
    _AttributeMap = GenericTimeStampType._AttributeMap.copy()
    # Base type is GenericTimeStampType
    
    # Element Include ({http://uri.etsi.org/01903/v1.3.2#}Include) inherited from {http://uri.etsi.org/01903/v1.3.2#}GenericTimeStampType
    
    # Element EncapsulatedTimeStamp ({http://uri.etsi.org/01903/v1.3.2#}EncapsulatedTimeStamp) inherited from {http://uri.etsi.org/01903/v1.3.2#}GenericTimeStampType
    
    # Element XMLTimeStamp ({http://uri.etsi.org/01903/v1.3.2#}XMLTimeStamp) inherited from {http://uri.etsi.org/01903/v1.3.2#}GenericTimeStampType
    
    # Element CanonicalizationMethod ({http://www.w3.org/2000/09/xmldsig#}CanonicalizationMethod) inherited from {http://uri.etsi.org/01903/v1.3.2#}GenericTimeStampType
    
    # Attribute Id is restricted from parent
    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_GenericTimeStampType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 96, 4)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 96, 4)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.XAdESTimeStampType = XAdESTimeStampType
Namespace.addCategoryObject('typeBinding', 'XAdESTimeStampType', XAdESTimeStampType)


# Complex type {http://uri.etsi.org/01903/v1.3.2#}OtherTimeStampType with content type ELEMENT_ONLY
class OtherTimeStampType (GenericTimeStampType):
    """Complex type {http://uri.etsi.org/01903/v1.3.2#}OtherTimeStampType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OtherTimeStampType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 103, 1)
    _ElementMap = GenericTimeStampType._ElementMap.copy()
    _AttributeMap = GenericTimeStampType._AttributeMap.copy()
    # Base type is GenericTimeStampType
    
    # Element ReferenceInfo ({http://uri.etsi.org/01903/v1.3.2#}ReferenceInfo) inherited from {http://uri.etsi.org/01903/v1.3.2#}GenericTimeStampType
    
    # Element EncapsulatedTimeStamp ({http://uri.etsi.org/01903/v1.3.2#}EncapsulatedTimeStamp) inherited from {http://uri.etsi.org/01903/v1.3.2#}GenericTimeStampType
    
    # Element XMLTimeStamp ({http://uri.etsi.org/01903/v1.3.2#}XMLTimeStamp) inherited from {http://uri.etsi.org/01903/v1.3.2#}GenericTimeStampType
    
    # Element CanonicalizationMethod ({http://www.w3.org/2000/09/xmldsig#}CanonicalizationMethod) inherited from {http://uri.etsi.org/01903/v1.3.2#}GenericTimeStampType
    
    # Attribute Id is restricted from parent
    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_3_2_GenericTimeStampType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 114, 4)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 114, 4)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.OtherTimeStampType = OtherTimeStampType
Namespace.addCategoryObject('typeBinding', 'OtherTimeStampType', OtherTimeStampType)


SigningTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigningTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 218, 1))
Namespace.addCategoryObject('elementBinding', SigningTime.name().localName(), SigningTime)

SPURI = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SPURI'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 262, 1))
Namespace.addCategoryObject('elementBinding', SPURI.name().localName(), SPURI)

Any = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Any'), AnyType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 5, 1))
Namespace.addCategoryObject('elementBinding', Any.name().localName(), Any)

ObjectIdentifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObjectIdentifier'), ObjectIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 14, 1))
Namespace.addCategoryObject('elementBinding', ObjectIdentifier.name().localName(), ObjectIdentifier)

EncapsulatedPKIData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedPKIData'), EncapsulatedPKIDataType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 42, 1))
Namespace.addCategoryObject('elementBinding', EncapsulatedPKIData.name().localName(), EncapsulatedPKIData)

Include = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Include'), IncludeType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 54, 1))
Namespace.addCategoryObject('elementBinding', Include.name().localName(), Include)

ReferenceInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceInfo'), ReferenceInfoType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 59, 1))
Namespace.addCategoryObject('elementBinding', ReferenceInfo.name().localName(), ReferenceInfo)

QualifyingProperties = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QualifyingProperties'), QualifyingPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 123, 1))
Namespace.addCategoryObject('elementBinding', QualifyingProperties.name().localName(), QualifyingProperties)

SignedProperties = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignedProperties'), SignedPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 134, 1))
Namespace.addCategoryObject('elementBinding', SignedProperties.name().localName(), SignedProperties)

UnsignedProperties = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnsignedProperties'), UnsignedPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 144, 1))
Namespace.addCategoryObject('elementBinding', UnsignedProperties.name().localName(), UnsignedProperties)

SignedSignatureProperties = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignedSignatureProperties'), SignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 154, 1))
Namespace.addCategoryObject('elementBinding', SignedSignatureProperties.name().localName(), SignedSignatureProperties)

SignedDataObjectProperties = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignedDataObjectProperties'), SignedDataObjectPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 167, 1))
Namespace.addCategoryObject('elementBinding', SignedDataObjectProperties.name().localName(), SignedDataObjectProperties)

UnsignedSignatureProperties = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnsignedSignatureProperties'), UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 179, 1))
Namespace.addCategoryObject('elementBinding', UnsignedSignatureProperties.name().localName(), UnsignedSignatureProperties)

UnsignedDataObjectProperties = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnsignedDataObjectProperties'), UnsignedDataObjectPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 201, 1))
Namespace.addCategoryObject('elementBinding', UnsignedDataObjectProperties.name().localName(), UnsignedDataObjectProperties)

QualifyingPropertiesReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QualifyingPropertiesReference'), QualifyingPropertiesReferenceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 210, 1))
Namespace.addCategoryObject('elementBinding', QualifyingPropertiesReference.name().localName(), QualifyingPropertiesReference)

SigningCertificate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigningCertificate'), CertIDListType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 221, 1))
Namespace.addCategoryObject('elementBinding', SigningCertificate.name().localName(), SigningCertificate)

SignaturePolicyIdentifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyIdentifier'), SignaturePolicyIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 242, 1))
Namespace.addCategoryObject('elementBinding', SignaturePolicyIdentifier.name().localName(), SignaturePolicyIdentifier)

SPUserNotice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SPUserNotice'), SPUserNoticeType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 263, 1))
Namespace.addCategoryObject('elementBinding', SPUserNotice.name().localName(), SPUserNotice)

CounterSignature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CounterSignature'), CounterSignatureType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 283, 1))
Namespace.addCategoryObject('elementBinding', CounterSignature.name().localName(), CounterSignature)

DataObjectFormat = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataObjectFormat'), DataObjectFormatType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 291, 1))
Namespace.addCategoryObject('elementBinding', DataObjectFormat.name().localName(), DataObjectFormat)

CommitmentTypeIndication = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeIndication'), CommitmentTypeIndicationType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 303, 1))
Namespace.addCategoryObject('elementBinding', CommitmentTypeIndication.name().localName(), CommitmentTypeIndication)

SignatureProductionPlace = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignatureProductionPlace'), SignatureProductionPlaceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 321, 1))
Namespace.addCategoryObject('elementBinding', SignatureProductionPlace.name().localName(), SignatureProductionPlace)

SignerRole = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignerRole'), SignerRoleType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 332, 1))
Namespace.addCategoryObject('elementBinding', SignerRole.name().localName(), SignerRole)

CompleteCertificateRefs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompleteCertificateRefs'), CompleteCertificateRefsType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 354, 1))
Namespace.addCategoryObject('elementBinding', CompleteCertificateRefs.name().localName(), CompleteCertificateRefs)

CompleteRevocationRefs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompleteRevocationRefs'), CompleteRevocationRefsType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 363, 1))
Namespace.addCategoryObject('elementBinding', CompleteRevocationRefs.name().localName(), CompleteRevocationRefs)

AttributeCertificateRefs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AttributeCertificateRefs'), CompleteCertificateRefsType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 421, 1))
Namespace.addCategoryObject('elementBinding', AttributeCertificateRefs.name().localName(), AttributeCertificateRefs)

AttributeRevocationRefs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AttributeRevocationRefs'), CompleteRevocationRefsType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 422, 1))
Namespace.addCategoryObject('elementBinding', AttributeRevocationRefs.name().localName(), AttributeRevocationRefs)

CertificateValues = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CertificateValues'), CertificateValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 426, 1))
Namespace.addCategoryObject('elementBinding', CertificateValues.name().localName(), CertificateValues)

RevocationValues = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RevocationValues'), RevocationValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 436, 1))
Namespace.addCategoryObject('elementBinding', RevocationValues.name().localName(), RevocationValues)

AttrAuthoritiesCertValues = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AttrAuthoritiesCertValues'), CertificateValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 461, 1))
Namespace.addCategoryObject('elementBinding', AttrAuthoritiesCertValues.name().localName(), AttrAuthoritiesCertValues)

AttributeRevocationValues = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AttributeRevocationValues'), RevocationValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 462, 1))
Namespace.addCategoryObject('elementBinding', AttributeRevocationValues.name().localName(), AttributeRevocationValues)

XAdESTimeStamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'XAdESTimeStamp'), XAdESTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 84, 1))
Namespace.addCategoryObject('elementBinding', XAdESTimeStamp.name().localName(), XAdESTimeStamp)

OtherTimeStamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherTimeStamp'), OtherTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 102, 1))
Namespace.addCategoryObject('elementBinding', OtherTimeStamp.name().localName(), OtherTimeStamp)

AllDataObjectsTimeStamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AllDataObjectsTimeStamp'), XAdESTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 350, 1))
Namespace.addCategoryObject('elementBinding', AllDataObjectsTimeStamp.name().localName(), AllDataObjectsTimeStamp)

IndividualDataObjectsTimeStamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IndividualDataObjectsTimeStamp'), XAdESTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 351, 1))
Namespace.addCategoryObject('elementBinding', IndividualDataObjectsTimeStamp.name().localName(), IndividualDataObjectsTimeStamp)

SignatureTimeStamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignatureTimeStamp'), XAdESTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 352, 1))
Namespace.addCategoryObject('elementBinding', SignatureTimeStamp.name().localName(), SignatureTimeStamp)

SigAndRefsTimeStamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigAndRefsTimeStamp'), XAdESTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 423, 1))
Namespace.addCategoryObject('elementBinding', SigAndRefsTimeStamp.name().localName(), SigAndRefsTimeStamp)

RefsOnlyTimeStamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RefsOnlyTimeStamp'), XAdESTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 424, 1))
Namespace.addCategoryObject('elementBinding', RefsOnlyTimeStamp.name().localName(), RefsOnlyTimeStamp)

ArchiveTimeStamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ArchiveTimeStamp'), XAdESTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 463, 1))
Namespace.addCategoryObject('elementBinding', ArchiveTimeStamp.name().localName(), ArchiveTimeStamp)



def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 7, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 8, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AnyType._Automaton = _BuildAutomaton()




ObjectIdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), IdentifierType, scope=ObjectIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 17, 3)))

ObjectIdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), pyxb.binding.datatypes.string, scope=ObjectIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 18, 3)))

ObjectIdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DocumentationReferences'), DocumentationReferencesType, scope=ObjectIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 19, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 18, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 19, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObjectIdentifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 17, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ObjectIdentifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 18, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ObjectIdentifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DocumentationReferences')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 19, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObjectIdentifierType._Automaton = _BuildAutomaton_()




DocumentationReferencesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DocumentationReference'), pyxb.binding.datatypes.anyURI, scope=DocumentationReferencesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 37, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DocumentationReferencesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DocumentationReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 37, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DocumentationReferencesType._Automaton = _BuildAutomaton_2()




ReferenceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestMethod'), _ImportedBinding__ds.DigestMethodType, scope=ReferenceInfoType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 96, 0)))

ReferenceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestValue'), _ImportedBinding__ds.DigestValueType, scope=ReferenceInfoType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 104, 0)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceInfoType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestMethod')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 62, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferenceInfoType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestValue')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 63, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferenceInfoType._Automaton = _BuildAutomaton_3()




GenericTimeStampType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Include'), IncludeType, scope=GenericTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 54, 1)))

GenericTimeStampType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceInfo'), ReferenceInfoType, scope=GenericTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 59, 1)))

GenericTimeStampType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedTimeStamp'), EncapsulatedPKIDataType, scope=GenericTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 76, 4)))

GenericTimeStampType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'XMLTimeStamp'), AnyType, scope=GenericTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 77, 4)))

GenericTimeStampType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'CanonicalizationMethod'), _ImportedBinding__ds.CanonicalizationMethodType, scope=GenericTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 44, 2)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 70, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 71, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 74, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GenericTimeStampType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Include')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 71, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GenericTimeStampType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceInfo')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 72, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GenericTimeStampType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'CanonicalizationMethod')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 74, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericTimeStampType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 76, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericTimeStampType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'XMLTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 77, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericTimeStampType._Automaton = _BuildAutomaton_4()




QualifyingPropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignedProperties'), SignedPropertiesType, scope=QualifyingPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 126, 3)))

QualifyingPropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnsignedProperties'), UnsignedPropertiesType, scope=QualifyingPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 127, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 126, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 127, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QualifyingPropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignedProperties')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 126, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(QualifyingPropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UnsignedProperties')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 127, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
QualifyingPropertiesType._Automaton = _BuildAutomaton_5()




SignedPropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignedSignatureProperties'), SignedSignaturePropertiesType, scope=SignedPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 137, 3)))

SignedPropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignedDataObjectProperties'), SignedDataObjectPropertiesType, scope=SignedPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 138, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 137, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 138, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SignedPropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignedSignatureProperties')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 137, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SignedPropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignedDataObjectProperties')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 138, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SignedPropertiesType._Automaton = _BuildAutomaton_6()




UnsignedPropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnsignedSignatureProperties'), UnsignedSignaturePropertiesType, scope=UnsignedPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 147, 3)))

UnsignedPropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnsignedDataObjectProperties'), UnsignedDataObjectPropertiesType, scope=UnsignedPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 148, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 147, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 148, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UnsignedPropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UnsignedSignatureProperties')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 147, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UnsignedPropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UnsignedDataObjectProperties')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 148, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UnsignedPropertiesType._Automaton = _BuildAutomaton_7()




SignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigningTime'), pyxb.binding.datatypes.dateTime, scope=SignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 157, 3)))

SignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigningCertificate'), CertIDListType, scope=SignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 158, 3)))

SignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyIdentifier'), SignaturePolicyIdentifierType, scope=SignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 159, 3)))

SignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignatureProductionPlace'), SignatureProductionPlaceType, scope=SignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 160, 3)))

SignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignerRole'), SignerRoleType, scope=SignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 161, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 157, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 158, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 159, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 160, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 161, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SigningTime')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 157, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SigningCertificate')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 158, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyIdentifier')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 159, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignatureProductionPlace')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 160, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignerRole')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 161, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SignedSignaturePropertiesType._Automaton = _BuildAutomaton_8()




SignedDataObjectPropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataObjectFormat'), DataObjectFormatType, scope=SignedDataObjectPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 170, 3)))

SignedDataObjectPropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeIndication'), CommitmentTypeIndicationType, scope=SignedDataObjectPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 171, 3)))

SignedDataObjectPropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AllDataObjectsTimeStamp'), XAdESTimeStampType, scope=SignedDataObjectPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 172, 3)))

SignedDataObjectPropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IndividualDataObjectsTimeStamp'), XAdESTimeStampType, scope=SignedDataObjectPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 173, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 170, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 171, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 172, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 173, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SignedDataObjectPropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataObjectFormat')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 170, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SignedDataObjectPropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeIndication')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 171, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SignedDataObjectPropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AllDataObjectsTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 172, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SignedDataObjectPropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IndividualDataObjectsTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 173, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SignedDataObjectPropertiesType._Automaton = _BuildAutomaton_9()




UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CounterSignature'), CounterSignatureType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 182, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignatureTimeStamp'), XAdESTimeStampType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 183, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompleteCertificateRefs'), CompleteCertificateRefsType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 184, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompleteRevocationRefs'), CompleteRevocationRefsType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 185, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AttributeCertificateRefs'), CompleteCertificateRefsType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 186, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AttributeRevocationRefs'), CompleteRevocationRefsType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 187, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigAndRefsTimeStamp'), XAdESTimeStampType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 188, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RefsOnlyTimeStamp'), XAdESTimeStampType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 189, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CertificateValues'), CertificateValuesType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 190, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RevocationValues'), RevocationValuesType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 191, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AttrAuthoritiesCertValues'), CertificateValuesType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 192, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AttributeRevocationValues'), RevocationValuesType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 193, 3)))

UnsignedSignaturePropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ArchiveTimeStamp'), XAdESTimeStampType, scope=UnsignedSignaturePropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 194, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CounterSignature')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 182, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignatureTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 183, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompleteCertificateRefs')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 184, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompleteRevocationRefs')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 185, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AttributeCertificateRefs')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 186, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AttributeRevocationRefs')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 187, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SigAndRefsTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 188, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RefsOnlyTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 189, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CertificateValues')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 190, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RevocationValues')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 191, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AttrAuthoritiesCertValues')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 192, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AttributeRevocationValues')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 193, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedSignaturePropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ArchiveTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 194, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://uri.etsi.org/01903/v1.3.2#')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 195, 3))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UnsignedSignaturePropertiesType._Automaton = _BuildAutomaton_10()




UnsignedDataObjectPropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnsignedDataObjectProperty'), AnyType, scope=UnsignedDataObjectPropertiesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 204, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UnsignedDataObjectPropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UnsignedDataObjectProperty')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 204, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UnsignedDataObjectPropertiesType._Automaton = _BuildAutomaton_11()




CertIDListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cert'), CertIDType, scope=CertIDListType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 224, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CertIDListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cert')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 224, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CertIDListType._Automaton = _BuildAutomaton_12()




CertIDType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CertDigest'), DigestAlgAndValueType, scope=CertIDType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 229, 3)))

CertIDType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IssuerSerial'), _ImportedBinding__ds.X509IssuerSerialType, scope=CertIDType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 230, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertIDType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CertDigest')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 229, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CertIDType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IssuerSerial')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 230, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CertIDType._Automaton = _BuildAutomaton_13()




DigestAlgAndValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestMethod'), _ImportedBinding__ds.DigestMethodType, scope=DigestAlgAndValueType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 96, 0)))

DigestAlgAndValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestValue'), _ImportedBinding__ds.DigestValueType, scope=DigestAlgAndValueType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 104, 0)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DigestAlgAndValueType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestMethod')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 236, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DigestAlgAndValueType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'DigestValue')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 237, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DigestAlgAndValueType._Automaton = _BuildAutomaton_14()




SignaturePolicyIdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyId'), SignaturePolicyIdType, scope=SignaturePolicyIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 245, 3)))

SignaturePolicyIdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyImplied'), pyxb.binding.datatypes.anyType, scope=SignaturePolicyIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 246, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SignaturePolicyIdentifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyId')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 245, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SignaturePolicyIdentifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignaturePolicyImplied')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 246, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SignaturePolicyIdentifierType._Automaton = _BuildAutomaton_15()




SignaturePolicyIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyId'), ObjectIdentifierType, scope=SignaturePolicyIdType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 251, 3)))

SignaturePolicyIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyHash'), DigestAlgAndValueType, scope=SignaturePolicyIdType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 253, 3)))

SignaturePolicyIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyQualifiers'), SigPolicyQualifiersListType, scope=SignaturePolicyIdType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 254, 3)))

SignaturePolicyIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Transforms'), _ImportedBinding__ds.TransformsType, scope=SignaturePolicyIdType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 77, 2)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 252, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 254, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SignaturePolicyIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyId')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 251, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SignaturePolicyIdType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Transforms')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 252, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SignaturePolicyIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyHash')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 253, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SignaturePolicyIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyQualifiers')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 254, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SignaturePolicyIdType._Automaton = _BuildAutomaton_16()




SigPolicyQualifiersListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyQualifier'), AnyType, scope=SigPolicyQualifiersListType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 259, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SigPolicyQualifiersListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SigPolicyQualifier')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 259, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SigPolicyQualifiersListType._Automaton = _BuildAutomaton_17()




SPUserNoticeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NoticeRef'), NoticeReferenceType, scope=SPUserNoticeType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 266, 3)))

SPUserNoticeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExplicitText'), pyxb.binding.datatypes.string, scope=SPUserNoticeType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 267, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 266, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 267, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SPUserNoticeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NoticeRef')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 266, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SPUserNoticeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExplicitText')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 267, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SPUserNoticeType._Automaton = _BuildAutomaton_18()




NoticeReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organization'), pyxb.binding.datatypes.string, scope=NoticeReferenceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 272, 3)))

NoticeReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NoticeNumbers'), IntegerListType, scope=NoticeReferenceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 273, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(NoticeReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organization')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 272, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NoticeReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NoticeNumbers')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 273, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
NoticeReferenceType._Automaton = _BuildAutomaton_19()




IntegerListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'int'), pyxb.binding.datatypes.integer, scope=IntegerListType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 278, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 278, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IntegerListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'int')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 278, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IntegerListType._Automaton = _BuildAutomaton_20()




CounterSignatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding__ds.SignatureType, scope=CounterSignatureType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 12, 0)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CounterSignatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 286, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CounterSignatureType._Automaton = _BuildAutomaton_21()




DataObjectFormatType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), pyxb.binding.datatypes.string, scope=DataObjectFormatType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 294, 3)))

DataObjectFormatType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObjectIdentifier'), ObjectIdentifierType, scope=DataObjectFormatType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 295, 3)))

DataObjectFormatType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MimeType'), pyxb.binding.datatypes.string, scope=DataObjectFormatType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 296, 3)))

DataObjectFormatType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Encoding'), pyxb.binding.datatypes.anyURI, scope=DataObjectFormatType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 297, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 294, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 295, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 296, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 297, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataObjectFormatType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 294, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataObjectFormatType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObjectIdentifier')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 295, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataObjectFormatType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MimeType')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 296, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DataObjectFormatType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Encoding')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 297, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DataObjectFormatType._Automaton = _BuildAutomaton_22()




CommitmentTypeIndicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeId'), ObjectIdentifierType, scope=CommitmentTypeIndicationType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 306, 3)))

CommitmentTypeIndicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ObjectReference'), pyxb.binding.datatypes.anyURI, scope=CommitmentTypeIndicationType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 308, 4)))

CommitmentTypeIndicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AllSignedDataObjects'), pyxb.binding.datatypes.anyType, scope=CommitmentTypeIndicationType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 309, 4)))

CommitmentTypeIndicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeQualifiers'), CommitmentTypeQualifiersListType, scope=CommitmentTypeIndicationType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 311, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 311, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CommitmentTypeIndicationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeId')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 306, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommitmentTypeIndicationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ObjectReference')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 308, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommitmentTypeIndicationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AllSignedDataObjects')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 309, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CommitmentTypeIndicationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeQualifiers')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 311, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CommitmentTypeIndicationType._Automaton = _BuildAutomaton_23()




CommitmentTypeQualifiersListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeQualifier'), AnyType, scope=CommitmentTypeQualifiersListType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 316, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 316, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CommitmentTypeQualifiersListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CommitmentTypeQualifier')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 316, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CommitmentTypeQualifiersListType._Automaton = _BuildAutomaton_24()




SignatureProductionPlaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'City'), pyxb.binding.datatypes.string, scope=SignatureProductionPlaceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 324, 3)))

SignatureProductionPlaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StateOrProvince'), pyxb.binding.datatypes.string, scope=SignatureProductionPlaceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 325, 3)))

SignatureProductionPlaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), pyxb.binding.datatypes.string, scope=SignatureProductionPlaceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 326, 3)))

SignatureProductionPlaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CountryName'), pyxb.binding.datatypes.string, scope=SignatureProductionPlaceType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 327, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 324, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 325, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 326, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 327, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SignatureProductionPlaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'City')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 324, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SignatureProductionPlaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StateOrProvince')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 325, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SignatureProductionPlaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 326, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SignatureProductionPlaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CountryName')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 327, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SignatureProductionPlaceType._Automaton = _BuildAutomaton_25()




SignerRoleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClaimedRoles'), ClaimedRolesListType, scope=SignerRoleType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 335, 3)))

SignerRoleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CertifiedRoles'), CertifiedRolesListType, scope=SignerRoleType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 336, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 335, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 336, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SignerRoleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClaimedRoles')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 335, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SignerRoleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CertifiedRoles')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 336, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SignerRoleType._Automaton = _BuildAutomaton_26()




ClaimedRolesListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClaimedRole'), AnyType, scope=ClaimedRolesListType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 341, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClaimedRolesListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClaimedRole')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 341, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ClaimedRolesListType._Automaton = _BuildAutomaton_27()




CertifiedRolesListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CertifiedRole'), EncapsulatedPKIDataType, scope=CertifiedRolesListType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 346, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CertifiedRolesListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CertifiedRole')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 346, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CertifiedRolesListType._Automaton = _BuildAutomaton_28()




CompleteCertificateRefsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CertRefs'), CertIDListType, scope=CompleteCertificateRefsType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 357, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CompleteCertificateRefsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CertRefs')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 357, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CompleteCertificateRefsType._Automaton = _BuildAutomaton_29()




CompleteRevocationRefsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CRLRefs'), CRLRefsType, scope=CompleteRevocationRefsType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 366, 3)))

CompleteRevocationRefsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OCSPRefs'), OCSPRefsType, scope=CompleteRevocationRefsType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 367, 3)))

CompleteRevocationRefsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherRefs'), OtherCertStatusRefsType, scope=CompleteRevocationRefsType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 368, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 366, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 367, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 368, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CompleteRevocationRefsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CRLRefs')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 366, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CompleteRevocationRefsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OCSPRefs')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 367, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CompleteRevocationRefsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OtherRefs')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 368, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CompleteRevocationRefsType._Automaton = _BuildAutomaton_30()




CRLRefsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CRLRef'), CRLRefType, scope=CRLRefsType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 374, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CRLRefsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CRLRef')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 374, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CRLRefsType._Automaton = _BuildAutomaton_31()




CRLRefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DigestAlgAndValue'), DigestAlgAndValueType, scope=CRLRefType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 379, 3)))

CRLRefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CRLIdentifier'), CRLIdentifierType, scope=CRLRefType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 380, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 380, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CRLRefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DigestAlgAndValue')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 379, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CRLRefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CRLIdentifier')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 380, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CRLRefType._Automaton = _BuildAutomaton_32()




CRLIdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issuer'), pyxb.binding.datatypes.string, scope=CRLIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 385, 3)))

CRLIdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IssueTime'), pyxb.binding.datatypes.dateTime, scope=CRLIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 386, 3)))

CRLIdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Number'), pyxb.binding.datatypes.integer, scope=CRLIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 387, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 387, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CRLIdentifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issuer')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 385, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CRLIdentifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IssueTime')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 386, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CRLIdentifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Number')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 387, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CRLIdentifierType._Automaton = _BuildAutomaton_33()




OCSPRefsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OCSPRef'), OCSPRefType, scope=OCSPRefsType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 393, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OCSPRefsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OCSPRef')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 393, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OCSPRefsType._Automaton = _BuildAutomaton_34()




OCSPRefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OCSPIdentifier'), OCSPIdentifierType, scope=OCSPRefType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 398, 3)))

OCSPRefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DigestAlgAndValue'), DigestAlgAndValueType, scope=OCSPRefType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 399, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 399, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OCSPRefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OCSPIdentifier')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 398, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OCSPRefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DigestAlgAndValue')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 399, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OCSPRefType._Automaton = _BuildAutomaton_35()




ResponderIDType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ByName'), pyxb.binding.datatypes.string, scope=ResponderIDType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 404, 3)))

ResponderIDType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ByKey'), pyxb.binding.datatypes.base64Binary, scope=ResponderIDType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 405, 3)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponderIDType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ByName')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 404, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponderIDType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ByKey')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 405, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ResponderIDType._Automaton = _BuildAutomaton_36()




OCSPIdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponderID'), ResponderIDType, scope=OCSPIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 410, 3)))

OCSPIdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProducedAt'), pyxb.binding.datatypes.dateTime, scope=OCSPIdentifierType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 411, 3)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OCSPIdentifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponderID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 410, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OCSPIdentifierType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProducedAt')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 411, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OCSPIdentifierType._Automaton = _BuildAutomaton_37()




OtherCertStatusRefsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherRef'), AnyType, scope=OtherCertStatusRefsType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 417, 3)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OtherCertStatusRefsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OtherRef')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 417, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OtherCertStatusRefsType._Automaton = _BuildAutomaton_38()




CertificateValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedX509Certificate'), EncapsulatedPKIDataType, scope=CertificateValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 429, 3)))

CertificateValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherCertificate'), AnyType, scope=CertificateValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 430, 3)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 428, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CertificateValuesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedX509Certificate')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 429, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CertificateValuesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OtherCertificate')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 430, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CertificateValuesType._Automaton = _BuildAutomaton_39()




RevocationValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CRLValues'), CRLValuesType, scope=RevocationValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 439, 3)))

RevocationValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OCSPValues'), OCSPValuesType, scope=RevocationValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 440, 3)))

RevocationValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherValues'), OtherCertStatusValuesType, scope=RevocationValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 441, 3)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 439, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 440, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 441, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RevocationValuesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CRLValues')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 439, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RevocationValuesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OCSPValues')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 440, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RevocationValuesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OtherValues')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 441, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RevocationValuesType._Automaton = _BuildAutomaton_40()




CRLValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedCRLValue'), EncapsulatedPKIDataType, scope=CRLValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 447, 3)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CRLValuesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedCRLValue')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 447, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CRLValuesType._Automaton = _BuildAutomaton_41()




OCSPValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedOCSPValue'), EncapsulatedPKIDataType, scope=OCSPValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 452, 3)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OCSPValuesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedOCSPValue')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 452, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OCSPValuesType._Automaton = _BuildAutomaton_42()




OtherCertStatusValuesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherValue'), AnyType, scope=OtherCertStatusValuesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 457, 3)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OtherCertStatusValuesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OtherValue')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 457, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OtherCertStatusValuesType._Automaton = _BuildAutomaton_43()




def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 89, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 90, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(XAdESTimeStampType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Include')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 89, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(XAdESTimeStampType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'CanonicalizationMethod')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 90, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XAdESTimeStampType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 92, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XAdESTimeStampType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'XMLTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 93, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
XAdESTimeStampType._Automaton = _BuildAutomaton_44()




def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 108, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OtherTimeStampType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceInfo')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 107, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OtherTimeStampType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'CanonicalizationMethod')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 108, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OtherTimeStampType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncapsulatedTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 110, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OtherTimeStampType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'XMLTimeStamp')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 111, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OtherTimeStampType._Automaton = _BuildAutomaton_45()

