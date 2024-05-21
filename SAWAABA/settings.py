"""
Django settings for SAWAABA project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from .env file
load_dotenv()


SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = os.environ["DEBUG"]

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS") #.split(" ")
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'travel.apps.TravelConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_q',
    'quran',
    'django_celery_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'SAWAABA.urls'

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

WSGI_APPLICATION = 'SAWAABA.wsgi.application'


# Database

DATABASES = {
    # 'default': {
    #     'ENGINE': os.environ['PG_DB_ENGINE'],
    #     'NAME': os.environ['PG_DB_NAME'],
    #     'USER': os.environ['PG_DB_USER'],
    #     'PASSWORD': os.environ['PG_DB_PASSWORD'],
    #     'HOST': os.environ['PG_DB_HOST'],
    #     'PORT': '5432'
    # }
}

import dj_database_url
database_url = os.environ["DATABASE_URL"]
DATABASES["default"] = dj_database_url.parse(database_url)


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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirect to home URL after login
LOGIN_REDIRECT_URL = '/travel/'

# Use the Django default authentication backend
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Email settings
EMAIL_BACKEND = os.environ['EMAIL_BACKEND']
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

# Media:
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# CELERY
from celery.schedules import crontab

CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}

CELERY_BEAT_SCHEDULE = {
    'notify-passport-expiry-every-5-minutes': {
        'task': 'travel.tasks.notify_passport_expiry',
        # 'schedule': crontab(hour=23, minute=59, day_of_month=1),
        'schedule': crontab(minute='*/5'),
    },
}

Q_CLUSTER = {
   'name': 'DjangORM',
   'workers': 4,
   'timeout': 90,
   'retry': 120,
   'queue_limit': 50,
   'bulk': 10,
   'orm': 'default',
}

APPOINTMENT_CLIENT_MODEL = 'auth.User'  # Deprecated
