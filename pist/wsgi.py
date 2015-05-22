"""
WSGI config for pist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import sys
import os
import os.path

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                'pist')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pist.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
