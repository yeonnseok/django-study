from django.urls import path

from store.views import *

urlpatterns = [
    path('author/create/', create_author, name="create_author"),
    path('author/list/', list_author, name="list_author"),
    path('books/create/', create_book, name="create_book"),
    path('books/list/', list_book, name="list_book"),

    path('orders/create/', create_order, name="create_order"),
    path('orders/list/', list_order, name="list_order")
]