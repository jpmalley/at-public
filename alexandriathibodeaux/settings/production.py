from __future__ import absolute_import, unicode_literals
from .base import *
import os


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
#         "LOCATION": "/tmp/cache"
#     }
# }

SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

PREPEND_WWW = False
BASE_URL = "alexandriathibodeaux.com"

ALLOWED_HOSTS = [
    'alexandriathibodeaux.com',
    'www.alexandriathibodeax.com',
    'at-website-prod.us-west-1.elasticbeanstalk.com'
]

private_ip = get_linux_ec2_private_ip()
if private_ip:
   ALLOWED_HOSTS.append(private_ip)

PAYPAL_LIVE_MODE = True

if PAYPAL_LIVE_MODE:
    PAYPAL_CLIENT_ID = PAYPAL_LIVE_CLIENT_ID
    PAYPAL_CLIENT_SECRET = PAYPAL_LIVE_CLIENT_SECRET
    PAYPAL_URL = PAYPAL_LIVE_URL
else:
    PAYPAL_CLIENT_ID = PAYPAL_SANDBOX_CLIENT_ID
    PAYPAL_CLIENT_SECRET = PAYPAL_SANDBOX_CLIENT_SECRET
    PAYPAL_URL = PAYPAL_SANDBOX_URL

try:
    from .local import *
except ImportError:
    pass
