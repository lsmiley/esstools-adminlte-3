"""
Django settings for django_adminlte3 project.

Generated by 'django-admin startproject' using Django 3.0b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k$v*ssgjspcgakja4u4yo-$=e6^#!wkns4rh6be7fd#m(ivg8('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'adminlte3',
    'adminlte3_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_tables2',
    'rest_framework',
    'django_ajax',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'category',
    'product',
    'order',
    'orderitem',
    'acctcust.apps.AcctcustConfig',
    'prodvendor.apps.ProdvendorConfig',
    'configmaster.apps.ConfigmasterConfig',
    'configtable.apps.ConfigtableConfig',
    'labordeliverytype.apps.LabordeliverytypeConfig',
    'labordelivery.apps.LabordeliveryConfig',
    'statusstate',
    'tntworksheet',

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


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

ROOT_URLCONF = 'django_adminlte3.urls'

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

WSGI_APPLICATION = 'django_adminlte3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# **** Local Database Settings ****
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'esstools-adminlte-3-db',
#         'USER': 'sizingadmin',
#         'PASSWORD': 'Malware12345',
#         'HOST': '127.0.0.1',
#         'PORT': '6326',
#     }
# }

# **** Cloud Database Settings ****
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'esstools-adminlte-3-db',
        'USER': 'sizingadmin',
        'PASSWORD': 'Malware12345',
        'HOST': '10.131.4.48',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
# STATICFILES_DIRS = [
#      os.path.join(BASE_DIR+'/bower_components'),
# ]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'

CURRENCY = 'Hrs'


####################################
    ##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
    },
}