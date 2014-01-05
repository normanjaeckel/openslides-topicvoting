# -*- coding: utf-8 -*-

from openslides.global_settings import *  # noqa

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Set timezone
TIME_ZONE = 'Europe/Berlin'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'secret'

# Add OpenSlides plugins to this list
INSTALLED_PLUGINS = (
    'openslides_topicvoting',
)

INSTALLED_APPS += INSTALLED_PLUGINS

# Absolute path to the directory that holds media.
# Use path of this file for tests
MEDIA_ROOT = os.path.realpath(os.path.dirname(__file__))

# Path to Whoosh search index
# Use RAM storage for tests
HAYSTACK_CONNECTIONS['default']['STORAGE'] = 'ram'

# Use a faster passwort hasher for tests
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
