# -*- coding: utf-8 -*-
from django.conf.urls import url

#from .views import business, stuffs, business_validator, logs, branch, conciliacion, profile, generatereport_sat, downloadreport_sat, profile_options, download_xml_sat, download_manifest_files
from .views import logs, profile, generatereport_sat, downloadreport_sat, profile_options, download_xml_sat, download_manifest_files, download_manifest_pdf, download_manifest_xml

app_name = 'core'

urlpatterns = [
  #url(u'^$', business, name='business'),
  #url(u'^branch/$', branch, name='branch'),
  # url(u'^activate/$', stuffs, name='stuffs'),
  # url(u'^validate/$', business_validator, name='validate'),
  url(u'^logs/$', logs, name='logs'),
  url(u'^generatereport_sat/$', generatereport_sat, name='generatereport_sat'),
  url(u'^downloadreport_sat/(?P<filename>(Reporte_20)[0-9]{2}-[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1}_[0-2]{1}[0-9]{1}-[0-5]{1}[0-9]{1}-[0-5]{1}[0-9]{1}[.]csv)/$', downloadreport_sat, name='downloadreport_sat'),
  #url(u'^downloadreport_sat/(?P<filename>(Reporte_20)[0-9]{2}-[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1}_[0-2]{1}[0-9]{1}-[0-5]{1}[0-9]{1}-[0-5]{1}[0-9]{1}[.]csv)/$', downloadreport_sat, name='downloadreport_sat'),
  url(u'^profile/options/$', profile_options, name='profile_options'),

  url(r'^download_xml/(?P<uuid>[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})+/$', download_xml_sat, name='download_xml'),
  url(r'^download_manifest_files/$', download_manifest_files, name='download_manifest_files'),

  url(r'^manifest/download/xml/$', download_manifest_xml, name="download_manifest_xml"),
  url(r'^manifest/download/pdf/$', download_manifest_pdf, name="download_manifest_pdf"),
 ]