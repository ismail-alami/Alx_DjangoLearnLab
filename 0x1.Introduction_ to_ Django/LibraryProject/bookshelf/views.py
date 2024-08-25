from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.
from django.http import HttpResponse


from django.views.generic import DetailView
from .models import Book

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get default context data
        context['average_rating'] = "testValue"  # Example additional context
        return context