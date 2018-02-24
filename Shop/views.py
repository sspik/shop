# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from shop.settings import MEDIA_ROOT
from cart.forms import CartAddProductForm

from models import *


def home(request):
    args = {}
    args.update(csrf(request))
    args['blocks'] = HomeBlock.objects.all().order_by('id')
    special = {}
    special_items = HomeSpecial.objects.all().order_by('id')
    for q in special_items:
        if q.item.itemsimage_set.all():
            img = q.item.itemsimage_set.all()[0].img
        else:
            img = MEDIA_ROOT + '/noimage.png'
        special[q.item] = img
    args['special'] = special
    return render(request, 'shop/index.html', args)


def catalog(request, full_url):
    url_arr = full_url.split('/')
    args = {}
    args.update(csrf(request))
    cat = get_object_or_404(Catalog, url=url_arr[-2])
    if cat.get_absolute_url() != '/' + full_url:
        raise Http404
    items = {}
    for c in cat.get_family():
        if c.level >= cat.level:
            for item in c.item_set.all():
                items[item.pk] = [item.name, item.get_absolute_url(), item.itemsimage_set.all(),
                                  item.short_desc, item.brand , item.price]
    filters = cat.catalogproperty_set.all()
    args['catalog'] = cat
    args['items'] = items
    args['filters'] = filters
    return render(request, 'shop/catalog.html', args)


def item(request, pk):
    args = {}
    args.update(csrf(request))
    get_item = get_object_or_404(Item, pk=pk)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/item.html', {
        'item': get_item,
        'cart_product_form': cart_product_form
    })


def search(request):
    if request.GET.get('search'):
        search_string = request.GET['search']
    else:
        return render(request, 'shop/search.html', {'data': 'none'})
    qs_items = Item.objects.filter(name__search=search_string)
    qs_catalog = Catalog.objects.filter(name__search=search_string)
    return render(request, 'shop/search.html', {
        'catalogs': qs_catalog,
        'items': qs_items
    })