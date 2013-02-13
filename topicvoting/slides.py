#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Slides for an overview of all categories and for the winners.
"""

from openslides.projector.api import register_slidemodel, register_slidefunc

from .models import Category
from .voting_system import Hoechstzahl, feed_hoechstzahls, POSTS


def overview_slide():
    """
    Slide with all categories. Similar to ListView.
    """
    return {
        'title': 'Alle Kategorien',
        'template': 'topic_voting/overview_slide.html',
        'category_list': Category.objects.all()}


def result_slide():
    """
    Slide for a table with all results. The winning topics are given too.
    """
    feed_hoechstzahls()
    results_generator = Hoechstzahl.get_results()
    winning_topics = []
    topic_post_warning = False
    for i in range(POSTS):
        try:
            winning_topics.append(results_generator.next())
        except StopIteration:
            topic_post_warning = True
            break
    return {
        'title': 'Ergebnisse',
        'template': 'topic_voting/result_slide.html',
        'winners_table': Hoechstzahl.get_result_table(),
        'winning_topics': winning_topics,
        'divisors': map(lambda rank: rank * 2 + 1, range(POSTS)),
        'topic_post_warning': topic_post_warning}


register_slidemodel(Category)
register_slidefunc('topicvotingoverview', overview_slide, name='Alle Kategorien')
register_slidefunc('topicvotingresult', result_slide, name='Ergebnisse')
