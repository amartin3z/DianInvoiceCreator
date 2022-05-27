# -*- coding: UTF-8 -*-
from decimal import (
  Decimal, 
  ROUND_UP,
  ROUND_HALF_EVEN, 
)

def trunc(num, digits, r=False):
  if r:
    factor = ''  
    for n in range(digits-1):
      factor += '0'
    if r == 'EVEN':
      num = Decimal(str(num)).quantize(Decimal('.%s1' % factor), rounding=ROUND_HALF_EVEN)
    else:
      num = Decimal(str(num)).quantize(Decimal('.%s1' % factor), rounding=ROUND_UP)
  try:
    sp = str(num).split('.')
    if len(sp) > 1:
      return float('.'.join([sp[0], sp[1][:digits]]))
  except:
    sp = str(Decimal(num)).split('.')
    if len(sp) > 1:
      return float('.'.join([sp[0], sp[1][:digits]]))
  return float(num)