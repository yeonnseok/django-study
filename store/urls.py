from django.urls import path

from store.views import create_author, list_author, create_book, list_book

urlpatterns = [
    path('author/create/', create_author, name="create-author"),
    path('author/list/', list_author, name="list-author"),
    path('books/create/', create_book, name="create-book"),
    path('books/list/', list_book, name="list-book"),
]