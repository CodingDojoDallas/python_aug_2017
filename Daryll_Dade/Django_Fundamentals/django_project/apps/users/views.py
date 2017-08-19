# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User

def home(request):


	return render(request, 'users/new')

def new(request):
	return render(request, 'users/new.html')

def create(request):
	print request.POST
	if request.method == 'Post':
		result = User.object.validate_registration(request.POST)
		print result
		return redirect('/')
