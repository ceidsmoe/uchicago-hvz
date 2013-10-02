"""
Django settings for uchicagohvz project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
	from secrets import SECRET_KEY
except:
	SECRET_KEY = "SECRET KEY PLACEHOLDER"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'ckeditor', 'htmlpurifier',
	'mptt', 'localflavor', 'compressor', 'rest_framework', 'djcelery',
	'uchicagohvz.users', 'uchicagohvz.game',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'uchicagohvz.urls'

WSGI_APPLICATION = 'uchicagohvz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = False

USE_L10N = False

USE_TZ = True

# Templates
TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, "templates"),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, "static"),
)

# Django Compressor
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
)

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee -bcs'),
    ('text/less', 'lessc {infile} {outfile}'),
)

# Datetime settings
DATETIME_FORMAT = 'N j, Y g:i A'
SHORT_DATETIME_FORMAT = 'm/d/Y g:i A'

# User-uploaded media
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Authentication
AUTHENTICATION_BACKENDS = (
	'uchicagohvz.users.backend.UChicagoLDAPBackend',
)
LOGIN_URL = "/users/login/"
LOGIN_REDIRECT_URL = "/"

# HTTPS settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

# Message framework settings
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {
    message_constants.DEBUG: 'info',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger'
} # Bootstrap 3 alert integration

# Celery configuration
import djcelery
djcelery.setup_loader()
BROKER_URL = 'redis://localhost:6379/0'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'UChicago HvZ <noreply@uchicagohvz.org>'

# HvZ game configuration
HUMAN_KILL_POINTS = 1 # how many points killing a human is worth
HVT_KILL_POINTS = 5 # how many points a high-value target is worth (replaces regular human kill points)
HVD_KILL_POINTS = 5 # how many points a target from a high-value dorm is worth (can stack on top of regular and HVT points)
NEXMO_NUMBER = '339-204-1936'