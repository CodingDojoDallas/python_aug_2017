# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponse

# def index(request):
#
#     Responce ="HttpResponse Index Page"
#     return HttpResponse(Responce)

def index(request, blog_id):

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

def show(request,blog_id=id):

    response = {
        'blog_id': id,
    }

    return HttpResponce(response)

def edit(request, id=id):

    response ={
        'edit_id': id,
    }
    return httpresponse(response)

def destroy(request, id=id):



    return redirect('/')
