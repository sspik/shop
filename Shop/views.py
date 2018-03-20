# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from django.views.generic import ListView

from shop.settings import MEDIA_ROOT
from cart.forms import CartAddProductForm
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.views.decorators.cache import cache_page
from models import *


#@cache_page(60 * 15)
def home(request):
    args = {}
    args.update(csrf(request))
    blocks = HomeBlock.objects.all()
    special_items = HomeSpecial.objects.all()
    args['blocks'] = list(blocks)
    args['special'] = list(special_items)
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
                                  item.short_desc, item.brand, item.price]
                if item.itemsimage_set.filter(prim=True):
                    items[item.pk].append(item.itemsimage_set.filter(prim=True))
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
    qs = Item.objects.all()
    query = SearchQuery(search_string)
    vector = SearchVector('name', 'detail_desc')
    qs = qs.annotate(search=vector).filter(search=query)
    return render(request, 'shop/search.html', {
        'items': qs
    })