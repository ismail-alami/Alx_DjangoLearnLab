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
