================================
 OpenSlides Topic Voting Plugin
================================

Overview
========

This plugin for OpenSlides features a structured voting on topics using the
Sainte-Laguë method.


Requirements
============

OpenSlides 1.6.x (http://openslides.org/)


Install
=======

This is only an example instruction to install the plugin on GNU/Linux. It
can also be installed as any other python package and on other platforms,
e. g. on Windows.

Change to a new directory::

    $ cd

    $ mkdir OpenSlides

    $ cd OpenSlides

Setup and activate a virtual environment::

    $ virtualenv .virtualenv

    $ source .virtualenv/bin/activate

Install OpenSlides and the plugin from the Python Package Index (PyPI)::

    $ pip install openslides-topicvoting==1.1.0  # or pip install <NAME_OF_ARCHIVE_FILE>

Start OpenSlides once to create its settings file if it does not exist yet::

    $ openslides

Stop OpenSlides::

    CTRL + C

Edit the file ``settings.py``. You can find it in the directory
``openslides`` in your user config path given in the environment variable
``$XDG_CONFIG_HOME``. Default is ``~/.config/openslides/`` on GNU/Linux and
``$HOME\AppData\Local\openslides\`` on Windows. Insert the line
``'openslides_topicvoting',`` into the INSTALLED_PLUGINS tuple::

    # Add OpenSlides plugins to this tuple
    INSTALLED_PLUGINS = (
        'openslides_topicvoting',
    )

Restart OpenSlides::

    $ openslides


License and authors
===================

This plugin is released under the MIT License, see LICENSE file. The
authors of this plugin are mentioned in the AUTHORS file.


Changelog
=========

Version 1.1.0 (unreleased)
--------------------------
- Updated to new plugin api of OpenSlides 1.6.
- Updated to new apis of OpenSlides 1.6 (slides urls, views, widget, main menu entry).
- Added winners as list to result view and slide.
- Changed several template files and updated some code styling stuff.


Version 1.0 (2014-01-04)
------------------------
- First release of this plugin.
