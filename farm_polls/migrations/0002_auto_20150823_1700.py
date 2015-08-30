# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm_polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='checkbox_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=models.IntegerField(default=1, choices=[(1, 'Radio button'), (2, 'Checkbox'), (3, 'Checkbox limited'), (4, 'Integer inputfield'), (5, 'String inputfield'), (6, 'ComboBox')]),
        ),
    ]
