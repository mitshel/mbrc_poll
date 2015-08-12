# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='polls',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='polls_Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('answer', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='polls_AnswersResults',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('open_answer', models.CharField(max_length=1024)),
                ('closed_answer', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='polls_Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('question', models.CharField(max_length=1024)),
                ('poll', models.ForeignKey(to='polls.polls')),
            ],
        ),
        migrations.CreateModel(
            name='polls_Results',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('poll', models.ForeignKey(to='polls.polls')),
            ],
        ),
        migrations.AddField(
            model_name='polls_answersresults',
            name='poll_result',
            field=models.ForeignKey(to='polls.polls_Results'),
        ),
        migrations.AddField(
            model_name='polls_answersresults',
            name='question',
            field=models.ForeignKey(to='polls.polls_Questions'),
        ),
        migrations.AddField(
            model_name='polls_answers',
            name='question',
            field=models.ForeignKey(to='polls.polls_Questions'),
        ),
    ]
