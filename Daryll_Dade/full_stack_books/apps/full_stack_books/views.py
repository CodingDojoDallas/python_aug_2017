from django.shortcuts import render, redirect
from .models import Book, Author
# Create your views here.
def index(request):
    books = Book.objects.all()
    context = { 'books' : books,
        }
    return render(request, 'full_stack_books/index.html', context)

def create(request):
    if request.method == "POST":

        errors = Book.objects.validate(request.POST)

        if not errors:
            name = request.POST['name']
            author = Author.objects.create(name=name)

            book = Book.objects.create(
                title = request.POST['title'],
                category = request.POST['category'],
                author = author,
            )
        print errors
    return redirect('/')
