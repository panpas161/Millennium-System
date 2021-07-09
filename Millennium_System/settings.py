"""
Django settings for Millennium_System project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime
import time
import mimetypes
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ztd0_ycg@e@4^mtb4y61narbk-i5)j!dh0!0gox)ar1e)m68-u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'login',
    'main',
    'students',
    'cash_register',
    'administrator',
    'efet',
    'farmingcert',
    'teachers',
    'securityexperts',
    'robotics',
    'blankpixel',
    'staff',
    'espa',
    'associate',
    'landing_page',
    'general_settings',
    'system_settings'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Millennium_System.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"),os.path.join(BASE_DIR,"assets/templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        'libraries':{
            'tags':'templatetags.tags',
            'render':'templatetags.render'
        }
        },
    },
]

WSGI_APPLICATION = 'Millennium_System.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'milsystem',
       'USER': 'postgres',
       'PASSWORD': 'postgres',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#MIME TYPES
mimetypes.add_type("text/javascript", ".js", True)
mimetypes.add_type("text/css", ".css", True)

#Additional Settings
DEFAULT_AUTO_FIELD='django.db.models.AutoField' #for id in each model

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,"assets")
MEDIA_URL = '/files/'
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
IMAGES_URL = '/images/'
IMAGES_ROOT = os.path.join(BASE_DIR, "assets/images/")
STYLE_URL = "/styles/"
STYLE_ROOT = os.path.join(BASE_DIR, "assets/style")
SCRIPT_URL = "/scripts/"
SCRIPT_ROOT = os.path.join(BASE_DIR, "assets/script")
BOOTSTRAP_URL = "/bootstrap/"
BOOTSTRAP_ROOT = os.path.join(BASE_DIR,"assets/bootstrap/")

#Date settings
DATE_FORMAT = '%d/%m/%Y'
TIMEZONE = "Test"#later it will be added for user to set custom date and time
CURRENT_DATE = datetime.datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = time.strftime("%H:%M:%S", time.localtime()) #note it's local time
PREVIOUS_SCHOOL_YEAR = str(datetime.date.today().year-1) + "-" + str(datetime.date.today().year)
CURRENT_SCHOOL_YEAR = str(datetime.date.today().year) + "-" + str(datetime.date.today().year + 1)

#Email Settings
EMAIL_HOST = 'mail.blankpixel.gr'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'palles@blankpixel.gr'
EMAIL_HOST_PASSWORD = 'n6Xo=e#%AGv]'
EMAIL_USE_TLS = True
