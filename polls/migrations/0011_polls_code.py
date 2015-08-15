# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20150815_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='polls_code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, null=True)),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
    ]
