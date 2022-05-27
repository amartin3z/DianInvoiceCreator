
import os

from django.core.wsgi import get_wsgi_application

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soriana.settings")

application = get_wsgi_application()
