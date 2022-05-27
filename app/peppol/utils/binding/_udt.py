# ./_udt.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3b8316427b9d04ab971fa43e6eb74533d8e2824e
# Generated 2020-05-26 15:40:38.330524 by PyXB version 1.2.6 using Python 3.7.5.final.0
# Namespace urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2 [xmlns:udt]

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
from . import _ccts_cct as _ImportedBinding__ccts_cct

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2', create_if_missing=True)
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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 5, 2)
    _Documentation = None
STD_ANON._InitializeFacetMap()
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 37, 2)
    _Documentation = None
STD_ANON_._InitializeFacetMap()
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 69, 2)
    _Documentation = None
STD_ANON_2._InitializeFacetMap()
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 101, 2)
    _Documentation = None
STD_ANON_3._InitializeFacetMap()
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 133, 2)
    _Documentation = None
STD_ANON_4._InitializeFacetMap()
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 165, 2)
    _Documentation = None
STD_ANON_5._InitializeFacetMap()
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 302, 2)
    _Documentation = None
STD_ANON_6._InitializeFacetMap()
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}DateTimeType with content type SIMPLE
class DateTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
        
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.dateTime
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateTimeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 215, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.dateTime
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DateTimeType = DateTimeType
Namespace.addCategoryObject('typeBinding', 'DateTimeType', DateTimeType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}DateType with content type SIMPLE
class DateType (pyxb.binding.basis.complexTypeDefinition):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.date
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 233, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.date
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DateType = DateType
Namespace.addCategoryObject('typeBinding', 'DateType', DateType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}TimeType with content type SIMPLE
class TimeType (pyxb.binding.basis.complexTypeDefinition):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.time
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 250, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.time
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TimeType = TimeType
Namespace.addCategoryObject('typeBinding', 'TimeType', TimeType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}IndicatorType with content type SIMPLE
class IndicatorType (pyxb.binding.basis.complexTypeDefinition):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.boolean
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 285, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.boolean
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IndicatorType = IndicatorType
Namespace.addCategoryObject('typeBinding', 'IndicatorType', IndicatorType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}AmountType with content type SIMPLE
class AmountType (_ImportedBinding__ccts_cct.AmountType):
    """
        
        
        
        
        
        
      """
    _TypeDefinition = STD_ANON
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AmountType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 5, 2)
    _ElementMap = _ImportedBinding__ccts_cct.AmountType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.AmountType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.AmountType
    
    # Attribute currencyID is restricted from parent
    
    # Attribute currencyID uses Python identifier currencyID
    __currencyID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'currencyID'), 'currencyID', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_AmountType_currencyID', pyxb.binding.datatypes.normalizedString, required=True)
    __currencyID._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 18, 8)
    __currencyID._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 18, 8)
    
    currencyID = property(__currencyID.value, __currencyID.set, None, '\n                 \n                 \n                 \n                 \n                 \n                 \n                 \n                 \n                 \n              ')

    
    # Attribute currencyCodeListVersionID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}AmountType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __currencyID.name() : __currencyID
    })
_module_typeBindings.AmountType = AmountType
Namespace.addCategoryObject('typeBinding', 'AmountType', AmountType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}BinaryObjectType with content type SIMPLE
class BinaryObjectType (_ImportedBinding__ccts_cct.BinaryObjectType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = STD_ANON_
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinaryObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 37, 2)
    _ElementMap = _ImportedBinding__ccts_cct.BinaryObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.BinaryObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.BinaryObjectType
    
    # Attribute mimeCode is restricted from parent
    
    # Attribute mimeCode uses Python identifier mimeCode
    __mimeCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mimeCode'), 'mimeCode', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_BinaryObjectType_mimeCode', pyxb.binding.datatypes.normalizedString, required=True)
    __mimeCode._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 51, 8)
    __mimeCode._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 51, 8)
    
    mimeCode = property(__mimeCode.value, __mimeCode.set, None, '\n                 \n                 \n                 \n                 \n                 \n                 \n                 \n                 \n              ')

    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute encodingCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute characterSetCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute uri inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute filename inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __mimeCode.name() : __mimeCode
    })
