"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.production")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = get_wsgi_application()
application = Cling(get_wsgi_application())
