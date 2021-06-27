"""
WSGI config for auto_pros_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#Luke: modify to new path once new settings in

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auto_pros_django.settings.prod')

application = get_wsgi_application()
