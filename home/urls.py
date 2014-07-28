#/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from django.views.generic import TemplateView

from .views import index

urlpatterns = patterns('home.views',
        url(r'^$', 'index', {'template': 'home.html'})
        )
