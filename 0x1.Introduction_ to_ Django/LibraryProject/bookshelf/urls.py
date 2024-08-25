from django.urls import path
from . import views

urlpatterns = [
     path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

]