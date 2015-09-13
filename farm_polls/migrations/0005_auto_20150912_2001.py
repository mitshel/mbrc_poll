# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm_polls', '0004_auto_20150912_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll_result',
            name='question_sequence',
        ),
        migrations.AddField(
            model_name='poll_result',
            name='json_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
