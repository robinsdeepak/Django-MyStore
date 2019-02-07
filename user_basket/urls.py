from django.urls import path
from user_basket import views as basket_views

app_name = 'basket'
urlpatterns = [
    path('', basket_views.ListView, name='list'),
    path('add-item/<product_id>/<shop_id>/', basket_views.AddToBasket, name='add-item'),
    path('rm-item/<basket_product_id>/', basket_views.RemoveFromBasket, name='remove-item'),
    path('update-item/<int:basket_product_id>/', basket_views.UpdateQuantity, name='update'),
]
