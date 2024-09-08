from django.db import models

# Create your models here.
from django.db import models
# Author model to represent an author of books.
# Handles storing the name of the author.
# Author model to store author details
class Author(models.Model):
    name = models.CharField(max_length=255)  # A field for the author's name

    def __str__(self):
        return self.name

# Book model to store book details
class Book(models.Model):
    title = models.CharField(max_length=255)  # A field for the book's title
    publication_year = models.IntegerField()  # A field for the publication year
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # A field linking to Author

    def __str__(self):
        return self.title