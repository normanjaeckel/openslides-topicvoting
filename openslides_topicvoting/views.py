# -*- coding: utf-8 -*-
"""
Views for categories and topics.
"""

import csv

from django.contrib import messages
from django.utils.translation import ugettext as _
from openslides.config.api import config
from openslides.utils.views import FormView, ListView, CreateView, UpdateView, DeleteView

from .forms import TopicvotingCSVImportForm
from .models import Category, Topic
from .voting_system import Hoechstzahl, feed_hoechstzahls


class TopicvotingCategoryListView(ListView):
    """
    View to list all categories and all topics.
    """
    model = Category
    permission_required = 'openslides_topicvoting.can_see'

    def get_context_data(self, **kwargs):
        context = super(TopicvotingCategoryListView, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        context['lost_topics'] = Topic.objects.filter(category=None).exists()
        return context


class TopicvotingCategoryCreateView(CreateView):
    model = Category
    success_url_name = 'topicvoting_category_list'
    url_name_args = []
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingCategoryUpdateView(UpdateView):
    model = Category
    success_url_name = 'topicvoting_category_list'
    url_name_args = []
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingCategoryDeleteView(DeleteView):
    model = Category
    success_url_name = 'topicvoting_category_list'
    url_name_args = []
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingTopicCreateView(CreateView):
    model = Topic
    success_url_name = 'topicvoting_category_list'
    url_name_args = []
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingTopicUpdateView(UpdateView):
    model = Topic
    success_url_name = 'topicvoting_category_list'
    url_name_args = []
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingTopicDeleteView(DeleteView):
    model = Topic
    success_url_name = 'topicvoting_category_list'
    url_name_args = []
    permission_required = 'openslides_topicvoting.can_manage'


class TopicvotingCSVImportView(FormView):
    """
    View to import categories and topics using a csv file.
    """
    permission_required = 'openslides_topicvoting.can_manage'
    template_name = 'openslides_topicvoting/csv_import.html'
    form_class = TopicvotingCSVImportForm
    success_url_name = 'topicvoting_category_list'

    def form_valid(self, form):
        report, error = self.import_categories_and_topics()
        if error:
            messages.error(self.request, report)
        else:
            messages.success(self.request, report)
        return super(TopicvotingCSVImportView, self).form_valid(form)

    def import_categories_and_topics(self):
        csv_file = self.request.FILES['csvfile']
        # Check encoding
        try:
            csv_file.read().decode('utf8')
        except UnicodeDecodeError:
            message = _('Import file has wrong character encoding. Only UTF-8 is supported.')
            error = True
        else:
            csv_file.seek(0)
            topics = 0
            categories = 0
            for number, data in enumerate(csv.reader(csv_file)):
                # Do not read the header line
                if number == 0 or len(data) == 0:
                    continue
                # Check and repair format
                if len(data) < 3:
                    data.extend(['', ''])
                # Extract data
                title, submitter, category = data[:3]
                if not title:
                    continue
                if category:
                    category_object, created = Category.objects.get_or_create(name=category)
                    if created:
                        categories += 1
                else:
                    category_object = None
                Topic.objects.create(title=title, submitter=submitter, category=category_object)
                topics += 1
            message = _('%d categories and %d topics successfully imported.') % (categories, topics)
            error = False
        return message, error


class TopicvotingResultView(TopicvotingCategoryListView):
    """
    View to show the results in a nice table.
    """
    template_name = 'openslides_topicvoting/result.html'
    permission_required = 'openslides_topicvoting.can_see'

    def get_context_data(self, **kwargs):
        """
        Inserts the results table and additional flags and variables into the context.
        """
        context = super(TopicvotingResultView, self).get_context_data(**kwargs)
        feed_hoechstzahls()
        result_table_and_info = Hoechstzahl.get_result_table_and_info()
        context['result_table'] = result_table_and_info['result_table']
        context['winning_topics'] = result_table_and_info['winning_topics']
        context['runoff_poll_warning'] = result_table_and_info['runoff_poll_warning']
        context['topic_post_warning'] = result_table_and_info['topic_post_warning']
        context['divisors'] = map(lambda rank: rank * 2 + 1, range(max(config['openslides_topicvoting_posts'], 3)))
        return context
