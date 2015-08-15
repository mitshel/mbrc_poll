# -*- coding: utf-8 -*-

from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone

TEMPLATE_EMAIL_SUBJECT = 'Подтверждение регистрации MBRC.POLLS'
TEMPLATE_EMAIL_BODY = "Здравствуйте %s, благодарим за регистрацию на сервисе анкетирования компании MBRC.\n" \
                      "Для активации Вашего аккаунта перейдите по ссылке ниже в течение 48 часов \n " \
                      "http://127.0.0.1:8000/auth/email_confirm/%s/"
EMAIL_FROM = 'mitshel@mail.ru'
ACTIVATION_PERIOD_HOURS = 48

def send_email_confirmation(user_profile):
            email = user_profile.uid.username
            salt = hashlib.sha1(str(random.random()).encode()).hexdigest()[:5]
            user_profile.activation_key = hashlib.sha1((salt+email).encode()).hexdigest()
            user_profile.key_send_time = timezone.now()
            user_profile.save()
            email_subject = TEMPLATE_EMAIL_SUBJECT
            email_body = TEMPLATE_EMAIL_BODY % (user_profile.uid.username, user_profile.activation_key)

            send_mail(email_subject, email_body, EMAIL_FROM, [email], fail_silently=False)
