from django.contrib import admin

from store.models import Book, Author, MemberBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'stock_quantity']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(MemberBook)
class MemberBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'member_id', 'book_id', 'count']