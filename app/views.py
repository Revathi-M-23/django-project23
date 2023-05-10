from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def insert_topics(request):
    Tfo=TopicForm()
    d={'Tfo':Tfo}

    if request.method=='POST':
        tdof=TopicForm(request.POST)
        if tdof.is_valid():
            tdof.save()
            return HttpResponse('topic inserted..')

    return render(request,'insert_topics.html',d)

def insert_web(request):
    wfo=WebpageForm()
    d={'wfo':wfo}

    if request.method=='POST':
        wfd=WebpageForm(request.POST)
        if wfd.is_valid():
            wfd.save()
            return HttpResponse('webpage inserted..')

    return render(request,'insert_web.html',d)

