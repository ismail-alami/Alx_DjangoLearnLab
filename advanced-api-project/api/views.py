from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
# BookListView handles listing all books.
# It uses ListAPIView to provide a simple read-only interface to the list of books.
# This view is publicly accessible as indicated by the AllowAny permission class.
# ListView to retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access this view

# DetailView to retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access this view

# CreateView to add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

# UpdateView to modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update

# DeleteView to remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Override perform_create to add extra functionality if needed
    def perform_create(self, serializer):
        # Example: Add current logged-in user as a creator, if needed
        serializer.save()  # Customize save logic as needed

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Override perform_update to add extra functionality if needed
    def perform_update(self, serializer):
        # Example: Log updates or apply additional validations
        serializer.save()  # Customize save logic as needed