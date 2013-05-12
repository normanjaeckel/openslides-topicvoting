#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fabric file for development use.
"""

import os
import sys

from django.core import management

from fabric.api import local
from fabric.contrib import django


def start():
    """
    Starts OpenSlides installed in the python path.

    At the moment passing additional args to OpenSlides is not possible.
    """
    sys.path.insert(0, '')
    from openslides.main import main
    sys.argv.remove('start')
    main()


def pep8():
    """
    Checks for PEP 8 errors in openslides_topicvoting and in tests.
    """
    local('pep8 --max-line-length=150 --statistics openslides_topicvoting')
    local('pep8 --max-line-length=150 --statistics tests')


def test(module='tests'):
    """
    Runs the unit tests.
    """
    sys.path.insert(0, '')
    django.settings_module('tests.settings')
    sys.argv.pop()
    sys.argv.extend(['test', module])
    management.execute_from_command_line()


def prepare_commit():
    """
    Does everything that should be done before a commit.

    At the moment it is running the tests and check for PEP 8 errors.
    """
    test()
    pep8()
