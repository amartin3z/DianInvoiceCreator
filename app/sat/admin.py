from django.contrib import admin
from .models import *

class LCOAdmin(admin.ModelAdmin):

  search_fields = ('rfc', )
  list_display = ('rfc', 'validez', 'estatus', 'serial', 'inicio', 'fin', )
  
  empty_value_display = 'Sin definir'
  


class LRFCAdmin(admin.ModelAdmin):
  
  search_fields = ('rfc', )
  
  empty_value_display = 'Sin definir.'
  list_display = ('rfc', 'sncf', 'subcontratacion', )

admin.site.register(LCO, LCOAdmin)
admin.site.register(LRFC, LRFCAdmin)