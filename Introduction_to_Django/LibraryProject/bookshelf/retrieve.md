
---

## ✅ `retrieve.md`

```markdown
# Retrieve the Book instance

```python
from bookshelf.models import Book

# Retrieve all Book instances
books = Book.objects.all()

books
# <QuerySet [<Book: Book object (1)>]>

# Display attributes of the first book
book = books.first()

book.id
# 1

book.title
# '1984'

book.author
# 'George Orwell'

book.publication_year
# 1949
