from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import settings
from django.conf.urls.static import static
from user import views as user_views


urlpatterns = [
    url('admin/', admin.site.urls, name='admin'),
    url('', include('homepage.urls')),
    url('product/', include('product.urls')),
    url('shop/', include('shop.urls')),
    url('user/', include('user.urls')),
    url('order/', include('order.urls')),

    path('login/', user_views.Login, name='login'),
    path('logout/', user_views.LogOut, name='logout'),
    path('register/', user_views.UserSignUp, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

