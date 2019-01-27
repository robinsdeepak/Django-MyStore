from django.urls import path
from . import views


app_name = 'order'
urlpatterns = [
    path('list/', views.OrderListView, name='list'),
    path('orderNO/Detail/', views.OrderDetailView, name='detail'),
    path('process-order/', views.OrderProcess, name='process-order'),
    path('order-detail/', views.OrderDetailView, name='order-detail'),
]
