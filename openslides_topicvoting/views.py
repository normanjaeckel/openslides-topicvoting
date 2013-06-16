#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Views for categories and topics
"""

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from openslides.config.api import config
from openslides.utils.views import ListView, CreateView, UpdateView, DeleteView
from openslides.utils.template import Tab
from openslides.projector.projector import Widget, SLIDE

from .models import Category, Topic
from .voting_system import Hoechstzahl, feed_hoechstzahls


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
    apply_url_name = 'topicvoting_category_list'  # TODO: Remove this when openslides/utils/views.py changed from 'edit' to 'update'.
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingCategoryDeleteView(DeleteView):
    model = Category
    success_url_name = 'topicvoting_category_list'
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingTopicCreateView(CreateView):
    model = Topic
    success_url_name = 'topicvoting_category_list'
    apply_url_name = 'topicvoting_category_list'  # TODO: Remove this when openslides/utils/views.py changed from 'edit' to 'update'.
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingTopicUpdateView(UpdateView):
    model = Topic
    success_url_name = 'topicvoting_category_list'
    apply_url_name = 'topicvoting_category_list'  # TODO: Remove this when openslides/utils/views.py changed from 'edit' to 'update'.
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingTopicDeleteView(DeleteView):
    model = Topic
    success_url_name = 'topicvoting_category_list'
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingResultView(TopicvotingCategoryListView):
    """
    View to show the results in a nice table.
    """
    template_name = 'openslides_topicvoting/result.html'

    def get_context_data(self, **kwargs):
        """
        Inserts the results table and additional variables into the context.
        """
        context = super(TopicvotingResultView, self).get_context_data(**kwargs)
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
        context['result_table'] = Hoechstzahl.get_result_table()
        context['winning_topics'] = winning_topics
        context['divisors'] = map(lambda rank: rank * 2 + 1, range(config['openslides_topicvoting_posts']))
        context['topic_post_warning'] = topic_post_warning
        return context


def register_tab(request):
    """
    Registers the main menu entry (tab).
    """
    from . import BASE_URL
    return Tab(
        title=_('Topicvoting'),
        app='openslides_topicvoting',
        stylefile='styles/openslides_topicvoting.css',
        url=reverse('topicvoting_category_list'),
        selected=request.path.startswith('/%s/' % BASE_URL))


def get_widgets(request):
    """
    Returns the widget.
    """
    return [Widget(
        request,
        name='topicvoting',
        display_name=_('Topicvoting'),
        template='openslides_topicvoting/category_widget.html',
        context={'overview_slide': SLIDE['topicvotingoverview'],
                 'result_slide': SLIDE['topicvotingresult'],
                 'category_list': Category.objects.all()},
        permission_required='projector.can_manage_projector',
        default_column=1)]
