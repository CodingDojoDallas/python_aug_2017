from django.shortcuts import render, redirect, reverse

# Create your views here.

def index(request):
    context = {
        'key' : 'i want to make this thing a function so i can just do all my logic in here and print everything out'
    }
    return render(request, 'survey_app/index.html', context)