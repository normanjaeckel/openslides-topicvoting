#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .slides import *
from .urls import urlpatterns


VERSION = '1.0b2'
RELEASE = False

BASE_URL = 'topicvoting'
URLPATTERS = urlpatterns

def get_version():
    if RELEASE:
        return VERSION
    else:
        return '%s-dev' % VERSION
