# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_auto_20170929_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='catalog',
        ),
        migrations.AddField(
            model_name='item',
            name='catalog',
            field=models.ManyToManyField(blank=True, null=True, to='Shop.Catalog', verbose_name='\u041a\u0430\u0442\u0430\u043b\u043e\u0433\u0438'),
        ),
    ]