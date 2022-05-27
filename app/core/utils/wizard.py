# -*- encoding: UTF-8 -*-
from datetime import date
from django.db.models import Q
from django.conf import settings
from django.utils.translation import ugettext as _

from app.core.models import Business
from app.sat.models.cfdi import RegimenFiscal, CodigoPostal

import re
from pdb import set_trace

TAXPAYER_ID_REGEX = r'^[A-Z&Ñ]{3,4}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A]$';

def validate_taxpayer_id(taxpayer_id):
  success = True
  message = _('Taxpayer id is valid.')
  try:
    taxpayer_id_compiled = re.compile(TAXPAYER_ID_REGEX)
    if taxpayer_id_compiled.match(taxpayer_id) is None:
      success = False
      message = _("Taxpayer id does not match with the pattern.")
    if Business.objects.filter(taxpayer_id=taxpayer_id).exists():
      success = False
      message = _('Taxpayer id was register previously.')
    #taxpayer_lco = validate_lco
    # if success and not taxpayer_lco:
    #     success = False
    #     message = 'El RFC no se encuentra en la LCO.'
  except Exception as e:
    print(f'Exception on validate_taxpayer_id {e}')
    success = False
    message = _('An error occurred while validating the taxpayer id.')
  return success, message

def validate_taxregime(clave):
  #set_trace()
  success = True
  message = _('The tax regime is valid.')
  try:
    assert RegimenFiscal.validar(clave), _('The tax regime {} was not found in the SAT catalog.'.format(clave))
    print (clave)
  except Exception as e:
    print(f'Exception on validate_taxregime {e}')
    success = False
    message = _('An error occurred while validating tax regime')
  return success, message


def validate_cp(clave, date=date.today()):
  success = True
  message = _('Zip code is valid.')
  try:
    assert CodigoPostal.validar(clave=clave), _('Zip code {} was not found in the SAT catalog.'.format(clave))
  except Exception as e:
    print(f'Exception on validate_cp {e}')
    success = False
    message = _('An error occurred while validation Zip code')
  return success, message


def validate_wizard(tax_regime, taxpayer_id, cp):
  is_valid, message = validate_taxpayer_id(taxpayer_id)
  if is_valid:
    is_valid, message = validate_taxregime(tax_regime)
  if is_valid:
    is_valid, message = validate_cp(cp)
  return is_valid, message


        





