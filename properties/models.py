# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from six import python_2_unicode_compatible

from Shop.models import Item, Catalog


@python_2_unicode_compatible
class CatalogProperty(models.Model):

    class Meta():

        db_table = 'Catalog_Property'
        verbose_name = 'Свойство каталога'
        verbose_name_plural = 'свойства каталога'

    name = models.CharField(verbose_name='Имя', max_length=255, default='')
    catalog = models.ForeignKey(Catalog, verbose_name='Каталог', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.catalog.name)


@python_2_unicode_compatible
class ItemProperty(models.Model):

    class Meta():

        db_table = 'Item_Property'
        verbose_name = 'Свойство товара'
        verbose_name_plural = 'свойства товара'

    catalog_property = models.ForeignKey(CatalogProperty, verbose_name='Свойство', null=True, blank=True)
    value = models.CharField(verbose_name='Значение', max_length=255, default='')
    item = models.ForeignKey(Item, verbose_name='Товар', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.catalog_property.name, self.value)


@python_2_unicode_compatible
class Offer(models.Model):

    class Meta():

        db_table = 'Offer'
        verbose_name = 'Вариация'
        verbose_name_plural = 'вариации'

    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар', null=True, blank=True)
    name = models.CharField(verbose_name='Имя', max_length=255, default='')
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, default=0.00, verbose_name='Цена')

    def __str__(self):
        return self.name, self.item.name