from django.contrib import auth
from django.shortcuts import render, redirect

from store.models import Book, Author


def index(request):
    return render(request, "store/index.html")


def create_author(request):
    # TODO: 저자 생성
    pass


def list_author(request):
    # TODO: 저자 목록 조회
    pass


def create_book(request):
    # TODO: 책 생성
    pass


def list_book(request):
    # TODO: 책 목록 조회
    pass


def create_order(request):
    # TODO: 주문 생성
    pass


def list_order(request):
    # TODO: 주문 목록 조회
    pass
