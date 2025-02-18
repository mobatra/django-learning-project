from django.shortcuts import render
from django.http import HttpResponse

def book(req):
    book = req.GET
    book_name = book['name']
    book_auth = book['auth']
    book_release = book['release']
    content = f'<h1>welcome to books library!</h1> <h3>The "{book_name}", {book_release}th release for {book_auth}'
    response = HttpResponse(content)
    return response