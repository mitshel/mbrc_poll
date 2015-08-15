# -*- coding: utf-8 -*-

from random import randint
import datetime
from django.utils import timezone
from mbrc_profile.models import UserProfile

import urllib
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


sms_template = 'Для подтверждения регистрации и активации анкет для Вашего логина %s введите следующий код: %s.'
SMS_SEND_TIMEOUT_SEC = 3600

def send_sms_confirmation(user_profile):
    """ Отправляет СМС по телефонному номеру из профайла пользователя
        возвращает 0 - в случае успеха
        возвращает 1 - в случае отказа отправки по причине не исчерпания таймаута SMS_SEND_TIMEOUT_SEC со времени отправки предыдущей СМС
        возвращает 2 - в случае сбоя отправки со стороны СМС шлюза
    """
    if (user_profile.last_sms_time!=None) and ((timezone.now()-user_profile.last_sms_time)<=datetime.timedelta(seconds=SMS_SEND_TIMEOUT_SEC)):
        return 1
    else:
        user_profile.last_sms=randint(100000,999999)
        user_profile.last_sms_time = timezone.now()
        user_profile.save()
    #    api2_epochta_confirmation(user_profile.tel, user_profile.last_sms)
        return 0


#------------------------------------------------------------------
#--  ePochta API
#--
epochta_openkey='49b498c373461eff6d94d54647e58658'
epochta_privatekey='e243dca7005c9ae344eb99fde30b640a'

epochta_email="mitshel@mail.ru"
epochta_password="gluckomail52"

epochta_send_sms = '''<?xml version="1.0" encoding="UTF-8"?>
<SMS>
<operations>
<operation>SEND</operation>
</operations>
<authentification>
<username>%s</username>
<password>%s</password>
</authentification>
<message>
<sender>SMS</sender>
<text>%s</text>
</message>
<numbers>
<number messageID="%s">%s</number>
</numbers>
</SMS>'''

def api2_epochta_confirmation(phone, code):
    full_phone='+7' + phone
    sms_string =  sms_template %(full_phone, code)
    send_sms = epochta_send_sms % (epochta_email, epochta_password, sms_string, full_phone, 'MBRC')
    send_sms = send_sms
    senddata=(('XML',send_sms),)
    senddata=urllib.parse.urlencode(senddata)
    path='http://atompark.com/members/sms/xml.php'
    headers = {"Content-type":"application/x-www-form-urlencoded"}
    req=urllib2.Request(path, data=senddata.encode('utf-8'), headers=headers, method='POST')
    result=urllib2.urlopen(req).read().decode('utf-8')
    return result

def api3_epochta_confirmation(phone, code):
    sms_string =  sms_template %(phone, code)
    params = {}
    params['version']='3.0'
    params['action']='sendSMS'
    params['key']=epochta_openkey
    params['sender']='MBRC'
    params['text']=sms_string
    params['phone']=phone
    params['datetime']=''
    params['sms_lifetime']=0
