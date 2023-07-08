from .base import *

DEBUG = False
#DEBUG = True

SECRET_KEY = 'd1e60d2b9c50ebbc5c83bc452da16fae'

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

ALLOWED_HOSTS = [
  'localhost',
  '127.0.0.1',
  'www.l-g-v.com',
  'wagtail.l-g-v.com',
  'gvois.in',
  'www.gvois.in',
  'gvcoop.org',
  'www.gvcoop.org',
  'gvcoop.com',
  'www.gvcoop.com',
  'coopgv.org',
  'www.coopgv.org',
  'coopgv.com',
  'www.coopgv.com',
]
CSRF_TRUSTED_ORIGINS = [
  'http://localhost',
  'http://127.0.0.1',
  'https://www.l-g-v.com',
  'https://wagtail.l-g-v.com',
  'https://gvcoop.org',
  'https://www.gvcoop.org',
  'https://gvcoop.com',
  'https://www.gvcoop.com',
  'https://coopgv.org',
  'https://www.coopgv.org',
  'https://coopgv.com',
  'https://www.coopgv.com',
  'https://gvois.in',
  'https://www.gvois.in',
]
try:
    from .local import *
except ImportError:
    pass
