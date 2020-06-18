from django.contrib import auth
from django.shortcuts import render, redirect

from store.models import Book, Author, MemberBook


def index(request):
    return render(request, "store/index.html")


def create_author(request):
    if request.method == 'POST':
        Author.objects.create(name=request.POST['name'])
        return redirect("/")
    return render(request, "store/author-form.html")


def list_author(request):
    authors = Author.objects.all()
    return render(request, "store/author-list.html", {"authors": authors})


def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author_id = request.POST['author']
        stock_quantity = request.POST['stockQuantity']
        Book.objects.create(title=title, author_id=author_id, stock_quantity=stock_quantity)
        return redirect("/")
    authors = Author.objects.all()
    return render(request, "store/book-form.html", {"authors": authors})


def list_book(request):
    books = Book.objects.all()
    return render(request, "store/book-list.html", {"books": books})


def create_order(request):
    if request.method == 'POST':
        book_id = request.POST['book']
        count = request.POST['count']
        member = request.user.member
        MemberBook.objects.create(member_id=member.id, book_id=book_id, count=count)

        target_book = Book.objects.get(id=book_id)
        target_book.stock_quantity -= int(count)
        target_book.save()
        return redirect("/")

    books = Book.objects.all()
    return render(request, "store/order-form.html", {"books": books})


def list_order(request):
    orders = MemberBook.objects.all()
    return render(request, "store/order-list.html", {"orders": orders})
