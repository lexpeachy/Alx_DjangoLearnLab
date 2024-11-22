from rest_framework import serializers
from .model import Book

class Bookserializer(rest_framework.serializers.ModelSerializer):
    class meta():
        model = Book
        fields "__all__"