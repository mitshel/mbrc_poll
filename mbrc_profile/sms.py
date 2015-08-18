# -*- coding: utf-8 -*-

from datetime import timedelta
from random import randint
from django.utils import timezone
from mbrc_profile.models import UserProfile
from mbrc_profile.smsc_api import *

sms_template = 'Для подтверждения телефона на сайте MBRC.ANKETA введите следующий код: %s.'
SMS_SEND_TIMEOUT_SEC = 3

def send_sms_confirmation(user_profile):
    """ Отправляет СМС по телефонному номеру из профайла пользователя
        возвращает 0 - в случае успеха
        возвращает 1 - в случае отказа отправки по причине не исчерпания таймаута SMS_SEND_TIMEOUT_SEC со времени отправки предыдущей СМС
        возвращает 2 - в случае сбоя отправки со стороны СМС шлюза
    """
    if (user_profile.last_sms_time!=None) and ((timezone.now()-user_profile.last_sms_time)<=timedelta(seconds=SMS_SEND_TIMEOUT_SEC)):
        return 1
    else:
        last_sms=randint(100000,999999)
        last_sms_time = timezone.now()
        r=smsc_confirmation(user_profile.tel, last_sms)
        if r[1]>"0":
            user_profile.last_sms=last_sms
            user_profile.last_sms_time = last_sms_time
            user_profile.n_sms=user_profile.n_sms+1
            user_profile.save()
            return 0
        else:
            return 2

    return 3

def smsc_confirmation(tel, last_sms):
    smsc = SMSC()
    r = smsc.send_sms("7%s"%tel, sms_template%last_sms, sender="MBRC")
    return r
