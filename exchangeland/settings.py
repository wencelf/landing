"""
Django settings for exchangeland project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8m=i+q#2!a9c#4qq5#87r+wuqpek*fyb%-&i%20nsv(2my_@v('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'landing',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'exchangeland.urls'

WSGI_APPLICATION = 'exchangeland.wsgi.application'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'd5u401mgrj8ce5',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'lxkxfqgzezlofi',
        'PASSWORD': 'usvV36CdwZsayZoxxmJf9vLMkU',
        'HOST': 'ec2-23-21-231-14.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
        
    }
}
######Comment this for development enviroment############
#Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


MEDIA_ROOT = '/media/'
STATIC_ROOT = '/static/'
DEFAULT_FILE_STORAGE = 'landing.s3utils.FixedS3BotoStorage'
STATICFILES_STORAGE = 'landing.s3utils.FixedS3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAJOWFPQTYY5NA3AZA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'landing-exchange' #For development
AWS_PRELOAD_METADATA = True
S3_URL = 'http://s3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME + '/'
COMPRESS_URL = "https://s3.amazonaws.com/landing-exchange/" #development
STATIC_URL = COMPRESS_URL
MEDIA_URL = S3_URL + MEDIA_ROOT
AWS_QUERYSTRING_AUTH = False

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@startupessentials.co'
EMAIL_HOST_PASSWORD = 'St4rtupEssenti4ls1'
 
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
