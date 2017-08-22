from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count

from .models import User
# Create your views here.
def home(request):
	return redirect('/users/new')

def new(request):
	return render(request, 'users/new.html')

def create(request):
	if request.method == 'POST':
		result = User.objects.validate_registration(request.POST)
		if result['status'] == False:
			#create flash messages
			for error in result['errors']:
				messages.error(request, error)
			#redirect to home page
			return redirect('/users/new')
		else:
			#put the user_id into session
			request.session['user_id'] = result['user'].id
			return redirect('/posts')

def success(request):
	return render(request, 'users/success.html')

def login(request):
	return render(request, 'users/login.html')

def authenticate(request):
	if request.method == 'POST':
		result = User.objects.validate_login(request.POST)
		if result['status'] == False:
			#generate error message
			messages.error(request, result['error'])
			return redirect('/users/login')
		else:
			#save the user_id into session
			request.session['user_id'] = result['user'].id
			return redirect('/posts')

def logout(request):
	request.session.flush()
	return redirect('/')

def show(request, user_id):
	user = User.objects.annotate(num_posts=Count('posts')).filter(id=user_id).first()
	context = {
		'user' : user,
	}
	return render(request, 'users/show.html', context)









