#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Signals for config variables.
"""

from django import forms
from django.dispatch import receiver

from openslides.config.api import ConfigVariable, ConfigPage
from openslides.config.signals import config_signal


@receiver(config_signal, dispatch_uid='setup_openslides_topicvoting_config')
def setup_openslides_topicvoting_config(sender, **kwargs):
    """
    Config variables:
        * openslides_topicvoting_posts
        * openslides_topicvoting_ballotpaper_title
        * openslides_topicvoting_ballotpaper_text
    """
    posts = ConfigVariable(
        name='openslides_topicvoting_posts',
        default_value=8,
        form_field=forms.IntegerField(
            label='Anzahl der zu wählenden Themen',
            min_value=1,
            help_text='In der Ergebnistabelle wird die Anzahl der zu wählenden Themen '
                      'von vorn beginnend als Gewinner hervorgehoben.'))

    ballotpaper_title = ConfigVariable(
        name='openslides_topicvoting_ballotpaper_title',
        default_value='Wahlen der Themenabende',
        form_field=forms.CharField(
            required=False,
            label='Titel des Wahlzettels'))

    ballotpaper_text = ConfigVariable(
        name='openslides_topicvoting_ballotpaper_text',
        default_value='Sie haben 5 Stimmen. Ein Thema kann bis zu 5 Stimmen '
                      'erhalten. Schreiben Sie die Zahl vor das jeweilige Thema.',
        form_field=forms.CharField(
            widget=forms.Textarea(),
            required=False,
            label='Erläuterung auf dem Wahlzettel'))

    return ConfigPage(title='Themenwahl',
                      url='openslides_topicvoting',
                      required_permission='openslides_topicvoting.can_manage',
                      weight=130,
                      variables=(posts, ballotpaper_title, ballotpaper_text))
