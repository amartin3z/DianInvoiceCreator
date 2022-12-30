from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, re_path
from app.core.accounts import session_verify
from django.utils.translation import ugettext_lazy as _
from django.views.i18n import JavaScriptCatalog
from django.conf import settings
from django.conf.urls.static import static
from pdb import set_trace

from app.users.views import index, index_sat, password_reset

from app.core.accounts import session_verify

from app.core.urls import profile as core_profile
from app.core.views import invoices_sat

from app.invoicing.views import (
    prodservs as invoicing_prodservs,
    receivers as invoicing_receivers,
    new_invoice as invoicing_invoice,
    new_payment as invoicing_payment
)

urlpatterns = [
    url('i18n/', include('django.conf.urls.i18n')),
    url('jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^{}/'.format(settings.ADMIN_URL), admin.site.urls),
    # URLS USERS
    url(r'^', include('app.users.urls')),
    # URLS BUSINESS
    url(r'^business/', include('app.core.urls')),
        url(u'^profile/$', core_profile, name='profile'),

    # URLS FACTURADOR Y OTROS
    url(r'^invoices/', include('app.invoicing.urls')),
        url(r'^Products-Services/', invoicing_prodservs, name='list-prodservs'),
        url(r'^receivers/', invoicing_receivers, name='list-receivers'),
        url(u'^invoicing/$', invoicing_invoice, name='add-invoice'),
        url(u'^invoicing/payments/$', invoicing_payment, name='add-payment'),

    # URLS SOPORTE
    url(r'^support/', include('app.support.urls'),),

    # URL INDEX
    url(r'^$', index, name='index'),

    # URL SAT
    url(r'^sat/$', index_sat, name='index_sat'),
        url(u'^sat/invoices/$', invoices_sat, name='invoices_sat'),
    
    # URL WS
    url(r'^ws/', include('app.cfdi.urls'),),

    # URL CAMBIO DE CONTRASEÑÁ
	url(r'^resetpassword/success/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	url(r'^account/resetpassword/$', password_reset, name='auth_password_reset'),
    url(r'^app/session/verify/$', session_verify, name='session_verify'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
