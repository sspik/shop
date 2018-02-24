# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import mptt
from django.db import models
from django.db.models.signals import pre_save, pre_delete
from mptt.models import MPTTModel, TreeForeignKey
from six import python_2_unicode_compatible
from Shop.translify import translify
from string import ascii_lowercase
from sorl.thumbnail import ImageField
from sorl.thumbnail import delete
from .search import ItemIndex


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')
    objects = models.Manager()

    class Meta:
        abstract = True


class OrderingBaseModel(BaseModel):

    published = models.BooleanField(verbose_name='Опубликовать', default=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Catalog(MPTTModel):

    class Meta():

        db_table = 'Catalog'
        verbose_name = 'каталог'
        verbose_name_plural = 'каталоги'
        ordering = ['tree_id']

    name = models.CharField(max_length=255, verbose_name='Название', null=True)
    url = models.CharField(max_length=255, null=True, blank=True, verbose_name='URL каталога',
                           help_text='Оставить пустым для автозаполнения')
    top_menu = models.BooleanField(verbose_name='Отображать в топ-меню', default=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    img = ImageField(verbose_name='Изображение', upload_to='images/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return '{} {} - ID: {}'.format('-'*self.get_level(), self.name, str(self.id))

    def get_items(self):
        return self.item_set.all()

    def get_absolute_url(self):
        url = '/%s/' % self.url
        page = self
        while page.parent:
            url = "/%s%s" % (page.parent.url, url)
            page = page.parent
        return '/catalog' + url


mptt.register(Catalog, order_insertion_by=['name'])


@python_2_unicode_compatible
class Brand(models.Model):

    class Meta():

        db_table = 'Brand'
        verbose_name = 'Бренд'
        verbose_name_plural = 'бренды'

    name = models.CharField(max_length=255, verbose_name='Имя')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Item(models.Model):

    class Meta():

        db_table = 'Item'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    catalog = models.ManyToManyField(Catalog, verbose_name='Каталоги')
    brand = models.ForeignKey(Brand, verbose_name='Бренд', null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='Название', null=True)
    url = models.CharField(max_length=255, null=True, blank=True, verbose_name='URL каталога',
                           help_text='Оставить пустым для автозаполнения', unique=True)
    price = models.IntegerField(verbose_name='Цена', default=0)
    quantity = models.IntegerField(verbose_name='Количество', default=0)
    is_discont = models.BooleanField(verbose_name='Скидка?', default=False)
    old_price = models.IntegerField(verbose_name='Старая цена', blank=True, null=True, default=0)
    short_desc = models.TextField(verbose_name='Краткое описание', blank=True, null=True, max_length=300)
    detail_desc = models.TextField(verbose_name='Подробное описание', blank=True, default='В стадии наполнения...')
    created = models.DateField(verbose_name='Время создания', auto_now_add=True)
    updated = models.DateField(verbose_name='Время редактирования', auto_now=True)

    def __str__(self):
        return '%s | %s' % (self.name, self.catalog.name)

    def get_absolute_url(self):
        return '/catalog/{}.html'.format(self.pk)

    def indexing(self):
        obj = ItemIndex(
            meta={'id': self.id},
            name=self.name,
            short_desc=self.short_desc,
            detail_desc=self.detail_desc
        )
        obj.save()
        return obj.to_dict(include_meta=True)


@python_2_unicode_compatible
class ItemsImage(models.Model):

    class Meta():

        db_table = 'ItemsImage'
        verbose_name = 'Изображение'
        verbose_name_plural = 'изабражения'

    img = ImageField(verbose_name='Изображение', upload_to='images/%Y/%m/%d/')
    item = models.ForeignKey(Item, verbose_name='Товар', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.item.name


@python_2_unicode_compatible
class HomePage(models.Model):

    class Meta():

        db_table = 'HomePage'
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    seo_title = models.CharField(max_length=255, verbose_name='Title')
    seo_desc = models.CharField(max_length=500, verbose_name='Description')

    def __str__(self):
        return 'Главная страница'


@python_2_unicode_compatible
class HomeBlock(models.Model):

    class Meta():

        db_table = 'HomeBlock'
        verbose_name = 'Блок на главной странице'
        verbose_name_plural = 'блоки на главной странице'

    SMALL = 'sm'
    SMALL_H = 'smh'
    MIDDLE = 'mid'
    LARGE = 'lg'

    ARRAY = 'arr'
    BUTTON = 'lnk'

    BLOCK_SIZE = (
        (SMALL, 'Маленький блок 365x268'),
        (SMALL_H, 'Маленький блок 365x291'),
        (MIDDLE, 'Средний блок 555x386'),
        (LARGE, 'Большой блок 745x291')
    )

    ARRAY_TYPE = (
        (ARRAY, 'Стрелкой'),
        (BUTTON, 'Кнопкой')
    )

    block_title = models.CharField(max_length=100, verbose_name='Заголовок блока', null=True, blank=True)
    block_desc = models.CharField(max_length=255, verbose_name='Описание блока', null=True, blank=True)
    catalog = models.OneToOneField(Catalog, verbose_name='Каталог', on_delete=models.CASCADE)
    block_size = models.CharField(max_length=3, choices=BLOCK_SIZE,
                                  default=SMALL, verbose_name='Размер блока')
    img = ImageField(verbose_name='Изображение', upload_to='images/%Y/%m/%d/')
    link_type = models.CharField(max_length=3, choices=ARRAY_TYPE,
                                 default=BUTTON, verbose_name='Ссылку стрелкой или кнопкой?')
    button_text = models.CharField(max_length=20, verbose_name='Текст на кнопке', default='Подробней')
    home = models.ForeignKey(HomePage, verbose_name='Главная страница', on_delete=models.CASCADE,
                             blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.catalog.name)


@python_2_unicode_compatible
class HomeSpecial(models.Model):

    class Meta():

        db_table = 'HomeSpecial'
        verbose_name = 'Специальное предложение'
        verbose_name_plural = 'специальные предложения'

    item = models.OneToOneField(Item, verbose_name='Товар', on_delete=models.CASCADE)
    home = models.ForeignKey(HomePage, verbose_name='Главная страница', on_delete=models.CASCADE,
                             blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.item.name)


def gen_url(sender, instance, **kwargs):
    if not instance.url:
        get_url = translify(instance.name.strip().lower().replace(' ', '_'))
        instance.url = ''.join([i for i in get_url if i == '_' or i.isdigit() or i in ascii_lowercase])


def del_img(sender, instance, **kwargs):
    if instance.img:
        delete(instance.img)


pre_save.connect(gen_url, sender=Catalog)
pre_save.connect(gen_url, sender=Item)
pre_delete.connect(del_img, ItemsImage)
pre_delete.connect(del_img, HomeBlock)
pre_delete.connect(del_img, Catalog)