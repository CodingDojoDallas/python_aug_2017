from django.shortcuts import render

def index(request):
	return render(request, 'dojo_ninjas/index.html')
