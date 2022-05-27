# ./_sbc.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ac4e5de5bd937bf30fa93f2547fd2fe847e70896
# Generated 2020-05-26 15:40:38.330786 by PyXB version 1.2.6 using Python 3.7.5.final.0
# Namespace urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2 [xmlns:sbc]

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
import _udt as _ImportedBinding__udt
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2', create_if_missing=True)
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


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2}ReferencedSignatureIDType with content type SIMPLE
class ReferencedSignatureIDType (_ImportedBinding__udt.IdentifierType):
    """Complex type {urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2}ReferencedSignatureIDType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.normalizedString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferencedSignatureIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureBasicComponents-2.1.xsd', 9, 3)
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
_module_typeBindings.ReferencedSignatureIDType = ReferencedSignatureIDType
Namespace.addCategoryObject('typeBinding', 'ReferencedSignatureIDType', ReferencedSignatureIDType)


ReferencedSignatureID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferencedSignatureID'), ReferencedSignatureIDType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureBasicComponents-2.1.xsd', 6, 3))
Namespace.addCategoryObject('elementBinding', ReferencedSignatureID.name().localName(), ReferencedSignatureID)
