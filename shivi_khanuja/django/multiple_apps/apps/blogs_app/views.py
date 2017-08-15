from django.shortcuts import render, redirect, reverse
#Create your views here.
def index(request):
    return render(request, 'blogs_app/index.html')
def new(request):
    return render(request, 'blogs_app/new.html')
def create(request):
    return render(request, 'blogs_app/create.html')
#def  2/edit (request):
    #return render(request, 'blogs/2/edit.html')



