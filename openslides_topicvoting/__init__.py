#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import signals
from . import slides
from .urls import urlpatterns


NAME = 'openslides-topicvoting'
VERSION = '1.4b1-dev'
DESCRIPTION = 'Topic Voting Plugin for OpenSlides'
BASE_URL = 'openslides-topicvoting'  # TODO: Rename to topicvoting
URLPATTERS = urlpatterns


def get_name():
    """
    Function for OpenSlides' version page.
    """
    return '%s (%s)' % (DESCRIPTION, NAME)
