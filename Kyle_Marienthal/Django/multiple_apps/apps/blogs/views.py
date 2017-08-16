from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):
    return render(request, 'blogs/index.html')

def new(request):
    return render(request, 'blogs/new.html')

def create(request):
    return render(request, 'blogs/create.html')