# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	content = 'placeholder to later display all the list of users'
	return HttpResponse(content)

def register(request):
	content = 'placeholder for users to create a new user record'
	return HttpResponse(content)

def login(request):
	content = 'placeholder for users to login'
	return HttpResponse(content)

def new(request):
	return redirect('/register')
