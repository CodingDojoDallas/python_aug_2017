from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
  response = "Hello, I am your index request!"
  #placerholder to later display all blogs
  return HttpResponse(response)

def new(request):
  response = "Hello, I am your create/new request!"
  #placerholder to later display a new form to create a new blog
  return HttpResponse(response)

def display(request):
  response = "Hello, I am your display request!"
  #placerholder to later display a specific blog
  return HttpResponse(response)

def edit(request):
  response = "Hello, I am your edit request!"
  #placerholder to later edit a specific blog
  return HttpResponse(response)

def destroy(request):
  response = "Hello, I am your destroy request!"
  #placerholder to later delete a specific blog
  return HttpResponse(response)
