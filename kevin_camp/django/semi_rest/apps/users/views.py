from django.shortcuts import render, redirect, request
from django.contrib import messages
from .models import User

def index(request):
	return redirect('/users/new')

def new(request):
	return render(request, 'users/new.html')

def create(request):
	User.objects.create(
		name=request.POST['name'],
		email=request.POST['email'],
		age=request.POST['age']
	)
	return redirect('/users')

def getUsers(request):
	users = User.objects.all()
	context = { 'users' : users }
	return render(request, 'users/index.html', context)
