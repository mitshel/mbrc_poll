# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mbrc_profile', '0008_auto_20150823_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='anketa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=256)),
                ('specialize', models.ForeignKey(to='mbrc_profile.specialize', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='anketa_reslut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=8, null=True)),
                ('a_start', models.DateTimeField(blank=True, null=True)),
                ('a_finish', models.DateTimeField(blank=True, null=True)),
                ('a_ls_start', models.DateTimeField(blank=True, null=True)),
                ('a_ls_finish', models.DateTimeField(blank=True, null=True)),
                ('a_nsessions', models.IntegerField(default=0)),
                ('is_pay', models.BooleanField(default=False)),
                ('pay_phone', models.CharField(max_length=10, null=True)),
                ('pay_cost', models.IntegerField(default=0)),
                ('pay_time', models.DateTimeField(null=True)),
                ('anketa', models.ForeignKey(to='farm_polls.anketa')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=256)),
                ('anketa', models.ForeignKey(to='farm_polls.anketa')),
            ],
        ),
        migrations.CreateModel(
            name='poll_result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question_sequence', models.CharField(max_length=1024)),
                ('anketa_result', models.ForeignKey(to='farm_polls.anketa_reslut')),
                ('poll', models.ForeignKey(to='farm_polls.poll')),
            ],
        ),
        migrations.CreateModel(
            name='preparat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('poll', models.ForeignKey(to='farm_polls.poll')),
            ],
        ),
        migrations.CreateModel(
            name='preparat_result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('result_sequence', models.CharField(max_length=1024)),
                ('poll_result', models.ForeignKey(to='farm_polls.poll_result')),
                ('preparat', models.ForeignKey(to='farm_polls.preparat')),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=256)),
                ('pos', models.IntegerField(blank=True, null=True)),
                ('answer_type', models.IntegerField(default=1, choices=[(1, 'Radio button'), (2, 'Checkbox'), (3, 'Integer inputfield'), (4, 'String inputfield'), (5, 'ComboBox')])),
                ('combobox_csv', models.CharField(max_length=256, null=True)),
                ('poll', models.ForeignKey(to='farm_polls.poll')),
            ],
        ),
    ]
