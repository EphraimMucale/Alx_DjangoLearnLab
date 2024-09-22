from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from .views import CustomLoginView, CustomLogoutView, register, profile
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    path('', PostListView.as_view(), name='post-list'),
    path('', PostDetailView.as_view(), name='post-detail'),
    path('', PostCreateView.as_view(), name='post-create'),
    path('', PostUpdateView.as_view(), name='post-update'),
    path('', PostDeleteView.as_view(), name='post-delete'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

]
