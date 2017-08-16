from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string



def index(request):
    context = {
        'count': 0,
        'random': 0,
    }
    return render(request, 'random_word/index.html', context)

def something(request):
    unique_id = get_random_string(length=16)
    print unique_id
    count =0
    print request.method
    context = {
        'count': count,
        'random': unique_id,
    }
    return redirect('/random_word')