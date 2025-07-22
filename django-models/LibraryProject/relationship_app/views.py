from django.shortcuts import render
from urllib3 import HTTPResponse
from .models import Book , Library
from django.views.generic import DetailView
# Create your views here.
def list_books(request):
    books = Book.objects.select_related('author').all()
    output = '\n'.join([f"{book.title} by {book.author.name}" for book in books])
    return HTTPResponse(output, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"