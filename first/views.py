from http.client import HTTPResponse
from django.shortcuts import render, redirect
from first.models import Profile
from django.http import JsonResponse

# Create your views here.
def index(request):
    return redirect('viewprofiles')

def getprofiles(requests):
    profiles = Profile.objects.all()
    return JsonResponse({
        'profiles':list(profiles.values())
    })
    
def viewprofiles(request):
    return render(request, 'viewprofiles.html')

    
def postprofile(request):
    if request.method == 'POST':
        name=request.POST['name']
        figure=request.POST['figure']
        bio=request.POST['bio']
        postform=Profile.objects.create(
        name=name, figure=figure, bio=bio
        )
        postform.save()
        print('1')
    param={

    }
    return render(request, 'postprofileform.html', param)

def postprofileform(request):

    param={

    }
    return render(request, 'postprofileform.html', param)
    
    
    
