# -*- coding: utf-8 -*-

from django import forms
from polls.models import specialize

class RegForm(forms.Form):
    specialize_queryset = specialize.objects.all()
    email = forms.EmailField(label='Ваш E-Mail*')
    tel = forms.CharField(max_length=10, label='Номер мобильного телефона (10 знаков без кода страны)*')
    f = forms.CharField(max_length=32, label='Фамилия*')
    i = forms.CharField(max_length=32, label='Имя*')
    o = forms.CharField(max_length=32, required=False, label='Отчество')
    pwd1 = forms.CharField(max_length=16,label='Пароль*', widget=forms.PasswordInput)
    pwd2 = forms.CharField(max_length=16,label='Повторите пароль*',widget=forms.PasswordInput)
    specialize = forms.ModelChoiceField(specialize_queryset, label='Врачебная специализация*')
    employment = forms.CharField(max_length=64,label='Место работы*')
    position = forms.CharField(max_length=64,label='Должность*')
    ranks = forms.CharField(max_length=256, required=False, label='Звания (если имеются)')

class ProfileForm(forms.Form):
    specialize_queryset = specialize.objects.all()
    tel = forms.CharField(max_length=10, label='Номер мобильного телефона (10 знаков без кода страны)*')
    f = forms.CharField(max_length=32, label='Фамилия*')
    i = forms.CharField(max_length=32, label='Имя*')
    o = forms.CharField(max_length=32, required=False, label='Отчество')
    specialize = forms.ModelChoiceField(specialize_queryset, label='Врачебная специализация*')
    employment = forms.CharField(max_length=64,label='Место работы*')
    position = forms.CharField(max_length=64,label='Должность*')
    ranks = forms.CharField(max_length=256, required=False, label='Звания (если имеются)')

class PasswordForm(forms.Form):
    pwd0 = forms.CharField(max_length=16,label='Введите текущий пароль*', widget=forms.PasswordInput)
    pwd1 = forms.CharField(max_length=16,label='Введите новый пароль*', widget=forms.PasswordInput)
    pwd2 = forms.CharField(max_length=16,label='Повторите новый пароль*', widget=forms.PasswordInput)