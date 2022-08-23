"""
Django settings for bigfoot_django project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import json
import base64
from pathlib import Path

# This variable should always match the primary database relationship name,
#   configured in .platform.app.yaml.
PLATFORMSH_DB_RELATIONSHIP="database"


from platformshconfig import Config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '90ny91c0)^1zl=_tr%6r%edy9-hn%2yssqg_wd3*sr@+8941*z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'seneque.lan',
    '192.168.86.249',
    '.platformsh.site',
]


# Application definition

INSTALLED_APPS = [
    'bigfoot',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'bigfoot_django.urls'

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

WSGI_APPLICATION = 'bigfoot_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bigfoot',
        'USER': 'bigfoot',
        'PASSWORD': 'bigfoot',
        'HOST': 'localhost',
        'PORT': '5432',
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

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# Default STATIC_ROOT, i.e. for local testing.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#################################################################################
# Platform.sh-specific configuration
# Helper function for decoding base64-encoded JSON variables.
@staticmethod
def decode(variable):
    """Decodes a Platform.sh environment variable.
    Args:
        variable (string):
            Base64-encoded JSON (the content of an environment variable).
    Returns:
        An dict (if representing a JSON object), or a scalar type.
    Raises:
        JSON decoding error.
    """
    try:
        if sys.version_info[1] > 5:
            return json.loads(base64.b64decode(variable))
        else:
            return json.loads(base64.b64decode(variable).decode('utf-8'))
    except json.decoder.JSONDecodeError:
        print('Error decoding JSON, code %d', json.decoder.JSONDecodeError)

# Import some Platform.sh settings from the environment.
if (os.getenv('PLATFORM_APPLICATION_NAME') is not None):
    DEBUG = False
    if (os.getenv('PLATFORM_APP_DIR') is not None):
        STATIC_ROOT = os.path.join(os.getenv('PLATFORM_APP_DIR'), 'static')
    if (os.getenv('PLATFORM_PROJECT_ENTROPY') is not None):
        SECRET_KEY = config.projectEntropy
    # Database service configuration, post-build only.
    if (os.getenv('PLATFORM_ENVIRONMENT') is not None):
        platformRelationships = decode(os.getenv('PLATFORM_RELATIONSHIPS'))
        db_settings = platformRelationships[PLATFORMSH_DB_RELATIONSHIP][0]
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': db_settings['path'],
                'USER': db_settings['username'],
                'PASSWORD': db_settings['password'],
                'HOST': db_settings['host'],
                'PORT': db_settings['port'],
            },
            'sqlite': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
