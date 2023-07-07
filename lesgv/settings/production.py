from .base import *

DEBUG = False

STATIC_ROOT = '/var/www/wagtail/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wagtail'
    }
}

try:
    from .local import *
except ImportError:
    pass
