#!/usr/bin/env python
# encoding: utf-8

from django import forms
from models import BaseWebConfig, AdvanceWebConfig

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

v_conftype = (
        ('1', '国家级Ⅰ类'),
        ('2', '国家级Ⅱ类'),
        ('3', '省级Ⅰ类'),
        ('4', '省级Ⅱ类'),
        ('5', '市级Ⅰ类'),
        ('6', '市级Ⅱ类')
    )

class ConfigForm(forms.ModelForm):
    class Meta:
        model = BaseWebConfig

    conf_type = forms.CharField(label='会议分类', widget=forms.Select)

    helper = FormHelper()
    helper.form_id = 'regNewWeb'
    helper.form_class = 'form-horizontal'
    helper.form_action = ''
    helper.label_class = 'col-lg-4'
    helper.field_class = 'col-lg-7'

    helper.layout = Layout(
            'site_id',
            'weburl',
            'confname',
            Field('conftime', css_class='date'),
            Field('conf_type', id='id_conf_type'),
            'credit_property',
            'course_credit',
            'mobile_nd',
            'template_id',
            FormActions(
                Submit('save_changes', u'创建会议网站', css_class='btn-primary col-md-12'),
                )
            )

