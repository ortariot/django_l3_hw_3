from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_query = Phone.objects.all()
    if request.GET.get('sort') == 'name':
        phone_query = phone_query.order_by('name')
    elif request.GET.get('sort') == 'min_price':
        phone_query = phone_query.order_by('price')
    elif request.GET.get('sort') == 'max_price':
        phone_query = phone_query.order_by('-price')
 
    context = {'phones': phone_query}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)


