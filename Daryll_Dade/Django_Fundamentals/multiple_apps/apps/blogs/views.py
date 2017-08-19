# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponse

# def index(request):
#
#     Responce ="HttpResponse Index Page"
#     return HttpResponse(Responce)

def index(request, blog_id=0):

    if blog_id == 0:
        index_page_info = "Placeholder for Blogs List"
        return HttpResponse (index_page_info)
    else:
        context = {
        'blog_id': blog_id,
        }
    return render(request, 'blogs/index.html', context)

def new(request):
    response = "New Blog"
    return HttpResponse(response)

def create(request):

    return redirect('/')

def show(request,blog_id = 0):

    response = {
        'blog_id': blog_id,
    }

    return HttpResponce(response)

def edit(request, blog_id = 0):

    response ={
        'edit_id': blog_id,
    }
    return httpresponse(response)

def destroy(request, blog_id=0):



    return redirect('/')
