#!/usr/bin/env python
# encoding: utf-8

from django import forms
from models import BaseWebConfig, AdvanceWebConfig

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

v_conftype = (
        ('1', '国家级Ⅰ类'),
        ('2', '国家级Ⅱ类'),
        ('3', '省级Ⅰ类'),
        ('4', '省级Ⅱ类'),
        ('5', '市级Ⅰ类'),
        ('6', '市级Ⅱ类')
    )
