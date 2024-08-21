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
            edit_task_button=request.POST.get("etask")
            reset_task_button=request.POST.get("rtask")
            search_task_button=request.POST.get("searchbtn")
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
                        s_task=Task.objects.get(id=i.id)
                        s_task.C_or_Not=True
                        s_task.save()
                result=Task.objects.filter(task_user_name=Uname)
                pintask = Users.objects.get(username=Uname).T_task - Users.objects.get(username=Uname).C_task
                ele={
                    "tasks":result,
                    "log":log,
                    "Uname":Uname,
                    "passw":passw,
                    "num_of_C_task":Users.objects.get(username=Uname).C_task,
                    "numtasks":Users.objects.get(username=Uname).T_task,
                    "pintask":pintask,
                }
                return render(request, 'home.html',ele)
            elif add_task_button=="True":
                x=Users.objects.get(username=Uname).T_task
                data=Users.objects.get(username=Uname)
                data.T_task=x+1
                data.save()
                return redirect("/addtask")
            elif search_task_button=="True":
                search_task=request.POST.get("UTsearch")
                result=Task.objects.filter(user_task__icontains=search_task)
                pintask = Users.objects.get(username=Uname).T_task - Users.objects.get(username=Uname).C_task
                ele={
                    "tasks":result,
                    "log":log,
                    "Uname":Uname,
                    "passw":passw,
                    "num_of_C_task":Users.objects.get(username=Uname).C_task,
                    "numtasks":Users.objects.get(username=Uname).T_task,
                    "pintask":pintask,
                }
                return render(request, 'home.html',ele)
            elif reset_task_button=="True":
                return redirect("/resettask")
            elif edit_task_button=="True":
                v=[]
                for i in tasks:
                    check_task=request.POST.get(f"task{i.id}")
                    if check_task=="on":
                        v.append(i.id)
                if len(v)==1:
                    founded_Task=Task.objects.get(id=v[0])
                    ele={
                        "main_task":founded_Task.user_task,
                        "log":log,
                        "Uname":Uname,
                        "passw":passw,
                        "task_id":v[0],
                    }
                    return render(request,"edit.html",ele)
                else:
                    pintask = Users.objects.get(username=Uname).T_task - Users.objects.get(username=Uname).C_task
                    ele={
                        "tasks":Task.objects.filter(task_user_name=Uname),
                        "log":log,
                        "Uname":Uname,
                        "passw":passw,
                        "num_of_C_task":Users.objects.get(username=Uname).C_task,
                        "numtasks":Users.objects.get(username=Uname).T_task,
                        "pintask":pintask,
                        "ala":True,
                    }
                    return render(request, 'home.html',ele)
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

def about(request):
    Uname=request.session.get("username")
    passw=request.session.get("password")
    log=request.session.get("logornot")
    ele={
        "log":log,
        "Uname":Uname,
        "passw":passw,
    }
    return render(request,"about.html",ele)

def addtask(request):
    Uname=request.session.get("username")
    passw=request.session.get("password")
    log=request.session.get("logornot")
    if  request.method=="POST":
        User_task=request.POST.get("user_task")
        uname=request.session.get("username")
        data=Task(
            task_user_name=uname,
            user_task=User_task,
        )
        data.save()
        return redirect("/")
    ele={
        "log":log,
        "Uname":Uname,
        "passw":passw,
    }
    return render(request,"addtask.html",ele)

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
        chak=Users.objects.filter(username=username,password=password)
        if chak:
            num_of_C_task=0                  
            request.session["cmptask"] = num_of_C_task
            if chak:
                request.session["username"] =  username
                request.session["password"] = password
                request.session["logornot"] = logornot
            return redirect("/")
        else:
            return redirect("/login")
    return render(request,"login.html") 

def edittask(request):
    if request.method=="POST":
        UP_task=request.POST.get("user_edited_task")
        u_task_id=request.POST.get("task_id")
        data=Task.objects.get(id=u_task_id)
        data.user_task=UP_task
        data.save()
        return redirect("/")
    return render(request,"edit.html")


def resettask(request):
    Uname=request.session.get("username")
    passw=request.session.get("password")
    log=request.session.get("logornot")
    if request.method=="POST":
        Uname=request.session.get("username")
        yes_buttom=request.POST.get("byes")
        no_buttom=request.POST.get("bno")
        if yes_buttom=="True":
            data=Task.objects.filter(task_user_name=Uname)
            user_data=Users.objects.get(username=Uname)
            data.delete()
            user_data.T_task=0
            user_data.C_task=0
            user_data.save()
            return redirect("/")
        elif  no_buttom=="True":
            return redirect("/")
    ele={
        "log":log,
        "Uname":Uname,
        "passw":passw,
    }
    return render(request,"reset.html",ele)

def logout(request):
    Uname=request.session.get("username" )
    data=Task.objects.filter(task_user_name=Uname)
    data.delete()
    data=Users.objects.get(username=Uname)
    data.T_task=0
    data.C_task=0
    data.save()
    request.session.flush()
    return redirect("/")