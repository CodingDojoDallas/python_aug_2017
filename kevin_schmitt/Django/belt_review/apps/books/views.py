# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def add(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'books/add.html', context)

def create(request):
    print 'this is create***********************'
    #!!!Create book and review in database
    author = Author.objects.make_author(request.POST)
    print author
    return redirect('/books/book_show')

def success(request):
    print 'this is success***************'
    return render(request, 'books/wall.html')

def book_show(request):
    print 'book added to database**********'
    return render(request, 'books/show.html')