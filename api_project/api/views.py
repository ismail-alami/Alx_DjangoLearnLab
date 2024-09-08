from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# generics.ListAPIView
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer