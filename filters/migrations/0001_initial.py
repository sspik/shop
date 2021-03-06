# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 04:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shop', '0009_auto_20171012_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('name', models.CharField(default='', max_length=255, verbose_name='\u0418\u043c\u044f')),
                ('Catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.Catalog', verbose_name='\u041a\u0430\u0442\u0430\u043b\u043e\u0433')),
            ],
            options={
                'db_table': 'Filter_catalog',
                'verbose_name': '\u0424\u0438\u043b\u044c\u0442\u0440',
                'verbose_name_plural': '\u0444\u0438\u043b\u044c\u0441\u0442\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='FilterSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('name', models.CharField(default='', max_length=255, verbose_name='\u0418\u043c\u044f')),
                ('filter_catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filters.FilterCatalog', verbose_name='\u0424\u0438\u043b\u044c\u0442\u0440 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430')),
            ],
            options={
                'db_table': 'Filter_select',
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u0444\u0438\u043b\u044c\u0442\u0440\u0430',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u0444\u0438\u043b\u044c\u0442\u0440\u0430',
            },
        ),
        migrations.CreateModel(
            name='ItemFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('filter_catalog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='filters.FilterCatalog', verbose_name='\u0424\u0438\u043b\u044c\u0442\u0440 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.Item', verbose_name='\u0422\u043e\u0432\u0430\u0440')),
                ('values', models.ManyToManyField(blank=True, to='filters.FilterSelect', verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f')),
            ],
            options={
                'db_table': 'Item_filter',
                'verbose_name': '\u0424\u0438\u043b\u044c\u0442\u0440 \u0442\u043e\u0432\u0430\u0440\u0430',
                'verbose_name_plural': '\u0444\u0438\u043b\u044c\u0442\u0440\u044b \u0442\u043e\u0432\u0430\u0440\u0430',
            },
        ),
    ]
