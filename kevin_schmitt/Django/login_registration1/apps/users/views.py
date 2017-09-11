from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    print 'THIS IS MY HOME def******************'
    return redirect('/users/new')

def new(request):
    print "this is new**********"
    if 'user_id' in request.session:
        return redirect('/users/success')
    else:
        return render(request, 'users/new.html')

def create(request):
    print 'this is create************'
    print request.POST
    if request.method == 'POST':
        result = User.objects.validate_registration(request.POST)
        print result
        print result['status']
        #if dict - have to use square bracket notation
        #if class - have to use . notation
        if result['status'] == False:
            #create flash messages
            for error in result['errors']:
                messages.error(request, error)
            return redirect('/users/new')
        else:
            #put user_id into session
            request.session['user_id'] = result['user'].id
            request.session['name'] = result['user'].name
            return redirect('/users/success')

def success(request):
    print 'this is success***********'
    if 'user_id' not in request.session:
        return redirect('/users/new')
    else:
        return render(request, 'users/success.html')

# def login(request):
#     return render(request, 'users/login.html')

def authenticate(request):
    print 'this is authenticate*******************'
    if request.method == 'POST':
        result = User.objects.validate_login(request.POST)
        print result
        if result['status'] == False:
            #generate error message
            messages.error(request, result['error'])
            return redirect('/users/new')
        else:
            request.session['user_id'] = result['user'].id
            request.session['name'] = result['user'].name
            return redirect('/users/success')

def logout(request):
    print 'this is logout***************'
    request.session.flush()
    return redirect('/')