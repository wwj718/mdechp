#/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import show_info

urlpatterns = patterns('home',
        url(r'^test$', show_info, name='wwj_test'),
        )
