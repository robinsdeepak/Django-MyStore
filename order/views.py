from django.shortcuts import render, HttpResponse, reverse
from django.http import JsonResponse
from order.models import user_order
from product.models import product_data
from django.contrib.auth.decorators import login_required


@login_required
def OrderListView(request):
    user = request.user
    all_orders = user_order.objects.filter(user=user)

    return render(request, 'order/order_list.html',
                  {'all_order': all_orders})


@login_required
def OrderProcess(request):

    products = [product_data.objects.get(name='Maggie'),
                product_data.objects.get(name='Choco Pie - Premium Quality')]

    return render(request, 'order/order_processing.html',
                  {'products': products})


@login_required
def OrderDetailView(request):

    # get order id
    # get products and quantity
    # pass product list in context

    products = [product_data.objects.get(name='Maggie'),
                product_data.objects.get(name='Choco Pie - Premium Quality')]

    return render(request, 'order/order-detail.html',
                  {'products': products})

