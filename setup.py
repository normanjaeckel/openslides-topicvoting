#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for the Topic Voting Plugin for OpenSlides.
"""

from setuptools import setup, find_packages

FILEDIR = os.path.dirname(__file__)


with open(os.path.join(FILEDIR, 'openslides_topicvoting', 'NAME')) as metadata_file:
    NAME = metadata_file.read().strip()


with open(os.path.join(FILEDIR, 'openslides_topicvoting', 'VERSION')) as metadata_file:
    VERSION = metadata_file.read().strip()


with open(os.path.join(FILEDIR, 'openslides_topicvoting', 'DESCRIPTION')) as metadata_file:
    DESCRIPTION = metadata_file.read().strip()


with open(os.path.join(FILEDIR, 'README.rst')) as readme:
    long_description = readme.read()


with open(os.path.join(FILEDIR, 'requirements_production.txt')) as requirements_production:
    install_requires = requirements_production.readlines()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author='Team of Topic Voting Plugin for OpenSlides, see AUTHORS',
    author_email='openslides-topicvoting@normanjaeckel.de',
    url='https://github.com/normanjaeckel/openslides-topicvoting',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2'],
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=install_requires)
