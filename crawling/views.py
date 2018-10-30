#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from crawling.models import Taglist
import json
# Create your views here.

def tagnum(request):
    tags=[]
    tags.append(request.GET.get('name1'))
    tags.append(request.GET.get('name2'))
    tags.append(request.GET.get('name3'))
    tags.append(request.GET.get('name4'))
    tags.append(request.GET.get('name5'))
    jsonlist=[]
    m=Taglist.objects
    for i in range(0,5):
        f=m.filter(tag_name=tags[i]).count()
        if f!=1:
            value=None
        else:
            value=m.get(tag_name=tags[i]).num_tag
        n={tags[i]:value}
        jsonlist.append(n)
    return HttpResponse(json.dumps(jsonlist), content_type=u"application/json; charset=utf-8")

def pictures(request):
    tag=request.GET.get('name')
    jsonlist=[]
    m=Taglist.objects
    if m.filter(tag_name=tag).count()!=1:
        urls=None
    else:
        urls=m.get(tag_name=tag).imgurls
    return HttpResponse(json.dumps({tag:urls}), content_type=u"application/json; charset=utf-8")
