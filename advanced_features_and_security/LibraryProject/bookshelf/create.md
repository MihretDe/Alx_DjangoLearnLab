# Create a Book instance

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book
# <Book: Book object (1)>
