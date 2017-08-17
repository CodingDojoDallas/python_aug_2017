from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
    if 'word_array' not in request.session:
        print 'RESETTING ARRAY!!!!!'
        request.session['word_array'] = []
    print request.session['word_array']

    return render(request, 'main/index.html')

def create(request):
    #step 0 : GET or POST?
    if request.method == 'POST':
        print request.POST
        #step 1 : validations
        if request.POST['word'] == '':
            messages.error(request, 'Word cannot be blank')
            return redirect('/')
        #step2 : figure out what was selected
        if 'color' not in request.POST:
            color = 'black'
        else:
            color = request.POST['color']
        if 'font' not in request.POST:
            font_size = 'default_font'
        else:
            font_size = 'large_font'

        word = {
            'value': request.POST['word'],
            'font_size': font_size,
            'color': color,
            'time': datetime.now().strftime("%A, %d %b %Y %l:%M %p")
        }

        request.session['word_array'].append(word)
        
        #tell session to save itself
        request.session.modified = True

    return redirect('/')

def reset(request):
    if request.method == 'POST':
        request.session.flush()
    return redirect('/')


