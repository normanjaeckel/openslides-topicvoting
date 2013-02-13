#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Model classes for categories and topics.
"""

from django.db import models

from openslides.projector.projector import SlideMixin


class Category(models.Model, SlideMixin):
    name = models.CharField(max_length=255)
    weight = models.IntegerField(default=0)

    prefix = 'topicvotingcategory'  # prefix for the slides, - and _ is not allowed

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        """
        Method for representation in Django.
        """
        return self.name

    @models.permalink
    def get_absolute_url(self, link='update'):
        """
        Gets the url of the update view or the delete view of a category instance.
        """
        if link == 'update':
            return ('topic_voting_category_update', [str(self.id)])
        if link == 'delete':
            return ('topic_voting_category_delete', [str(self.id)])

    def get_sum_of_votes(self):
        _sum = 0
        for topic in self.topic_set.all():
            if topic.votes:
                _sum += topic.votes
        return _sum

    sum_of_votes = property(get_sum_of_votes)

    def slide(self):
        """
        Returns a map with the data for the model slides.
        """
        return {
            'category': self,
            'title': 'Kategorie',
            'template': 'topic_voting/category_slide.html'}


class Topic(models.Model):
    title = models.CharField(max_length=255)
    submitter = models.CharField(max_length=255)  # To do: change here to a person
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    votes = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(default=0)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        """
        Method for representation in Django.
        """
        return '%s (Vorschlag von %s)' % (self.title, self.submitter)

    @models.permalink
    def get_absolute_url(self, link='update'):
        """
        Gets the url of the update view or the delete view of a topic instance.
        """
        if link == 'update':
            return ('topic_voting_topic_update', [str(self.id)])
        if link == 'delete':
            return ('topic_voting_topic_delete', [str(self.id)])

    def winner_output(self):
        """
        Gets the title and the votes if there are some.
        """
        if self.votes is not None:
            return '%s (%d)' % (self.title, self.votes)
        else:
            return self.title
