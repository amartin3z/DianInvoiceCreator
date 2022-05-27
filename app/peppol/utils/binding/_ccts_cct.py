# ./_ccts_cct.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1f67187bae020696b10d12403debb16fa03cfbbd
# Generated 2020-05-26 15:40:38.330392 by PyXB version 1.2.6 using Python 3.7.5.final.0
# Namespace urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2 [xmlns:ccts-cct]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}AmountType with content type SIMPLE
class AmountType (pyxb.binding.basis.complexTypeDefinition):
    """
            
            
            
            
            
            
            
         """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AmountType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 6, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    
    # Attribute currencyID uses Python identifier currencyID
    __currencyID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'currencyID'), 'currencyID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_AmountType_currencyID', pyxb.binding.datatypes.normalizedString)
    __currencyID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 20, 12)
    __currencyID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 20, 12)
    
    currencyID = property(__currencyID.value, __currencyID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute currencyCodeListVersionID uses Python identifier currencyCodeListVersionID
    __currencyCodeListVersionID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'currencyCodeListVersionID'), 'currencyCodeListVersionID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_AmountType_currencyCodeListVersionID', pyxb.binding.datatypes.normalizedString)
    __currencyCodeListVersionID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 35, 12)
    __currencyCodeListVersionID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 35, 12)
    
    currencyCodeListVersionID = property(__currencyCodeListVersionID.value, __currencyCodeListVersionID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __currencyID.name() : __currencyID,
        __currencyCodeListVersionID.name() : __currencyCodeListVersionID
    })
_module_typeBindings.AmountType = AmountType
Namespace.addCategoryObject('typeBinding', 'AmountType', AmountType)


# Complex type {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType with content type SIMPLE
class BinaryObjectType (pyxb.binding.basis.complexTypeDefinition):
    """
            
            
            
            
            
            
            
         """
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinaryObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 54, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.base64Binary
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_BinaryObjectType_format', pyxb.binding.datatypes.string)
    __format._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 68, 12)
    __format._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 68, 12)
    
    format = property(__format.value, __format.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute mimeCode uses Python identifier mimeCode
    __mimeCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mimeCode'), 'mimeCode', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_BinaryObjectType_mimeCode', pyxb.binding.datatypes.normalizedString)
    __mimeCode._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 82, 12)
    __mimeCode._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 82, 12)
    
    mimeCode = property(__mimeCode.value, __mimeCode.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute encodingCode uses Python identifier encodingCode
    __encodingCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'encodingCode'), 'encodingCode', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_BinaryObjectType_encodingCode', pyxb.binding.datatypes.normalizedString)
    __encodingCode._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 96, 12)
    __encodingCode._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 96, 12)
    
    encodingCode = property(__encodingCode.value, __encodingCode.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute characterSetCode uses Python identifier characterSetCode
    __characterSetCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'characterSetCode'), 'characterSetCode', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_BinaryObjectType_characterSetCode', pyxb.binding.datatypes.normalizedString)
    __characterSetCode._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 110, 12)
    __characterSetCode._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 110, 12)
    
    characterSetCode = property(__characterSetCode.value, __characterSetCode.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_BinaryObjectType_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 124, 12)
    __uri._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 124, 12)
    
    uri = property(__uri.value, __uri.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute filename uses Python identifier filename
    __filename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filename'), 'filename', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_BinaryObjectType_filename', pyxb.binding.datatypes.string)
    __filename._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 138, 12)
    __filename._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 138, 12)
    
    filename = property(__filename.value, __filename.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __format.name() : __format,
        __mimeCode.name() : __mimeCode,
        __encodingCode.name() : __encodingCode,
        __characterSetCode.name() : __characterSetCode,
        __uri.name() : __uri,
        __filename.name() : __filename
    })
_module_typeBindings.BinaryObjectType = BinaryObjectType
Namespace.addCategoryObject('typeBinding', 'BinaryObjectType', BinaryObjectType)


