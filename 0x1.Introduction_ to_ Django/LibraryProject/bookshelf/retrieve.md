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