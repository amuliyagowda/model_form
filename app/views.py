from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('DATA SUBMITTED')
        else:
            return HttpResponse('DATA INVALID')
    else:
        return render(request,'insert_topic.html',d)
    
def insert_webpages(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('DATA SUBMITTED')
        else:
            return HttpResponse('DATA INVALID')
    return render(request,'insert_webpages.html',d)

def insert_AccessRecordForm(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('DATA SUBMITTED')
        else:
            return HttpResponse('DATA INVALID')
    else:
        return render(request,'insert_AccessRecordForm.html',d)



