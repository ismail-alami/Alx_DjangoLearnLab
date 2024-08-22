import os
import sys
import django

# Ensure the project directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Filtering books by the author
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author with name '{author_name}' does not exist.")

def query_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library with name '{library_name}' does not exist.")

def query_librarian_of_library(library_name):
    try:
        librarian = Librarian.objects.get(library__name=library_name)  # Getting librarian by library
        print(f"\nLibrarian of {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"Library '{library_name}' does not have an assigned librarian.")
    except Library.DoesNotExist:
        print(f"Library with name '{library_name}' does not exist.")

if __name__ == "__main__":
    # You can change these values to test with different data
    author_name = "J.K. Rowling"
    library_name = "Central Library"

    query_books_by_author(author_name)
    query_books_in_library(library_name)
    query_librarian_of_library(library_name)
