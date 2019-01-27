from django.urls import path
from django.conf.urls import url
from product import views

app_name = 'product'
urlpatterns = [
    # /products/
    path('', views.product_list, name='product-list'),

    # /product/<pk>/ # to be done later
    path(r'<pk>/', views.productView, name='productView'),
]
