from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return HttpResponse('I am loading all users from the database')

def new(request):
	return render(request,'users/new_user.html')

def create(request):
	print 'Adding user to the database!'
	return redirect('/users')