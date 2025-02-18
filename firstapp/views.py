from django.shortcuts import render
from django.http import HttpResponse

def user(req, name, age):
  content = f'<h1>Hello Boss</h1> <h2> The age of {name} is : {age}</h2>'
  response = HttpResponse(content)
  return response
  