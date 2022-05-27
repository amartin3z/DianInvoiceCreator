# -*- coding: UTF-8 -*-
from django import forms

from app.invoicing.models import Receiver

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Button, HTML
from django.utils.translation import ugettext as _

class ReceiverForm(forms.ModelForm):
    
  class Meta:
    model = Receiver
    fields = (
      'taxpayer_id',
      'name',
      'use_cfdi',
      'status',
      'emails'
    )

    error_messages = {
      'taxpayer_id':{
        'unique': (_('Previously registered RFC.')),
      },
      'emails':{
        'required': (_('You must register an email.')),
      }
    }

  def __init__(self, *args, **kwargs):
    super(ReceiverForm, self).__init__(*args, **kwargs)
    
    self.helper_receiver = FormHelper()
    self.helper_receiver.form_id = 'formReceiver'
    self.helper_receiver.form_method = 'POST'
    self.helper_receiver.label_class = 'col-lg-12'
    self.helper_receiver.layout = Layout(
      Div(
        Div('name', css_class="form-group col-sm-12 col-md-12 col-lg-12"),
        Div('taxpayer_id', css_class="form-group col-sm-4 col-md-4 col-lg-4 upper"),
        #Div('use_cfdi', css_class="form-group col-sm-4 col-md-4 col-lg-4"),
        #Div('emails', css_class="form-group col-sm-6 col-md-6 col-lg-6 emails-input"),
        HTML('''
        {% load i18n %}
          <div class="form-group col-sm-4 col-md-4 col-lg-4">
            <label for="id_use_cfdi" class="control-label requiredField">{% trans 'Company ID' %}<strong>*</strong></label>
            <select id="id_use_cfdi" class="select2-single" name="use_cfdi" required></select>
          </div>
        '''),
        HTML('''
        {% load i18n %}
          <div class="form-group col-sm-4 col-md-4 col-lg-4">
            <label for="id_taxScheme" class="control-label">{% trans 'TaxScheme ID' %}</label><br>
            <input id="id_taxScheme" type="text" name="taxScheme" data-role="tagsinput" required></input>
          </div>
        '''),
        HTML('''
        {% load i18n %}
          <div class="form-group col-sm-12 col-md-12 col-lg-12">
            <label for="id_emails" class="control-label">&nbsp;&nbsp;&nbsp;&nbsp;{% trans 'Emails' %}*</label><br>
            <input id="id_emails" type="text" value="" data-role="tagsinput" placeholder="{% trans 'Add Emails separated by commas (,)' %}" /><br><br>
          </div>
        '''),
        Div(
          Submit('addreceiver', 'Agregar'), 
          Button('cancel', 'Cancelar', css_class="canr"), 
          css_class="col-sm-12"
        ),
        
      ),
    )

