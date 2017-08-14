from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
  response = "Hello, I am your first request!"
  #placer holder to later display all blogs
  return HttpResponse(response)

def new(request):
  response = "Hello, I am your second request!"
  #placer holder to later display a new form to create a new blog
  return HttpResponse(response)

def display(request):
  response = "Hello, I am your third request!"
  #placer holder to later display a specific blog
  return HttpResponse(response)

def edit(request):
  response = "Hello, I am your fourth request!"
  #placer holder to later edit a specific blog
  return HttpResponse(response)

def destroy(request):
  response = "Hello, I am your fifth request!"
  #placer holder to later delete a specific blog
  return HttpResponse(response)
