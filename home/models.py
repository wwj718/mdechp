#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.db import transaction

class BaseWebConfig(models.Model):
    """
    配置站点基本信息
    """

    siteid = models.IntegerField(verbose_name='新站点ID')
    weburl = models.CharField(max_length=256, verbose_name=u'新站点网址')
    confname = models.CharField(max_length=256, verbose_name=u'会议名称')
    conftime = models.DateField(blank=True, null=True, verbose_name=u'会议时间')
    credit_property = models.CharField(max_length=32, verbose_name=u'学分属性')
    course_credit = models.DecimalField(default=0, max_digits=2, decimal_places=2, verbose_name=u'学分')
    conf_type = models.CharField(max_length=32, verbose_name=u'会议分类')
    mobile_nb = models.CharField(max_length=16, verbose_name=u'手机号')
    template_id = models.CharField(max_length=32, verbose_name=u'模板编号')

    class Meta:
        db_table = 'BaseWebConfig'


class AdvanceWebConfig(models.Model):
    """
    配置高级应用
    """

    app_id = models.CharField(max_length=32, verbose_name=u'App应用')
