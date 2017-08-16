from django.shortcuts import render, redirect, HttpResponse
import random
import string


def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1

    context = {
        'count' : request.session['count']
    }
    return render(request, 'rndm_word/index.html', context)

def generate(request):
    request.session['count'] +=1
    request.session['rndm_word'] = ' '.join(    random.choice(string.ascii_uppercase)     for x in range(14)     )
    context2 = {
        'rndm_word' : request.session['rndm_word'],
        'count' : request.session['count']
    }
    return render(request, 'rndm_word/index.html', context2)
