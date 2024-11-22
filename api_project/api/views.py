from django.shortcuts import render
from rest_framework import generics
from .model import Book
from .serializers import Bookserializer
# Create your views here.

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer