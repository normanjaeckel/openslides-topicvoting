#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Url patterns
"""

from django.conf.urls import url, patterns

from .views import \
    TopicvotingCategoryListView, \
    TopicvotingCategoryCreateView, \
    TopicvotingCategoryUpdateView, \
    TopicvotingCategoryDeleteView, \
    TopicvotingTopicCreateView, \
    TopicvotingTopicUpdateView, \
    TopicvotingTopicDeleteView, \
    TopicvotingResultView


urlpatterns = patterns('',

    # Category
    url(r'^$',
        TopicvotingCategoryListView.as_view(),
        name='topic_voting_category_list',),
    url(r'^category/create/$',
        TopicvotingCategoryCreateView.as_view(),
        name='topic_voting_category_create',),
    url(r'^category/(?P<pk>\d+)/update/$',
        TopicvotingCategoryUpdateView.as_view(),
        name='topic_voting_category_update',),
    url(r'^category/(?P<pk>\d+)/delete/$',
        TopicvotingCategoryDeleteView.as_view(),
        name='topic_voting_category_delete',),

    # Topic
    url(r'^topic/create/$',
        TopicvotingTopicCreateView.as_view(),
        name='topic_voting_topic_create',),
    url(r'^topic/(?P<pk>\d+)/update/$',
        TopicvotingTopicUpdateView.as_view(),
        name='topic_voting_topic_update',),
    url(r'^topic/(?P<pk>\d+)/delete/$',
        TopicvotingTopicDeleteView.as_view(),
        name='topic_voting_topic_delete',),

    # Ballot paper
    url(r'^ballotpaper/$',
        TopicvotingCategoryListView.as_view(template_name='topic_voting/ballotpaper.html'),
        name='topic_voting_ballotpaper'),

    # Voting results
    url(r'^result/$',
        TopicvotingResultView.as_view(),
        name='topic_voting_result'),
)
