# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse

def index(request):

    return render(request, 'surveys/index.html')

def new(request):

    return render(request,'surveys/new.html')

# Create your views here.
