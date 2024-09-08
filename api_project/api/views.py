from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework import viewsets
from .models import Book

class Booklist(viewsets.ModelViewSet):
   queryset = Book.objects.all()
   serializer = BookSerializer
    
