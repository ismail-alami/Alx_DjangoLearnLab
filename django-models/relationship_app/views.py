from django.shortcuts import render, redirect
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login

# Login View - using Django's built-in view
class LoginView(auth_views.LoginView):
    template_name = 'login.html'

# Logout View - using Django's built-in view
class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'

# Registration View - using a custom view based on Django's UserCreationForm
def register(request):
    form = UserCreationForm()", "relationship_app/register.html
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'register.html', {'form': form})