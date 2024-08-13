## Create a Book Instance

### Command:

```python
# Import the Book model
from bookshelf.models import Book

# Create a new Book instance
book = Book(title='1984', author='George Orwell', publication_year=1949)

# Save the instance to the database
book.save()

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