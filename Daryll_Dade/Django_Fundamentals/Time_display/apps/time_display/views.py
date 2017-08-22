from django.shortcuts import render, HttpResponse
from datetime import datetime



# Create your views here.
def index(request):
    date = datetime.now()

    context = {
        'date': date,
    }

    return render(request, 'time_display/index.html', context)
