from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework import viewsets
from .models import Book
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class Booklist(generics.ListAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
    
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(generics.CreateAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticatedOrReadOnly