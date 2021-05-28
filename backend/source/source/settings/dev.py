from service.backend.source.source.settings.base import *

# Override base settings here

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

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
