from os import environ, path

# FIXME: We can't use the production settings because those enable CAS/SSO that
# causes all kinds of issues with the Wagtail admin.
from .base import *  # noqa
from .base import PROJECT_ROOT, STATIC_URL

# Disable debug mode
DEBUG = False
ENV = 'prd'

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': STATIC_URL,
    'ENV': ENV,
}

SECRET_KEY = environ.get('SECRET_KEY', 'please-change-me')

MEDIA_ROOT = path.join(PROJECT_ROOT, 'media')
STATIC_ROOT = path.join(PROJECT_ROOT, 'static')

# FIXME: Scaffolded settings file has an invalid STATICFILES_DIRS
STATICFILES_DIRS = []
