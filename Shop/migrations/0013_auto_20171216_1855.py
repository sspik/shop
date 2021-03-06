# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0012_auto_20171216_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f')),
            ],
            options={
                'db_table': 'Brand',
                'verbose_name': '\u0411\u0440\u0435\u043d\u0434',
                'verbose_name_plural': '\u0431\u0440\u0435\u043d\u0434\u044b',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.Brand', verbose_name='\u0411\u0440\u0435\u043d\u0434'),
        ),
    ]
