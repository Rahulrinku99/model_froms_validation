from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}
    if request.method=="POST":
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('topic inserted successfully')
        else:
            return HttpResponse('data is not valid')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WF=WebpageForm()
    d={'WF':WF}
    if request.method=='POST':
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse('Webpage inserted succesfully')
        else:
            return HttpResponse('datat is not valid')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    AF=AccessRecordForm()
    d={'AF':AF}
    if request.method=="POST":
        AFD=AccessRecordForm(request.POST)
        if AFD.is_valid():
            AFD.save()
            return HttpResponse('AccessRecord submitted successfuly')
        else:
            return HttpResponse('data is not valid')
    return render(request,'insert_access.html',d)