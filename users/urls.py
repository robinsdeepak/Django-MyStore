from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'users'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="sign-in"),
    # path('login/', views.LogInView, name='sign-in'),
]
