from django.urls import path, re_path
from chartjs import views as v

# app_name = AppName

urlpatterns = [
    path('', v.viewchart, name='viewchart'),
    path('news/', v.viewnews, name='viewnews'),
]