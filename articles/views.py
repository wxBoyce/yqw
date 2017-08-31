# !/usr/bin/python
# -*-coding:utf-8-*-

from django.core import serializers
from django.http import HttpResponse

from .models import Article

# Create your views here.


def index_list(request):
    article_list = Article.objects.order_by("create_time")
    json_data = serializers.serialize("json", article_list)
    return HttpResponse(json_data, content_type="application/json")


def article_detail(request, article_id):
    article_data = Article.objects.get(pk=article_id)
    json_data = serializers.serialize("json", [article_data])
    return HttpResponse(json_data, content_type="application/json")

