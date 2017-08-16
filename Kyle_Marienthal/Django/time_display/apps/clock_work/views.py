from django.shortcuts import render, redirect, reverse
from time import gmtime, strftime
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        'time1' : datetime.now().strftime("%m %d, %Y"),
        'time2' : datetime.now().strftime('%I:%M %p'),
    }
    return render(request, 'clock_work/index.html', context)