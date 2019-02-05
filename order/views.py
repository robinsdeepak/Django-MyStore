from django.shortcuts import render, HttpResponse, reverse
from django.http import JsonResponse
from order import models as user_models
from product import models as product_models
from django.contrib.auth.decorators import login_required
from user_basket.models import basket
from shop import models as shop_models


@login_required
def OrderListView(request):
    user = request.user
    all_orders = user_models.user_order.objects.filter(user=user).order_by('-date_ordered')

    return render(request, 'order/order_list.html',
                  {'all_order': all_orders})


@login_required
def BasketCheckOutProcess(request):
    user = request.user

    basket_obj = basket.objects.get(user=user)
    all_basket_product_sets = basket_obj.basket_product_set.all()

    return render(request, 'order/order_processing.html', {
            'all_basket_product_sets': all_basket_product_sets,
            'basket_obj': basket_obj,
        })


@login_required
def OrderProcessing(request, product_id, shop_id):
    """
    OrderProcessing takes the user to a page to confirm the items and make payment.

    :param request:
    :param product_id:
    :param shop_id:
    :return:
    """
    user =request.user
    product = product_models.product_data.objects.get(pk=product_id)
    shop = shop_models.Shop.objects.get(pk=shop_id)

    # try:
    #     # if quantity
    #         pass
    # except:
    #   quantity = 1

    quantity = 1

    return render(request, 'order/order_processing.html', {
                                    'SingleCheckout': True,
                                    'shop': shop,
                                    'product': product,
                                    'quantity': quantity,
                                    'total_amount': product.price*quantity,
                                })


@login_required
def OrderDetailView(request):

    # get order id
    # get products and quantity
    # pass product list in context

    products = [product_models.product_data.objects.get(name='Maggie'),
                product_models.product_data.objects.get(name='Choco Pie - Premium Quality')]

    return render(request, 'order/order-detail.html',
                  {'products': products})


@login_required
def CheckoutBasketView(request):
    """
    CheckoutBasketView checkout all the product in basket.
    It groups the product according to shop.
    There is a different order for every shop.
    Constraint should be applied for max number of shop per checkout.

    :param request:
    :return:


    ** Exception handling is not applied**

     >> shop_and_product is json like object
    shop_and_product = { shop1: {
                                    product1 : quantity
                                    product2 : quantity
                                    ....
                                    }

                         shop2: {
                                    product1 : quantity
                                    product2 : quantity
                                    ....
                                    }
                        ......
    """
    user = request.user
    basket_obj = basket.objects.get(user=user)

    all_basket_product_sets = basket_obj.basket_product_set.all()
    shop_and_products = {}

    for product_set in all_basket_product_sets:
        shop = product_set.basket_product_shop

        if shop not in shop_and_products:
            shop_and_products[shop] = {}

        product = product_set.basket_product
        quantity = product_set.quantity
        shop_and_products[shop][product] = quantity

    # placing orders one by one
    # one order from one shop
    # two different shop can't have same order
    for shop, products_dict in shop_and_products.items():
        order = user_models.user_order.objects.create(user=user, ordered_from_shop=shop)

        for product in products_dict:
            user_order_product_set = user_models.user_order_products.objects.create(
                for_order=order, ordered_product=product, ordered_quantity=products_dict[product]
            )
            user_order_product_set.save()

        order.save()
    # After the order has been placed successfully
    # Delete the products from basket
    # Missing -- Check if the order was successful or not before deleting.

    for product_set in all_basket_product_sets:
        product_set.delete()

    return render(request, 'order/order-successful.html')


@login_required
def CheckOutView(request, product_id, shop_id):
    """
    CheckOutView places the order for single product.



    :param request:
    :param product_id:
    :param shop_id:
    :return:
    """
    user = request.user
    product = product_models.product_data.objects.get(pk=product_id)
    shop = shop_models.Shop.objects.get(pk=shop_id)
    order = user_models.user_order.objects.create(user=user, ordered_from_shop=shop)

    user_order_product_set = user_models.user_order_products.objects.create(
        for_order=order, ordered_product=product, ordered_quantity=1
        )

    user_order_product_set.save()

    order.save()

    return render(request, 'order/order-successful.html')










