from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string



def index(request):
    print 'LINE 7 PRINT'
    if 'count' not in request.session:
        print 'LINE 8 PRINT'
        request.session['count']=0
    if 'random' not in request.session:
        print 'LINE 11 PRINT'
        request.session['random']=0
    context = {
        'count': request.session['count'],
        'random': request.session['random'],
    }
    print 'LINE 17 PRINT'
    return render(request, 'random_word/index.html', context)

def something(request):
    unique_id = get_random_string(length=16)
    print unique_id
    count = request.session['count']
    request.session['random']=unique_id
    count += 1
    print request.method
    context = {
        'count': count,
        'random': unique_id,
    }
    print '*'*30
    return redirect('/random_word')