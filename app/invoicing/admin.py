# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import ProdServ, Receiver, InvoicingSerial, Buyer

# class ProdServAdmin(admin.ModelAdmin):

#   search_fields = ('prodserv', 'identifier')
  
#   empty_value_display = 'Sin definir'
#   list_display = ('identifier', 'description', 'business', 'price','key_unit', 'prodserv')
#   list_display_links = ('identifier', 'description', 'key_unit')

#   fieldsets = (
#     ('Negocio', { 
#       'fields': ('business',), 
#     }),
#     (u'Información SAT', {
#       'classes': ('extrapretty',),
#       'fields': (('key_unit', 'prodserv'),),
#     }),
#     (u'Información Interna', {
#       'classes': ('extrapretty',),
#       'fields': (('unit', 'identifier'), ('description'), 'unit_price'),
#     })
#   )
  
#   def price(self, obj):
#     return u'$ {}'.format(obj.unit_price)

class ReceiverAdmin(admin.ModelAdmin):
  
  search_fields = ('taxpayer_id', 'name')
  
  empty_value_display = 'Sin definir.'
  list_display = ('taxpayer_id', 'name', 'business', 'status', 'modified')
  list_display_links = ('taxpayer_id', 'name')

  fieldsets = (
    ('Negocio', { 
      'fields': ('business',), 
    }),
    (u'Informacion del Receptor', {
      'classes': ('wide',),
      'fields': (('taxpayer_id', 'name', 'use_cfdi'), 'emails'),
    }),
  )

class InvoicingSerialAdmin(admin.ModelAdmin):
  
  search_fields = ('business',)
  
  empty_value_display = 'Sin definir.'
  list_display = ('business', 'sequence')
  list_display_links = ('business', 'sequence')

  fieldsets = (
    ('Negocio', { 
      'fields': (
        'business',
        'serie',
      ), 
    }),
    (u'Sequencia', {
      'classes': ('wide',),
      'fields': ('sequence',),
    }),
  )

# admin.site.register(ProdServ, ProdServAdmin)
admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(Buyer)
admin.site.register(InvoicingSerial, InvoicingSerialAdmin)

