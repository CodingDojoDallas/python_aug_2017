from django.shortcuts import render

def index(request):
	return render(request, 'likes_books/index.html')
