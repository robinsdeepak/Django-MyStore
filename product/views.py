from django.shortcuts import render
from product.models import product_data


def product_list(request):
    products = product_data.objects.all()[:50]
    return render(request, 'product/product_list.html',
                  {'products': products})


def productView(request, pk):
    product = product_data.objects.get(pk=pk)
    return render(request, 'product/product-detail.html',
                  {'product': product})
