# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def index(request):
	return render(request, 'surveys/index.html')

def results(request):
	if request.method == "POST":
		try:
			request.session['tries']
		except KeyError:
			request.session['tries'] = 0
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		request.session['tries'] += 1

		return render(request, 'surveys/results.html')
	else:
		return redirect('/')

def redirect(request):
	return redirect('/')
