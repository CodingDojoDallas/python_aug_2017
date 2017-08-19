from django.shortcuts import render, redirect, reverse
from django.contrib import messages #this came from the documentation page
from datetime import datetime

# Create your views here.
def index(request):
    # request.session.flush()
    if 'word_array' not in request.session:
        request.session['word_array'] = []

    return render(request,'session_words_app/index.html')

def create(request):
    # step 0 get or post?
    if request.method == 'POST':
        print '*'*50
        print request.POST
        print '*'*50
    # step 1 validations
        if request.POST['word'] == '':
            messages.error(request, 'word cannot be blank')
            return redirect('/')
    # step 2 figure out what was selected
        if 'color' not in request.POST:
            color = 'black'   # give it a default of black
        else:
            color = request.POST['color']
        if 'font' not in request.POST:
            font_size = 'default_font'
        else:
            font_size = 'large_font'
        word = {
            'value' : request.POST['word'],
            'font_size' : font_size,
            'color' : color,
            'time' : datetime.now().strftime("%H:%M %p, %B %d, %Y")
        }     
        request.session['word_array'].append(word)
        request.session.modified = True #this line makes session save itself so it actually prints

    return redirect('/')

def reset(request):
    if request.method == 'POST':
        request.session.flush()
    return redirect('/')


    
