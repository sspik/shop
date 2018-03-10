# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save, pre_delete
from six import python_2_unicode_compatible
from sorl.thumbnail import ImageField

from Shop.models import gen_url, del_img
from django.db import models


@python_2_unicode_compatible
class Contacts(models.Model):

    class Meta():
        db_table = 'contacts_page'
        verbose_name = 'Страница Контакты'
        verbose_name_plural = 'Страница Контакты'

    title = models.CharField(max_length=255, verbose_name='Заголовок страницы')
    description = models.TextField(max_length=255, verbose_name='Описание страницы')
    url = models.CharField(max_length=255, null=True, blank=True, verbose_name='URL страницы',
                           help_text='Оставить пустым для автозаполнения', unique=True)
    text = RichTextField(verbose_name='Текст страницы')

    def __str__(self):
        return 'Контакты'


@python_2_unicode_compatible
class Socal(models.Model):

    class Meta():
        db_table = 'socal'
        verbose_name = 'Соцсеть'
        verbose_name_plural = ('соцсети')

    name = models.CharField(max_length=255, verbose_name='Имя')
    pub = models.BooleanField(default=True, verbose_name='Включить')
    img = ImageField(verbose_name='Изображение', upload_to='images/%Y/%m/%d/')
    url = models.CharField(max_length=500, verbose_name='Ссылка', null=True, blank=True)
    parent = models.ForeignKey(Contacts, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Phone(models.Model):

    class Meta():
        db_table = 'phone'
        verbose_name = 'Телефон'
        verbose_name_plural = 'телефоны'

    phone = models.CharField(max_length=20, verbose_name='Телефон')
    pub = models.BooleanField(default=True, verbose_name='Включить')
    primary = models.BooleanField(default=True, verbose_name='Главная?', help_text='Будет отображена в шапке и подвале')
    parent = models.ForeignKey(Contacts, null=True)

    def __str__(self):
        return self.phone


@python_2_unicode_compatible
class Email(models.Model):

    class Meta():
        db_table = 'email'
        verbose_name = 'Электронная почта'
        verbose_name_plural = 'почты'

    email = models.EmailField(verbose_name='почта')
    pub = models.BooleanField(default=True, verbose_name='Включить')
    primary = models.BooleanField(default=True, verbose_name='Главная?', help_text='Будет отображена в шапке и подвале')
    parent = models.ForeignKey(Contacts, null=True)

    def __str__(self):
        return self.email


pre_save.connect(gen_url, sender=Contacts)
pre_delete.connect(del_img, sender=Socal)