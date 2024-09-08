# api/urls.py
from django.urls import path, include
from .views import BookList
from .views import BookViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'books', BookViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]