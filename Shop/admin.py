# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.forms import ModelForm, SelectMultiple
from Shop.models import *
from sorl.thumbnail.admin import AdminImageMixin
from django_mptt_admin.admin import DjangoMpttAdmin
from filters.models import FilterSelect, ItemFilter, FilterCatalog
from properties.models import CatalogProperty, ItemProperty, Offer


class ImagesInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = ItemsImage
    extra = 3
    verbose_name_plural = 'Изображения'
    suit_classes = 'suit-tab suit-tab-images'


class HomeBlockInlineAdmin(AdminImageMixin, admin.StackedInline):
    model = HomeBlock
    fields = (
        'block_title',
        'block_desc',
        'catalog',
        'link_type',
        'button_text',
        'img',
    )

    #def has_delete_permission(self, request, obj=None):
    #    return False

    #def has_add_permission(self, request, obj=None):
    #    return False


class HomeSpecialInlineAdmin(admin.StackedInline):
    model = HomeSpecial

    #def has_delete_permission(self, request, obj=None):
    #    return False

    #def has_add_permission(self, request, obj=None):
    #    return False


class HomePageAdmin(admin.ModelAdmin):

    inlines = [
        HomeBlockInlineAdmin,
        HomeSpecialInlineAdmin
    ]

    #def has_delete_permission(self, request, obj=None):
    #    return False

    #def has_add_permission(self, request, obj=None):
    #    return False


class CatalogPropertyInline(admin.TabularInline):
    model = CatalogProperty
    extra = 1
    verbose_name_plural = 'параметры'
    suit_classes = 'suit-tab suit-tab-params'


class ItemPropertyInline(admin.TabularInline):
    model = ItemProperty
    extra = 1
    verbose_name_plural = 'параметры'
    suit_classes = 'suit-tab suit-tab-params'


class OfferInline(admin.TabularInline):
    model = Offer
    extra = 1
    verbose_name_plural = 'вариации'
    suit_classes = 'suit-tab suit-tab-offers'


class ItemFilterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemFilterForm, self).__init__(*args, **kwargs)
        if self.instance:
            i = self.instance
            if i.filter_catalog:
                self.fields["values"].queryset = FilterSelect.objects.filter(filter_catalog=i.filter_catalog)
            else:
                self.fields["values"].queryset = FilterSelect.objects.all()[:1]

    class Meta:
        model = ItemFilter
        fields = '__all__'


class ItemFilterInline(admin.TabularInline):
    form = ItemFilterForm
    model = ItemFilter
    extra = 1
    verbose_name_plural = 'Filters'
    suit_classes = 'suit-tab suit-tab-filters'


class FilterCatalogInline(admin.TabularInline):
    model = FilterCatalog
    extra = 1
    verbose_name_plural = 'Filters'
    suit_classes = 'suit-tab suit-tab-filters'

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'name': ('name',)
        }


class BrandAdmin(admin.ModelAdmin):
    pass


class CatalogAdmin(DjangoMpttAdmin):
    inlines = [CatalogPropertyInline, FilterCatalogInline]
    suit_form_tabs = (('general', 'General'),
                      ('params', 'Params'),
                      ('filters', 'Filters'))

    fieldsets = [
        ('General', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'name',
                'url',
                'top_menu',
                'parent',
                'img',
            ]
        }),
    ]

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'name': ('name',)
        }


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'15'})}
    }

    inlines = [ItemPropertyInline,
               OfferInline,
    #           ItemFilterInline,
               ImagesInlineAdmin,
               ]
    list_display = ('name',)
    list_filter = ('catalog',)
    serch_fields = ['id', 'name']
    suit_form_tabs = (('general', 'Главная'),
                      ('offers', 'Вариации'),
                      ('params', 'Параметры'),
   #                   ('filters', 'Фильтры'),
                      ('images', 'Изображения'),
                      )

    fieldsets = [
        ('General', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['name',
                       'url',
                       'catalog',
                       'brand',
                       'price',
                       'quantity',
                       'is_discont',
                       'old_price',
                       'short_desc',
                       'detail_desc',
                       ]
        }),
    ]


# class FilterCatalogAdmin(admin.ModelAdmin):
#     pass


# class FilterSelectAdmin(admin.ModelAdmin):
#     pass

# class PropertiesAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(HomePage, HomePageAdmin)
