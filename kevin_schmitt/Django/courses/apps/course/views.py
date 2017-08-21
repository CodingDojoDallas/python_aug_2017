from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    print 'this is my index!************'
    return redirect('/course/new')

def new(request):
    print 'this is my new.html page! its rendering'
    return render(request, 'course/new.html')