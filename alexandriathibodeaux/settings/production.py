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
# DATABASES['default'] = env['DATABASE_URL']
# DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "cache"
    }
}

SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

PREPEND_WWW = True
BASE_URL = "www.alexandriathibodeaux.com"

ALLOWED_HOSTS = ['*']

# Recaptcha settings
RECAPTCHA_PUBLIC_KEY = env['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = env['RECAPTCHA_PRIVATE_KEY']
NOCAPTCHA = True

# S3 settings
AWS_STORAGE_BUCKET_NAME = env['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = env['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = env['AWS_SECRET_ACCESS_KEY']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# PayPal settings
PAYPAL_LIVE_CLIENT_ID = env['PAYPAL_LIVE_CLIENT_ID']
PAYPAL_LIVE_CLIENT_SECRET = env['PAYPAL_LIVE_CLIENT_SECRET']
PAYPAL_LIVE_URL = 'https://api-m.paypal.com'

PAYPAL_SANDBOX_CLIENT_ID = env['PAYPAL_SANDBOX_CLIENT_ID']
PAYPAL_SANDBOX_CLIENT_SECRET = env['PAYPAL_SANDBOX_CLIENT_SECRET']
PAYPAL_SANDBOX_URL = 'https://api-m.sandbox.paypal.com'

PAYPAL_LIVE_MODE = False

if PAYPAL_LIVE_MODE:
    PAYPAL_CLIENT_ID = PAYPAL_LIVE_CLIENT_ID
    PAYPAL_CLIENT_SECRET = PAYPAL_LIVE_CLIENT_SECRET
    PAYPAL_URL = PAYPAL_LIVE_URL
else:
    PAYPAL_CLIENT_ID = PAYPAL_SANDBOX_CLIENT_ID
    PAYPAL_CLIENT_SECRET = PAYPAL_SANDBOX_CLIENT_SECRET
    PAYPAL_URL = PAYPAL_SANDBOX_URL

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
