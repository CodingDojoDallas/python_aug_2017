# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect

def random_word(n):
	return get_random_string(length = n)

# Create your views here.
def index(request):
	try:
		request.session['tries']
	except KeyError:
		request.session['tries'] = 0

	return render(request, 'word_generator/index.html')

def generate(request):
	request.session['tries'] += 1
	request.session['word'] = random_word(14)
	return redirect ('/')

def reset(request):
	del request.session['tries']
	del request.session['word']
	return redirect('/')
