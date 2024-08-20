from django.shortcuts import render ,redirect
from  datas.models import Task,Users

def home(request):
    log=request.session.get("logornot")
    if log:
        Uname=request.session.get("username")
        passw=request.session.get("password")
        tasks=Task.objects.filter(task_user_name=Uname)
        if request.method=="POST":
            add_task_button=request.POST.get("atask")
            complet_task_button=request.POST.get("ctask")
            delete_task_button=request.POST.get("dtask")
            if delete_task_button=="True":
                for i in tasks:
                    check_task=request.POST.get(f"task{i.id}")
                    if check_task=="on":
                        x=Users.objects.get(username=Uname).T_task
                        data=Users.objects.get(username=Uname)
                        data.T_task=x-1
                        data.save()
                        s_task=Task.objects.filter(id=i.id)
                        s_task.delete()
            elif complet_task_button=="True":
                for i in tasks:
                    check_task=request.POST.get(f"task{i.id}")
                    if check_task=="on":
                        x=Users.objects.get(username=Uname).C_task
                        data=Users.objects.get(username=Uname)
                        data.C_task=x+1
                        data.save()
                        s_task=Task.objects.filter(id=i.id)
                        s_task.delete()
            elif add_task_button=="True":
                x=Users.objects.get(username=Uname).T_task
                data=Users.objects.get(username=Uname)
                data.T_task=x+1
                data.save()
                return redirect("/addtask")
            return redirect("/")
        pintask = Users.objects.get(username=Uname).T_task - Users.objects.get(username=Uname).C_task
        ele={
            "tasks":Task.objects.filter(task_user_name=Uname),
            "log":log,
            "Uname":Uname,
            "passw":passw,
            "num_of_C_task":Users.objects.get(username=Uname).C_task,
            "numtasks":Users.objects.get(username=Uname).T_task,
            "pintask":pintask,

        }
        return render(request, 'home.html',ele)
    else:
        return render(request, 'home.html')

def addtask(request):
    if  request.method=="POST":
        User_task=request.POST.get("user_task")
        uname=request.session.get("username")
        data=Task(
            task_user_name=uname,
            user_task=User_task,
        )
        data.save()
        return redirect("/")

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
    if request.method=="POST"          :
        logornot=True
        username=request.POST.get("username")
        password=request.POST.get("password")
        chak=Users.objects.get(username=username,password=password)
        num_of_C_task=0                  
        request.session["cmptask"] = num_of_C_task
        if chak:
            request.session["username"] =  username
            request.session["password"] = password
            request.session["logornot"] = logornot
        return redirect("/")
    return render(request,"login.html") 

def logout(request):
    Uname=request.session.get("username" )
    data=Task.objects.filter(task_user_name=Uname  )
    data.delete()
    data=Users.objects.get(username=Uname)
    data.T_task=0
    data.C_task=0
    data.save()
    request.session.flush()
    return redirect("/")