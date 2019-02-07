from django.shortcuts import render, HttpResponse, reverse, redirect
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
        searched_text = request.POST['search_text']
        if searched_text:
            searched_products = product_models.product_data.objects.filter(name__icontains=searched_text)[:50]
            if searched_products:
                context = {
                    'searched_text': searched_text,
                    'products': searched_products,
                }
            else:
                context = {
                    'searched_text': searched_text,
                    'error_message': f'No items has been found for {searched_text}!'
                }
                return render(request, 'product/product_list.html', context)

        else:
            return redirect('homepage:homepage-index')
    else:
        return redirect('homepage:homepage-index')

    return render(request, 'product/product_list.html', context)