# Complex type {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}CodeType with content type SIMPLE
class CodeType (pyxb.binding.basis.complexTypeDefinition):
    """
            
            
            
            
            
            
            
            
         """
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 157, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.normalizedString
    
    # Attribute listID uses Python identifier listID
    __listID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'listID'), 'listID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_CodeType_listID', pyxb.binding.datatypes.normalizedString)
    __listID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 172, 12)
    __listID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 172, 12)
    
    listID = property(__listID.value, __listID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute listAgencyID uses Python identifier listAgencyID
    __listAgencyID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'listAgencyID'), 'listAgencyID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_CodeType_listAgencyID', pyxb.binding.datatypes.normalizedString)
    __listAgencyID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 186, 12)
    __listAgencyID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 186, 12)
    
    listAgencyID = property(__listAgencyID.value, __listAgencyID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute listAgencyName uses Python identifier listAgencyName
    __listAgencyName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'listAgencyName'), 'listAgencyName', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_CodeType_listAgencyName', pyxb.binding.datatypes.string)
    __listAgencyName._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 201, 12)
    __listAgencyName._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 201, 12)
    
    listAgencyName = property(__listAgencyName.value, __listAgencyName.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute listName uses Python identifier listName
    __listName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'listName'), 'listName', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_CodeType_listName', pyxb.binding.datatypes.string)
    __listName._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 215, 12)
    __listName._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 215, 12)
    
    listName = property(__listName.value, __listName.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute listVersionID uses Python identifier listVersionID
    __listVersionID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'listVersionID'), 'listVersionID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_CodeType_listVersionID', pyxb.binding.datatypes.normalizedString)
    __listVersionID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 229, 12)
    __listVersionID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 229, 12)
    
    listVersionID = property(__listVersionID.value, __listVersionID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_CodeType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 243, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 243, 12)
    
    name = property(__name.value, __name.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute languageID uses Python identifier languageID
    __languageID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'languageID'), 'languageID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_CodeType_languageID', pyxb.binding.datatypes.language)
    __languageID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 257, 12)
    __languageID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 257, 12)
    
    languageID = property(__languageID.value, __languageID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute listURI uses Python identifier listURI
    __listURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'listURI'), 'listURI', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_CodeType_listURI', pyxb.binding.datatypes.anyURI)
    __listURI._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 271, 12)
    __listURI._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 271, 12)
    
    listURI = property(__listURI.value, __listURI.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute listSchemeURI uses Python identifier listSchemeURI
    __listSchemeURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'listSchemeURI'), 'listSchemeURI', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_CodeType_listSchemeURI', pyxb.binding.datatypes.anyURI)
    __listSchemeURI._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 285, 12)
    __listSchemeURI._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 285, 12)
    
    listSchemeURI = property(__listSchemeURI.value, __listSchemeURI.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __listID.name() : __listID,
        __listAgencyID.name() : __listAgencyID,
        __listAgencyName.name() : __listAgencyName,
        __listName.name() : __listName,
        __listVersionID.name() : __listVersionID,
        __name.name() : __name,
        __languageID.name() : __languageID,
        __listURI.name() : __listURI,
        __listSchemeURI.name() : __listSchemeURI
    })
_module_typeBindings.CodeType = CodeType
Namespace.addCategoryObject('typeBinding', 'CodeType', CodeType)


