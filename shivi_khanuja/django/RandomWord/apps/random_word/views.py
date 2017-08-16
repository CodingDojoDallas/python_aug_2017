from django.shortcuts import render , redirect, reverse
from django.utils.crypto import get_random_string

def index(request):
    count = request.session['count']
    count += 1
    context = {
    'unique_id' : unique_id,
    'count' : count,
    }
    return render(request, 'random_word/index.html')

