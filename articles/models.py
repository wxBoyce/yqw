# !/usr/bin/python
# -*-coding:utf-8-*-

from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    author = models.CharField(max_length=100, default=u"yqw", verbose_name=u'auth')
    title = models.CharField(max_length=100, verbose_name=u'title')
    img = RichTextField(max_length=200, default='')
    summary = models.TextField(default="", verbose_name=u'summary')
    tags = models.IntegerField(default=0, verbose_name=u'tags')
    content = RichTextField(verbose_name=u'content')
    status = models.IntegerField(default=0, verbose_name=u'status')
    create_time = models.DateTimeField(u'create_time', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'article'
        ordering = ['-create_time']

    def __unicode__(self):
        return self.title

    __str__ = __unicode__
