#/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import show_info,edit_meet_info,test_ajax

urlpatterns = patterns('',
        url(r'^test$', show_info, name='wwj_test'),
        url(r'^test_ajax$', test_ajax, name='test_ajax'),
        url(r'^edit_meet_info/(?P<id>\d+)$', edit_meet_info, name='edit_meet_info'),

        )
