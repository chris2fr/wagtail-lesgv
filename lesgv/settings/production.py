from .base import *
from .websites import *

DEBUG = False
#DEBUG = True

SECRET_KEY = 'd1e60d2b9c50ebbc5c83bc452da16fae'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fairemain'
    }
}

STATIC_ROOT = '/var/www/wagtail/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/var/www/wagtail/media/'
MEDIA_URL = '/media/'

ALLOWED_HOSTS = [
  'localhost',
  '127.0.0.1',
  'wagtail.l-g-v.com',
] + allowed_hosts()

CSRF_TRUSTED_ORIGINS = [
  'http://localhost',
  'http://127.0.0.1',
  'https://www.l-g-v.com',
] + csrf_trusted_origins()


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'django-debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
try:
    from .local import *
except ImportError:
    pass
