
from django.urls import path, include
from . views import MyModelViewset
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views


router = DefaultRouter()
router.register(r'books', viewset=views.BookViewSet)
router.register(r'detail', viewset=views.DetailViewSet)
router.register(r'create', viewset=views.CreateViewSet)
router.register(r'update', viewset=views.UpdateViewSet)
router.register(r'delete', viewset=views.DeleteViewSet)


urlpatterns = [
    path(' ', 'BookList/', views.Booklist),
    path('api/', include(router.urls)),
]

