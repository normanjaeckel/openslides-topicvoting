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
    success_url_name = 'topicvoting_category_list'
    apply_url_name = 'topicvoting_category_list'  # TODO: Remove this when openslides/utils/views.py changed from 'edit' to 'update'.
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingCategoryUpdateView(UpdateView):
    model = Category
    success_url_name = 'topicvoting_category_list'
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingCategoryDeleteView(DeleteView):
    model = Category
    success_url_name = 'topicvoting_category_list'  # TODO: Check this.
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingTopicCreateView(CreateView):
    model = Topic
    success_url_name = 'topicvoting_category_list'
    apply_url_name = 'topicvoting_category_list'  # TODO: Remove this when openslides/utils/views.py changed from 'edit' to 'update'.
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingTopicUpdateView(UpdateView):
    model = Topic
    success_url_name = 'topicvoting_category_list'


class TopicvotingTopicDeleteView(DeleteView):
    model = Topic
    success_url_name = 'topicvoting_category_list'  # TODO: Check this.
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingResultView(TopicvotingCategoryListView):
    """
    View to show the results in a nice table.
    """
    template_name = 'openslides_topicvoting/results.html'

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
        # app,
        # stylefile='.css',  # TODO: Add nice icon
        url=reverse('topicvoting_category_list'),
        selected=request.path.startswith('/%s/' % BASE_URL))


def get_widgets(request):
    """
    Returns the widget.
    """
    return [Widget(
        name='topicvoting',
        display_name='Themenwahl',
        template='openslides_topicvoting/category_widget.html',
        context={'overview_slide': SLIDE['topicvotingoverview'],
                 'result_slide': SLIDE['topicvotingresult'],
                 'category_list': Category.objects.all()},
        permission_required='projector.can_manage_projector',
        default_column=1)]
