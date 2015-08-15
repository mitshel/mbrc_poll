# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20150812_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='specialize',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='uid',
        ),
        migrations.AlterField(
            model_name='polls',
            name='specialize',
            field=models.ForeignKey(to='mbrc_profile.specialize', null=True),
        ),
        migrations.DeleteModel(
            name='specialize',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
