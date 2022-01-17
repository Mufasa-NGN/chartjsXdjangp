from sre_constants import ATCODES
from django.shortcuts import render
from first.models import Profile 
import requests
# Create your views here.
def viewchart(request):

    labels=[]
    data=[]

    profile=Profile.objects.order_by('name')[:9]
    for i in profile:
        labels.append(i.name)
        data.append(i.figure)

    p={
        'labels':labels,
        'data':data,
    }
    return render(request, 'charts.html', p)
    
def viewnews(request):
    url = 'https://newsapi.org/v2/top-headlines?q=tesla&from=2021-12-16&sortBy=publishedAt&apiKey=7592c6a9adcf478ab80bd16bacb6e0ac'
    r=requests.get(url)

    j=r.json()
    article = j["articles"]



    p={
        'article':article
    }
    return render(request, 'news_api.html', p)
    
