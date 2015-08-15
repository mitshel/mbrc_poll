# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from .forms import RegForm, ProfileForm, PasswordForm
from django.db  import IntegrityError
from .sms import send_sms_confirmation
from mbrc_profile.models import specialize, UserProfile
from mbrc_profile.email import send_email_confirmation, ACTIVATION_PERIOD_HOURS
import datetime
from django.utils import timezone

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        try:
            user_profile=UserProfile.objects.get(uid=user)
        except UserProfile.DoesNotExist:
            user = None

        if (user is not None) and user.is_active:
            auth.login(request, user)

            if user_profile.is_confirmed:
                return redirect('/')
            else:
                args['username']=user.username
                args['tel']=user_profile.tel
                args['last_sms_time'] = user_profile.last_sms_time
                return render_to_response('sms_confirm.html', args)
        else:
            if user is None:
                args['errorvalue'] = "Пользователь не найден либо пароль не верен."
            elif not user.is_active:
                args['errorvalue'] = "Профиль не активен. Необходимо подтвердить регистрацию перейдя по ссылке, " \
                                     "отправленной Вам по электронной почте до %s. В случае отустствия подтверждения " \
                                     "до указанного времени Ваш профиль будет удален автоматически." % (user_profile.key_send_time + datetime.timedelta(hours=ACTIVATION_PERIOD_HOURS)).strftime('%d.%m.%Y %H:%M')
            return render_to_response('login.html', args)


    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = RegForm()
    if request.POST:
        newuser_form =RegForm(request.POST)
        if newuser_form.is_valid():
            tel=newuser_form.cleaned_data['tel']
            pwd1=newuser_form.cleaned_data['pwd1']
            pwd2=newuser_form.cleaned_data['pwd2']
            email=newuser_form.cleaned_data['email']
            f=newuser_form.cleaned_data['f']
            i=newuser_form.cleaned_data['i']
            o=newuser_form.cleaned_data['o']
            employment=newuser_form.cleaned_data['employment']
            position=newuser_form.cleaned_data['position']
            ranks=newuser_form.cleaned_data['ranks']
            specialize=newuser_form.cleaned_data['specialize']

            if pwd1==pwd2:
                try:
                    user = User.objects.create_user(email,email,pwd2,first_name=i, last_name=f)
                    user.is_active=False
                    user.save()
                    user_profile = UserProfile.objects.create(uid=user, tel=tel, employment=employment, position=position, ranks=ranks, is_confirmed=False, specialize=specialize, o=o)
                    send_email_confirmation(user_profile)
                except IntegrityError:
                    args['errorvalue']='Ошибка добавления пользователя. Пользователь %s существует.' % email
                else:
#                    newuser = auth.authenticate(username=email, password=pwd2)
#                    auth.login(request, newuser)
#                    user_profile=UserProfile.objects.get(uid=user)
#                    args['username']=email
#                    args['tel']=tel
#                    args['last_sms_time'] = user_profile.last_sms_time
#                    return render_to_response('sms_confirm.html', args)
                    args['activation_send']=1
                    return render_to_response('email_confirm_info.html', args)
            else:
                args['errorvalue']='Пароли не совпадают.'
        else:
            args['errorvalue'] = 'Заполните правильно все поля формы регистрации.'

        args['form'] = newuser_form

    return render_to_response('register.html', args)

def edit_profile(request):
    args = {}
    user=auth.get_user(request)
    args['username']=user.username
    user_profile=UserProfile.objects.get(uid=user)
    args.update(csrf(request))
    #(fields = 'tel,f,i,o,pwd1,pwd2,specialize,employment,position,ranks')
    default_data={'tel':user_profile.tel,'f':user_profile.uid.last_name,'i':user_profile.uid.first_name,'o':user_profile.o,
                  'specialize':user_profile.specialize, 'employment':user_profile.employment,'position':user_profile.position,
                  'ranks':user_profile.ranks}
    query_form = ProfileForm(default_data)
    args['form'] = query_form
    if request.POST:
        if request.POST.__contains__('ok'):
            profile_form =ProfileForm(request.POST)
            if profile_form.is_valid():
                new_tel=profile_form.cleaned_data['tel']
                old_tel=user_profile.tel
                user_profile.tel=new_tel
                if new_tel!=old_tel:
                    user_profile.is_confirmed=False
                user_profile.uid.last_name=profile_form.cleaned_data['f']
                user_profile.uid.first_name=profile_form.cleaned_data['i']
                user_profile.o=profile_form.cleaned_data['o']
                user_profile.employment=profile_form.cleaned_data['employment']
                user_profile.position=profile_form.cleaned_data['position']
                user_profile.ranks=profile_form.cleaned_data['ranks']
                user_profile.specialize=profile_form.cleaned_data['specialize']
                user_profile.uid.save()
                user_profile.save()
                args['profile_change_success'] = 1
                return render_to_response('profile_change_info.html', args)
            else:
                args['errorvalue'] = 'Заполните правильно все поля Вашего профиля.'
                args['form'] = profile_form
        elif request.POST.__contains__('password'):
            return redirect("/auth/password/")
        else:
            return redirect("/")

    return render_to_response('profile.html', args)


