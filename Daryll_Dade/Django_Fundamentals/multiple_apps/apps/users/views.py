# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse

def index(request):

	return render(request, 'users/index.html')

def new(request):

	return render(request, 'users/new.html')

def register(request):

	return render(request, 'users/new.html')

def login(request):

	return render(request, 'users/login.html')

# Create your views here.
