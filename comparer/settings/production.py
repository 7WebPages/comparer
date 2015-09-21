"""Production settings and globals."""

from __future__ import absolute_import

# from os import environ
from os.path import join, normpath

from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
# from django.core.exceptions import ImproperlyConfigured


# def get_env_setting(setting):
#     """ Get the environment setting or return exception """
#     try:
#         return environ[setting]
#     except KeyError:
#         error_msg = "Set the %s env variable" % setting
#         raise ImproperlyConfigured(error_msg)

# HOST CONFIGURATION
DEBUG = True
# See:
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['.comparer-f8a6d5.herokuapp.com']
# END HOST CONFIGURATION

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
# EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
# EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
# EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
# EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
# EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
# EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
# SERVER_EMAIL = EMAIL_HOST_USER
# END EMAIL CONFIGURATION

# DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
# END DATABASE CONFIGURATION


# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# END CACHE CONFIGURATION
