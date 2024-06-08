from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sl6(apz*4^ai+agf&tyq^!3jt1ehec_u5p)_ul_as$+#yv8g6&'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hello@alexandriathibodeaux.com'
EMAIL_HOST_PASSWORD = 'icbwccchlgwpaywt'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'wagtail.contrib.styleguide',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ("127.0.0.1")

ALLOWED_HOSTS = [
    'dev.alexandriathibodeaux.com',
    'at-website-ef8c5d760f75.herokuapp.com',
    '127.0.0.1',
    'locoalhost',
]

CORS_ALLOWED_ORIGINS = [
    'https://dev.alexandriathibodeaux.com',
    'http://at-website-ef8c5d760f75.herokuapp.com',
    'http://localhost:8080',
    'http://127.0.0.1:8000',
]

private_ip = get_linux_ec2_private_ip()
if private_ip:
   ALLOWED_HOSTS.append(private_ip)

PAYPAL_LIVE_MODE = False

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
