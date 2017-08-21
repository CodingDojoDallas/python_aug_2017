from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
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
    # print 'this is my add page! its redirecting'
    # name = request.POST['name']
    # desc = request.POST['desc']
    # Course.objects.create(name=name,desc=desc)
    if request.method == 'POST':
        result = Course.objects.validate(request.POST)
        print result
        print result['status']
        #if dict - have to use square bracket notation
        #if class - have to use . notation
        if result['status'] == False:
            #create flash messages
            for error in result['errors']:
                messages.error(request, error)
            return redirect('/course/new')
        else:
            #put user_id into session
            # request.session['user_id'] = result['user'].id
            return redirect('/course/new')

def get(request):
    courses = Course.objects.all()
    context = { 'courses': courses }
    return render(request, 'course/new.html', context)

def delete(request, course_id):
    Course.objects.filter(id=course_id).delete()
    return redirect('/course/new')