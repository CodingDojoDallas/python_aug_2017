from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
  response = "Hello, I am your first request!"
  return HttpResponse(response)

def test(request):
  response = 'Hello. I am your test method. Look in views.py from first_app on line 7.'
  return HttpResponse(response)