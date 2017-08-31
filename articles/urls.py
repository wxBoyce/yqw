# !/usr/bin/python
# -*-coding:utf-8-*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_list, name="list"),
    url(r'^(?P<article_id>[0-9]+)/$', views.article_detail, name='detail'),
]
