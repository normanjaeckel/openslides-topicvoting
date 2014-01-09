# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy


class TopicvotingCSVImportForm(forms.Form):  # CssClassMixin
    """
    Form to choose the import file.
    """
    csvfile = forms.FileField(
        widget=forms.FileInput(attrs={'size': '50'}),
        label=ugettext_lazy('CSV File'),
        help_text=ugettext_lazy('The file has to be encoded in UTF-8.'))
