from django.shortcuts import render, redirect,reverse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
 
  return render(request, 'random_word/index.html')

def generated(request):
    # the counter wont increment
    count = 0
    unique_id = get_random_string(length=14)
    count = count + 1
    context = {
        'unique_id' : unique_id,
        'count' : count,

    }
    
    return render(request, 'random_word/index.html', context)


