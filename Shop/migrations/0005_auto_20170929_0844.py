# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 05:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_auto_20170929_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featurevalues',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='featurevalues',
            name='variation',
        ),
        migrations.DeleteModel(
            name='FeatureValues',
        ),
    ]
