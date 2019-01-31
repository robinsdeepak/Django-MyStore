from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('list/', views.OrderListView, name='list'),
    path('orderNO/Detail/', views.OrderDetailView, name='detail'),
    path('process-order/', views.BasketCheckOutProcess, name='process-order'),
    path('process/<product_id>/<shop_id>/', views.OrderProcessing, name='process'),
    path('order-detail/', views.OrderDetailView, name='order-detail'),
    path('place-order/', views.CheckoutBasketView, name='place-order'),
    path('checkout/<product_id>/<shop_id>/', views.CheckOutView, name='checkout')
]
