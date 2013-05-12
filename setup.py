#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for the Topic Voting Plugin for OpenSlides.
"""

from setuptools import setup, find_packages

from openslides_topicvoting import NAME, VERSION, DESCRIPTION


with open('README.txt') as readme:
    long_description = readme.read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author='Team of Topic Voting Plugin for OpenSlides, see AUTHORS',
    author_email='openslides-topicvoting@normanjaeckel.de',
    url='https://github.com/normanjaeckel/openslides-topicvoting',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2'],
    license='MIT',
    install_requires='openslides==1.4')
