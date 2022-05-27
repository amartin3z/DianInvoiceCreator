# ./_sac.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:bd794131cb7c2b1e52ff4e6220a49c5d8509c55c
# Generated 2020-05-26 15:40:38.330914 by PyXB version 1.2.6 using Python 3.7.5.final.0
# Namespace urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2 [xmlns:sac]

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
import _cbc as _ImportedBinding__cbc
import _sbc as _ImportedBinding__sbc

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ds = _ImportedBinding__ds.Namespace
_Namespace_ds.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cbc = _ImportedBinding__cbc.Namespace
_Namespace_cbc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_sbc = _ImportedBinding__sbc.Namespace
_Namespace_sbc.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2}SignatureInformationType with content type ELEMENT_ONLY
class SignatureInformationType (pyxb.binding.basis.complexTypeDefinition):
    """
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignatureInformationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureAggregateComponents-2.1.xsd', 17, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__urnoasisnamesspecificationublschemaxsdSignatureAggregateComponents_2_SignatureInformationType_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 12, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ID'), 'ID', '__urnoasisnamesspecificationublschemaxsdSignatureAggregateComponents_2_SignatureInformationType_urnoasisnamesspecificationublschemaxsdCommonBasicComponents_2ID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 327, 3), )

    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Element {urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2}ReferencedSignatureID uses Python identifier ReferencedSignatureID
    __ReferencedSignatureID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_sbc, 'ReferencedSignatureID'), 'ReferencedSignatureID', '__urnoasisnamesspecificationublschemaxsdSignatureAggregateComponents_2_SignatureInformationType_urnoasisnamesspecificationublschemaxsdSignatureBasicComponents_2ReferencedSignatureID', False, pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureBasicComponents-2.1.xsd', 6, 3), )

    
    ReferencedSignatureID = property(__ReferencedSignatureID.value, __ReferencedSignatureID.set, None, None)

    _ElementMap.update({
        __Signature.name() : __Signature,
        __ID.name() : __ID,
        __ReferencedSignatureID.name() : __ReferencedSignatureID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SignatureInformationType = SignatureInformationType
Namespace.addCategoryObject('typeBinding', 'SignatureInformationType', SignatureInformationType)


SignatureInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignatureInformation'), SignatureInformationType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureAggregateComponents-2.1.xsd', 14, 3))
Namespace.addCategoryObject('elementBinding', SignatureInformation.name().localName(), SignatureInformation)



SignatureInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding__ds.SignatureType, scope=SignatureInformationType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-xmldsig-core-schema-2.1.xsd', 12, 0)))

SignatureInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ID'), _ImportedBinding__cbc.IDType, scope=SignatureInformationType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonBasicComponents-2.1.xsd', 327, 3)))

SignatureInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_sbc, 'ReferencedSignatureID'), _ImportedBinding__sbc.ReferencedSignatureIDType, scope=SignatureInformationType, location=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureBasicComponents-2.1.xsd', 6, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureAggregateComponents-2.1.xsd', 29, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureAggregateComponents-2.1.xsd', 45, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureAggregateComponents-2.1.xsd', 61, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SignatureInformationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cbc, 'ID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureAggregateComponents-2.1.xsd', 29, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SignatureInformationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_sbc, 'ReferencedSignatureID')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureAggregateComponents-2.1.xsd', 45, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SignatureInformationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('/home/amartinez/MORROCO/xsd/Invoice/xsd_download/xsd/docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-SignatureAggregateComponents-2.1.xsd', 61, 9))
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
SignatureInformationType._Automaton = _BuildAutomaton()

