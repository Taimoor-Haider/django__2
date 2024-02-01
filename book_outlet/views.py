from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg
# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {"books": books, "total_number_of_book": num_books, "average_rating": avg_rating})


def book_detail(request, slug):
    # book=get_object_or_404(Book,pk=id)
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request, "book_outlet/book_details.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling,
    })
