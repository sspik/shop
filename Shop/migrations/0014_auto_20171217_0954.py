# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0013_auto_20171216_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]