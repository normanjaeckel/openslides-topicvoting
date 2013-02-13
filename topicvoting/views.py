#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Views for categories and topics
"""

from django.core.urlresolvers import reverse

from openslides.utils.views import ListView, CreateView, UpdateView, DeleteView
from openslides.utils.template import Tab
from openslides.projector.projector import Widget, SLIDE

from .models import Category, Topic


class TopicvotingCategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(TopicvotingCategoryListView, self).get_context_data(**kwargs)
        context['lost_topics'] = Topic.objects.filter(category=None)
        return context


uebergangsloesung = 'topic_voting_category_list'  # Großer Mist hier, das ist keine URL, sondern es wird unerwarteterweise nochmal umgewandelt.


class TopicvotingCategoryCreateView(CreateView):
    model = Category
    success_url = uebergangsloesung
    apply_url = 'topic_voting_category_update'


class TopicvotingCategoryUpdateView(UpdateView):
    model = Category
    success_url = uebergangsloesung


class TopicvotingCategoryDeleteView(DeleteView):
    model = Category
    url = uebergangsloesung  # redirect


class TopicvotingTopicCreateView(CreateView):
    model = Topic
    success_url = uebergangsloesung
    apply_url = 'topic_voting_topic_update'


class TopicvotingTopicUpdateView(UpdateView):
    model = Topic
    success_url = uebergangsloesung


class TopicvotingTopicDeleteView(DeleteView):
    model = Topic
    url = uebergangsloesung  # redirect


class TopicvotingResultView(TopicvotingCategoryListView):
    template_name = 'topic_voting/results.html'

    def get_context_data(self, **kwargs):
        context = super(TopicvotingResultView, self).get_context_data(**kwargs)
        context['foobar'] = 'foobar'  # To do: Insert winner table here
        return context


def register_tab(request):
    """
    Registers the tab.
    """
    return Tab(
        title='Themenwahl',
        url=reverse('topic_voting_category_list'),
        selected=request.path.startswith('/topic-voting/'))


def get_widgets(request):
    """
    Returns the widget.
    """
    return [Widget(
        name='topic_voting',
        display_name='Themenwahl',
        template='topic_voting/category_widget.html',
        context={'overview_slide': SLIDE['topicvotingoverview'],
                 'result_slide': SLIDE['topicvotingresult'],
                 'category_list': Category.objects.all()},
        permission_required='projector.can_manage_projector',
        default_column=1)]
