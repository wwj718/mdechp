#/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from home import views

urlpatterns = patterns('home',
        url(r'^$', views.index, name='home_index'),
        )
