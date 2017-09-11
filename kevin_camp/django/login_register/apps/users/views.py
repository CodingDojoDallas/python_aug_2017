from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

# Create your views here.
def home(request):
	return redirect('/users/new')

def new(request):
	return render(request, 'users/new.html')

def create(request):
	if request.method == 'POST':
		result = User.objects.validate_registration(request.POST)
		if result['status'] == False:
			for error in result['errors']:
				messages.error(request, error)
			return redirect('/users/new')
		else:
			request.session['user_id'] = result['user'].id
			return redirect('/users/travels')

def travels(request):
	return render(request, 'users/travels.html')

def login(request):
	return redirect('/users/travels')

def authenticate(request):
	if request.method == 'POST':
		result = User.objects.validate_login(request.POST)
		if result['status'] == True:
			request.session['user_id'] = result['user'].id
			return redirect('/users/travels')
		else:
			messages.error(request, result['error'])
			return redirect('/')

#to clear session run request.session.flush()
def logout(request):
	request.session.flush()
	return redirect('/')
