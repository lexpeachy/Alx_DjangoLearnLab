from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # gets all books from the database
    serializer_class = BookSerializer # use bookserializer for serializatin