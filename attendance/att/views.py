from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def login(request):
  username=request.POST['username']
  password=request.POST['password']
  if(Login.objects.filter(user_id=username,password=password)):
    obj=Login.objects.filter(user_id=username,password=password).values()
    print(obj)
    if(obj[0]['user_type']=="1"):
      return JsonResponse({"message":"Success","user":"teacher","userid":username,"status":True})
    else:
      return JsonResponse({"message":"Success","user":"student","userid":username,"status":True})

  else:
    return JsonResponse({"message":"Failed","status":False})
def getnotificationforteacher(request):
  querySet = Notification.objects.filter(destination="1").values()
  # notifications=Notification.objects.filter(destination="3" or destination="1").values()
  lst=[]
  for x in querySet:
    lst.append(x)
  print(lst)
  return JsonResponse({"message":"Success","data":lst})
def getnotificationforstudents(request):
  querySet = Notification.objects.filter(destination="0").values()
  # notifications=Notification.objects.filter(destination="3" or destination="1").values()
  # print(querySet)
  lst=[]
  for x in querySet:
    lst.append(x)
  print(lst)
  return JsonResponse({"message":"Success","data":lst})
def getprofile(request):
  userid=request.POST['userid']
  log=Login.objects.get(user_id=userid)
  if(log.user_type=="0"):
    obj=Student.objects.filter(user_id=userid).values()
    d=obj[0]
    d.update({"image":"media/"+d['image']})
    print(d)
    
    return JsonResponse({"Message":"Success","Data":d})
  elif(log.user_type=="1"):
    obj=Teacher.objects.filter(user_id=userid).values()
    d=obj[0]
    d.update({"image":"media/"+d['image']})
    print(d)
    
    return JsonResponse({"Message":"Success","Data":d})
  else:
    return JsonResponse({"Message":"Failed"})
def gettimetable(request):
  classid=request.POST['classid']
  timetable=Timetable.objects.filter(class_id=classid).values()
  print(timetable)
  return JsonResponse({"Message":"Success","Data":timetable[0]})

#  Time table(classid)
# Student Search(id)