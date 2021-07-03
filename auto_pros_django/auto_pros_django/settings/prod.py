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
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': '',
    }
}

