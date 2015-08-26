# coding=utf-8
"""
Django settings for pratosocial project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
from decouple import config

SECRET_KEY = config('SECRET_KEY')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (os.path.join(MEDIA_ROOT, 'static'),)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
ADMINS = (
    ('Erivanio Vasconcelos', 'erivanio.vasconcelos@gmail.com')
)

MANAGERS = ADMINS

DEBUG = config('DEBUG')

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'pratosocial.context_processor.statics',
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect'
)

INSTALLED_APPS = (
    'flat',
    'easy_thumbnails',
    'image_cropping',
    'widget_tweaks',
    'ckeditor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_comments',
    'social.apps.django_app.default',
    'annoying',
    'taggit',
    'daterange_filter',
    'apps.core',
    'apps.website',
    'apps.recipe'
)

COMMENTS_APP = 'apps.recipe'

AUTH_USER_MODEL = 'core.User'

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ROOT_URLCONF = 'pratosocial.urls'

WSGI_APPLICATION = 'pratosocial.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.instagram.InstagramOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'apps.core.pipeline.social_user',
    'social.pipeline.user.get_username',
    # 'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

SOCIAL_AUTH_FACEBOOK_KEY = config('FACEBOOK_KEY')

SOCIAL_AUTH_FACEBOOK_SECRET = config('FACEBOOK_SECRET')

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_photos']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_OAUTH2_KEY')

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_USE_DEPRECATED_API = True

SOCIAL_AUTH_GOOGLE_PLUS_USE_DEPRECATED_API = True

SOCIAL_AUTH_INSTAGRAM_KEY = config('INSTAGRAM_KEY')

SOCIAL_AUTH_INSTAGRAM_SECRET = config('INSTAGRAM_SECRET')

SOCIAL_AUTH_INSTAGRAM_AUTH_EXTRA_ARGUMENTS = {'scope': 'basic likes'}

SOCIAL_AUTH_INSTAGRAM_REDIRECT_URL = 'http://beta.pratosocial.com.br/complete/instagram/'

SOCIAL_AUTH_USER_MODEL = 'core.User'

# SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email', ]

# FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'pt_BR'}

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', cast=int),
    }
}

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_PWD')
EMAIL_SUBJECT_PREFIX = config('EMAIL_SUBJECT_PREFIX')
EMAIL_USE_TLS = config('EMAIL_TLS', cast=bool)
EMAIL_PORT = config('EMAIL_PORT', cast=int)


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CKEDITOR_UPLOAD_PATH = 'uploads/ckeditor'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            {'name': 'clipboard',  'items': ['Undo', 'Redo']},
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'RemoveFormat']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent']},
            {'name': 'tools', 'items': ['Maximize']}
        ],
    },
}

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

