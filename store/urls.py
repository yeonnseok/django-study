from django.urls import path

from store.views import create

urlpatterns = [
    path('books/', create, name="create")
]