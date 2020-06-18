from django.shortcuts import render, redirect

from store.models import Book, Author


def index(request):
    return render(request, "store/index.html")


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author_id = request.POST['author']
        stock_quantity = request.POST['stockQuantity']
        Book.objects.create(title=title, author_id=author_id, stock_quantity=stock_quantity)
        return redirect("/")
    authors = Author.objects.all()
    return render(request, "store/book-form.html", {"authors": authors})