_module_typeBindings.BinaryObjectType = BinaryObjectType
Namespace.addCategoryObject('typeBinding', 'BinaryObjectType', BinaryObjectType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}GraphicType with content type SIMPLE
class GraphicType (_ImportedBinding__ccts_cct.BinaryObjectType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = STD_ANON_2
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GraphicType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 69, 2)
    _ElementMap = _ImportedBinding__ccts_cct.BinaryObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.BinaryObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.BinaryObjectType
    
    # Attribute mimeCode is restricted from parent
    
    # Attribute mimeCode uses Python identifier mimeCode
    __mimeCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mimeCode'), 'mimeCode', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_BinaryObjectType_mimeCode', pyxb.binding.datatypes.normalizedString, required=True)
    __mimeCode._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 83, 8)
    __mimeCode._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 83, 8)
    
    mimeCode = property(__mimeCode.value, __mimeCode.set, None, '\n                 \n                 \n                 \n                 \n                 \n                 \n                 \n                 \n              ')

    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute encodingCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute characterSetCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute uri inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute filename inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __mimeCode.name() : __mimeCode
    })
_module_typeBindings.GraphicType = GraphicType
Namespace.addCategoryObject('typeBinding', 'GraphicType', GraphicType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}PictureType with content type SIMPLE
class PictureType (_ImportedBinding__ccts_cct.BinaryObjectType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = STD_ANON_3
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PictureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 101, 2)
    _ElementMap = _ImportedBinding__ccts_cct.BinaryObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.BinaryObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.BinaryObjectType
    
    # Attribute mimeCode is restricted from parent
    
    # Attribute mimeCode uses Python identifier mimeCode
    __mimeCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mimeCode'), 'mimeCode', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_BinaryObjectType_mimeCode', pyxb.binding.datatypes.normalizedString, required=True)
    __mimeCode._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 115, 8)
    __mimeCode._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 115, 8)
    
    mimeCode = property(__mimeCode.value, __mimeCode.set, None, '\n                 \n                 \n                 \n                 \n                 \n                 \n                 \n                 \n              ')

    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute encodingCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute characterSetCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute uri inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute filename inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __mimeCode.name() : __mimeCode
    })
_module_typeBindings.PictureType = PictureType
Namespace.addCategoryObject('typeBinding', 'PictureType', PictureType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}SoundType with content type SIMPLE
class SoundType (_ImportedBinding__ccts_cct.BinaryObjectType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = STD_ANON_4
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoundType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 133, 2)
    _ElementMap = _ImportedBinding__ccts_cct.BinaryObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.BinaryObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.BinaryObjectType
    
    # Attribute mimeCode is restricted from parent
    
    # Attribute mimeCode uses Python identifier mimeCode
    __mimeCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mimeCode'), 'mimeCode', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_BinaryObjectType_mimeCode', pyxb.binding.datatypes.normalizedString, required=True)
    __mimeCode._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 147, 8)
    __mimeCode._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 147, 8)
    
    mimeCode = property(__mimeCode.value, __mimeCode.set, None, '\n                 \n                 \n                 \n                 \n                 \n                 \n                 \n                 \n              ')

    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute encodingCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute characterSetCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute uri inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute filename inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __mimeCode.name() : __mimeCode
    })
_module_typeBindings.SoundType = SoundType
Namespace.addCategoryObject('typeBinding', 'SoundType', SoundType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}VideoType with content type SIMPLE
class VideoType (_ImportedBinding__ccts_cct.BinaryObjectType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = STD_ANON_5
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 165, 2)
    _ElementMap = _ImportedBinding__ccts_cct.BinaryObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.BinaryObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.BinaryObjectType
    
    # Attribute mimeCode is restricted from parent
    
    # Attribute mimeCode uses Python identifier mimeCode
    __mimeCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mimeCode'), 'mimeCode', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_BinaryObjectType_mimeCode', pyxb.binding.datatypes.normalizedString, required=True)
    __mimeCode._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 179, 8)
    __mimeCode._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 179, 8)
    
    mimeCode = property(__mimeCode.value, __mimeCode.set, None, '\n                 \n                 \n                 \n                 \n                 \n                 \n                 \n                 \n              ')

    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute encodingCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute characterSetCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute uri inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    
    # Attribute filename inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}BinaryObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __mimeCode.name() : __mimeCode
    })
