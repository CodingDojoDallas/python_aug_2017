from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'ninja_models_app/index.html')