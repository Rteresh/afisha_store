from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect
from concert.models import ClassicalMusic, OpenAir, Party, Concert, Basket
from django.contrib.auth.decorators import login_required
import afisha_store.settings as setting


# Create your views here.
def index(request):
    context = {
        'tittle': 'Afisha',
        'name': 'roma'
    }
    return render(request, 'concerts/index.html', context)


def concerts(request, category_id=None, page=1):
    context = {
        'tittle': 'test',
        'categories': [ClassicalMusic.__name__, OpenAir.__name__, Party.__name__],

    }
    if category_id:
        products = Concert.objects.filter(id=category_id)
    else:
        products = Concert.objects.all()

    paginator = Paginator(products, setting.COUNT_PRODUCT_PAGE)
    products_paginator = paginator.page(page)
    context.update({'products': products_paginator})

    return render(request, 'concerts/concerts.html', context)


@login_required
def basket_add(request, concert_id):
    concert = Concert.objects.get(id=concert_id)
    baskets = Basket.objects.filter(user=request.user, concert=concert)
    current_page = request.META.get('HTTP_REFERER')
    if not baskets.exists():
        # basket = Basket(user=request.user, concert=concert, quantity_items_on_basket=1)
        # basket.save()
        Basket.objects.create(user=request.user, concert=concert, quantity_items_on_basket=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity_items_on_basket += 1
        basket.save()
        return HttpResponseRedirect(current_page)


def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    if basket.quantity_items_on_basket > 0:
        basket.quantity_items_on_basket = basket.quantity_items_on_basket - 1
        basket.save()
    if basket.quantity_items_on_basket == 0:
        basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def product(request, concert_id):
    item = Concert.objects.get(id=concert_id)
    context = {
        'product': item
    }
    return render(request, 'concerts/product.html', context)


def search(request, search_str=None):
    concert_name = str(search_str)
    concert = Concert.objects.filter(name=concert_name)
    context = {
        'concert': concert
    }

    return render(request, 'concerts/concerts.html', context)
