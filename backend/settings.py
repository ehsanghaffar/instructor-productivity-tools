"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&24ubb46zaej*fd9jz1^mw1t0)-@zd9g74f!hcs1a48-7loo0r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Application definition

INSTALLED_APPS = [
    'backend.canvas_app_explorer',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'webpack_loader',
    'rest_framework',
    'pylti1p3.contrib.django.lti1p3_tool_config'

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

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'canvas_app_explorer_local'),
        'USER': os.getenv('DB_USER', 'cae_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'cae_pw'),
        'HOST': os.getenv('DB_HOST', 'canvas_app_explorer_mysql'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {'charset': 'utf8mb4'},
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci'
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/django_static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend'),
)

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/webpack-stats.json')
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DEFAULT_FILE_STORAGE = 'canvas_app_explorer.storage_get_file.DatabaseFileStorage'

# TODO: Switch this to CSP for additional security
X_FRAME_OPTIONS = 'ALLOWALL'

# So request works over the proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DB_CACHE_CONFIGS = os.getenv('DB_CACHE_CONFIGS',
                           {'CACHE_TTL': 600, 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
                            'LOCATION': 'django_app_explorer_cache',
                            'CACHE_KEY_PREFIX': 'app_explorer',
                            'CACHE_OPTIONS': {'COMPRESS_MIN_LENGTH': 5000, 'COMPRESS_LEVEL': 6}
                            })

CACHES = {
    'default': {
        'BACKEND': DB_CACHE_CONFIGS['BACKEND'],
        'LOCATION': DB_CACHE_CONFIGS['LOCATION'],
        'OPTIONS': DB_CACHE_CONFIGS['CACHE_OPTIONS'],
        "KEY_PREFIX": DB_CACHE_CONFIGS['CACHE_KEY_PREFIX'],
        "TIMEOUT": DB_CACHE_CONFIGS['CACHE_TTL']
    }
}