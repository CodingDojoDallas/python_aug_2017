from django.shortcuts import render, HttpResponse, redirect
import string, random
  # the index function is called when root is visited
def index(request):
    return render(request, 'random_word/index.html')

def generate(request, methods=['POST']):
    if request.method == "POST":
        print '***'*25
        return redirect('/')
    else:
        return redirect('/')