# Complex type {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}DateTimeType with content type SIMPLE
class DateTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
            
            
            
            
            
            
            
            
         """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateTimeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 304, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_DateTimeType_format', pyxb.binding.datatypes.string)
    __format._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 319, 12)
    __format._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 319, 12)
    
    format = property(__format.value, __format.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __format.name() : __format
    })
_module_typeBindings.DateTimeType = DateTimeType
Namespace.addCategoryObject('typeBinding', 'DateTimeType', DateTimeType)


# Complex type {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IdentifierType with content type SIMPLE
class IdentifierType (pyxb.binding.basis.complexTypeDefinition):
    """
            
            
            
            
            
            
            
         """
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 338, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.normalizedString
    
    # Attribute schemeID uses Python identifier schemeID
    __schemeID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemeID'), 'schemeID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_IdentifierType_schemeID', pyxb.binding.datatypes.normalizedString)
    __schemeID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 352, 12)
    __schemeID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 352, 12)
    
    schemeID = property(__schemeID.value, __schemeID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute schemeName uses Python identifier schemeName
    __schemeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemeName'), 'schemeName', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_IdentifierType_schemeName', pyxb.binding.datatypes.string)
    __schemeName._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 366, 12)
    __schemeName._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 366, 12)
    
    schemeName = property(__schemeName.value, __schemeName.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute schemeAgencyID uses Python identifier schemeAgencyID
    __schemeAgencyID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemeAgencyID'), 'schemeAgencyID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_IdentifierType_schemeAgencyID', pyxb.binding.datatypes.normalizedString)
    __schemeAgencyID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 380, 12)
    __schemeAgencyID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 380, 12)
    
    schemeAgencyID = property(__schemeAgencyID.value, __schemeAgencyID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute schemeAgencyName uses Python identifier schemeAgencyName
    __schemeAgencyName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemeAgencyName'), 'schemeAgencyName', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_IdentifierType_schemeAgencyName', pyxb.binding.datatypes.string)
    __schemeAgencyName._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 395, 12)
    __schemeAgencyName._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 395, 12)
    
    schemeAgencyName = property(__schemeAgencyName.value, __schemeAgencyName.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute schemeVersionID uses Python identifier schemeVersionID
    __schemeVersionID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemeVersionID'), 'schemeVersionID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_IdentifierType_schemeVersionID', pyxb.binding.datatypes.normalizedString)
    __schemeVersionID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 409, 12)
    __schemeVersionID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 409, 12)
    
    schemeVersionID = property(__schemeVersionID.value, __schemeVersionID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute schemeDataURI uses Python identifier schemeDataURI
    __schemeDataURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemeDataURI'), 'schemeDataURI', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_IdentifierType_schemeDataURI', pyxb.binding.datatypes.anyURI)
    __schemeDataURI._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 423, 12)
    __schemeDataURI._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 423, 12)
    
    schemeDataURI = property(__schemeDataURI.value, __schemeDataURI.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute schemeURI uses Python identifier schemeURI
    __schemeURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemeURI'), 'schemeURI', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_IdentifierType_schemeURI', pyxb.binding.datatypes.anyURI)
    __schemeURI._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 437, 12)
    __schemeURI._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 437, 12)
    
    schemeURI = property(__schemeURI.value, __schemeURI.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __schemeID.name() : __schemeID,
        __schemeName.name() : __schemeName,
        __schemeAgencyID.name() : __schemeAgencyID,
        __schemeAgencyName.name() : __schemeAgencyName,
        __schemeVersionID.name() : __schemeVersionID,
        __schemeDataURI.name() : __schemeDataURI,
        __schemeURI.name() : __schemeURI
    })
_module_typeBindings.IdentifierType = IdentifierType
Namespace.addCategoryObject('typeBinding', 'IdentifierType', IdentifierType)


# Complex type {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}IndicatorType with content type SIMPLE
class IndicatorType (pyxb.binding.basis.complexTypeDefinition):
    """
            
            
            
            
            
            
            
         """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 456, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_IndicatorType_format', pyxb.binding.datatypes.string)
    __format._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 470, 12)
    __format._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 470, 12)
    
    format = property(__format.value, __format.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __format.name() : __format
    })
_module_typeBindings.IndicatorType = IndicatorType
Namespace.addCategoryObject('typeBinding', 'IndicatorType', IndicatorType)


# Complex type {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}MeasureType with content type SIMPLE
class MeasureType (pyxb.binding.basis.complexTypeDefinition):
    """
            
            
            
            
            
            
            
         """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 489, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    
    # Attribute unitCode uses Python identifier unitCode
    __unitCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitCode'), 'unitCode', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_MeasureType_unitCode', pyxb.binding.datatypes.normalizedString)
    __unitCode._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 503, 12)
    __unitCode._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 503, 12)
    
    unitCode = property(__unitCode.value, __unitCode.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute unitCodeListVersionID uses Python identifier unitCodeListVersionID
    __unitCodeListVersionID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitCodeListVersionID'), 'unitCodeListVersionID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_MeasureType_unitCodeListVersionID', pyxb.binding.datatypes.normalizedString)
    __unitCodeListVersionID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 518, 12)
    __unitCodeListVersionID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 518, 12)
    
    unitCodeListVersionID = property(__unitCodeListVersionID.value, __unitCodeListVersionID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unitCode.name() : __unitCode,
        __unitCodeListVersionID.name() : __unitCodeListVersionID
    })
_module_typeBindings.MeasureType = MeasureType
Namespace.addCategoryObject('typeBinding', 'MeasureType', MeasureType)


# Complex type {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}NumericType with content type SIMPLE
class NumericType (pyxb.binding.basis.complexTypeDefinition):
    """
            
            
            
            
            
            
            
         """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NumericType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 537, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_NumericType_format', pyxb.binding.datatypes.string)
    __format._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 551, 12)
    __format._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 551, 12)
    
    format = property(__format.value, __format.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __format.name() : __format
    })
_module_typeBindings.NumericType = NumericType
Namespace.addCategoryObject('typeBinding', 'NumericType', NumericType)


# Complex type {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}QuantityType with content type SIMPLE
class QuantityType (pyxb.binding.basis.complexTypeDefinition):
    """
            
            
            
            
            
            
            
         """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QuantityType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 570, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    
    # Attribute unitCode uses Python identifier unitCode
    __unitCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitCode'), 'unitCode', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_QuantityType_unitCode', pyxb.binding.datatypes.normalizedString)
    __unitCode._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 584, 12)
    __unitCode._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 584, 12)
    
    unitCode = property(__unitCode.value, __unitCode.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute unitCodeListID uses Python identifier unitCodeListID
    __unitCodeListID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitCodeListID'), 'unitCodeListID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_QuantityType_unitCodeListID', pyxb.binding.datatypes.normalizedString)
    __unitCodeListID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 598, 12)
    __unitCodeListID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 598, 12)
    
    unitCodeListID = property(__unitCodeListID.value, __unitCodeListID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute unitCodeListAgencyID uses Python identifier unitCodeListAgencyID
    __unitCodeListAgencyID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitCodeListAgencyID'), 'unitCodeListAgencyID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_QuantityType_unitCodeListAgencyID', pyxb.binding.datatypes.normalizedString)
    __unitCodeListAgencyID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 612, 12)
    __unitCodeListAgencyID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 612, 12)
    
    unitCodeListAgencyID = property(__unitCodeListAgencyID.value, __unitCodeListAgencyID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute unitCodeListAgencyName uses Python identifier unitCodeListAgencyName
    __unitCodeListAgencyName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitCodeListAgencyName'), 'unitCodeListAgencyName', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_QuantityType_unitCodeListAgencyName', pyxb.binding.datatypes.string)
    __unitCodeListAgencyName._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 627, 12)
    __unitCodeListAgencyName._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 627, 12)
    
    unitCodeListAgencyName = property(__unitCodeListAgencyName.value, __unitCodeListAgencyName.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unitCode.name() : __unitCode,
        __unitCodeListID.name() : __unitCodeListID,
        __unitCodeListAgencyID.name() : __unitCodeListAgencyID,
        __unitCodeListAgencyName.name() : __unitCodeListAgencyName
    })
_module_typeBindings.QuantityType = QuantityType
Namespace.addCategoryObject('typeBinding', 'QuantityType', QuantityType)


# Complex type {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType with content type SIMPLE
class TextType (pyxb.binding.basis.complexTypeDefinition):
    """
            
            
            
            
            
            
            
         """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 646, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute languageID uses Python identifier languageID
    __languageID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'languageID'), 'languageID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_TextType_languageID', pyxb.binding.datatypes.language)
    __languageID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 660, 12)
    __languageID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 660, 12)
    
    languageID = property(__languageID.value, __languageID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    
    # Attribute languageLocaleID uses Python identifier languageLocaleID
    __languageLocaleID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'languageLocaleID'), 'languageLocaleID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_TextType_languageLocaleID', pyxb.binding.datatypes.normalizedString)
    __languageLocaleID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 674, 12)
    __languageLocaleID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/CCTS_CCT_SchemaModule-2.1.xsd', 674, 12)
    
    languageLocaleID = property(__languageLocaleID.value, __languageLocaleID.set, None, '\n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __languageID.name() : __languageID,
        __languageLocaleID.name() : __languageLocaleID
    })
_module_typeBindings.TextType = TextType
Namespace.addCategoryObject('typeBinding', 'TextType', TextType)