_module_typeBindings.VideoType = VideoType
Namespace.addCategoryObject('typeBinding', 'VideoType', VideoType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}CodeType with content type SIMPLE
class CodeType (_ImportedBinding__ccts_cct.CodeType):
    """
        
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 197, 2)
    _ElementMap = _ImportedBinding__ccts_cct.CodeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.CodeType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.CodeType
    
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
_module_typeBindings.CodeType = CodeType
Namespace.addCategoryObject('typeBinding', 'CodeType', CodeType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}IdentifierType with content type SIMPLE
class IdentifierType (_ImportedBinding__ccts_cct.IdentifierType):
    """
        
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 267, 2)
    _ElementMap = _ImportedBinding__ccts_cct.IdentifierType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.IdentifierType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.IdentifierType
    
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
_module_typeBindings.IdentifierType = IdentifierType
Namespace.addCategoryObject('typeBinding', 'IdentifierType', IdentifierType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}MeasureType with content type SIMPLE
class MeasureType (_ImportedBinding__ccts_cct.MeasureType):
    """
        
        
        
        
        
        
        
        
      """
    _TypeDefinition = STD_ANON_6
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 302, 2)
    _ElementMap = _ImportedBinding__ccts_cct.MeasureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.MeasureType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.MeasureType
    
    # Attribute unitCode is restricted from parent
    
    # Attribute unitCode uses Python identifier unitCode
    __unitCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitCode'), 'unitCode', '__urnununeceuncefactdataspecificationCoreComponentTypeSchemaModule2_MeasureType_unitCode', pyxb.binding.datatypes.normalizedString, required=True)
    __unitCode._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 317, 8)
    __unitCode._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 317, 8)
    
    unitCode = property(__unitCode.value, __unitCode.set, None, '\n                 \n                 \n                 \n                 \n                 \n                 \n                 \n                 \n                 \n              ')

    
    # Attribute unitCodeListVersionID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}MeasureType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unitCode.name() : __unitCode
    })
_module_typeBindings.MeasureType = MeasureType
Namespace.addCategoryObject('typeBinding', 'MeasureType', MeasureType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}NumericType with content type SIMPLE
class NumericType (_ImportedBinding__ccts_cct.NumericType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NumericType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 336, 2)
    _ElementMap = _ImportedBinding__ccts_cct.NumericType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.NumericType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.NumericType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}NumericType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NumericType = NumericType
Namespace.addCategoryObject('typeBinding', 'NumericType', NumericType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}ValueType with content type SIMPLE
class ValueType (_ImportedBinding__ccts_cct.NumericType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 353, 2)
    _ElementMap = _ImportedBinding__ccts_cct.NumericType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.NumericType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.NumericType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}NumericType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ValueType = ValueType
Namespace.addCategoryObject('typeBinding', 'ValueType', ValueType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}PercentType with content type SIMPLE
class PercentType (_ImportedBinding__ccts_cct.NumericType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 370, 2)
    _ElementMap = _ImportedBinding__ccts_cct.NumericType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.NumericType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.NumericType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}NumericType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PercentType = PercentType
Namespace.addCategoryObject('typeBinding', 'PercentType', PercentType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}RateType with content type SIMPLE
class RateType (_ImportedBinding__ccts_cct.NumericType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 387, 2)
    _ElementMap = _ImportedBinding__ccts_cct.NumericType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.NumericType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.NumericType
    
    # Attribute format inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}NumericType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RateType = RateType
Namespace.addCategoryObject('typeBinding', 'RateType', RateType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}QuantityType with content type SIMPLE
class QuantityType (_ImportedBinding__ccts_cct.QuantityType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QuantityType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 404, 2)
    _ElementMap = _ImportedBinding__ccts_cct.QuantityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.QuantityType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.QuantityType
    
    # Attribute unitCode inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}QuantityType
    
    # Attribute unitCodeListID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}QuantityType
    
    # Attribute unitCodeListAgencyID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}QuantityType
    
    # Attribute unitCodeListAgencyName inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}QuantityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QuantityType = QuantityType
Namespace.addCategoryObject('typeBinding', 'QuantityType', QuantityType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}TextType with content type SIMPLE
class TextType (_ImportedBinding__ccts_cct.TextType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 421, 2)
    _ElementMap = _ImportedBinding__ccts_cct.TextType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.TextType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.TextType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    
    # Attribute languageLocaleID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TextType = TextType
Namespace.addCategoryObject('typeBinding', 'TextType', TextType)


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2}NameType with content type SIMPLE
class NameType (_ImportedBinding__ccts_cct.TextType):
    """
        
        
        
        
        
        
        
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-UnqualifiedDataTypes-2.1.xsd', 438, 2)
    _ElementMap = _ImportedBinding__ccts_cct.TextType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ccts_cct.TextType._AttributeMap.copy()
    # Base type is _ImportedBinding__ccts_cct.TextType
    
    # Attribute languageID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    
    # Attribute languageLocaleID inherited from {urn:un:unece:uncefact:data:specification:CoreComponentTypeSchemaModule:2}TextType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NameType = NameType
Namespace.addCategoryObject('typeBinding', 'NameType', NameType)

