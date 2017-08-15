# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime

# Create your views here.
def index(request):
	context = {
	"time_date": datetime.now().strftime("%I:%M %p %m-%d-%Y")
	}
	return render(request, 'time_display/index.html', context)
