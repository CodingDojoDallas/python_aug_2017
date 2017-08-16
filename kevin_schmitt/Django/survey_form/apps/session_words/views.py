from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime

def index(request):
    if 'word_array' not in request.session:
        request.session['word_array'] = []

    return render(request, 'session_words/index.html')


def add(request):
    #step 0 : GET or POST?
    if request.method == 'POST':
        print '*'*30
        #step 1 : Validate if they have picked anything
        if request.POST['word'] == '':
            messages.error(request, 'Word cannot be blank')
            return redirect('/session_words') 
        #step 2 : find out what was selected      
        if 'color' not in request.POST:
            color = 'black'
        else:
            color = request.POST['color']
        if 'font' not in request.POST:
            font_size = 'default_font'
        else:
            font_size = 'large_font'
    
        time = datetime.now().strftime("%Y-%m-%d %H:%M")
        word = {
            'value': request.POST['word'],
            'font_size': font_size,
            'color': color,
            'time': time,
        }
        request.session['word_array'].append(word)
        print '*'*30
        print request.session['word_array']
        #tell session to save itself
        request.session.modified = True
    return redirect('/session_words')

def reset(request):
    if request.method == 'POST':
        request.session.flush()
    return redirect('/session_words')

