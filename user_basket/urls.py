from django.urls import path

from . import views

app_name = 'basket'
urlpatterns = [
    path('', views.ListView, name='list'),
    path('add-item/<product_id>/<shop_id>/', views.AddToBasket, name='add-item'),

]
