from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(request):
  context = {
    "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  return render(request,'likes_books/index.html', context)