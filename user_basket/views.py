from django.shortcuts import render, redirect, HttpResponse
from user_basket.models import basket
from product import models as product_models
from shop import models as shop_models


def ListView(request):
    """
    ListView function Show the item currently in Basket,


    :param request:
    :return: List of Items in User's Basket.

    :: Modifications Required:
            1.

    """

    user = request.user
    if user.is_authenticated:
        try:
            basket_obj = basket.objects.get(user=user)
        except basket.DoesNotExist:
            basket_obj = basket.objects.create(user=user)
            basket_obj.save()

        all_product_sets = basket_obj.basket_product_set.all()

        return render(request, 'user_basket/basket-page.html', {
                'all_product_sets': all_product_sets,
                'basket_obj': basket_obj,
            })
    else:
        return render(request, 'user_basket/basket-page.html')


def AddToBasket(request, product_id, shop_id):
    """
    Function will be called to Add the item to the cart,
        A new instance for user_basket.models.basket_product.

    :param request:
    :param product_id:
    :param shop_id:
    :param quantity:
    :return: Doesn't Return anything, Just do the work.

    :: Modifications Required:
            1. all the parameter need to be removed and using form will be better.
            2. Handling error 'AddToBasket returned None'
    """
    user = request.user
    product = product_models.product_data.objects.get(pk=product_id)
    shop = shop_models.Shop.objects.get(pk=shop_id)
    if user.is_authenticated:
        basket_obj = basket.objects.get(user=user)
        product_set = basket_obj.basket_product_set.create(basket_product=product, basket_product_shop=shop)
        product_set.save()
        return HttpResponse('Successfully Added.')

    else:
        # set to the cookie
        pass
        return HttpResponse('Successfully Added.')














