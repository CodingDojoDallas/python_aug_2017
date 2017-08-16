from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "Hello, I am your index request!"
    context = {
        'myClass': request.session['box']
    }

    return render(request, 'session_words/index.html', context)


def add(request):
    print request.POST
    if 'box' in request.POST:
        request.session['box'] = 'checked'
        print 'IT WAS CHECKED*************'
        print request.session['box']
        print '*&'*15
    elif 'box' not in request.POST:
        request.session['box'] = 'unchecked'
        print 'IT WAS NOT CHECKED*************'
        print request.session['box']
        print '*&'*15

    # elif request.POST['color'] = 'blue'
    #     request.session['color'] = 'blue'


    # print request.POST['font']
    # if request.POST.get('font', True):
    #     #css font now BIG
    return redirect('/session_words')

