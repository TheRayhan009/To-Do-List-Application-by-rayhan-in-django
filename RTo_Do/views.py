from django.shortcuts import render ,redirect
from  datas.models import Task,Users

def home(request):
    log=request.session.get("logornot")
    Uname=request.session.get("username")
    passw=request.session.get("password")
    tasks=Task.objects.all()
    if request.method=="POST":
        add_task_button=request.POST.get("atask")
        complet_task_button=request.POST.get("ctask")
        delete_task_button=request.POST.get("dtask")
        if delete_task_button=="True":
            for i in tasks:
                if check_task=="on":
                    check_task=request.POST.get(f"task{i.id}")
                    s_task=Task.objects.filter(id=i.id)
                    s_task.delete()
        elif complet_task_button=="True":
            for i in tasks:
                ##
                if check_task=="on":
                    check_task=request.POST.get(f"task{i.id}")
                    s_task=Task.objects.filter(id=i.id)
                    s_task.delete()
        elif add_task_button=="True":
            return redirect("/addtask")
        return redirect("/")
    ele={
        "tasks":tasks,
        "log":log,
        "Uname":Uname,
        "passw":passw,
    }
    return render(request, 'home.html',ele)

def addtask(request):
    if  request.method=="POST":
        task_name=request.POST.get("taskname")

    return render(request,"addtask.html")

def signin(request):
    if request.method=="POST":
        fname=request.POST.get("first_name")
        lname=request.POST.get("last_name")
        uname=request.POST.get("username")
        upass=request.POST.get("password")
        
        data=Users(
            Fname=fname,
            Lname=lname,
            username=uname,
            password=upass
        )
        data.save()
        return redirect("/login")
    return render(request,"signin.html")

def login(request):
    if request.method=="POST":
        logornot=True
        username=request.POST.get("username")
        password=request.POST.get("password")
        chak=Users.objects.get(username=username,password=password)
        if chak:
            request.session["username"] = username
            request.session["password"] = password
            request.session["logornot"] = logornot
        return redirect("/")
    return render(request,"login.html") 

def logout(request):
    request.session.flush()
    return redirect("/")