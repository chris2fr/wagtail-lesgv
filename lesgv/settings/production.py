from .base import *

DEBUG = False

STATIC_ROOT = '/var/www/wagtail/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wagtail'
    }
}

STATIC_ROOT = '/var/www/wagtail/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/var/www/wagtail/media/'
MEDIA_URL = '/media/'

try:
    from .local import *
except ImportError:
    pass
