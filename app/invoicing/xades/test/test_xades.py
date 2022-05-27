import unittest
from datetime import datetime
from os import path
from copy import deepcopy

import xmlsig
from mock import patch
from OpenSSL import crypto
from xades import ObjectIdentifier, XAdESContext, template, utils
from xades.policy import GenericPolicyId, ImpliedPolicy
from lxml import etree
from pdb import set_trace
import tempfile
from io import StringIO, BytesIO, TextIOWrapper
import os
from OpenSSL import crypto
import xml.etree.cElementTree as ET

BASE_DIR = path.dirname(__file__)

def parse_xml(name):
    # return ET.fromstring(name)
    return etree.parse(path.join(BASE_DIR, name)).getroot()

class UrllibMock:
    def read(self):
        with open(path.join(BASE_DIR, "data/policy.pdf"), "rb") as f:
            result = f.read()
        return result


class TestXadesSignature(unittest.TestCase):
    def test_verify(self):
        root = parse_xml("data/sample.xml")
        sign = root.xpath("//ds:Signature", namespaces={"ds": xmlsig.constants.DSigNs})[
            0
        ]
        ctx = XAdESContext()
        with patch("xades.policy.urllib.urlopen") as mock:
            mock.return_value = UrllibMock()
            ctx.verify(sign)

    def test_sign(self):
        # root = parse_xml("data/unsigned-sample.xml")
        namespaces = deepcopy(root.nsmap)
        sign = root.xpath("//ds:Signature", namespaces={"ds": xmlsig.constants.DSigNs})[0]
        policy = GenericPolicyId(
            "http://www.facturae.es/politica_de_firma_formato_facturae/"
            "politica_de_firma_formato_facturae_v3_1.pdf",
            u"Politica de Firma FacturaE v3.1",
            xmlsig.constants.TransformSha1,
        )
        ctx = XAdESContext(policy)
        with open(path.join(BASE_DIR, "data/keyStore.p12"), "rb") as key_file:
            ctx.load_pkcs12(crypto.load_pkcs12(key_file.read()))
        with patch("xades.policy.urllib.urlopen") as mock:
            mock.return_value = UrllibMock()
            ctx.sign(sign)
            ctx.verify(sign)
        print(etree.tostring(sign))

    def test_create_2(self, xml, cer, key, _pass):
        try:
            tmp_xml = tempfile.NamedTemporaryFile(delete=False)
            tmp_xml.write(xml)
            tmp_xml.seek(0)
            root = parse_xml(tmp_xml.name)
            
            signature = xmlsig.template.create(
                xmlsig.constants.TransformInclC14N,
                xmlsig.constants.TransformRsaSha1,
                "Signature",
            )
            ref = xmlsig.template.add_reference(
                signature, xmlsig.constants.TransformSha1, uri="", name="R1"
            )
            xmlsig.template.add_transform(ref, xmlsig.constants.TransformEnveloped)
            xmlsig.template.add_reference(
                signature, xmlsig.constants.TransformSha1, uri="#KI", name="RKI"
            )
            ki = xmlsig.template.ensure_key_info(signature, name="KI")
            data = xmlsig.template.add_x509_data(ki)
            xmlsig.template.x509_data_add_certificate(data)
            serial = xmlsig.template.x509_data_add_issuer_serial(data)
            xmlsig.template.x509_issuer_serial_add_issuer_name(serial)
            xmlsig.template.x509_issuer_serial_add_serial_number(serial)
            xmlsig.template.add_key_value(ki)
            qualifying = template.create_qualifying_properties(signature)
            utils.ensure_id(qualifying)
            utils.ensure_id(qualifying)
            props = template.create_signed_properties(qualifying, datetime=datetime.now())
            template.add_claimed_role(props, "emisor")
            signed_do = template.ensure_signed_data_object_properties(props)
            
            root.append(signature)
            ctx = XAdESContext(ImpliedPolicy(xmlsig.constants.TransformSha1))
            
            tmp_p12_cer = tempfile.NamedTemporaryFile(delete=False)
            tmp_p12_cer.seek(0)

            tmp_cer = tempfile.NamedTemporaryFile(delete=False)
            tmp_cer.seek(0)

            tmp_key = tempfile.NamedTemporaryFile(delete=False)
            tmp_key.seek(0)

            # cer_pem = open("/var/unnamedpac/satfiles/EKU9003173C9/30001000000400002434.cer_YRoPmeE.pem", 'rb')
            # key_pem = open("/var/unnamedpac/satfiles/EKU9003173C9/30001000000400002434.key_a7NMPil.pem", 'rb')
            # cer_pem = open("/var/unnamedpac/satfiles/EKU9003173C9/IVD920810GU2.cer.pem", 'rb')
            # key_pem = open("/var/unnamedpac/satfiles/EKU9003173C9/IVD920810GU2.key.pem", 'rb')
# 
            cer_pem = open(cer, 'rb')
            key_pem = open(key, 'rb')
            command_pem_cer = b'openssl x509 -outform der -in %s -out %s' % (bytes(bytearray(cer_pem.name, encoding='utf-8')), bytes(bytearray(tmp_cer.name, encoding="utf-8")))
            os.system(command_pem_cer)
            
            # key_pass = "12345678a"
            # set_trace()
            key_pass = _pass
            command_p12_cer = b"openssl pkcs12 -export -out %s -inkey %s -in %s -passout pass:%s" % (bytes(bytearray(tmp_p12_cer.name, encoding='utf-8')), bytes(bytearray(key_pem.name, encoding="utf-8")), bytes(bytearray(cer_pem.name, encoding="utf-8")), key_pass.encode('utf-8'))
            os.system(command_p12_cer)

            key_file = open(path.join(BASE_DIR, "data/keyStore2.p12"), "rb")
            ctx.load_pkcs12(crypto.load_pkcs12(tmp_p12_cer.read(), key_pass))
            # set_trace()
            # ctx.load_pkcs12(crypto.load_pkcs12(key_file.read()))
            with patch("xades.policy.urllib.urlopen") as mock:
                mock.return_value = UrllibMock()
                # set_trace()
                try:
                    ctx.sign(signature)
                except:
                    pass

                # set_trace()
                # print(dir(ctx.x509))
                # ctx.verify(signature)
        except Exception as e:
            print(f"Exception in test_create_2 | {e}")
        return signature

test_sign = TestXadesSignature()
# signature = test_sign.test_create_2()
# print(etree.tostring(signature))
