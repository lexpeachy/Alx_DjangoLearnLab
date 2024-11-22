from rest_framework import serializer
from .model import Book

class Bookserializer(rest_framework.serializers.modelserializer):
    class meta():
        model = Book
        fields "__all__"