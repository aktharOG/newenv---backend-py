from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from .views import *
urlpatterns = [
    path('login', csrf_exempt(login)),
    path('getnotificationforteacher', csrf_exempt(getnotificationforteacher)),
    path('getnotificationforstudents', csrf_exempt(getnotificationforstudents)),
    path('getprofile', csrf_exempt(getprofile)),
    path('gettimetable', csrf_exempt(gettimetable)),
   




    
]
