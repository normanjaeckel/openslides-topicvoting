#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

from topicvoting import get_version()

setup(name='openslides-topicvoting',
      version=get_version(),
      description='This is an OpenSlides (http://openslides.org) plugin. It features a structured voting on topics using the Sainte-Laguë method.',
      author='See section ‘Authors’ in README.rst.',
      license='BSD',
      url='https://github.com/normanjaeckel/openslides-topicvoting',
      packages=['topicvoting',],
      package_data={'topicvoting': ['templates/topicvoting/*.html']},
      #classifiers=['foo', 'bar'],
      )