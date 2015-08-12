# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class specialize(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    uid = models.ForeignKey(User, null=True)
    specialize = models.ForeignKey(specialize, null=True)
    tel = models.CharField(max_length=10)
    employment = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    ranks = models.CharField(max_length=256)
    last_sms = models.CharField(max_length=6, null=True)
    last_sms_time = models.DateTimeField(null=True)
    is_confirmed = models.BooleanField(default=False)

class polls(models.Model):
    """ Класс опроса """
    name = models.CharField(max_length=64)
    poll_sort = models.BooleanField(default=False)          # Включение сортировки вопросов в анкете по номеру pos
    specialize = models.ForeignKey(specialize, null=True)

    def __str__(self):
        return self.name

class polls_Questions(models.Model):
    """ Перечень вопросов входящих в опрос """
    ANSWER_TYPE_CHOICES =(
        (1,'Закрытый радиокнопки'),
        (2,'Закрытый чекбоксы'),
        (11,'Полузакрытый радиокнопки'),
        (12,'Полузакрытый чекбоксы'),
        (20,'Открытый'),
    )
    poll = models.ForeignKey(polls)
    question = models.TextField()
    pos = models.IntegerField(null=True, blank=True)
    answer_type = models.IntegerField(default=1, choices=ANSWER_TYPE_CHOICES)
    answer_sort = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class polls_Answers(models.Model):
    """ Список ответов к соответсвующему вопросу """
    question = models.ForeignKey(polls_Questions)
    answer = models.CharField(max_length=512)
    pos = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.answer

class polls_Results(models.Model):
    """ Результаты опроса, привязанные к зарегистрированному пользователю """
    uid = models.ForeignKey(User, null=True)
    code = models.CharField(max_length=8, null=True)
    poll = models.ForeignKey(polls)                                    # Ссылка на опрос
    poll_start = models.DateTimeField(null=True, blank=True)           # Начало работы пользователя с опросом
    poll_finish = models.DateTimeField(null=True, blank=True)          # Завершение работы пользователя с опросом
    poll_ls_start = models.DateTimeField(null=True, blank=True)        # Начало последней сессии работы пользователя с опросом
    poll_ls_finish = models.DateTimeField(null=True, blank=True)       # Завершение последней сессии работы пользователя с опросом
    poll_nsessions = models.IntegerField(default=0)                    # всего было попвток (сессий) заполнить опрос

class polls_AnswersResults(models.Model):
    poll_result = models.ForeignKey(polls_Results)
    question = models.ForeignKey(polls_Questions)
    open_answer = models.CharField(max_length=1024)
    closed_answer = models.CommaSeparatedIntegerField(max_length=64)
