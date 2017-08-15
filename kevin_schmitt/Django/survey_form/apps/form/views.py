from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "Hello, I am your index request!"
    return render(request, 'form/index.html')

def display(request):
    print request.method
    request.session['name']=request.POST['name']
    request.session['email']=request.POST['email']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    request.session['comment']=request.POST['comment']
    print request.session['comment']
    return redirect(request, 'form/display.html')

