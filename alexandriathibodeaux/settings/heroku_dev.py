from __future__ import absolute_import, unicode_literals
from .base import *
import dj_database_url
import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DEBUG = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

DATABASES['default'] = dj_database_url.config()

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "cache"
    }
}

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

if DEBUG is True:
    class AllIPS(list):
        def __contains__(self, item):
            return True

INTERNAL_IPS = AllIPS()

# SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True

# PREPEND_WWW = True
BASE_URL = "dev.alexandriathibodeaux.com"

ALLOWED_HOSTS = [
    'alexandriathibodeaux.com',
    'www.alexandriathibodeaux.com',
    'dev.alexandriathibodeaux.com',
    'dev-alexandriathibodeaux.herokuapp.com',
    'localhost',
]

PAYPAL_LIVE_MODE = False

if PAYPAL_LIVE_MODE:
    PAYPAL_CLIENT_ID = PAYPAL_LIVE_CLIENT_ID
    PAYPAL_CLIENT_SECRET = PAYPAL_LIVE_CLIENT_SECRET
    PAYPAL_URL = PAYPAL_LIVE_URL
else:
    PAYPAL_CLIENT_ID = PAYPAL_SANDBOX_CLIENT_ID
    PAYPAL_CLIENT_SECRET = PAYPAL_SANDBOX_CLIENT_SECRET
    PAYPAL_URL = PAYPAL_SANDBOX_URL

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

try:
    from .local import *
except ImportError:
    pass
