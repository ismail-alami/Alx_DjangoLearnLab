# test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        # Create sample author and books
        self.author = Author.objects.create(name='Jane Austen')
        self.book1 = Book.objects.create(title='Pride and Prejudice', publication_year=1813, author=self.author)
        self.book2 = Book.objects.create(title='Emma', publication_year=1815, author=self.author)
# This test verifies that a new book can be created successfully and that
# the created book's title matches the input data.
    def test_create_book(self):
        # Test creating a new book
        url = reverse('book-create')
        data = {
            'title': 'Sense and Sensibility',
            'publication_year': 1811,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'Sense and Sensibility')

    def test_retrieve_books(self):
        # Test retrieving the list of books
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check that two books are returned

    def test_update_book(self):
        # Test updating a book
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {'title': 'Pride & Prejudice'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Pride & Prejudice')

    def test_delete_book(self):
        # Test deleting a book
        url = reverse('book-delete', kwargs={'pk': self.book2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        # Test filtering books by title
        url = reverse('book-list') + '?title=Pride and Prejudice'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Pride and Prejudice')

    def test_search_books(self):
        # Test searching books by author name
        url = reverse('book-list') + '?search=Austen'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_publication_year(self):
        # Test ordering books by publication year
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1811)

    def test_permissions_create_book(self):
        # Test permissions for creating a book (must be authenticated)
        self.client.logout()
        url = reverse('book-create')
        data = {'title': 'New Book', 'publication_year': 2023, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
