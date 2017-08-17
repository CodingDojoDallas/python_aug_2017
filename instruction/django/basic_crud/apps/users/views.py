from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    return redirect('/users/new')

def new(request):
    return render(request, 'users/new.html')

def create(request):
    User.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        age=request.POST['age']
    )
    return redirect('/users')

def getUsers(request):
    # go to to the DB, get all the users
    # display them on an HTML page
    users = User.objects.all()
    context = { 'users' : users }
    return render(request, 'users/index.html', context)

def show(request, user_id):
    user = User.objects.get(id=user_id)
    context = { 'user' : user }
    return render(request, 'users/show.html', context)

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    context = { 'user' : user }
    return render(request, 'users/edit.html', context)

def update(request, user_id):
    User.objects.filter(id=user_id).update(
        name=request.POST['name'],
        email=request.POST['email'],
        age=request.POST['age']
    )
    return redirect('/users')

def destroy(request, user_id):
    User.objects.filter(id=user_id).delete()
    return redirect('/users')
