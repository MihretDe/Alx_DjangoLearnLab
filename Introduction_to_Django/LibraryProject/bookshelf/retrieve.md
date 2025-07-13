# Retrieve the Book instance

```python
from bookshelf.models import Book

# Retrieve the Book by ID
book = Book.objects.get(id=1)

# Display attributes
book.id
# 1

book.title
# '1984'

book.author
# 'George Orwell'

book.publication_year
# 1949
