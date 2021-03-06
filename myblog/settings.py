"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '632a5v(hpmjm@z2b7!69h7po*ffkbi+=&g74^7+i()s-8bzkyb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'gallery.apps.GalleryConfig',
    'crispy_forms',
    'thumbnails',
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

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog/templates/blog')],
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

# THUMBNAILS = {
#     'METADATA': {
#         'BACKEND': 'thumbnails.backends.metadata.DatabaseBackend',
#     },
#     'STORAGE': {
#         'BACKEND': 'django.core.files.storage.FileSystemStorage',
#         # You can also use Amazon S3 or any other Django storage backends
#     },
#     'SIZES': {
#         'small': {
#             'PROCESSORS': [
#                 {'PATH': 'thumbnails.processors.resize', 'width': 10, 'height': 10},
#                 {'PATH': 'thumbnails.processors.crop', 'width': 80, 'height': 80}
#             ],
#             'POST_PROCESSORS': [
#                 {
#                     'processor': 'thumbnails.post_processors.optimize',
#                     'png_command': 'optipng -force -o7 "%(filename)s"',
#                     'jpg_command': 'jpegoptim -f --strip-all "%(filename)s"',
#                 },
#             ],
#         },
#         'large': {
#             'PROCESSORS': [
#                 {'PATH': 'thumbnails.processors.resize', 'width': 20, 'height': 20},
#                 {'PATH': 'thumbnails.processors.flip', 'direction': 'horizontal'}
#             ],
#         }
#     }
# }

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Sofia'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/blog/"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


