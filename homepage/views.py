from django.shortcuts import render, HttpResponse, reverse
from django.http import JsonResponse
from product.models import product_data
from shop.models import Shop
import json


def index(request):
    context = {
            'trending_products': [product for product in product_data.objects.all()[:50]],
            'nearby_shops': [shop for shop in Shop.objects.all()[:20]],
            'nearby_products': [product for product in product_data.objects.all()[200:250]],
            'history_product': [product for product in product_data.objects.all()[250:300]],
        }
    return render(request, 'homepage/homepage.html', context)
