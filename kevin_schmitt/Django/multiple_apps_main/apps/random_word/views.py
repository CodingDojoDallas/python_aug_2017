from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
unique_id = get_random_string(length=10)
def index(request):
    return render(request, 'random_word/index.html')

def generate(request):
    count = 0
    print request.method
    if request.method == 'POST':
        print '*'*35
        count += 1
        print count
        print unique_id
        return redirect('/', count=count)
    else:
        return redirect('/')

