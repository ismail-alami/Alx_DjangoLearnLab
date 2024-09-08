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

# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# ListView to retrieve all books with filtering, searching, and ordering
# views.py (complete)

class BookListView(generics.ListAPIView):
    """
    View to list all books with filtering, searching, and ordering capabilities.
    - Filtering: Filter books by title, author's name, and publication year.
    - Searching: Search books by title or author's name.
    - Ordering: Order results by title or publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
# from django_filters import rest_framework