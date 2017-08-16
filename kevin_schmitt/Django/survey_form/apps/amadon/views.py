from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "Hello, I am your index request!"

    return render(request, 'session_words/index.html', context)


def checkout(request):
    print '*'*25

    return redirect('/session_words')

