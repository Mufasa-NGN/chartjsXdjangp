from django.urls import path, re_path
from first import views as v

# app_name = 'first'

urlpatterns = [
    path('', v.index, name='index'),
    path('getprofiles/', v.getprofiles, name='getprofiles'),
    path('viewprofiles/', v.viewprofiles, name='viewprofiles'),
    path('postprofileform/', v.postprofileform, name='postprofileform'),
    path('postprofile/', v.postprofile, name='postprofile'),
    
    
]