from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    print 'this is my index!************'
    return redirect('/course/new')

def new(request):
    print 'this is my new.html page! its rendering'
    courses = Course.objects.all()
    context = { 'courses': courses }
    return render(request, 'course/new.html', context)

def add(request):
    # errors=[]
    # print 'this is my add page! its redirecting'
    # if len(request.POST['name']) < 6:
    #     errors.append('Name must be more than 5 characters')
    # if len(request.POST['desc']) < 16:
    #     errors.append('Description must be more than 15 characters')
    # return redirect('/course/get')
    # if not errors:
    name = request.POST['name']
    desc = request.POST['desc']
    Course.objects.create(name=name,desc=desc)
    return redirect('/course/get')

def get(request):
    courses = Course.objects.all()
    context = { 'courses': courses }
    return render(request, 'course/new.html', context)

def delete(request, course_id):
    Course.objects.filter(id=course_id).delete()
    return redirect('/course/new')