from .base import *

# Override base settings here

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

HOST_DOMAIN = 'http://' +  ALLOWED_HOSTS[0] + ':8000'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'servicedatabase',
        'USER': 'luke',
        'PASSWORD': 'MadebyCAR1!',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
