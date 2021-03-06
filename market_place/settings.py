"""
Django settings for market_place project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import MEDIA_ROOT

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#y6yf6cezo#wsrj3y5qdl+u(_4whm1*^!x0blxn%r^a9^%bx8c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '..','templates').replace('\\', '/'),
)

MEDIA_PATH= os.path.join(BASE_DIR, "media")

ALLOWED_HOSTS = []

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nishant@wedwise.in'
EMAIL_HOST_PASSWORD = 'Nishu@26'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'customer',
    'vendor',
    'wedwise_messages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'api.api_middleware.ApiMiddleware'
)

ROOT_URLCONF = 'market_place.urls'

WSGI_APPLICATION = 'market_place.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
from database_settings import DATABASES



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TASTYPIE_DEFAULT_FORMATS = ['json']
