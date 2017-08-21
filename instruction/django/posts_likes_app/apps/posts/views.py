from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from ..users.models import User

# POSTS VIEW FILE

# Create your views here.

def is_logged_in(request):
	if 'user_id' not in request.session:
		return redirect('/')

def index(request):
	is_logged_in(request)

	if 'user_id' not in request.session:
		return redirect('/')
	context = {
		'posts' : Post.objects.all(),
	}
	return render(request, 'posts/index.html', context)

def create(request):
	is_logged_in(request)

	result = Post.objects.validate_post(request.POST, request.session['user_id'])

	if result['status'] == False:
		#create flash messages, redirect to the correct form page
		for error in result['errors']:
			messages.error(request, error)
	return redirect('/posts')

def create_like(request, post_id):
	is_logged_in(request)

	current_user = User.objects.get(id=request.session['user_id'])
	post = Post.objects.get(id=post_id)
	post.likes.add(current_user)
	return redirect('/posts')

