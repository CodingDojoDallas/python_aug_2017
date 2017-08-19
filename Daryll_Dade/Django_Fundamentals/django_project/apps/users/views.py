# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import User

def home(request):


	return render(request, 'users/index.html')

def new(request):
	return render(request, 'users/new.html')

def create(request):
	print request.POST
	if request.method == 'POST':
		result = User.objects.validate_registration(request.POST)
		print result['status']
		if result['status'] == False:
			#create flash messages
			for error in result['errors']:
				messages.error(request, error )
			#redirect to home page
		return redirect('/users/new.html')
	else:
		#put the user_id into session
		request.session['user_id'] = result['user'].id
		#above line = DICTIONARIES GET BRACKAT NOTATION
					#Classes get DOT Notation!
		#all database entries are instances of a class so DOT notation for db entries!!!!!
		return redirect('users/success')

def success(request):
	print "success route"
	return render(request, 'users/success.html')
