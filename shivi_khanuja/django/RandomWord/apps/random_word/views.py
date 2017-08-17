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

def generated(request):
    unique_id = get_random_string(length = 14)

    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1    

    request.session['unique_id'] = unique_id    

    return redirect(request, 'random_word/index.html')


