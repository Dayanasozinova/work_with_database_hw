import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    print(request.GET)
    if request.GET == {}:
        phones = Phone.objects.all()
        context = {
            'phones': phones
        }
        return render(request, template, context)

    elif request.GET['sort'] == 'name':

        phones = Phone.objects.order_by("name")
        context = {
            'phones': phones
        }
        return render(request, template, context)
    elif request.GET['sort'] == 'min_price':
        phones = Phone.objects.order_by("price")
        context = {
            'phones': phones
        }
        return render(request, template, context)
    elif request.GET['sort'] == 'max_price':
        phones = Phone.objects.order_by("-price")
        context = {
            'phones': phones
        }
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    slug = Phone.objects.get(slug=slug)
    context = {
        'phone': slug
    }
    return render(request, template, context)
