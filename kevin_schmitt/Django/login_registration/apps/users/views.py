from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def home(request):
    print 'index'
    return redirect('/users/new')

def new(request):
    return render(request, 'users/users.html')

def create(request):
    if request.method == 'POST':
        User.objects.validate_registration()

    return redirect()