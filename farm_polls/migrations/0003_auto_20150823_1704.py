# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm_polls', '0002_auto_20150823_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='combobox_csv',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
