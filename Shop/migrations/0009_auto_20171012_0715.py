# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_catalogproperty_filtercatalog_filterselect_itemfilter_itemproperty_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogproperty',
            name='catalog',
        ),
        migrations.RemoveField(
            model_name='filtercatalog',
            name='Catalog',
        ),
        migrations.RemoveField(
            model_name='filterselect',
            name='filter_catalog',
        ),
        migrations.RemoveField(
            model_name='itemfilter',
            name='filter_catalog',
        ),
        migrations.RemoveField(
            model_name='itemfilter',
            name='product',
        ),
        migrations.RemoveField(
            model_name='itemfilter',
            name='values',
        ),
        migrations.RemoveField(
            model_name='itemproperty',
            name='catalog_property',
        ),
        migrations.RemoveField(
            model_name='itemproperty',
            name='item',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='item',
        ),
        migrations.AlterField(
            model_name='item',
            name='catalog',
            field=models.ManyToManyField(to='Shop.Catalog', verbose_name='\u041a\u0430\u0442\u0430\u043b\u043e\u0433\u0438'),
        ),
        migrations.DeleteModel(
            name='CatalogProperty',
        ),
        migrations.DeleteModel(
            name='FilterCatalog',
        ),
        migrations.DeleteModel(
            name='FilterSelect',
        ),
        migrations.DeleteModel(
            name='ItemFilter',
        ),
        migrations.DeleteModel(
            name='ItemProperty',
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
    ]
