# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mbrc_profile', '0011_auto_20150912_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_send_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 20, 1, 8, 896995)),
        ),
    ]
