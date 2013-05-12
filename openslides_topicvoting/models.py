#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Model classes for categories and topics.
"""

from django.db import models

from openslides.projector.projector import SlideMixin


class Category(models.Model, SlideMixin):
    """
    The model for categories of topics.
    """

    name = models.CharField(max_length=255)
    """A string, the name of the category of topics."""

    weight = models.IntegerField(default=0)
    """
    An integer. A higher value prioritises the category in result view
    and slide. This can be used if there was a runoff poll.
    """

    prefix = 'topicvotingcategory'
    """The prefix for the slides, hyphen and underscore are not allowed."""

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        """
        Method for representation.
        """
        return self.name

    @models.permalink
    def get_absolute_url(self, link='update'):
        """
        Gets the url of the update view or the delete view of a category instance.
        """
        if link == 'update':
            return ('topicvoting_category_update', [str(self.id)])
        if link == 'delete':
            return ('topicvoting_category_delete', [str(self.id)])

    @property
    def sum_of_votes(self):
        """
        Returns the sum of all votes of the topic of a category.
        """
        sum_of_votes = 0
        for topic in self.topic_set.all():
            if topic.votes:
                sum_of_votes += topic.votes
        return sum_of_votes

    def slide(self):
        """
        Returns a dictionary with the data for the model slides.
        """
        return {
            'category': self,
            'title': 'Kategorie',
            'template': 'openslides_topicvoting/category_slide.html'}


class Topic(models.Model):
    """
    The model for topics.
    """

    title = models.CharField(max_length=255)
    """A string, the name of the topic."""

    submitter = models.CharField(max_length=255)  # TODO: Change this to a person field
    """A string, the name of the submitter of the topic."""

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    """
    A foreign key to a category the topic belongs to. If it is None, the
    topic is a ‘lost topic’. Deleting a category will become their topics
    lost.
    """

    votes = models.IntegerField(null=True, blank=True)
    """
    An integer, the votes for this topic. The OpenSlides poll system is
    not available yet.
    """

    weight = models.IntegerField(default=0)
    """
    An integer. A higher value prioritises the topic in result view
    and slide. This can be used if there was a runoff poll.
    """

    class Meta:
        ordering = ('title',)
        permissions = (
            # ('can_see', 'Can see categories and topics'),
            ('can_manage', 'Can manage categories an topics'),)

    def __unicode__(self):
        """
        Method for representation.
        """
        return '%s (Vorschlag von %s)' % (self.title, self.submitter)

    @models.permalink
    def get_absolute_url(self, link='update'):
        """
        Gets the url of the update view or the delete view of a topic instance.
        """
        if link == 'update':
            return ('topicvoting_topic_update', [str(self.id)])
        if link == 'delete':
            return ('topicvoting_topic_delete', [str(self.id)])

    def get_title_with_votes(self):
        """
        Gets the title and the votes if there are some.
        """
        if self.votes is not None:
            return '%s (%d)' % (self.title, self.votes)
        else:
            return self.title