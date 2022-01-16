from django.shortcuts import render
from first.models import Profile 
import pandas as pd

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
    
    

