from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from .views import CustomLoginView, CustomLogoutView, register, profile

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
