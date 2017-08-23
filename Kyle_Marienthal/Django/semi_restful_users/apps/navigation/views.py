from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return redirect('index')

def index(request):
    return render(request, 'index.html')