def change_password(request):
    args = {}
    user=auth.get_user(request)
    args['username']=user.username
    user_profile=UserProfile.objects.get(uid=user)
    args.update(csrf(request))
    args['form'] = PasswordForm()
    if request.POST:
        if request.POST.__contains__('ok'):
            password_form =PasswordForm(request.POST)
            if password_form.is_valid():
                pwd0=password_form.cleaned_data['pwd0']
                pwd1=password_form.cleaned_data['pwd1']
                pwd2=password_form.cleaned_data['pwd2']
                if not auth.authenticate(username=user.username, password=pwd0):
                   args['errorvalue'] = 'Текущий пароль неверен.'
                   return render_to_response('password.html', args)
                if pwd1!=pwd2:
                   args['errorvalue'] = 'Новые пароли не идентичны.'
                   return render_to_response('password.html', args)

                user_profile.uid.set_password(pwd1)
                user_profile.uid.save()
                args['pwd_change_success'] = 1
                return render_to_response('profile_change_info.html', args)
            else:
                args['errorvalue'] = 'Введите текущий, а затем новый пароль и его подтверждение.'
        else:
            return redirect("/")

    return render_to_response('password.html', args)

def email_confirm(request, activation_key):
    args = {}
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        redirect('/')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    try:
        user_profile = UserProfile.objects.get(activation_key=activation_key)
    except UserProfile.DoesNotExist:
        user_profile = None

    if user_profile is not None:
        user = user_profile.uid

        #check if the activation key has expired, if it hase then render confirm_expired.html
        if (user_profile.key_send_time + datetime.timedelta(hours=ACTIVATION_PERIOD_HOURS)) < timezone.now():
            args['activation_expired']=1
            return render_to_response('email_confirm_info.html', args)

        #if the key hasn't expired save user and set him as active and render some template to confirm activation
        user.is_active = True
        user.save()

        args['activation_success']=1
        args['username_confirm']=user.username
        return render_to_response('email_confirm_info.html',args)
    else:
        args['activation_failed']=1
        return render_to_response('email_confirm_info.html', args)


def sms_confirm(request, send_sms=0):
    args = {}
    args.update(csrf(request))
    user=auth.get_user(request)
    args['username']=user.username
    user_profile=UserProfile.objects.get(uid=user)
    last_sms=-1

    if send_sms:
        sms_result = send_sms_confirmation(user_profile)
        if sms_result==0:
            args['infovalue'] = "Вам была отправлена повторная СМС с кодом подтверждения телефонного номера."
        elif sms_result==1:
           args['errorvalue'] = "Со времени отправки предидущей СМС прошло слишком мало времени."
        elif sms_result==2:
           args['errorvalue'] = "Произошла ошибка отправки СМС шлюзом."
        else:
           args['errorvalue'] = "Неизвестная ошибка отправки СМС."

        args['last_sms_time'] = user_profile.last_sms_time
        return render_to_response('sms_confirm.html', args)

    if user_profile.last_sms is not None:
       last_sms = int(user_profile.last_sms)
       last_sms_time = user_profile.last_sms_time
       args['last_sms']=int(last_sms)
       args['last_sms_time'] = last_sms_time

    if request.POST:
        try:
            sms_code = int(request.POST.get('sms_code', '0'))
        except ValueError:
            sms_code=0

        if sms_code==last_sms:
            user_profile.is_confirmed=True
            user_profile.save()
            return redirect('/')
        else:
            args['errorvalue'] = "Код из SMS неверен."
            return render_to_response('sms_confirm.html', args)
    else:
        return render_to_response('sms_confirm.html', args)

def sms_reconfirm(request):
    return sms_confirm(request,1)