# -*- coding: UTF-8 -*-

from django import forms
from django.forms import widgets
from django.forms import fields
from django.utils.translation import ugettext_lazy as _


from app.core.catalogs import (
	PAYMENT_METHOD, 
	PAYMENT_WAY,
	CURRENCIES,
  USE_CFDI,
)

from app.sat.models import MetodoPago, FormaPago, Moneda, UsoCFDI, TipoDeComprobante, Pais, CodigoPostal
from app.peppol.models import UNCL1001INV, ISO4217, ISO3166, UNCL4461
from app.invoicing.models import InvoicingSerial

import pickle
from datetime import date, datetime
from django.db.models import Q
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, MultiField, Field, Row, MultiWidgetField, Column


class InvoiceForm(forms.Form):
  # Comprobante Fields
  id_invoice = forms.CharField(
    label = _('ID'),
    widget = forms.TextInput(
      attrs = {
        'readonly': "readonly",
      }
    ),
  )

  type_invoice = forms.ModelChoiceField(
    queryset = UNCL1001INV.objects.all(),
    label = _('Invoice Type'),
    widget = forms.Select(),
    to_field_name='code',
    initial='380'
   # choices=PAYMENT_WAY,
  )

  # payment_method = forms.ChoiceField(
  #payment_method = forms.ModelChoiceField(
  #  queryset = MetodoPago.objects.all(),
  #  label = 'Método de Pago',
  #  widget = forms.Select(),
  #  to_field_name='clave',
  #  initial='PUE'
  #  # choices=PAYMENT_METHOD
  #)
  # payment_way = forms.ChoiceField(
  #payment_way = forms.ModelChoiceField(
  #  queryset = FormaPago.objects.all(),
  #	label = 'Forma de Pago',
  #	widget = forms.Select(),
  #  to_field_name='clave',
  #  initial='01'
  #	# choices=PAYMENT_WAY,
  #)
  # payment_date = forms.DateField(
  # 	label='Fecha de Pago',
  # 	initial=date.today
  # )
  #confirmation = forms.CharField(
  #	label='Confirmación',
  #  widget=widgets.TextInput(
  #    attrs = {
  #      'disabled': "disabled",
  #    }
  #  )
  #)
  #expedition_place = forms.ChoiceField(
  #	label='Lugar Expedición',
  #  widget=forms.Select(),
  #)
  #currency = forms.FloatField(
  #  label = 'Tipo Cambio',
  #  widget=widgets.NumberInput(
  #    attrs={
  #      'value': 1,
  #      'readonly': 'readonly'
  #    }
  #  )
  #)
  #select = forms.ChoiceField(
  select = forms.ModelChoiceField(
    queryset=ISO4217.objects.all(),    
    label= _('Currency'),
    widget=forms.Select(),
    to_field_name='code',
    initial='MAD',
    #choices=(
    #  ('MXN', 'MXN - Peso Mexicano'),('XXX', 'XXX - Sin moneda'),
    #)
    #choices=CURRENCIES,
    #to_field_name='clave',
    #initial='MXN'
    # required=False,
  )

  payment_name = forms.ChoiceField(
    label=_('Way to pay'),
    #queryset = Moneda.objects.all().exclude(clave = 'XXX'),
    widget=forms.Select(
      attrs={
        'id': 'payment_name_select',
      }
    ),
    #to_field_name='clave',
    # initial='30',
    # choices=(
    #   ('30', '30 - Credit transfer'),
    # )
  )
  #accounting_cost_invoice = forms.CharField(
  #  label = _('Accounting Cost'),
  #  widget = forms.TextInput(),
  #)
 
  #buyer_reference_invoice = forms.CharField(
  #  label = _('Buyer Reference'),
  #  widget = forms.TextInput(),
  #)

  #serial = forms.ChoiceField(
  #  label='Serie',
  #  widget=forms.Select(),
  #  required=False,
  #  # choices=CURRENCIES,
  #)
  #folio = forms.CharField(
  #  label='Folio',
  #  widget=forms.TextInput(attrs={
  #    'pattern': '[^|]{1,1000}',
  #  }),
  #  required=False,
  #  # choices=CURRENCIES,
  #)
  #type_invoice =  forms.ModelChoiceField(
  #  queryset = TipoDeComprobante.objects.exclude(clave__in=('N', 'T')),
  #  label = 'Tipo de Comprobante',
  #  widget = forms.Select(),
  #  to_field_name='clave',
  #  initial='I'
  #  # choices=CURRENCIES,
  #  # required=False,
  #)
  # payment_conditions = forms.CharField(
  #   label='Condiciones de pago',
  #   widget=widgets.Textarea(
  #     attrs={
  #       'rows': 5,
  #     }
  #   )
  # )
  # Receptor Fields
  rtaxpayer = forms.ChoiceField(
    label= _('Tax Identifier Number'),
    widget=forms.Select(),
    required=True,
    # choices=CURRENCIES,
  )
  #rtaxpayer = forms.ChoiceField(
  #  label='Rfc',
  #  widget=forms.Select(),
  #  required=True,
  #  # choices=CURRENCIES,
  #)
  # use_cfdi = forms.ChoiceField(
  # use_cfdi = forms.ChoiceField(
  #use_cfdi = forms.ModelChoiceField(
  #  queryset=UsoCFDI.objects.all(),
  #  label='Uso cfdi',
  #  widget=forms.Select(),
  #  to_field_name='clave',
  #  initial='G03',
  #  # choices=USE_CFDI
  #)
  # business_name = forms.CharField(
  #   label = 'Razon social'
  # )
  fiscal_address = forms.ModelChoiceField(
    queryset=ISO3166.objects.all(),
    label= _('Country'),
    widget=forms.Select(
      #attrs={
      #  'disabled': 'disabled'
      #}
    ),
    to_field_name='code',
    initial='MA',
    # choices=USE_CFDI
  )

  ##----------------DESCOMENTAR?
  #####id_company = forms.CharField(
  #####  label = _('CompanyID'),
  #####  widget = forms.TextInput(),
  #####)
  #rit = forms.CharField(
  #  label = 'Número de registro Tributario',
  #  widget=widgets.TextInput(
  #    attrs = {
  #      'maxlength': 40,
  #      'disabled': 'disabled'
  #    }
  #  )
  #)
  # name = forms.CharField(
  #   label = 'Nombre'
  # )
  # last_name = forms.CharField(
  #   label = 'Apellido Paterno'
  # )
  # second_last_name = forms.CharField(
  #   label = 'Apellido Materno'
  # )
  # emails = forms.CharField(
  #   label = u'Correo electrónico',
  #   widget=widgets.TextInput(
  #     attrs = {
  #       'data-role': 'tagsinput',
  #     }
  #   )
  # )
  # Concepto Fields
  description = forms.CharField(
    label= _('Descripcion'),
    widget=widgets.Textarea(
      attrs={
        'rows': 5,
        'col': 5,
        'id': 'description_0',
      }
    )
  )
  quantity = forms.FloatField(
    label= _('InvoicedQuantity'),
    min_value=1.0,
    widget=widgets.NumberInput(
      attrs={
        'id': 'quantity_0',
        'value': 1.0,
        'pattern': r'^[0-9]*\.?[0-9]+$',
        'class': 'amounts',
      }
    )
  )
  unit_price = forms.FloatField(
    label= _('Price'),
    min_value=1.0,
    widget=widgets.NumberInput(
      attrs={
        'id': 'unit_price_0',
        'value': 0.0,
        'pattern': r'^[0-9]*\.?[0-9]+$',
        'class': 'amounts',
      }
    )
  )
  amount = forms.FloatField(
    label= _('Price Amount'),
    #disabled=True,
    widget=widgets.NumberInput(
      attrs={
        'id': 'amount_0',
        'pattern': r'^[0-9]*\.?[0-9]+$',
        'class': 'amounts',
        'value': 0.0,
        'readonly': 'readonly',
      }
    ),
    required=False,
  )
  identifier = forms.CharField(
    label= _('ID'),
    widget=forms.Select(
      attrs={
        'id': 'identifier_0',
      }
    ),
    required=True,
  )
  key_unit = forms.CharField(
    label= _('Unit Code'),
    widget=widgets.Input(
      attrs={
        'id': 'key_unit_0',
        'readonly': 'readonly',
      }
    )
  )
  unit = forms.CharField(
    label= _('Unit'),
  )
  prodservice = forms.CharField(
    label= _('Classification Code'),
    widget=widgets.Input(
      attrs={
        'id': 'prodservice_0',
        'disabled': 'disabled'
      }
    )
  )
  discount = forms.FloatField(
    label= _('Discount'),
    widget=widgets.NumberInput(
      attrs={
        'id': 'discount_0',
        'pattern': r'^[0-9]*\.?[0-9]+$',
        'class': 'amounts',
        'value': 0.0,
      }
    )
  )


  #complemento de pagos - nodo pago

  pago_date = forms.DateField(
    label='Fecha de Pago',
    widget=widgets.TextInput()
  )
  pago_way = forms.ModelChoiceField(
    queryset = FormaPago.objects.all().exclude(clave = '99'),
    label = 'Forma de Pago',
    widget = forms.Select(),
    to_field_name='clave',
    initial='01'
    #choices=(('01', '01 - Efectivo'),('02', '02 - Cheque nominativo'),('03', '03 - Transferencia electrónica de fondos'),)
  )
  pago_select = forms.ChoiceField(
    #queryset = Moneda.objects.all().exclude(clave = 'XXX'),
    initial='MXN',
    label='Moneda de Pago',
    widget=forms.Select(),
    choices=(
      ('MXN', 'MXN - Peso Mexicano'),
    )
    #to_field_name='clave',
    #choices=(('MXN', 'MXN - Peso Mexicano'),('USD', 'USD - Dolar americano'),)
  )
  pago_current = forms.FloatField(
    label='Tipo Cambio de Pago',
    widget=widgets.NumberInput(),
    required=False
  )
  pago_mount = forms.FloatField(
    label='Monto',
    widget=widgets.NumberInput(
      attrs={
        'value': 1,
      })
  )
  pago_numoper = forms.CharField(
    label='Número de Operación',
    widget=widgets.TextInput(
      attrs={
        "pattern": "[^|]{1,100}",
        "maxlength": 100
      }
    ),
    required=False
  )
  pago_rfcCtaOrd = forms.CharField(
    label='Rfc Cuenta Ordenante',
    widget=widgets.TextInput(
      attrs={
        "pattern": "XEXX010101000|[A-Z&Ñ]{3}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A]"
      }
    ),
    required=False
  )
  pago_nomBanOrd = forms.CharField(
    label='Nombre del Banco Ordenante',
    widget=widgets.TextInput(
      attrs={
        "pattern": "[^|]{1,300}",
        "maxlength": 300
      }
    ),
    required=False
  )
  pago_ctaOrd = forms.CharField(
    label='Cuenta Ordenante',
    widget=widgets.TextInput(
      attrs={
        "pattern": "[A-Z0-9_]{10,50}",
        "maxlength": 50
      }
    ),
    required=False
  )
  pago_rfcCtaBen = forms.CharField(
    label='Rfc Cuenta Beneficiaria',
    widget=widgets.TextInput(
      attrs={
        "pattern": "[A-Z&Ñ]{3}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A]"
      }
    ),
    required=False
  )
  pago_ctaBen = forms.CharField(
    label='Cuenta Beneficiaria',
    widget=widgets.TextInput(
      attrs={
        "pattern": "[A-Z0-9_]{10,50}",
        "maxlength": 50
      }
    ),
    required=False
  )
  pago_tipocadena = forms.CharField(
    label='Tipo Cadena Pago',
    widget=widgets.TextInput(),
    required=False
  )
  pago_cert = forms.CharField(
    label='Certificado Pago',
    widget=widgets.TextInput(),
    required=False
  )
  pago_cadena = forms.CharField(
    label='Cadena Pago',
    widget=widgets.TextInput(),
    required=False
  )
  pago_sello = forms.CharField(
    label='Sello Pago',
    widget=widgets.TextInput(),
    required=False
  )

  #complemento de pagos - nodo doctoRelacionado
  
  docto_idDoc = forms.CharField(
    label='Id del Documento',
    widget=widgets.TextInput(
      attrs={
        'id': 'docto_idDoc_0',
        "pattern": "([a-f0-9A-F]{8}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{12})|([0-9]{3}-[0-9]{2}-[0-9]{9})",
        "maxlength": 36,
      }
    ),
    required=True,
  )
  docto_serie = forms.CharField(
    label='Serie',
    widget=widgets.TextInput(
      attrs={
        'id': 'docto_serie_0',
        "pattern": "[^|]{1,25}",
        "maxlength": 25
      }
    ),
    required=False
  )
  docto_folio = forms.CharField(
    label='Folio',
    widget=widgets.TextInput(
      attrs={
        'id': 'docto_folio_0',
        "pattern": "[^|]{1,40}",
        "maxlength": 40
      }
    ),
    required=False
  )
  docto_monedaDr = forms.ChoiceField(
    label='Moneda Dr',
    #queryset = Moneda.objects.all().exclude(clave = 'XXX'),
    widget=forms.Select(
      attrs={
        'id': 'docto_monedaDr_0',
      }
    ),
    #to_field_name='clave',
    initial='MXN',
    choices=(
      ('MXN', 'MXN - Peso Mexicano'),
    )
  )
  docto_tipoCambioDr = forms.FloatField(
    label='Tipo de Cambio Dr',
    widget=widgets.NumberInput(
      attrs={
        'id': 'docto_tipoCambioDr_0',
      }
    ),
    required=False
  )
  docto_metodoPagoDr = forms.ModelChoiceField(
    queryset = MetodoPago.objects.all().exclude(clave = 'PUE'),
    label='Método de Pago Dr',
    widget = forms.Select(
      attrs={
        'id': 'docto_metodoPagoDr_0',
      }
    ),
    to_field_name='clave',
    initial='PPD'
  )
  docto_numParcialidad = forms.CharField(
    label='Número de parcialidad',
    widget=widgets.TextInput(
      attrs={
        'id': 'docto_numParcialidad_0',
        "pattern": "[1-9][0-9]{0,2}",
      }
    )
  )
  docto_impSalAnt = forms.FloatField(
    label='Importe de Saldo Anterior',
    widget=widgets.NumberInput(
      attrs={
        'value': 1,
        'id': 'docto_impSalAnt_0',
      }
    )
  )
  docto_impPagado = forms.FloatField(
    label='Importe Pagado',
    widget=widgets.NumberInput(
      attrs={
        'value': 1,
        'id': 'docto_impPagado_0',
      }
    )
  )
  docto_impSaldoInsoluto = forms.FloatField(
    label='Importe de Saldo Insoluto',
    widget=widgets.NumberInput(
      attrs={
        'value': 0,
        'id': 'docto_impSaldoInsoluto_0',
      }
    )
  )

  def __init__(self, *args, **kwargs):
    
    #paymentmethod_form_field = Div('payment_method', css_class='col-xs-12 col-sm-6 col-md-3 col-lg-3')
    #paymentway_form_field = Div('payment_way', css_class='col-xs-12 col-sm-6 col-md-3 col-lg-3')
    #currency_form_field = Div('currency', css_class='col-sm-6 col-md-3 col-lg-3')
    
    initial_arguments = kwargs.pop('initial')
    payment_arguments = kwargs.pop('pagos')
    
    concept_cols = 'col-xs-12 col-sm-11 col-md-11 col-lg-11'

    if initial_arguments:
      user = initial_arguments.get('user', None)
      business = user.business_set.get()
      self.base_fields['quantity'].widget.attrs.pop('readonly', False)
      self.base_fields['type_invoice'].widget.attrs.pop('disabled', False)
      self.base_fields['select'].widget.attrs.pop('disabled', False)
      #self.base_fields['use_cfdi'].widget.attrs.pop('disabled', False)
      self.base_fields['identifier'].widget.attrs.pop('disabled', False)
      self.base_fields['discount'].widget.attrs.pop('disabled', False)
      
      kwargs['initial'] = {
        'quantity': 1.0,
        'discount': 0.0,
      }
      #if hasattr(business, 'address'):
      #  codigo_postal_obj = CodigoPostal.objects.filter(clave=business.address.zipcode).filter(inicio__lte=datetime.now()).filter(Q(fin__gte=datetime.now()) | Q(fin=None)).first()
      #  if codigo_postal_obj is not None:
      #    self.declared_fields['expedition_place'].choices = [
      #      (codigo_postal_obj.clave, f'{codigo_postal_obj.clave} - {codigo_postal_obj.estado}')
      #    ]
      #    self.declared_fields['expedition_place'].initial = [codigo_postal_obj.clave]
      if payment_arguments is not None:
        concept = payment_arguments.get('concepto', None)
        comprobante = payment_arguments.get('comprobante', None)
        receptor = payment_arguments.get('receptor', None)
        if concept is not None:
        #pagos = initial_arguments.pop('pagos')
        #print(pagos_arguments)

          kwargs['initial'] = {
            "expedition_place" : business.address.zipcode,
            }
          kwargs['initial'].update({
            "prodservice": concept['claveprodserv'],
            "key_unit": concept['claveunidad'],
            "unit_price": concept['valorunitario'], 
            "quantity": concept['cantidad'],
            "amount": concept['importe'],
            "type_invoice": comprobante['tipodecomprobante'],
            "select": comprobante['moneda'],
            # "select_name": comprobante['select_name'],
            #"use_cfdi": receptor['usocfdi'],
            'discount': '',
          })

          paymentmethod_form_field = None
          paymentway_form_field = None
          currency_form_field = None
          self.base_fields['quantity'].widget.attrs['readonly'] = 'readonly'
          self.base_fields['type_invoice'].widget.attrs['disabled'] = 'disabled'
          #self.declared_fields['select'].widget.attrs['value'] = 'XXX'
          self.base_fields['select'].widget.attrs['disabled'] = 'disabled'
          #self.base_fields['payment_conditions'].widget.attrs['readonly'] = 'readonly'
          #self.base_fields['use_cfdi'].widget.attrs['disabled'] = 'disabled'
          self.base_fields['identifier'].widget.attrs['disabled'] = 'disabled'
          self.base_fields['discount'].widget.attrs['disabled'] = 'disabled'

          self.base_fields['discount'].widget.attrs['value'] = ''

          concept_cols = 'col-xs-12 col-sm-12 col-md-12 col-lg-12'

    super(InvoiceForm, self).__init__(*args, **kwargs)
    from pdb import set_trace
    
    self.helper_header = FormHelper()
    self.helper_receiver = FormHelper()
    self.helper_concepts = FormHelper()

    self.helper_pagos = FormHelper()
    self.helper_docto = FormHelper()

    self.helper_header.form_tag = False # how do you render two or more forms? you need to set from_tag to false in every helper
    self.helper_header.disable_csrf = True
    # self.helper_header.wrapper_class = 'form-group'

    self.helper_receiver.form_tag = False
    self.helper_receiver.disable_csrf = True
    # self.helper_receiver.wrapper_class = 'form-group'

    self.helper_concepts.form_tag = False
    self.helper_concepts.disable_csrf = True
    # self.helper_concepts.wrapper_class = 'form-group'
    #self.helper_concepts.form_id = 'section_concepts'
    #import pdb; pdb.set_trace()

    self.helper_pagos.form_tag = False
    self.helper_pagos.disable_csrf = True

    self.helper_docto.form_tag = False
    self.helper_docto.disable_csrf = True

    self.helper_header.layout = Layout(
      Div(
        Div('id_invoice', css_class='col-xs-12 col-sm-6 col-md-4 col-lg-4'),
        Div('type_invoice', css_class='col-xs-12 col-sm-6 col-md-3 col-lg-3'),
        #Div('payment_method', css_class='col-xs-12 col-sm-6 col-md-3 col-lg-3'),
        #paymentmethod_form_field,
        #Div('payment_way', css_class='col-xs-12 col-sm-6 col-md-3 col-lg-3'),
        #paymentway_form_field,
        #Div('expedition_place', css_class='col-xs-12 col-sm-6 col-md-3 col-lg-3'),
        # Div('payment_date', css_class='col-sm-6 col-md-6 col-lg-6'),
        # Div('confirmation', css_class='col-sm-6 col-md-3 col-lg-3'),
        
        #Div('serial', css_class='col-sm-6 col-md-3 col-lg-3'),
        #Div('folio', css_class='col-sm-6 col-md-3 col-lg-3'),
        Div('select', css_class='col-sm-6 col-md-2 col-lg-2'),
        Div('payment_name', css_class='col-sm-6 col-md-2 col-lg-2'),
        #currency_form_field, 
        #Div('accounting_cost_invoice', css_class='col-xs-12 col-sm-6 col-md-3 col-lg-3'),
        #Div('buyer_reference_invoice', css_class='col-xs-12 col-sm-6 col-md-3 col-lg-3'),
        #Div('currency', css_class='col-sm-6 col-md-3 col-lg-3'),
        css_class='col-sm-12 col-md-12 col-lg-12',
      ),
      # Div(
      #   Div('payment_conditions'),
      #   css_class='col-sm-6 col-md-6 col-lg-6',
      # ),
    )

    self.helper_receiver.layout = Layout(
      Div(
        Div('rtaxpayer', css_class='col-xs-12 col-sm-4 col-md-4 col-lg-3 rfc'),
        # Div('business_name', css_class='col-xs-12 col-sm-6 col-md-3 col-lg-3'),
        #Div('use_cfdi', css_class='col-xs-12 col-sm-4 col-md-4 col-lg-3'),
        #Div('id_company', css_class='col-xs-12 col-sm-4 col-md-4 col-lg-3'),
        Div('fiscal_address', css_class='col-xs-12 col-sm-4 col-md-4 col-lg-3'),
        css_class='form-group col-sm-12 collapse in', id='div_receptor'
      ),
      #Div(
      #  Div('rtaxpayer', css_class='col-sm-4'),
      #  #Div('business_name', css_class='col-sm-4'),
      #  Div('use_cfdi', css_class='col-sm-4'),
      #  css_class='col-sm-12'
      #),
      #Div(
        #Div('name', css_class='col-sm-3'),
        #Div('last_name', css_class='col-sm-3'),
        #Div('second_last_name', css_class='col-sm-3'),
      #  Div('emails', css_class='col-sm-3'),
      #  css_class='col-sm-12'
      #),
    )
    
    self.helper_concepts.layout = Layout(
      # Div(
        Div(
            Div('identifier', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('prodservice', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('key_unit', css_class='col-sm-4 col-md-4 col-lg-2'),
            #Div('unit', css_class='col-sm-2 col-md-2 col-lg-2'),
            #Div('unit_price', css_class='col-sm-2 col-md-2 col-lg-2'),
            Div('quantity', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('discount', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('amount', css_class='col-sm-4 col-md-4 col-lg-2'),
          css_class=concept_cols
        ),
        #Div(
        #  Div('description', css_class='col-sm-12 col-md-12 col-lg-12'),
        #  css_class='col-sm-12 col-md-6 col-lg-6'
        # ),
      #   css_class='row',
      # ),
    )

    self.helper_pagos.layout = Layout(
      # Div(
        Div(
            Div('pago_date', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_way', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_select', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_current', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_mount', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_numoper', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_rfcCtaOrd', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_nomBanOrd', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_ctaOrd', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_rfcCtaBen', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_ctaBen', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_tipocadena', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_cert', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_cadena', css_class='col-sm-4 col-md-4 col-lg-2'),
            Div('pago_sello', css_class='col-sm-4 col-md-4 col-lg-2'),
        ),
        #Div(
        #  Div('description', css_class='col-sm-12 col-md-12 col-lg-12'),
        #  css_class='col-sm-12 col-md-6 col-lg-6'
        # ),
      #   css_class='row',
      # ),
    )


    self.helper_docto.layout = Layout(
        # Div(
          Div(
              Div('docto_idDoc', css_class='col-sm-4 col-md-4 col-lg-2'),
              Div('docto_serie', css_class='col-sm-4 col-md-4 col-lg-2'),
              Div('docto_folio', css_class='col-sm-4 col-md-4 col-lg-2'),              
              Div('docto_monedaDr', css_class='col-sm-4 col-md-4 col-lg-2'),
              Div('docto_tipoCambioDr', css_class='col-sm-4 col-md-4 col-lg-2'),
              Div('docto_metodoPagoDr', css_class='col-sm-4 col-md-4 col-lg-2'),
              Div('docto_numParcialidad', css_class='col-sm-4 col-md-4 col-lg-2'),
              Div('docto_impSalAnt', css_class='col-sm-4 col-md-4 col-lg-2'),
              Div('docto_impPagado', css_class='col-sm-4 col-md-4 col-lg-2'),
              Div('docto_impSaldoInsoluto', css_class='col-sm-4 col-md-4 col-lg-2'),
          ),
          #Div(
          #  Div('description', css_class='col-sm-12 col-md-12 col-lg-12'),
          #  css_class='col-sm-12 col-md-6 col-lg-6'
          # ),
        #   css_class='row',
        # ),
      )

#Div(
#  Div('payment_method', wrapper_class='form-control', css_class='col-sm-3'),
#  Div('payment_way', wrapper_class='form-control', css_class='col-sm-3'),
#  Div(
#    MultiWidgetField('currency',
#      attrs=({
#        'class': 'col-sm-3',
#      }),
#      css_class='col-sm-3'
#    ),
#    css_class='row'
#  ),
#  Div('payment_way', wrapper_class='form-control'),
#),
#Field('payment_conditions', css_class='form-control'),
#ButtonHolder(
#  Submit('submit', 'Crear', css_class='btn btn-success')
#)
