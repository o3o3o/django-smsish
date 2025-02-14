# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+=kvb(v+q4xltkc3%wb5@%rn#p@gm^b97-a$g^0#rye!ctm4qn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

SILENCED_SYSTEM_CHECKS = [
    'admin.E408',
    'admin.E409',
    'admin.E410',
]

# ======================
# django-smsish settings
# ======================

TESTING = bool(int(os.getenv("TESTING", str(int(False)))))

# Add `smsish` to your INSTALLED_APPS
INSTALLED_APPS += (
    'django_extensions',
    'django_rq',  # Required by `smsish.sms.backends.rq.SMSBackend`.
    'smsish',
)

# Set `SMS_BACKEND` in your settings.
SMS_BACKEND_CONSOLE = 'smsish.sms.backends.console.SMSBackend'
SMS_BACKEND_DUMMY = 'smsish.sms.backends.dummy.SMSBackend'
SMS_BACKEND_LOCMEM = 'smsish.sms.backends.locmem.SMSBackend'
SMS_BACKEND_MAILTRAP = 'smsish.sms.backends.mailtrap.SMSBackend'
SMS_BACKEND_RQ = 'smsish.sms.backends.rq.SMSBackend'
SMS_BACKEND_TWILIO = 'smsish.sms.backends.twilio.SMSBackend'
SMS_BACKEND = os.getenv("SMS_BACKEND", SMS_BACKEND_CONSOLE)

# Set Twilio settings if needed.
# Note: `pip install twilio` to use the Twilio backend.
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", None)
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", None)
TWILIO_MAGIC_FROM_NUMBER = "+15005550006"  # This number passes all validation.
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER", TWILIO_MAGIC_FROM_NUMBER)

if 'django_rq' in INSTALLED_APPS:
    RQ_QUEUES = {
        'default': {
            'URL': os.getenv("REDIS_URL", None),
        },
    }
    if DEBUG or TESTING:
        if DEBUG or TESTING:
            for queueConfig in RQ_QUEUES.values():
                queueConfig['ASYNC'] = False

SMS_BACKEND = SMS_BACKEND_MAILTRAP
if SMS_BACKEND == SMS_BACKEND_RQ:
    SMSISH_RQ_SMS_BACKEND = SMS_BACKEND_CONSOLE
    SMSISH_RQ_SMS_BACKEND = os.getenv("SMSISH_RQ_SMS_BACKEND", SMS_BACKEND_CONSOLE)
elif SMS_BACKEND == SMS_BACKEND_MAILTRAP:
    SMSISH_MAILTRAP_SMS_BACKEND_EMAIL_BACKEND = "smsish.mail.backends.mailtrap.EmailBackend"

MAILTRAP_EMAIL_HOST = os.getenv("MAILTRAP_EMAIL_HOST", "mailtrap.io")
MAILTRAP_EMAIL_HOST_USER = os.getenv("MAILTRAP_EMAIL_HOST_USER", None)
MAILTRAP_EMAIL_HOST_PASSWORD = os.getenv("MAILTRAP_EMAIL_HOST_PASSWORD", None)
MAILTRAP_EMAIL_HOST_PORT = os.getenv("MAILTRAP_EMAIL_HOST_PORT", "2525")
