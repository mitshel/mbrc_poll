# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm_polls', '0005_auto_20150912_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='anketa_result',
            name='json_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
