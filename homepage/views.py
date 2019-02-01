from django.shortcuts import render, HttpResponse, reverse
from product import models as product_models
from shop import models as shop_models
from order import models as order_models


def index(request):
    context = {
            'trending_products': [product for product in order_models.product_data.objects.all()[:50]],
            'nearby_shops': [shop for shop in shop_models.Shop.objects.all()[:20]],
            'nearby_products': [product for product in order_models.product_data.objects.all()[200:250]],
            'history_product': [product for product in order_models.product_data.objects.all()[250:300]],
        }
    return render(request, 'homepage/homepage.html', context)


def SerarchResultView(request):

    if request.method == "POST":
        search_text = request.POST['search']
    return HttpResponse('Search Result')








