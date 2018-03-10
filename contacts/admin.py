# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


class AddressInlineAdmin(admin.StackedInline):

    model = Address
    extra = 1


class EmailInlineAdmin(admin.StackedInline):

    model = Email
    extra = 1


class PhoneInlineAdmin(admin.StackedInline):

    model = Phone
    extra = 1


class ContactsAdmin(admin.ModelAdmin):

    inlines = [
        AddressInlineAdmin,
        EmailInlineAdmin,
        PhoneInlineAdmin
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Contacts, ContactsAdmin)