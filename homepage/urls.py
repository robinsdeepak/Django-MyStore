from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.index, name='homepage-index'),
    path('search/', views.SerarchResultView, name='search'),
    ]
