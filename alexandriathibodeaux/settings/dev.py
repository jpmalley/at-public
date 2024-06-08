from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

env = os.environ.copy()
SECRET_KEY = os.getenv('SECRET_KEY')

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'wagtail.contrib.styleguide',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ("127.0.0.1")

ALLOWED_HOSTS = ['*']

# Recaptcha settings
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
NOCAPTCHA = True

# S3 settings
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# PayPal settings
PAYPAL_LIVE_CLIENT_ID = os.getenv('PAYPAL_LIVE_CLIENT_ID')
PAYPAL_LIVE_CLIENT_SECRET = os.getenv('PAYPAL_LIVE_CLIENT_SECRET')
PAYPAL_LIVE_URL = 'https://api-m.paypal.com'

PAYPAL_SANDBOX_CLIENT_ID = os.getenv('PAYPAL_SANDBOX_CLIENT_ID')
PAYPAL_SANDBOX_CLIENT_SECRET = os.getenv('PAYPAL_SANDBOX_CLIENT_SECRET')
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

try:
    from .local import *
except ImportError:
    pass
