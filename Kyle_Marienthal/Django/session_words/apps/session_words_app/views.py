from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):
    return render(request,'session_words_app/index.html')