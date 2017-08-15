from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
  response = "Hello, I am your display request!"
  #placeholder to display all users
  return HttpResponse(response)

def register(request):
  response = 'Hello. I am your register method.'
  #placerholder to create a new user record
  return HttpResponse(response)

def login(request):
  response = 'Hello. I am your login method.'
  #placerholder to login a user
  return HttpResponse(response)
