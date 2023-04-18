import os
import requests
from pytz import common_timezones
from pathlib import Path

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition
INSTALLED_APPS = [
    'home',
    'search',
    'flex',
    'streams',
    'site_settings',
    'menus',
    'users',
    'subscribers',
    'blog',
    'form',
    'paypal',

    'django_extensions',
    'widget_tweaks',
    'corsheaders',

    'wagtail.contrib.forms',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.redirects',
    'wagtail.contrib.settings',
    'wagtail.contrib.routable_page',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'captcha',
    'wagtailcaptcha',
    'storages',
]

# Authorization settings
AUTH_APPS = [
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # "allauth.socialaccount.providers.facebook",
    # "allauth.socialaccount.providers.google",
    # "allauth.socialaccount.providers.twitter",
]

SITE_ID = 1

INSTALLED_APPS += AUTH_APPS

AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Settings for email as username
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

# Email confirmation
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# After 10 failed login attempts, restrict logins for 30 minutes
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 1800
ACCOUNT_PASSWORD_MIN_LENGTH = 8

# Login settings
LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/account/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/account/login/'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
SOCIALACCOUNT_AUTO_SIGNUP = False
ACCOUNT_LOGOUT_ON_GET = True
LOGOUT_REDIRECT_URL = '/account/login/'
WAGTAIL_FRONTEND_LOGIN_URL = LOGIN_URL

# Other settings
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'alexandriathibodeaux.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'alexandriathibodeaux.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'at-import',
            'USERNAME': 'jm',
            'PASSWORD': 'password',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'


# Wagtail settings

WAGTAIL_SITE_NAME = "alexandriathibodeaux"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://alexandriathibodeaux.com'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Recaptcha settings
if 'RECAPTCHA_PUBLIC_KEY' in os.environ:
    RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
    RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']
    NOCAPTCHA = True
else:
    SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# S3 settings
if 'AWS_STORAGE_BUCKET_NAME' in os.environ:
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']

    AWS_S3_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_S3_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

    # AWS_S3_SESSION_PROFILE = os.environ['AWS_S3_SESSION_PROFILE']

    AWS_QUERYSTRING_AUTH = False

# PayPal settings
if 'PAYPAL_LIVE_URL' in os.environ:
    PAYPAL_LIVE_CLIENT_ID = os.environ['PAYPAL_LIVE_CLIENT_ID']
    PAYPAL_LIVE_CLIENT_SECRET = os.environ['PAYPAL_LIVE_CLIENT_SECRET']
    PAYPAL_LIVE_URL = os.environ['PAYPAL_LIVE_URL']

PAYPAL_SANDBOX_CLIENT_ID = 'AQjztLEHkjCIkE9x8_E5wwD8UErJYTu5mvsHVtk_j9LCabXsyJge8bgowUxcg33nOhtws3qMvXT3jRca'
PAYPAL_SANDBOX_CLIENT_SECRET = 'EOFn_kYzb8iLqgH_ed1J77bw5kZ2mRkto-MQNfehY1MfeNk1Vl_TOBJfzSoIVGbaQbSH9AxML7BPxVHk'
PAYPAL_SANDBOX_URL = 'https://api-m.sandbox.paypal.com'

PAYPAL_LIVE_MODE = True

if PAYPAL_LIVE_MODE and 'PAYPAL_LIVE_URL' in os.environ:
    PAYPAL_CLIENT_ID = PAYPAL_LIVE_CLIENT_ID
    PAYPAL_CLIENT_SECRET = PAYPAL_LIVE_CLIENT_SECRET
    PAYPAL_URL = PAYPAL_LIVE_URL
else:
    PAYPAL_CLIENT_ID = PAYPAL_SANDBOX_CLIENT_ID
    PAYPAL_CLIENT_SECRET = PAYPAL_SANDBOX_CLIENT_SECRET
    PAYPAL_URL = PAYPAL_SANDBOX_URL


# EC2 get instance IP   
def is_ec2_linux():
    """Detect if we are running on an EC2 Linux Instance
    See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
    """
    if os.path.isfile("/sys/hypervisor/uuid"):
        with open("/sys/hypervisor/uuid") as f:
            uuid = f.read()
            return uuid.startswith("ec2")
    return False

def get_token():
    """Set the autorization token to live for 6 hours (maximum)"""
    headers = {
        'X-aws-ec2-metadata-token-ttl-seconds': '21600',
    }
    response = requests.put('http://169.254.169.254/latest/api/token', headers=headers)
    return response.text


def get_linux_ec2_private_ip():
    """Get the private IP Address of the machine if running on an EC2 linux server.
    See https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html"""

    if not is_ec2_linux():
        return None
    try:
        token = get_token()
        headers = {
            'X-aws-ec2-metadata-token': f"{token}",
        }
        response = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', headers=headers)
        return response.text
    except:
        return None
    finally:
        if response:
            response.close()