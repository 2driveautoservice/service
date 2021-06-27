from .base import *
import os

# Override base settings here

DEBUG = False

ALLOWED_HOSTS = ['134.122.43.162', 'localhost']

HOST_DOMAIN = 'http://' +  ALLOWED_HOSTS[0] + ':8000'

# Luke: modified for cors
CORS_ALLOWED_ORIGINS = [
    "http://134.122.43.162:8080",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USERNAME'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT')
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
