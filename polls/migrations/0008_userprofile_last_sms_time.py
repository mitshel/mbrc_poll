# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20150808_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_sms_time',
            field=models.DateTimeField(null=True),
        ),
    ]
