# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 22:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20170818_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpost',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
    ]
