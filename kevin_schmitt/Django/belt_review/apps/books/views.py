# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def add(request):
    return render(request, 'books/add.html')

def create(request):
    print 'this is create***********************'
    # if request.method == 'POST':
    #     book = Book.objects.create(
    #         title = request.POST['title'],
    #         author = request.POST['author'],
    #         review = request.POST['review'],
    #         rating = request.POST['rating'],
    #         user = request.session['user_id'],
    #     )
    #     print book
    return redirect('/user_review/success')

def success(request):
    print 'this is success***************'
    return render(request, 'books/wall.html')