# !/usr/bin/python
# -*-coding:utf-8-*-

from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fields = ["author", 'title', "tags", "content", "status", "img", "summary"]

admin.site.register(Article, ArticleAdmin)
