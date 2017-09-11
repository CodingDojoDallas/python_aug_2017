# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	comment = "placeholder to display all the surveys created"
	return HttpResponse(comment)

def new(request):
	comment = "placeholder for users to add a new survey"
	return HttpResponse(comment)
