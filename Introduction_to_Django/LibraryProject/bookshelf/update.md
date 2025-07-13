
---

## ✅ `update.md`

```markdown
# Update the Book title

```python
from bookshelf.models import Book

# Retrieve the Book instance
book = Book.objects.get(id=1)

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the change
book.title
# 'Nineteen Eighty-Four'
