from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    return HttpResponse("hello!")


def see_all_books(request):
    return HttpResponse("see all books reviews")


def see_one_book(request, book_id):
    return HttpResponse(f"See book with id : {book_id}")
