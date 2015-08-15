# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mbrc_profile', '0002_auto_20150815_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='key_expires',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='key_send_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 14, 51, 23, 369931, tzinfo=utc)),
        ),
    ]
