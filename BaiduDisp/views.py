from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
import pandas as pd
import os
import csv
import numpy as np
# Create your views here.
import datetime
date = str(datetime.date.today())
class Record():
    def __init__(self, title, abstract, url, source):
        self.title = title
        self.abstract = abstract
        self.url = url
        self.source = source

def display(request):
    rootway = "F:\SpiderData"
    filename=date+'.csv'
    fileway = os.path.join(rootway,filename)
    data = pd.DataFrame(pd.read_csv(fileway,header=0))
    #_id = data['_id'].values
    title = data['title'].values
    abstract = data['abstract'].values
    url = data['url'].values
    source = data['source'].values
    #date = data['date'].values
    Record_list = []
    for i in range(len(title)):
        record = Record(title[i], abstract[i],url[i],source[i])
        Record_list.append(record)
    count=len(title)
    print(count)
    return render(request, 'display.html',{'Record_list':Record_list,'count':count,'date':date})

def save(request):
    count = int(request.POST.get("count"))
    print(count)
    for i in range(1,count+1):
        title=request.POST.get("title"+str(i))
        abstract=request.POST.get("abstract"+str(i))
        url=request.POST.get("url"+str(i))
        source=request.POST.get("source"+str(i))
        tag = request.POST.get("tag"+str(i))
        if tag==None:
            tag=0
        rootway = "F:\TagData"
        filename=date+'.csv'
        fileway = os.path.join(rootway, filename)
        with open(fileway, 'a', newline='', encoding='utf-8-sig') as f:
            text = [title, abstract, url,
                    source, tag]
            writer = csv.writer(f)
            writer.writerow(text)
        #print("保存csv成功")
        # print(title)
        # print(url)
        # print(abstract)
        # print(source)
        # print(tag)
    return render(request,'Success.html')