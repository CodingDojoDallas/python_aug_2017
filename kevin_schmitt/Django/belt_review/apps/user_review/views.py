from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    print 'this is index****************'
    # request.session.flush()
    return redirect('/user_review/new')

def new(request):
    print 'this is new*****************'
    return render(request, 'user_review/new.html')


def register(request):
    print 'this is register***************'
    print request.POST
    if request.method == 'POST':
        result = User.objects.validate_registration(request.POST)
        print result
        print result['status']
        #if dict - have to use square bracket notation
        #if class - have to use . notation
        if result['status'] == False:
            # request.session['name'] = ''
            #create flash messages
            for error in result['errors']:
                messages.error(request, error)
            return redirect('/user_review/new')
        else:
            #put user_id into session
            request.session['user_id'] = result['user'].id
            request.session['name'] = result['user'].name
            return redirect('/books/success')

def login(request):
    print 'this is login**********************'
    if request.method == 'POST':
        result = User.objects.validate_login(request.POST)
        print result
        if result['status'] == False:
            request.session['name'] = ''
            #generate error message
            messages.error(request, result['error'])
            return redirect('/user_review/new')
        else:
            request.session['user_id'] = result['user'].id
            request.session['name'] = result['user'].name
            return redirect('/books/success')


def logout(request):
    request.session.flush()
    print 'this is logout*****************'
    return redirect('/user_review')


