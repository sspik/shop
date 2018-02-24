# coding=utf-8
from django.contrib import admin
from .models import CatalogProperty, ItemProperty


class ProductPropertyInline(admin.TabularInline):
    model = ItemProperty
    extra = 1
    verbose_name_plural = 'Values'
    suit_classes = 'suit-tab suit-tab-values'


@admin.register(CatalogProperty)
class CategoryPropertyAdmin(admin.ModelAdmin):
    inlines = [ProductPropertyInline,]
    suit_form_tabs = (('general', 'Главная'),
        ('values', u'Значения'), )
    fieldsets = [
        ('Главная', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
             'name',
             'catalog',
             #'published',
             #'ordering',
             ]
        }),
    ]


@admin.register(ItemProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    pass