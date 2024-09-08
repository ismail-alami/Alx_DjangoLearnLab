from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializer for Book model
# BookSerializer handles serialization of Book instances.
# It validates that the publication year is not set in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

# Serializer for Author model, including nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for books

    class Meta:
        model = Author
        fields = ['name', 'books']  # Including the author's name and related books