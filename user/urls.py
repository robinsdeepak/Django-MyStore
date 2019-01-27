from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views


app_name = 'user'
urlpatterns = [
    path('profile/', user_views.UserProfileView, name="profile")
]
