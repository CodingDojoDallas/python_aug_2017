from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect('/users/new')

def new(request):
    return render(request, 'users/new.html')