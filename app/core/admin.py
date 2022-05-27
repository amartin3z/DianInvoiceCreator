# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Business, Address, Log, Branch, SatFaq, Manifest, SatFile
# Register your models here.


class BusinessInfo(admin.ModelAdmin):
	list_display = ('taxpayer_id', 'name', 'email')


class AddressInfo(admin.ModelAdmin):
	list_display = ('country', 'street', 'zipcode')


class LogInfo(admin.ModelAdmin):
	list_display = ('user', 'module', 'action', 'level', 'timestamp', 'data')


class BranchInfo(admin.ModelAdmin):
	list_display = ('name', 'zipcode', 'locality', 'municipality', 'state', 'latitude', 'longitude')


class SatFaqAdmin(admin.ModelAdmin):
	list_display = ('question', 'can_show', 'added',)


class ManifestAdmin(admin.ModelAdmin):
	list_display = ('business', 'signed', 'date_signed')
	
admin.site.register(Address, AddressInfo)
admin.site.register(Business, BusinessInfo)
admin.site.register(Log, LogInfo)
admin.site.register(Branch, BranchInfo)
admin.site.register(SatFaq, SatFaqAdmin)
admin.site.register(Manifest, ManifestAdmin)
admin.site.register(SatFile)