from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    print 'this is my index'
    return redirect('/users/new')

def new(request):
    return render(request, 'users/new.html')

def create(request):
    User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        age = request.POST['age'],
    )
    return redirect('/users/get')

def getUsers(request):
    users = User.objects.all()
    context = { 'users': users}
    return render(request, 'users/index.html', context)