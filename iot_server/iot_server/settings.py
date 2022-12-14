"""
Django settings for iot_server project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import json
import requests
#import pyrebase


# def add_url_to_firebase(url):
#     print('setting')
#     firebaseConfig = {"apiKey": "AIzaSyACZIpVXpHPsHUdewz0UbLP63vS5ljm7V8",
#                       "authDomain": "testarduino-0000.firebaseapp.com",
#                       "projectId": "testarduino-0000",
#                       "databaseURL": "https://testarduino-0000-default-rtdb.asia-southeast1.firebasedatabase.app",
#                       "storageBucket": "testarduino-0000.appspot.com",
#                       "messagingSenderId": "849041339991",
#                       "appId": "1:849041339991:web:b0a8bd2d653201c1275512",
#                       "measurementId": "G-LJZW5X7QG5"
#                       }
#     firebase = pyrebase.initialize_app(firebaseConfig)
#
#     db = firebase.database()
#
#     db.child("raspserver").child("url").set(url)
#     print('setting is ok')
#
# def get_ngrok_url():
#     url = "http://localhost:4040/api/tunnels/"
#     res = requests.get(url)
#     res_unicode = res.content.decode("utf-8")
#     res_json = json.loads(res_unicode)
#     for i in res_json["tunnels"]:
#         if i['name'] == 'django':
#             return i['public_url']
#
# url_string = get_ngrok_url()
# print(url_string)
# add_url_to_firebase(url_string)




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tup*k0w-dx%%sg-a21n1%-2s^y!*3njorms_#*r@*fs-1kzz*x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'www.localhost',
    '*',
    '104.46.229.78',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'farm.apps.FarmConfig',
    'home.apps.HomeConfig',
    'rest_framework',
    'channels',
    'stream.apps.StreamConfig',
    'corsheaders',
    'crispy_forms',
    'bootstrap4'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


CORS_ALLOWED_ORIGIN = [
    "*"
]
CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'iot_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'iot_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, '/static/'),
# )
ASGI_APPLICATION = 'iot_server.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'iot-home-dashboard'