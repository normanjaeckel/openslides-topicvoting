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
    """
    View to list all categories with all topics. The lost topics are also
    included.
    """
    model = Category

    def get_context_data(self, **kwargs):
        context = super(TopicvotingCategoryListView, self).get_context_data(**kwargs)
        context['lost_topics'] = Topic.objects.filter(category=None)
        return context


class TopicvotingCategoryCreateView(CreateView):
    model = Category
    success_url_name = 'topic_voting_category_list'
    apply_url_name = 'topic_voting_category_list'  # TODO: Remove this when openslides/utils/views.py changed from 'edit' to 'update'.


class TopicvotingCategoryUpdateView(UpdateView):
    model = Category
    success_url_name = 'topic_voting_category_list'


class TopicvotingCategoryDeleteView(DeleteView):
    model = Category
    success_url_name = 'topic_voting_category_list'  # TODO: Check this.


class TopicvotingTopicCreateView(CreateView):
    model = Topic
    success_url_name = 'topic_voting_category_list'
    apply_url_name = 'topic_voting_category_list'  # TODO: Remove this when openslides/utils/views.py changed from 'edit' to 'update'.


class TopicvotingTopicUpdateView(UpdateView):
    model = Topic
    success_url_name = 'topic_voting_category_list'


class TopicvotingTopicDeleteView(DeleteView):
    model = Topic
    success_url_name = 'topic_voting_category_list'  # TODO: Check this.


class TopicvotingResultView(TopicvotingCategoryListView):
    """
    View to show the results in a nice table.
    """
    template_name = 'topicvoting/results.html'

    def get_context_data(self, **kwargs):
        context = super(TopicvotingResultView, self).get_context_data(**kwargs)
        context['foobar'] = 'foobar'  # TODO: Insert winner table here
        return context


def register_tab(request):
    """
    Registers the tab.
    """
    from . import BASE_URL
    return Tab(
        title='Themenwahl',
        url=reverse('topic_voting_category_list'),
        selected=request.path.startswith('/%s/' % BASE_URL))


def get_widgets(request):
    """
    Returns the widget.
    """
    return [Widget(
        name='topicvoting',
        display_name='Themenwahl',
        template='topicvoting/category_widget.html',
        context={'overview_slide': SLIDE['topicvotingoverview'],
                 'result_slide': SLIDE['topicvotingresult'],
                 'category_list': Category.objects.all()},
        permission_required='projector.can_manage_projector',
        default_column=1)]
