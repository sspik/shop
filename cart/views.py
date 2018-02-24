# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from Shop.models import Item
from .cart import Cart
from .forms import CartAddProductForm
from json import dumps as _j


@csrf_exempt
@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=product_id)

    if request.is_ajax():
        if request.POST.get('quantity') and request.POST.get('update'):
            cart.add(product=product,
                     quantity=int(request.POST['quantity']),
                     update_quantity=request.POST['update'])
            return HttpResponse(_j({'ok': 'ok'}))

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('cart:CartDetail')


@csrf_exempt
def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')


def CartDetail(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})