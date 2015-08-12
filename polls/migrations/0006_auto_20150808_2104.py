# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150808_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='last_sms',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
