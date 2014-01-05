# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy

from openslides.utils.main_menu import MainMenuEntry


class TopicvotingMainMenuEntry(MainMenuEntry):
    """
    Main menu entry for the topicvoting plugin.
    """
    verbose_name = ugettext_lazy('Topicvoting')
    permission_required = 'openslides_topicvoting.can_see'
    default_weight = 130
    pattern_name = 'topicvoting_category_list'
    icon_css_class = 'icon-podium'
