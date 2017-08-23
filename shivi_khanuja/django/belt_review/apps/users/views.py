from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    return render(request, 'users/index.html')

# def register(request):
#     validate = User.objects.validate_registration(request.POST)
#     return redirect('/users/success')

def register(request):
    if request.method == 'POST':
        result = User.objects.validate_registration(request.POST)
        if result['status'] == False:
            for error in result['errors']:
                messages.error(request, error)
            return redirect('/')
        else:
            return redirect('/users/books')

def new(request):
    return render(request, 'users/books.html')
        
def login(request):
    return redirect('/users/books')

def success(request):
    return render(request, 'users/books.html')
