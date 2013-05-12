====================================
 Topic Voting Plugin for OpenSlides
====================================

This plugin features a structured voting on topics using the
Sainte-Laguë method.


Requirements
============

OpenSlides 1.4 (http://openslides.org)


Install
=======

1. Install OpenSlides into a virtual environment, see INSTALL.txt of OpenSlides.

2. Activate this virtual environment:

    $ source .venv/bin/activate

3. Install the CSV Export Plugin for OpenSlides from the Python Package Index:

    $ pip install openslides-topicvoting

4. Start OpenSlides once to create its settings file:

    $ openslides

5. Edit the settings file. You can find in the directory openslides in your
   user config path given in the environment variable $XDG_CONFIG_HOME.
   Default is ~/.config/openslides on GNU/Linux and $HOME\AppData\Local\openslides
   on Windows. Insert the line 'openslides_topicvoting,' into the INSTALLED_PLUGINS
   tuple.

6. Synchronize the database to add the new tables:

    $ openslides --syncdb

7. Restart OpenSlides.
