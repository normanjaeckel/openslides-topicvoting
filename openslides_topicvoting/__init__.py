#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from . import signals
from . import slides
from .urls import urlpatterns

BASE_URL = 'openslides_topicvoting'  # TODO: Rename to topicvoting when the functionality is implemented in OpenSlides
URLPATTERS = urlpatterns
FILEDIR = os.path.dirname(__file__)


with open(os.path.join(FILEDIR, 'NAME')) as metadata_file:
    NAME = metadata_file.read().strip()


with open(os.path.join(FILEDIR, 'VERSION')) as metadata_file:
    VERSION = metadata_file.read().strip()


with open(os.path.join(FILEDIR, 'DESCRIPTION')) as metadata_file:
    DESCRIPTION = metadata_file.read().strip()


def get_name():
    """
    Function for OpenSlides' version page.
    """
    return '%s (%s)' % (DESCRIPTION, NAME)
