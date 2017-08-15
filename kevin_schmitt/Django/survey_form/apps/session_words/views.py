from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "Hello, I am your index request!"
    context = {
        'myClass': 'checked'
    }
    return render(request, 'session_words/index.html', context)


def add(request):
    print request.POST
    if 'box' in request.POST:
        print 'IT WAS CHECKED'
    elif 'box' not in request.POST:
        print 'IT WAS NOT CHECKED'
    # print request.POST['font']
    # if request.POST.get('font', True):
    #     #css font now BIG
    return redirect('/session_words')

