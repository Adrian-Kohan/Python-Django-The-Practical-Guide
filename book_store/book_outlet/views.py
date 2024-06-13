from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    books = Book.objects.all()
    av_ratings = books.aaggregate(Avg("rating"))
    number_of_books = books.count()
    return render(request, "book_outlet/index.html", {"books": books,
                                                      "av_ratings": av_ratings,
                                                      "number_of_books": number_of_books})


def single_book(request, slug):
    # try:
    #     book =  Book.objects.get(slug=slug)
    # except:
    #     raise Http404
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/single_book.html", {"book": book})

