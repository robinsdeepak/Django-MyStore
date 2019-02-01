from django.shortcuts import render, HttpResponse, reverse
from product import models as product_models
from shop import models as shop_models
from order import models as order_models


def index(request):
    user = request.user
    context = {}
    if user.is_authenticated:

        # getting product history.

        all_ordered_products = []
        all_orders = order_models.user_order.objects.all()
        for order in all_orders:
            all_ordered_products = all_ordered_products + list(order.user_order_products_set.all())
            if len(all_ordered_products) > 10:
                context['history_product'] = all_ordered_products,
                break

    context['trending_products'] = [product for product in product_models.product_data.objects.all()[:50]],
    context['nearby_shops'] = [shop for shop in shop_models.Shop.objects.all()[:20]],
    context['nearby_products'] = [product for product in product_models.product_data.objects.all()[200:250]],

    return render(request, 'homepage/homepage.html', context)


def SerarchResultView(request):

    if request.method == "POST":
        search_text = request.POST['search']
    return HttpResponse('Search Result')











