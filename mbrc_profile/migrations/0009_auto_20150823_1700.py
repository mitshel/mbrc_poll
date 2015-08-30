# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mbrc_profile', '0008_auto_20150823_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_send_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 23, 17, 0, 27, 595433)),
        ),
    ]
