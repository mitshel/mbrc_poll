# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_polls_results_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls_questions',
            name='question',
            field=models.TextField(),
        ),
    ]
