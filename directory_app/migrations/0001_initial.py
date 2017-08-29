# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 17:54
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=200)),
                ('department', models.CharField(blank=True, choices=[('dean', "Dean's office"), ('bot', 'Botany'), ('chem', 'Chemistry'), ('geo', 'Geosciences'), ('math', 'Mathematics'), ('dev_math', 'Developmental Math'), ('micro', 'Microbiology'), ('phys', 'Physics'), ('planet_phys', 'Planetarium'), ('zoo', 'Zoology'), ('csme', 'Center of Science and Math Education'), ('other', 'Other or Unknown Department'), ('None', 'No department')], max_length=200, verbose_name='Department')),
                ('job_title', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number_1', models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(message="Phone extension must be entered in the format: '+9999'. Exactly 4 digits allowed.", regex='^\\+?1?\\d{4}$')], verbose_name='Office Ext.')),
                ('phone_number_2', models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Cell number')),
                ('location', models.CharField(max_length=200)),
                ('website', models.URLField(blank=True, null=True)),
                ('picture', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('current', 'Current'), ('not_current', 'Not Employed'), ('moved', 'Moved Departments'), ('retired', 'Retired'), ('sabbatical', 'Sabbatical'), ('adjunct', 'Adjunct'), ('temporary', 'Temporary')], default='current', max_length=200)),
                ('last_visit', models.DateTimeField(blank=True, null=True)),
                ('added_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(blank=True, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directory_added_user', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directory_modified_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalDirectory',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=200)),
                ('department', models.CharField(blank=True, choices=[('dean', "Dean's office"), ('bot', 'Botany'), ('chem', 'Chemistry'), ('geo', 'Geosciences'), ('math', 'Mathematics'), ('dev_math', 'Developmental Math'), ('micro', 'Microbiology'), ('phys', 'Physics'), ('planet_phys', 'Planetarium'), ('zoo', 'Zoology'), ('csme', 'Center of Science and Math Education'), ('other', 'Other or Unknown Department'), ('None', 'No department')], max_length=200, verbose_name='Department')),
                ('job_title', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number_1', models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(message="Phone extension must be entered in the format: '+9999'. Exactly 4 digits allowed.", regex='^\\+?1?\\d{4}$')], verbose_name='Office Ext.')),
                ('phone_number_2', models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Cell number')),
                ('location', models.CharField(max_length=200)),
                ('website', models.URLField(blank=True, null=True)),
                ('picture', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('current', 'Current'), ('not_current', 'Not Employed'), ('moved', 'Moved Departments'), ('retired', 'Retired'), ('sabbatical', 'Sabbatical'), ('adjunct', 'Adjunct'), ('temporary', 'Temporary')], default='current', max_length=200)),
                ('last_visit', models.DateTimeField(blank=True, null=True)),
                ('added_date', models.DateField(blank=True, editable=False)),
                ('modified_date', models.DateField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('added_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical directory',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
    ]
