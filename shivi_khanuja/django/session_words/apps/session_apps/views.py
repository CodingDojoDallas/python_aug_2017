from django.shortcuts import render

def index(request):
    return render(request,'session_apps/index.html')

def create(request):
    
    if request.method == 'POST':
        print request.POST

      if request.POST ['word'] == '':
          messages.error(request,'Word cannont be blank')         
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
          'value': request.POST['word'],
          'font_size': font_size,
          'color': color 
      }   

      request.session['word_array'].append(word)
      print '*'*25
      print request.session['word_array']   
      request.session.modified = True

    return redirect('/')    
