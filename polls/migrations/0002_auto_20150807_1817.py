# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='polls',
            name='poll_sort',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='polls_answers',
            name='pos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='polls_questions',
            name='answer_sort',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='polls_questions',
            name='answer_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='polls_questions',
            name='pos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='polls_results',
            name='poll_finish',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='polls_results',
            name='poll_ls_finish',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='polls_results',
            name='poll_ls_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='polls_results',
            name='poll_nsessions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polls_results',
            name='poll_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
