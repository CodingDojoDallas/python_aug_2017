from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
  response = "Hello, I am your request!"
  #placeholder to display all the surveys
  return HttpResponse(response)

def new(request):
  response = 'Hello. I am your new method.'
  #placeholder for users to add a new survey
  return HttpResponse(response)