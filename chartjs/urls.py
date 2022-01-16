from django.urls import path, re_path
from . import views as v

# app_name = AppName

urlpatterns = [
    path('', v.viewchart, name='viewchart'),
]