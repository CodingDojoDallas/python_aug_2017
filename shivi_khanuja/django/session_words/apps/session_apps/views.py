from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime

def index(request):
    # request.session.flush()
    if 'word_array' not in request.session:
        request.session['word_array'] = []

    return render(request,'session_apps/index.html')

def create(request):
    
    if request.method == 'POST':
        print'*'*50
        print request.POST
        print '*'*50
    if request.POST ['word'] == '' :
          messages.error(request, 'Word cannont be blank')         
          return redirect('/')

    if 'color' not in request.POST:
          color = 'black'
    else:
          color = request.POST['color']    
    if 'font' not in request.POST:
          font_size = 'default_font'
    else:
          font_size = 'large_font'

    word = {
         'value' : request.POST['word'],
         'font_size' : font_size,
         'color' : color ,
         'time' : datetime.now().strftime("%H:%M %p, %B %d, %Y")
      }   

    request.session['word_array'].append(word)
      
    request.session.modified = True

    return redirect('/')  

def reset(request):
    if request.method == 'POST':
        request.session.flush()
    return redirect('/')

