from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # your custom views

urlpatterns = [
    # Login and logout views using Django's built-in views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Custom views for user registration and profile
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
]

