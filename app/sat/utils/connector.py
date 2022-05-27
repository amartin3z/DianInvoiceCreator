import pycurl
import uuid
from io import StringIO, BytesIO
from lxml import etree
import urllib
from django.core.cache import cache
from pdb import set_trace
from django.conf import settings
from datetime import datetime, timedelta
import hashlib
import base64
import re
from app.cfdi.utils.sign import Signer
from M2Crypto import RSA
from M2Crypto import X509


class SATConnector(object):

  def autenticar(self, tipo='R', forzar=False):

    token = cache.get(f'SAT_TOKEN_{tipo}', None)

    if forzar or token is None:

      if tipo == 'R':
        url = settings.SAT_AUTENTICA_URL_R
      elif tipo == 'C':
        url = settings.SAT_AUTENTICA_URL_C

      cabeceras = [
        'SOAPAction: http://tempuri.org/IAutenticacion/Autentica',
        'Content-Type: text/xml; charset=utf-8',
      ]

      _uuid = 'uuid-{}-1'.format(uuid.uuid4())
      binary = settings.SAT_CERT_STR.replace('\n','')
      created = datetime.utcnow().isoformat()[:-3]+'Z'
      expires = (datetime.utcnow()+timedelta(seconds=300)).isoformat()[:-3]+'Z'
      c14n_timestamp = f'<u:Timestamp xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" u:Id="_0"><u:Created>{created}</u:Created><u:Expires>{expires}</u:Expires></u:Timestamp>'      
      digest = base64.encodestring(hashlib.sha1(c14n_timestamp.encode()).digest()).strip().decode()
      c14n_signed_info = f'<SignedInfo xmlns="http://www.w3.org/2000/09/xmldsig#"><CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"></CanonicalizationMethod><SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"></SignatureMethod><Reference URI="#_0"><Transforms><Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"></Transform></Transforms><DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"></DigestMethod><DigestValue>{digest}</DigestValue></Reference></SignedInfo>'            
      signer_obj = Signer()
      result = signer_obj.sign(data=c14n_signed_info, mechanism='sha1')
      if result['success']:
        signature = result['message']
      else:
        return None

      peticion = f"""<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"><s:Header><o:Security s:mustUnderstand="1" xmlns:o="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"><u:Timestamp u:Id="_0"><u:Created>{created}</u:Created><u:Expires>{expires}</u:Expires></u:Timestamp><o:BinarySecurityToken u:Id="{_uuid}" ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">{binary}</o:BinarySecurityToken><Signature xmlns="http://www.w3.org/2000/09/xmldsig#"><SignedInfo><CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/><SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/><Reference URI="#_0"><Transforms><Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/></Transforms><DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/><DigestValue>{digest}</DigestValue></Reference></SignedInfo><SignatureValue>{signature}</SignatureValue><KeyInfo><o:SecurityTokenReference><o:Reference ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" URI="#{_uuid}"/></o:SecurityTokenReference></KeyInfo></Signature></o:Security></s:Header><s:Body><Autentica xmlns="http://tempuri.org/"/></s:Body></s:Envelope>"""

      b = BytesIO()
      r = BytesIO()
      c = pycurl.Curl()
      c.setopt(pycurl.URL, url)
      c.setopt(pycurl.POST, 1)
      c.setopt(pycurl.SSL_VERIFYPEER, 0)
      c.setopt(pycurl.SSL_VERIFYHOST, 0)
      if settings.LOCALDEV:
          c.setopt(pycurl.VERBOSE, 1)
      c.setopt(pycurl.HTTPHEADER, cabeceras)
      c.setopt(pycurl.POSTFIELDS, peticion)
      c.setopt(pycurl.WRITEFUNCTION, b.write)
      c.setopt(pycurl.HEADERFUNCTION, r.write)
      c.setopt(pycurl.TIMEOUT, 45)
      c.setopt(pycurl.CONNECTTIMEOUT, 10)
      c.perform()

      response = b.getvalue()
      response_headers = r.getvalue()

      et = etree.fromstring(response)
      autentica_result = et.xpath('//tmp:AutenticaResult', namespaces={'tmp':'http://tempuri.org/'})[0]
      token = autentica_result.text
      token = urllib.parse.unquote(token)
      cache.set(f'SAT_TOKEN_{tipo}', token, 420)    

    return token



  def subir_blob(self, nombre, xml):
    cfdi = BytesIO(xml.encode())
    url = settings.SAT_BLOB_URL.format(filename=nombre)
    cabeceras = [
      'x-ms-version: 2011-08-18',
      'User-Agent: WA-Storage/1.6.0',
      'x-ms-blob-type: BlockBlob',
      f'x-ms-meta-versionCFDI: {settings.CFDI_VERSION}',
      f'Host: {settings.SAT_BLOB_HOST}',
    ]

    b = BytesIO()
    r = BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.UPLOAD, 1)
    c.setopt(pycurl.READDATA, cfdi)
    c.setopt(pycurl.INFILESIZE, len(cfdi.getvalue()))
    # if settings.LOCALDEV:
    #     c.setopt(pycurl.VERBOSE, 1)
    c.setopt(pycurl.HTTPHEADER, cabeceras)
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.setopt(pycurl.HEADERFUNCTION, r.write)
    c.setopt(pycurl.TIMEOUT, 45)
    c.setopt(pycurl.CONNECTTIMEOUT, 10)
    c.perform()

    response = b.getvalue()
    response_headers = r.getvalue()  

    ##### TODO ######
    ### validar response y response_headers ????

    created = False
    http_code = c.getinfo(pycurl.HTTP_CODE)
    if http_code == 201:
        created = True

    return created


  def enviar(self, metadatos, xml, forzar=False):
    #set_trace()
    nombre = metadatos['uuid']+'.xml'
    metadatos['ruta'] = settings.SAT_BLOB_PATH.format(filename=nombre)

    token = self.autenticar(tipo='R', forzar=forzar)
    if token is None:
      raise Exception('Token de Recepcion Invalido')

    created = self.subir_blob(nombre, xml)
    if not created:
      raise Exception('Error al Subir al Blob')

    cabeceras = [
        "SOAPAction: http://recibecfdi.sat.gob.mx/IRecibeCFDIService/Recibe",
        'Content-Type: text/xml; charset=utf-8',
        f'Authorization: WRAP access_token="{token}"'
    ]

    peticion = '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Header><h:EncabezadoCFDI xmlns:h="http://recibecfdi.sat.gob.mx" xmlns="http://recibecfdi.sat.gob.mx" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><RfcEmisor>{rfc}</RfcEmisor><UUID>{uuid}</UUID><Fecha>{fecha}</Fecha><NumeroCertificado>{no_certificado}</NumeroCertificado><VersionComprobante>{version}</VersionComprobante></h:EncabezadoCFDI></s:Header><s:Body xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><CFDI xmlns="http://recibecfdi.sat.gob.mx"><RutaCFDI>{ruta}</RutaCFDI></CFDI></s:Body></s:Envelope>'.format(**metadatos)

    b = BytesIO()
    r = BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, settings.SAT_RECIBE_URL)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    # if settings.LOCALDEV:
    #   c.setopt(pycurl.VERBOSE, 1)        
    c.setopt(pycurl.HTTPHEADER, cabeceras)
    c.setopt(pycurl.POSTFIELDS, peticion.encode())
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.setopt(pycurl.HEADERFUNCTION, r.write)
    c.setopt(pycurl.TIMEOUT, 45)
    c.setopt(pycurl.CONNECTTIMEOUT, 10)
    c.perform()

    recibe_response = b.getvalue()
    response_headers = r.getvalue()

    namespaces = {'namespaces': {'tmp':'http://recibecfdi.sat.gob.mx'}}
    response_obj = etree.fromstring(recibe_response)
    acuse_recepcion_cfdi = response_obj.xpath('//tmp:AcuseRecepcionCFDI', **namespaces)[0]
    acuse_recepcion_cfdi_keys = acuse_recepcion_cfdi.keys()
    acuse_recepcion_cfdi_values = acuse_recepcion_cfdi.values()
    acuse_recepcion_dict = dict(zip(acuse_recepcion_cfdi_keys, acuse_recepcion_cfdi_values))
    incidencias = response_obj.xpath('//tmp:Incidencia', **namespaces)
    incidencias_list = []
    for incidencia in incidencias:
        incidencia_dict = {}
        incidencia_dict['MensajeIncidencia'] = incidencia.xpath('string(tmp:MensajeIncidencia)', **namespaces)
        incidencia_dict['CodigoError'] = incidencia.xpath('string(tmp:CodigoError)', **namespaces)        
        incidencias_list.append(incidencia_dict)

    if settings.LOCALDEV:
        print(acuse_recepcion_dict)
        print(incidencias_list)

    return acuse_recepcion_dict, incidencias_list, recibe_response


  def cancelar(self, uuids, rfc, cer, key, passwd=None, tipo='PEM', forzar=False):
      
    if not rfc.find("&amp;") > 0:
        rfc = rfc.replace("&", "&amp;")

    fecha = datetime.now().isoformat()[:19]
    folio_tmpl = '<Folios><UUID>%s</UUID></Folios>'
    folios = ''
    for uuid in uuids:
      folios += folio_tmpl % uuid.upper()

    c14n_cancelacion = f'<Cancelacion xmlns="http://cancelacfd.sat.gob.mx" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" Fecha="{fecha}" RfcEmisor="{rfc}">{folios}</Cancelacion>'
    digest = base64.encodestring(hashlib.sha1(c14n_cancelacion.encode()).digest()).strip().decode()
    c14n_signed_info = f'<SignedInfo xmlns="http://www.w3.org/2000/09/xmldsig#" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"></CanonicalizationMethod><SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"></SignatureMethod><Reference URI=""><Transforms><Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"></Transform></Transforms><DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"></DigestMethod><DigestValue>{digest}</DigestValue></Reference></SignedInfo>'
    signed_info_digest_value = hashlib.sha1(c14n_signed_info.encode()).digest().strip()
    
    pri_key = RSA.load_key_string(key, callback=lambda a, pw=str(passwd): pw)
    if tipo == 'PEM':
      x509_cert = X509.load_cert_string(cer, X509.FORMAT_PEM)         
    elif tipoe == 'DER':
      x509_cert = X509.load_cert_string(cer, X509.FORMAT_DER)

    signature_value = pri_key.sign(signed_info_digest_value)
    x509_cert_pat = re.compile('-----BEGIN CERTIFICATE-----\n?(.*?)\n?-----END CERTIFICATE-----', re.S)
    certificate = x509_cert_pat.findall(x509_cert.as_pem().decode())[0].replace('\n', '')
    signature = base64.encodestring(signature_value).strip().decode().replace('\n', '')
    issuer = x509_cert.get_issuer().as_text()
    serial =x509_cert.get_serial_number()
  
    cancela_signed_txt = f'<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><CancelaCFD xmlns="http://cancelacfd.sat.gob.mx"><Cancelacion RfcEmisor="{rfc}" Fecha="{fecha}">{folios}<Signature xmlns="http://www.w3.org/2000/09/xmldsig#"><SignedInfo><CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/><SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/><Reference URI=""><Transforms><Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/></Transforms><DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/><DigestValue>{digest}</DigestValue></Reference></SignedInfo><SignatureValue>{signature}</SignatureValue><KeyInfo><X509Data><X509IssuerSerial><X509IssuerName>{issuer}</X509IssuerName><X509SerialNumber>{serial}</X509SerialNumber></X509IssuerSerial><X509Certificate>{certificate}</X509Certificate></X509Data></KeyInfo></Signature></Cancelacion></CancelaCFD></s:Body></s:Envelope>'
    
    token = self.autenticar(tipo='C', forzar=forzar)
    if token is None:
      raise Exception('Token de Cancelacion Invalido')

    cabeceras = [
        "SOAPAction: http://cancelacfd.sat.gob.mx/ICancelaCFDBinding/CancelaCFD",
        'Content-Type: text/xml; charset=utf-8',
        f'Authorization: WRAP access_token="{token}"'
    ]

    b = BytesIO()
    r = BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, settings.SAT_CANCELA_URL)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    if settings.LOCALDEV:
        c.setopt(pycurl.VERBOSE, 1)
    c.setopt(pycurl.HTTPHEADER, cabeceras)
    c.setopt(pycurl.POSTFIELDS, cancela_signed_txt.encode())
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.setopt(pycurl.HEADERFUNCTION, r.write)
    c.setopt(pycurl.TIMEOUT, 45)
    c.setopt(pycurl.CONNECTTIMEOUT, 10)
    c.perform()

    cancela_response = b.getvalue()
    response_headers = r.getvalue()

    faultcode = ''
    faultstring = ''
    cancela_cfd_dict = {}
    folios_list = []

    response_obj = etree.fromstring(cancela_response)
    namespaces = {'namespaces': {'tmp':'http://cancelacfd.sat.gob.mx'}}

    cancela_cfd = response_obj.xpath('//tmp:CancelaCFDResult', **namespaces)
    if cancela_cfd:
      cancela_cfd = cancela_cfd[0]
      cancela_cfd_keys = cancela_cfd.keys()
      cancela_cfd_values = cancela_cfd.values()
      cancela_cfd_dict = dict(zip(cancela_cfd_keys, cancela_cfd_values))        
      folios = cancela_cfd.xpath('tmp:Folios', **namespaces)
      for folio  in folios:
        uuid_obj = folio.xpath('string(tmp:UUID)', **namespaces)
        estatus_uuid_obj = folio.xpath('string(tmp:EstatusUUID)', **namespaces)
        folios_list.append({'UUID': uuid_obj, 'EstatusUUID': estatus_uuid_obj})
    else:
      faultcode = response_obj.xpath('//faultcode')[0].text
      faultstring = response_obj.xpath('//faultstring')[0].text    

    if settings.LOCALDEV:
      print(cancela_cfd_dict)
      print(folios_list)
      print(cancela_response)

    return cancela_cfd_dict, folios_list, cancela_response, faultcode, faultstring


  def consultar(self, rre, rr, tt, uuid, timeout=True):

    rre = rre.upper()
    rr = rr.upper()
    tt = "%0.6f" % float(tt)
    uuid = uuid.upper()

    if not rre.find("&amp;") > 0:
      rre = rre.replace("&", "&amp;")
    if not rr.find("&amp;") > 0:
      rr = rr.replace("&", "&amp;")

    #rre = rre.replace('Ñ', '&#209;')
    #rr = rr.replace('Ñ', '&#209;')

    while len(tt) < 17:
      tt = '0%s' % tt

    data = f"""<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
      <s:Body>
        <tem:Consulta>
          <tem:expresionImpresa>?re={rre}&amp;rr={rr}&amp;tt={tt}&amp;id={uuid}</tem:expresionImpresa>
        </tem:Consulta>
      </s:Body>
    </s:Envelope>"""

    headers = [
      'Host: consultaqr.facturaelectronica.sat.gob.mx',
      #'POST: https://consultaqr.facturaelectronica.sat.gob.mx/ConsultaCFDIService.svc HTTP/1.1',
      #'POST: https://srvconsultacfdiuat.cloudapp.net/ConsultaCFDIService.svc HTTP/1.1',
      'POST: https://pruebacfdiconsultaqr.cloudapp.net/ConsultaCFDIService.svc HTTP/1.1',
      'SOAPAction: http://tempuri.org/IConsultaCFDIService/Consulta',
      'Content-Type: text/xml; charset=utf-8',
      'Connection: keep-Alive'
    ]

    b = BytesIO()
    r = BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, settings.SAT_CONSULTA_URL)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    if settings.LOCALDEV:
        c.setopt(pycurl.VERBOSE, 1)
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(pycurl.POSTFIELDS, data.encode())
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.setopt(pycurl.HEADERFUNCTION, r.write)
    c.setopt(pycurl.TIMEOUT, 45)
    c.setopt(pycurl.CONNECTTIMEOUT, 10) 
    c.perform()

    consulta_response = b.getvalue()
    response_headers = r.getvalue()

    consulta_dict = {}
    namespaces = {'namespaces': {'a': 'http://schemas.datacontract.org/2004/07/Sat.Cfdi.Negocio.ConsultaCfdi.Servicio', 'tmp': 'http://tempuri.org/'}}
    response_obj = etree.fromstring(consulta_response)
    try:
      consulta = response_obj.xpath('//tmp:ConsultaResult', **namespaces)[0]
      codigo_estatus = consulta.xpath('string(//a:CodigoEstatus)', **namespaces)
      estado = consulta.xpath('string(//a:Estado)', **namespaces)
      es_cancelable = consulta.xpath('string(//a:EsCancelable)', **namespaces)
      estatus_cancelacion = consulta.xpath('string(//a:EstatusCancelacion)', **namespaces)
      consulta_dict = {'success': True, 'codigo_estatus': codigo_estatus, 'estado': estado, 'es_cancelable': es_cancelable, 'estatus_cancelacion': estatus_cancelacion}
    except Exception as e:
      print(f"Exception connector consultar => {e}")      

    if settings.LOCALDEV:
      print(consulta_dict)

    return consulta_dict