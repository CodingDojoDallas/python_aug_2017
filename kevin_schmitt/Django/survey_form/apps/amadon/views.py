from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "Hello, I am your index request!"

    return render(request, 'amadon/index.html')


def buy(request):
    print '*'*30

    return redirect('/amadon/receipt')

def receipt(request):
    print '$'*30

    return render(request, 'amadon/receipt.html')

