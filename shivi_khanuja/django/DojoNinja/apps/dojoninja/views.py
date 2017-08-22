from django.shortcuts import render, redirect
from .models import dojoninja


def index(request):
    Dojo.object.create(
        name =request.POST['name'],
        city =request.POST['city'],
        state =request.POST['state']
    )
    return redirect('/index.html')

def newList(request):
    Dojo=Dojo.object.all()
    context={ 'dojo' :Dojo }
    return request(request,'dojoninja/newList.html',context)        