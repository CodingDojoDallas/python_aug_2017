from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        'title': "Cody's amazing website",
        'date': datetime.now(),
        'img_url': 'http://blog.caranddriver.com/wp-content/uploads/2016/04/2018-Tesla-Model-3-105-626x382.jpg',
        'pokemon': [
            '1',
            '2',
        ]
    }
    return render(request, 'main_app/index.html', context)

def login(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        request.session['name'] = request.POST['name']
        return redirect('/dashboard')
        
def dashboard(request):
    return render(request, 'main_app/dashboard.html')

def favoriteNumber(request, fave_num):
    context = {
        'favorite_number': fave_num
    }
    return render(request, 'main_app/favorite_number.html', context)

def favoriteTeam(request, fave_team):
    context = {
        'favorite_team': fave_team
    }
    return render(request, 'main_app/favorite_team.html', context)