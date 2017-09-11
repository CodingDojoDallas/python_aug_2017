# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
	if 'word_array' not in request.session:
		request.session['word_array'] = []

	return render(request, 'session_words/index.html')

def create(request):
	#1: Validate
	if request.method == "POST":
		print request.POST
		if request.POST['word'] == "":
			messages.error(request, "Word cannot be blank")
	#2: Figure out what was selected
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
			'color': color,
			'time': datetime.now().strftime('%A,%d %b %Y %I:%M %p')
		}

		request.session['word_array'].append(word)
		request.session.modified = 'True'

	return redirect('/')

def reset(request):
	if request.method == 'POST':
		request.session.flush()
	return redirect('/')
