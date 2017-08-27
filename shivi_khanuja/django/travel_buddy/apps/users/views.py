from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
	

	# Create your views here.
	

def main(request):
    return render(request, 'users/main.html')


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
            return redirect('/users/success')


def new(request):
    return render(request, 'users/travels.html')
        
def login(request):
    # if they actually log in, then redirect to success, if not throw an error message at them
    if request.method == 'POST':
        result = User.objects.validate_login(request.POST)
    if result['status'] == False: #generate an error message
        messages.error(request, result['error'])
        return redirect('/')
    else: #save the id into session
        request.session['user_id'] = result['user'].id
        return redirect('/users/success')


def success(request):
    return render(request, 'users/travels.html')




def add(request):
    #validate the input
    context = {
        'authors' : Author.objects.all()
    }
    #return errors
    #query the DB??
    #redirect to the next page
    
    return render(request, 'users/add_book.html', context)
