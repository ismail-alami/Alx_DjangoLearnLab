## Create a Book Instance

### Command:

```python
# Import the Book model
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title='1984', author='George Orwell', published_year=1949)


# The book instance is successfully created and saved to the database.
# The database now contains a new entry in the books table with the following details:
# Title: 1984
# Author: George Orwell
# Published Year: 1949
```
# The book instance is successfully created and saved to the database.
# The database now contains a new entry in the books table with the following details:
# Title: 1984
# Author: George Orwell
# Published Year: 1949

## Retrieve and display all attributes of the book you just created.

### Command:

```python
# Import the Book model
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title='1984')

# Display the book attributes
print(f'Title: {book.title}, Author: {book.author}, Publication Date: {book.publication_date}')

# The command retrieves the book instance from the database.
# Expected Output:
# Title: 1984, Author: George Orwell, Published Year: 1949
```
# The command retrieves the book instance from the database.
# Expected Output:
# Title: 1984, Author: George Orwell, Published Year: 1949

## Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.

### Command :

```python
from bookshelf.models import Book
book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
# The book instance is successfully updated and saved to the database. with name 'Nineteen Eighty-Four'
```

# The book instance is successfully updated and saved to the database. with name 'Nineteen Eighty-Four'


## Delete the book you created and confirm the deletion by trying to retrieve all books again.

### Command :

```python
from bookshelf.models import Book
book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()
# The book instance is successfully deleted from the dB
```

# The book instance is successfully deleted from the dB
