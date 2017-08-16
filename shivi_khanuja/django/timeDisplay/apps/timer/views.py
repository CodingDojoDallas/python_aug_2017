from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
    'title': "The Current Time and Date",
    'date' : datetime.now(),
    }
    return render(request,'timer/index.html', context)