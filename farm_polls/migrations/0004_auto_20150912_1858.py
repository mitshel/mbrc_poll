# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farm_polls', '0003_auto_20150823_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='anketa_result',
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
        migrations.RemoveField(
            model_name='anketa_reslut',
            name='anketa',
        ),
        migrations.RemoveField(
            model_name='anketa_reslut',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['pos']},
        ),
        migrations.AlterField(
            model_name='poll_result',
            name='anketa_result',
            field=models.ForeignKey(to='farm_polls.anketa_result'),
        ),
        migrations.DeleteModel(
            name='anketa_reslut',
        ),
    ]
