#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Slides for an overview of all categories and for the results.
"""

from openslides.config.api import config
from openslides.projector.api import register_slidemodel, register_slidefunc

from .models import Category
from .voting_system import Hoechstzahl, feed_hoechstzahls


def overview_slide():
    """
    Slide with all categories. Similar to ListView. Lost topics are not shown.
    """
    return {
        'title': 'Alle Kategorien',
        'template': 'openslides_topicvoting/overview_slide.html',
        'category_list': Category.objects.all()}


def result_slide():
    """
    Slide for a table with all results. The winning topics are given too.
    """
    feed_hoechstzahls()
    results_generator = Hoechstzahl.get_results()
    winning_topics = []
    topic_post_warning = False
    for i in range(config['openslides_topicvoting_posts']):
        try:
            winning_topics.append(results_generator.next())
        except StopIteration:
            topic_post_warning = True
            break
    return {
        'title': 'Ergebnisse',
        'template': 'openslides_topicvoting/result_slide.html',
        'result_table': Hoechstzahl.get_result_table(),
        'winning_topics': winning_topics,
        'divisors': map(lambda rank: rank * 2 + 1, range(config['openslides_topicvoting_posts'])),
        'topic_post_warning': topic_post_warning}


register_slidemodel(Category)
register_slidefunc('topicvotingoverview', overview_slide, name='Alle Kategorien')
register_slidefunc('topicvotingresult', result_slide, name='Ergebnisse')
