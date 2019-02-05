from django.urls import path
from . import views


app_name = 'Shop'
urlpatterns = [

    path('', views.ShopListView, name='shop-list'),

    path('sd/<pk>/', views.ShopDetailView, name='shop-detail'),

    path('sc/<pk>/context/', views.ShopDetailContextView, name='shop-context'),

    path('sr/<pk>/add_review/', views.ShopAddReview, name="add-review"),

    path('AddNewShop/', views.AddNewShop.as_view(), name="add-shop"),

    # path('something/', views.AddNewShop.as_view(), name="something")
]

