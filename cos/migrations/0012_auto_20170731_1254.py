# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos', '0011_auto_20170731_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='computer_role',
            field=models.CharField(blank=True, choices=[('faculty_main', 'Faculty Main Computer'), ('faculty_secondary', 'Faculty Secondary Computer'), ('classroom_computer', 'Classroom Computer'), ('lab_research', 'Research Lab Computer'), ('lab_open', 'Open Lab Computer'), ('lab_closed', 'Closed Lab Computer')], max_length=200, verbose_name='What is the primary role of the computer'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='active_directory',
            field=models.BooleanField(default=False, verbose_name='Computer on the Domain'),
        ),
    ]
