# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_auto_20150807_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='specialize',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tel', models.CharField(max_length=10)),
                ('employment', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('ranks', models.CharField(max_length=256)),
                ('specialize', models.ForeignKey(null=True, to='polls.specialize')),
                ('uid', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='polls_results',
            name='code',
            field=models.CharField(null=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='polls_answersresults',
            name='closed_answer',
            field=models.CommaSeparatedIntegerField(max_length=64),
        ),
        migrations.AlterField(
            model_name='polls_questions',
            name='answer_type',
            field=models.IntegerField(choices=[(1, 'Закрытый радиокнопки'), (2, 'Закрытый чекбоксы'), (11, 'Полузакрытый радиокнопки'), (12, 'Полузакрытый чекбоксы'), (20, 'Открытый')], default=1),
        ),
        migrations.AddField(
            model_name='polls',
            name='specialize',
            field=models.ForeignKey(null=True, to='polls.specialize'),
        ),
    ]
