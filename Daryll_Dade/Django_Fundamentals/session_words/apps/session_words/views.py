# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import datetime


def index(request):


    return render(request, 'session_words/index.html')


def modify(request):
    #Step 1: validation
    print "posting"
    if request.method=="POST":
        if request.POST['name']:
            named=request.POST['name']
            print named
        # else:
        #     #flash message "Textbox cannot be empty"
        # pass

    #

        return redirect('/')
    return redirect('/')
    # Create your views here.
