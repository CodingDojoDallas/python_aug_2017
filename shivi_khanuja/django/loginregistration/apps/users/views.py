from django.shortcuts import render, redirect

from django.contrib import messages
from .models import User 

def home(request):
    return redirect('/users/new')

def new(request):
    return render(request,'users/new.html')

def create(request):
    if request.method == 'POST':
        result =User.objects.validate_registration(request.POST)
        if result['status'] == False:
            for error in result ['errors']:
                 messages.error(request, error)
                 return redirect ('/users/new')
        else:
            request.session['user_id'] = result ['user'].user_id
            return redirect('/users/success')

def success(request):
    return render(request, 'users/success.html')

def login(request):
    return render(request, 'users/success.html')

def authenticate(request):
    if request.method == 'POST':
          result = User.objects.validate_login(request.POST)
          if result ['status'] == False:
              messages.error(request, result['error'])
              return redirect('/users/new')
          else:
              
              return redirect('/users/success')

def logout(request):
    request.session.flush()
    return redirect ('/')                                 
