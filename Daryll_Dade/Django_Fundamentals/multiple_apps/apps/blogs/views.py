# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponse

def index(request):

    response = "Blogs Index"
    return HttpResponse(response)

def new(request):
    response = "New Blog"
    return HttpResponse(response)

def create(request):

    return redirect('/')

def show(request):

    response = ""

    return HttpResponce(response)

def edit(request):

    response =""
    return httpresponse(response)

def destroy(request):

    return redirect('/')
