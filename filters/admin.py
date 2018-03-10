# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from filters.models import FilterSelect, FilterCatalog, ItemFilter


class FilterSelectInline(admin.TabularInline):
    model = FilterSelect
    extra = 1

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'name': ('name',)
        }


#@admin.register(FilterCatalog)
class FilterCategoryAdmin(admin.ModelAdmin):
    inlines = [FilterSelectInline, ]
    list_display = ('name', 'published')
    list_editable = ('published',)

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'name': ('name',)
        }


#@admin.register(FilterSelect)
class FilterSelectAdmin(admin.ModelAdmin):
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'name': ('name',)
        }


#@admin.register(ItemFilter)
class ProductFilterAdmin(admin.ModelAdmin):
    pass