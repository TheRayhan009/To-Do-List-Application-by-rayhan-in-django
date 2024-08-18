from django.shortcuts import render
from  datas.models import Task,Users

def home(request):
    tasks=Task.objects.all()
    ele={
        "tasks":tasks,
    }
    return render(request, 'home.html',ele)

def signin(request):
    if request.method=="POST":
        pass
    return render(request,"signin.html")