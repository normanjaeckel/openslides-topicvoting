#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Class and function for the voting system.
"""

from operator import attrgetter

from openslides.config.api import config

from .models import Category


class Hoechstzahl(object):
    """
    An object represents one hoechstzahl in the Sainte-Laguë method.
    """
    all_hoechstzahls = []

    def __init__(self, category, rank):
        try:
            self.topic = category.topic_set.order_by('-votes', '-weight')[rank]
        except IndexError:
            return
        else:
            self.__class__.all_hoechstzahls.append(self)
        divisor = rank * 2 + 1
        self.value = float(category.sum_of_votes) / divisor

    @classmethod
    def get_results(cls):
        """
        Generator to get all hoechstzahl objects in the winning order.
        """
        cls.all_hoechstzahls.sort(key=attrgetter('value', 'topic.category.weight'), reverse=True)
        for hoechstzahl in cls.all_hoechstzahls:
            yield hoechstzahl

    @classmethod
    def get_result_table(cls):
        """
        Returns a nested list (table) with all hoechstzahls ordered by value.
        It has only as many columns as there are posts.
        """
        result_table = []
        all_categories = sorted(Category.objects.all(), key=attrgetter('sum_of_votes', 'weight'), reverse=True)
        for category in all_categories:
            category_list = []
            category_hoechstzahls = filter(lambda hoechstzahl: hoechstzahl.topic.category == category, cls.all_hoechstzahls)
            category_hoechstzahls.sort(key=lambda hoechstzahl: hoechstzahl.value, reverse=True)
            # TODO: Use a map here?
            for hoechstzahl in category_hoechstzahls:
                category_list.append(hoechstzahl)
            category_list += (config['openslides_topicvoting_posts'] - len(category_list)) * [None]
            result_table.append(category_list)
        return result_table


def feed_hoechstzahls():
    # Clear existing hoechstzahls
    Hoechstzahl.all_hoechstzahls = []
    for category in Category.objects.all():
        for rank in range(config['openslides_topicvoting_posts']):
            Hoechstzahl(category=category, rank=rank)
