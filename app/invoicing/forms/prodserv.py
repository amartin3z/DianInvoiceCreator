# -*- coding: UTF-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from app.invoicing.models import ProdServ

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, Div, Button, HTML

class ProdServForm(forms.ModelForm):
    
  class Meta:
    model = ProdServ
    fields = (
      # "prodserv",
      # "key_unit",
      # "identifier",
      # "unit",
      # "unit_price",
      # "description",
      'name',
      'description',
      'unit_code',
      # 'currency_id',
      'list_id',
      'unit_price',
      'origin_country',
      # 'seller_item_identification',
      # 'buyers_item_identification',
      'item_classification_code',
      # 'additional_item_name',
      # 'additional_item_value',
    )
    # error_messages = {
    #   'unit_price':{
    #     'required': (u'Precio unitario es requerido.'),
    #     'max_digits': (u'Asegúrese que el precio unitario no tenga más de %(max)s dígitos.')
    #   },
    #   'prodserv':{
    #     'required': (u'Clave producto servicio es requerido.'),
    #   },
    #   'key_unit':{
    #     'required': (u'Clave unidad es requerido.'),
    #   },
    #   'identifier':{
    #     'required': (u'Identificador es requerido.'),
    #   #'min_length': (u'Identificador debe tener más de %(min)s caracterés.')
    #   },
    #   'unit': {
    #     'required': (u'Unidad es requerida'),
    #   },
    # }

  def __init__(self, *args, **kwargs):
    super(ProdServForm, self).__init__(*args, **kwargs)
    self.helper_prodserv = FormHelper()
    #self.helper_prodserv.wrapper_class = 'form-group'
    # self.helper_prodserv.form_id = 'formProdserv'
    self.helper_prodserv.form_method = 'POST'
    self.helper_prodserv.label_class = 'col-lg-12'
    #self.helper_prodserv.field_class = 'col-lg-8'
    self.helper_prodserv.layout = Layout(
      Div(
        #Div('prodserv', css_class="form-group col-sm-6 col-md-6 col-lg-6 js-example-data-ajax"),
        HTML('''<div class="form-group col-sm-6 col-md-6 col-lg-6">

            <label for="id_prodserv" class="control-label requiredField">Clave Producto/Servicio<strong>*</strong></label>
            <select id="id_prodserv" class="select2-single" name="prodserv" required></select>
          </div>'''
        ),
        #Div('key_unit', css_class="form-group col-sm-6 col-md-6 col-lg-6"),
        HTML('''<div class="form-group col-sm-6 col-md-6 col-lg-6">
            <label for="id_key_unit" class="control-label requiredField">Clave Unidad<strong>*</strong></label>
            <select id="id_key_unit" class="select2-single" name="key_unit" required="required"></select>
          </div>'''
        ),
        Div('listID', css_class="form-group col-sm-6 col-md-6 col-lg-6"),
        Div('unitCode', css_class="form-group col-sm-3 col-md-3 col-lg-3"),
        Div('unitprice', css_class="form-group col-sm-3 col-md-3 col-lg-3"),
        Div('description', css_class="form-group col-sm-12 col-md-12 col-lg-12"),
        Div(
          Submit('addprodserv', 'Agregar'), 
          Button('cancel', 'Cancelar', css_class="canp"), 
          css_class='avoid',
        ),
        css_class='col-sm-12'
      ),
    )

