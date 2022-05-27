# ./_binding_.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:96626a27fd68cdb8d894ac246dd093c230124d50
# Generated 2020-05-26 15:40:38.331043 by PyXB version 1.2.6 using Python 3.7.5.final.0
# Namespace urn:oasis:names:specification:ubl:schema:xsd:CommonSignatureComponents-2

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
import _sac as _ImportedBinding__sac

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:oasis:names:specification:ubl:schema:xsd:CommonSignatureComponents-2', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_sac = _ImportedBinding__sac.Namespace
_Namespace_sac.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:CommonSignatureComponents-2}UBLDocumentSignaturesType with content type ELEMENT_ONLY
class UBLDocumentSignaturesType (pyxb.binding.basis.complexTypeDefinition):
    """
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UBLDocumentSignaturesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonSignatureComponents-2.1.xsd', 8, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2}SignatureInformation uses Python identifier SignatureInformation
    __SignatureInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_sac, 'SignatureInformation'), 'SignatureInformation', '__urnoasisnamesspecificationublschemaxsdCommonSignatureComponents_2_UBLDocumentSignaturesType_urnoasisnamesspecificationublschemaxsdSignatureAggregateComponents_2SignatureInformation', True, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureAggregateComponents-2.1.xsd', 14, 3), )

    
    SignatureInformation = property(__SignatureInformation.value, __SignatureInformation.set, None, None)

    _ElementMap.update({
        __SignatureInformation.name() : __SignatureInformation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UBLDocumentSignaturesType = UBLDocumentSignaturesType
Namespace.addCategoryObject('typeBinding', 'UBLDocumentSignaturesType', UBLDocumentSignaturesType)


UBLDocumentSignatures = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UBLDocumentSignatures'), UBLDocumentSignaturesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonSignatureComponents-2.1.xsd', 5, 3))
Namespace.addCategoryObject('elementBinding', UBLDocumentSignatures.name().localName(), UBLDocumentSignatures)



UBLDocumentSignaturesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_sac, 'SignatureInformation'), _ImportedBinding__sac.SignatureInformationType, scope=UBLDocumentSignaturesType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureAggregateComponents-2.1.xsd', 14, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UBLDocumentSignaturesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sac, 'SignatureInformation')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonSignatureComponents-2.1.xsd', 20, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UBLDocumentSignaturesType._Automaton = _BuildAutomaton()

