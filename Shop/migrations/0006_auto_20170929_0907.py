# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 06:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_auto_20170929_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='features',
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
    ]
