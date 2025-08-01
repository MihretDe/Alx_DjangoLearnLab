from relationship_app.models import Author, Book, Library, Librarian
from relationship_app.models import Author, Book

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = books.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []
    
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return []
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None