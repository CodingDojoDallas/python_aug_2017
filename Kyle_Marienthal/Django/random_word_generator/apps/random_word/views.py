from django.shortcuts import render, redirect,reverse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
 count = request.session['count']
 count += 1
 context = {
     'unique_id' : unique_id,
     'count' : count,
     }
     return render(request, 
    'random_word/index.html')

def generated(request):
    # the counter wont increment   
    
    #step 1: generate a random word
    unique_id = get_random_string(length=14)

    #step 2: decide if the count should be 1, or increase the count by one
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    #step 3: save count, and random word into session
    request.session['unique_id'] = unique_id

    #step 4: redirect back to index.html

    
    
    return redirect(request, 'index.html')


