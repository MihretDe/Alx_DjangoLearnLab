
---

## ✅ `delete.md`

```markdown
# Delete the Book instance

```python
from bookshelf.models import Book

# Retrieve the Book instance
book = Book.objects.get(id=1)

# Delete the book
book.delete()
# (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()
# <QuerySet []>
