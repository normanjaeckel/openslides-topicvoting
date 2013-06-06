#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import signals
from . import slides
from .urls import urlpatterns


NAME = 'openslides-topicvoting'
VERSION = '1.0b1-dev'
DESCRIPTION = 'Topic Voting Plugin for OpenSlides'
BASE_URL = 'openslides_topicvoting'  # TODO: Rename to topicvoting when the functionality is implemented in OpenSlides
URLPATTERS = urlpatterns


def get_name():
    """
    Function for OpenSlides' version page.
    """
    return '%s (%s)' % (DESCRIPTION, NAME)
