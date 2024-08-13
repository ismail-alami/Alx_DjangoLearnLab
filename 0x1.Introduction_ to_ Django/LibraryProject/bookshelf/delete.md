## Delete the book you created and confirm the deletion by trying to retrieve all books again.

### Command :

```python
from bookshelf.models import Book
book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()
# The book instance is successfully deleted from the dB
```

# The book instance is successfully deleted from the dB
