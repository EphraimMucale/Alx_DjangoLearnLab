
from django.urls import path, include
from . views import MyModelViewset
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views


router = DefaultRouter()
router.register(r'books', viewset=views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

