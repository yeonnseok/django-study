from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)


class Book(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book")
    stock_quantity = models.IntegerField()



