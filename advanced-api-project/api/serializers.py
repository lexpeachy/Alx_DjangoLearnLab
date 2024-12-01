from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class meta:
        model = Book
        fields ='__all__'

    def validate_publication_year(self, value):  # Custom validation to ensure publication year is not in the future
        if value > 2024:
            raise serializers.ValidationError('publication can not be in the future')
        return value

class Authorserializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)   # Nested serializer to show related books

    class meta:
        model = Author
        fields = 'name', 'books'