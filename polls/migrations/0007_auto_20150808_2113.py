# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0006_auto_20150808_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('tel', models.CharField(max_length=10)),
                ('employment', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('ranks', models.CharField(max_length=256)),
                ('last_sms', models.CharField(max_length=6, null=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('specialize', models.ForeignKey(to='polls.specialize', null=True)),
                ('uid', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='specialize',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='uid',
        ),
        migrations.DeleteModel(
            name='user_profile',
        ),
    ]
