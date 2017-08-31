# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-31 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='yqw', max_length=100, verbose_name='auth')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('tags', models.IntegerField(default=0, verbose_name='tags')),
                ('content', models.TextField(verbose_name='content')),
                ('status', models.IntegerField(default=0, verbose_name='status')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': 'article',
                'verbose_name_plural': 'article',
            },
        ),
    ]