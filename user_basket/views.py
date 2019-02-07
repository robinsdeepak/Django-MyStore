from django.shortcuts import render, redirect, HttpResponse
from product import models as product_models
from shop import models as shop_models
from user_basket import models as basket_models


def ListView(request):
    """
    ListView function Show the item currently in Basket,
    :param request:
    :return: List of Items in User's Basket.
    : Modifications Required:
            1.
    """

    user = request.user
    if user.is_authenticated:
        try:
            basket_obj = basket_models.basket.objects.get(user=user)
        except basket_models.basket.DoesNotExist:
            basket_obj = basket_models.basket.objects.create(user=user)
            basket_obj.save()

        all_product_sets = basket_obj.basket_product_set.all().order_by('-date_added')

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
    :return: Doesn't Return anything, Just do the work.

    :: Modifications Required:
            1. all the parameter need to be removed and using form will be better.
            2. Handling error 'AddToBasket returned None'
            3. if product already in the basket
                increase the quantity if there is availability
                else Show the message "Not available."
    """
    user = request.user
    product = product_models.product_data.objects.get(pk=product_id)
    shop = shop_models.Shop.objects.get(pk=shop_id)
    if user.is_authenticated:
        basket_obj = basket_models.basket.objects.get(user=user)
        # Checking if product is already in the basket
        try:
            product_set = basket_obj.basket_product_set.get(basket_product=product)
            return HttpResponse('Product Already in Basket')
        except basket_models.basket_product.DoesNotExist:

            product_set = basket_obj.basket_product_set.create(basket_product=product, basket_product_shop=shop)
            product_set.save()
            return HttpResponse('Successfully Added.')
    else:
        # set to the cookie
        pass
        return HttpResponse('Successfully Added.')


def RemoveFromBasket(request, basket_product_id):
    user = request.user
    basket_obj = basket_models.basket.objects.get(user=user)
    try:
        basket_product = basket_obj.basket_product_set.get(pk=basket_product_id)
        basket_product.delete()

        # Redirect to the same page, currently redirecting to  basket
        return redirect('basket:list')

    except:
        return HttpResponse('Invalid Request!')


def UpdateQuantity(request, basket_product_id):
    user = request.user

    basket_obj = basket_models.basket.objects.get(user=user)
    try:
        basket_product = basket_obj.basket_product_set.get(pk=basket_product_id)

        # quantity = basket_product.quantity
        increase_by = request.GET['increase_by']
        if increase_by == '+1':
            print('increase_by is: ', increase_by)
            basket_product.quantity += 1
            basket_product.save()
            return redirect('basket:list')

        elif increase_by == '-1':
            if basket_product.quantity > 1:
                basket_product.quantity -= 1
                basket_product.save()
                return redirect('basket:list')

            elif basket_product.quantity == 1:
                """basket_product will be deleted!"""
                basket_product.delete()
                return redirect('basket:list')

            else:
                """Quantity cannot be made negative!"""
                return redirect('basket:list')

        elif increase_by == 'remove':
            basket_product.delete()
            return redirect('basket:list')

        else:
            """increase_by can only be 1, -1 or remove"""
            return redirect('basket:list')
    except Exception as e:
        """basket_product_set does not exist or doesn't belong to current user!"""
        return HttpResponse('Invalid Request!')
