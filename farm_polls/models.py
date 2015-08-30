# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from mbrc_profile.models import specialize, UserProfile

ANSWER_TYPE_CHOICES =(
    (1,'Radio button'),
    (2,'Checkbox'),
    (3,'Checkbox limited'),
    (4,'Integer inputfield'),
    (5,'String inputfield'),
    (6,'ComboBox'),
)

# Create your models here.
class anketa(models.Model):
    """Заголовой анкеты в которую может входить один или несоглько опросов"""
    name = models.CharField(max_length=256)
    specialize = models.ForeignKey(specialize, null=True)   # Анкета будет показана только врачам с соответствующей специализацией
    def __str__(self):
        return self.name

class poll(models.Model):
    """ Класс опроса """
    name = models.CharField(max_length=256)
    anketa = models.ForeignKey(anketa)
    def __str__(self):
        return self.name

class preparat (models.Model):
    """ Перечень препаратов, привязанный к опросу"""
    name = models.CharField(max_length=64)
    poll = models.ForeignKey(poll)
    def __str__(self):
        return self.name

class question(models.Model):
    """ Перечень вопросов входящих в опрос """
    poll = models.ForeignKey(poll)
    name = models.CharField(max_length=256)
    pos = models.IntegerField(null=True, blank=True)
    answer_type = models.IntegerField(default=1, choices=ANSWER_TYPE_CHOICES)    # Коакого типа могут быть ответы
    checkbox_limit = models.IntegerField(null=True, blank=True)
    combobox_csv = models.CharField(max_length=256, null=True, blank=True)                   # Здесь разделенные через ";" варианты выбора в combobox

    def __str__(self):
        return self.name

    class Meta:
            ordering = ['pos']

class anketa_reslut(models.Model):
    """ Результаты опроса, привязанные к зарегистрированному пользователю """
    user = models.ForeignKey(User, null=True)
    anketa = models.ForeignKey(anketa)                              # Ссылка на анкету
    code = models.CharField(max_length=8, null=True)                # Введенный код для выплаты денег
    a_start = models.DateTimeField(null=True, blank=True)           # Начало работы пользователя с анкетой
    a_finish = models.DateTimeField(null=True, blank=True)          # Завершение работы пользователя с анкетой
    a_ls_start = models.DateTimeField(null=True, blank=True)        # Начало последней сессии работы пользователя с анкетой
    a_ls_finish = models.DateTimeField(null=True, blank=True)       # Завершение последней сессии работы пользователя с анкетой
    a_nsessions = models.IntegerField(default=0)                    # всего было попвток (сессий) заполнить анкету
    is_pay = models.BooleanField(default=False)                     # Была ли выплата за заполненную анкету
    pay_phone = models.CharField(max_length=10, null=True)          # № телефона на который произведена оплата
    pay_cost  = models.IntegerField(default=0)                      # Сколько денег было перечислено
    pay_time  = models.DateTimeField(null=True)                     # Дата и время выплаты

class poll_result(models.Model):
    """Результаты опроса внутри анкеты"""
    anketa_result = models.ForeignKey(anketa_reslut)
    poll = models.ForeignKey(poll)
    question_sequence = models.CharField(max_length=1024)           # Порядок следования вопросов (question_id) разделенные ";"


class preparat_result(models.Model):
    """ Результаты заполнения опроса по конкретному препарату"""
    poll_result = models.ForeignKey(poll_result)
    preparat = models.ForeignKey(preparat)
    result_sequence = models.CharField(max_length=1024)             # Содержание ответов разделенные знаком ";"
