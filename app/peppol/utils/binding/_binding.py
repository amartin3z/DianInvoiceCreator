# ./_binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:883188f134433f2b45c3f67c1d97547fce4cacc0
# Generated 2020-05-26 15:40:38.330207 by PyXB version 1.2.6 using Python 3.7.5.final.0
# Namespace http://uri.etsi.org/01903/v1.4.1#

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
import _xades as _ImportedBinding__xades

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://uri.etsi.org/01903/v1.4.1#', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xades = _ImportedBinding__xades.Namespace
_Namespace_xades.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {http://uri.etsi.org/01903/v1.4.1#}ValidationDataType with content type ELEMENT_ONLY
class ValidationDataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/01903/v1.4.1#}ValidationDataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValidationDataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv141-2.1.xsd', 5, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uri.etsi.org/01903/v1.3.2#}CertificateValues uses Python identifier CertificateValues
    __CertificateValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_xades, 'CertificateValues'), 'CertificateValues', '__httpuri_etsi_org01903v1_4_1_ValidationDataType_httpuri_etsi_org01903v1_3_2CertificateValues', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 426, 1), )

    
    CertificateValues = property(__CertificateValues.value, __CertificateValues.set, None, None)

    
    # Element {http://uri.etsi.org/01903/v1.3.2#}RevocationValues uses Python identifier RevocationValues
    __RevocationValues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_xades, 'RevocationValues'), 'RevocationValues', '__httpuri_etsi_org01903v1_4_1_ValidationDataType_httpuri_etsi_org01903v1_3_2RevocationValues', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 436, 1), )

    
    RevocationValues = property(__RevocationValues.value, __RevocationValues.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpuri_etsi_org01903v1_4_1_ValidationDataType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv141-2.1.xsd', 10, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv141-2.1.xsd', 10, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Attribute UR uses Python identifier UR
    __UR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UR'), 'UR', '__httpuri_etsi_org01903v1_4_1_ValidationDataType_UR', pyxb.binding.datatypes.anyURI)
    __UR._DeclarationLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv141-2.1.xsd', 11, 2)
    __UR._UseLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv141-2.1.xsd', 11, 2)
    
    UR = property(__UR.value, __UR.set, None, None)

    _ElementMap.update({
        __CertificateValues.name() : __CertificateValues,
        __RevocationValues.name() : __RevocationValues
    })
    _AttributeMap.update({
        __Id.name() : __Id,
        __UR.name() : __UR
    })
_module_typeBindings.ValidationDataType = ValidationDataType
Namespace.addCategoryObject('typeBinding', 'ValidationDataType', ValidationDataType)


TimeStampValidationData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeStampValidationData'), ValidationDataType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv141-2.1.xsd', 4, 1))
Namespace.addCategoryObject('elementBinding', TimeStampValidationData.name().localName(), TimeStampValidationData)

ArchiveTimeStampV2 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ArchiveTimeStampV2'), _ImportedBinding__xades.XAdESTimeStampType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv141-2.1.xsd', 13, 1))
Namespace.addCategoryObject('elementBinding', ArchiveTimeStampV2.name().localName(), ArchiveTimeStampV2)



ValidationDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_xades, 'CertificateValues'), _ImportedBinding__xades.CertificateValuesType, scope=ValidationDataType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 426, 1)))

ValidationDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_xades, 'RevocationValues'), _ImportedBinding__xades.RevocationValuesType, scope=ValidationDataType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv132-2.1.xsd', 436, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv141-2.1.xsd', 7, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv141-2.1.xsd', 8, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ValidationDataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xades, 'CertificateValues')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv141-2.1.xsd', 7, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ValidationDataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xades, 'RevocationValues')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-XAdESv141-2.1.xsd', 8, 3))
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
ValidationDataType._Automaton = _BuildAutomaton()

