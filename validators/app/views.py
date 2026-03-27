from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse


def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            topic_name=TFDO.cleaned_data['topic_name']
            LTO=Topic.objects.get_or_create(topic_name=topic_name)
            if LTO[1]:
                return HttpResponse('New Topic is Created')
            else:
                return HttpResponse('Topic Is Already present')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_topic.html',d)


def insert_webpage_by_mf(request):
    EWMFO=Webpageform()
    d={'EWMFO':EWMFO}
    if request.method=='POST':
        WDMFO=Webpageform(request.POST)
        if WDMFO.is_valid():
            WDMFO.save()
            return HttpResponse('Webpage  is created')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'insert_webpage_by_mf.html',d)