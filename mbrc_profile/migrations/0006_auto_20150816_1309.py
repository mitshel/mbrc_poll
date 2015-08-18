# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mbrc_profile', '0005_auto_20150815_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='n_sms',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_send_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 16, 13, 9, 37, 718319)),
        ),
    ]
