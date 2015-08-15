# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mbrc_profile', '0003_auto_20150815_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='o',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_send_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 20, 34, 42, 416000)),
        ),
    ]
