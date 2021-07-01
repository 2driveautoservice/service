from .base import *
import os

# Override base settings here

DEBUG = False

ALLOWED_HOSTS = ['autopros.app', 'localhost']

HOST_DOMAIN = 'https://' +  ALLOWED_HOSTS[0]

# Luke: modified for cors
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "https://autopros.app"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'servicedatabase',
        'USER': 'luke',
        'PASSWORD': 'MadebyCAR1!',
        'HOST': 'localhost',
        'PORT': ''
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

