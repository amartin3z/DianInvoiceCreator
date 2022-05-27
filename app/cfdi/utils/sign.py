from django.conf import settings
import PyKCS11
import base64
from M2Crypto import RSA
import hashlib
from pdb import set_trace


class HSM:

  PKCS11_LIB = PyKCS11.PyKCS11Lib()
  
  def __init__(self):

    try:        
      self.PKCS11_LIB.load(settings.HSM_PKCS11_LIB)
      self.KEY_LABEL = settings.HSM_KEY_LABEL
      self.SLOT_ID = int(settins.HSM_SLOT_ID)
      self.PIN = settings.HSM_PIN
      self.SLOTS = PKCS11_LIB.getSlotList()
      self.SLOT = self.SLOTS[self.SLOTS.index(self.SLOT_ID)]
      self.HSM_MECHANISM = {
        'sha1': PyKCS11.Mechanism(PyKCS11.CKM_SHA1_RSA_PKCS, None),
        'sha256': PyKCS11.Mechanism(PyKCS11.CKM_SHA256_RSA_PKCS, None),
      }       
    except Exception as e:
      print("Exception HSM slot => " + str(e))

    try:
      self.hsm_session = self.PKCS11_LIB.openSession(self.SLOT)
      self.hsm_session.login(pin=self.PIN)
      self.hsm_key_object = self.hsm_session.findObjects([(PyKCS11.CKA_LABEL, self.KEY_LABEL),])
      self.hsm_key_object = self.hsm_key_object[0]
    except Exception as e:
      print("Exception HSM login => " + str(e))

    
  def sign(self, data, mechanism='sha1'):
    
    success = False
    signed = None
    try:
      if mechanism not in self.HSM_MECHANISM.keys():
        raise Exception('Mecanismo No Soportado')
      signed = self.hsm_session.sign(self.hsm_key_object, data, self.HSM_MECHANISM[mechanism])
      signed = ''.join(map(chr, signed))
      signed = base64.b64encode(signed)
      success = True
    except Exception as e:
      signed = "Exception HSM sign => " + str(e)

    return {'success': success, 'message': signed}



class HSM_LOCAL:

  def __init__(self):

    self.rsa = RSA.load_key_string(settings.SAT_PAC_KEY)

  def sign(self, data, mechanism):
    
    success = False
    signed = None
    try:
      assert len(self.rsa) in (1024, 2048)
      assert mechanism in ('sha1', 'sha256')
      assert self.rsa.e == b'\000\000\000\003\001\000\001'
      if mechanism == 'sha1':
        md5_digest = hashlib.sha1(data.encode()).digest()
      elif mechanism == 'sha256':
        md5_digest = hashlib.sha256(data.encode()).digest()
      rsa_signature = self.rsa.sign(md5_digest, mechanism)
      signed = base64.b64encode(rsa_signature)
      signed = signed.decode()
      signed.replace('\n','')
      success = True
    except Exception as e:
      signed = "Exception sign => {}".format(str(e))

    return {'success': success, 'message': signed}



class Signer:

  def __init__(self):

    self.hsm_obj = None

    if settings.HSM_TYPE == 'hardware':
      self.hsm_obj = HSM()
    elif settings.HSM_TYPE == 'software':
      self.hsm_obj = HSM_LOCAL()

  def sign(self, data, mechanism):

    return self.hsm_obj.sign(data, mechanism)