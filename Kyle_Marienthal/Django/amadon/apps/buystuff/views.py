from django.shortcuts import render, redirect, reverse

# Create your views here.

def index(request):
    return render(request, 'buystuff/index.html') #go back here and add in the app name/index.html

def buy(request):
    
    return render(request, '/thankyou.html')
