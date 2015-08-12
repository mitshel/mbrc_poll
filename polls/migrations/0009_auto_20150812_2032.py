# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_userprofile_last_sms_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='uid',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
