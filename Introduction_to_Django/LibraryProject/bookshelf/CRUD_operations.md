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
