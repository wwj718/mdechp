#/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import urls, patterns
from django.views.generic import TemplateView

from .view import index

home_patterns = patterns()
