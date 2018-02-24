# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from six import python_2_unicode_compatible

from Shop.models import OrderingBaseModel, Item, Catalog


@python_2_unicode_compatible
class FilterCatalog(OrderingBaseModel):

    class Meta():

        db_table = 'Filter_catalog'
        verbose_name = 'Фильтр'
        verbose_name_plural = 'фильтры'

    Catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='Каталог')
    name = models.CharField(verbose_name='Имя', max_length=255, default='')

    def __str__(self):
        return '{} {}'.format(self.name, self.Catalog.name)


@python_2_unicode_compatible
class FilterSelect(OrderingBaseModel):

    class Meta():

        db_table = 'Filter_select'
        verbose_name = 'Вариант фильтра'
        verbose_name_plural = 'Варианты фильтра'

    filter_catalog = models.ForeignKey(FilterCatalog, on_delete=models.CASCADE, verbose_name='Фильтр каталога')
    name = models.CharField(verbose_name='Имя', max_length=255, default='')

    def __str__(self):
        return '{} {}'.format(self.name, self.filter_catalog.name)


@python_2_unicode_compatible
class ItemFilter(OrderingBaseModel):

    class Meta():

        db_table = 'Item_filter'
        verbose_name = 'Фильтр товара'
        verbose_name_plural = 'фильтры товара'

    product = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар', null=True)
    filter_catalog = models.ForeignKey(FilterCatalog, on_delete=models.CASCADE,
                                       null=True, verbose_name='Фильтр категории')
    values = models.ManyToManyField(FilterSelect, blank=True, verbose_name='Значения')

    def __str__(self):
        return "ID = %s, Item =  %s" % (str(self.id), self.product.name)
