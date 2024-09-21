from django.shortcuts import render ,redirect
from  datas.models import Task,Users
from datetime import datetime
from django.utils.html import strip_tags
from django.core.mail import send_mail
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
                return redirect("/")
            elif add_task_button=="True":
                x=Users.objects.get(username=Uname).T_task
                data=Users.objects.get(username=Uname)
                data.T_task=x+1
                data.save()
                return redirect("/addtask")
            elif search_task_button=="True":
                search_task=request.POST.get("UTsearch")
                result=Task.objects.filter(user_task__icontains=search_task,task_user_name=Uname)
                start_date = datetime.now()
                user_all_tasks=Task.objects.filter(task_user_name=Uname)
                deadLine_D=[]
                deadLine_H=[]
                deadLine_M=[]
                deadLine_S=[]
                for l in user_all_tasks:
                    user_last_time=l.EndTime
                    user_last_date=l.EndDate
                    user_last_date=user_last_date.replace("-","/")
                    end_date = datetime.strptime(f"{user_last_date} {user_last_time}", "%Y/%m/%d %I:%M %p")
                    time_difference = end_date - start_date
                    total_day = int(((time_difference.total_seconds() / 60) / 60) / 24)
                    total_hour = int((time_difference.total_seconds() / 60) / 60)
                    total_minute = int(time_difference.total_seconds() / 60)
                    total_second = int(time_difference.total_seconds())
                    deadLine_D.append(total_day)
                    deadLine_H.append(total_hour)
                    deadLine_M.append(total_minute)
                    deadLine_S.append(total_second)
                    
                tasks_with_deadlines = zip(result, deadLine_D, deadLine_H, deadLine_M, deadLine_S)
                
                pintask = Users.objects.get(username=Uname).T_task - Users.objects.get(username=Uname).C_task
                ele={
                    "tasks":result,
                    "log":log,
                    "Uname":Uname,
                    "passw":passw,
                    "num_of_C_task":Users.objects.get(username=Uname).C_task,
                    "numtasks":Users.objects.get(username=Uname).T_task,
                    "pintask":pintask,
                    "tasks_with_deadlines":tasks_with_deadlines,
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
        result=Task.objects.filter(task_user_name=Uname)
        pintask = Users.objects.get(username=Uname).T_task - Users.objects.get(username=Uname).C_task
        start_date = datetime.now()
        user_all_tasks=Task.objects.filter(task_user_name=Uname)
        deadLine_D=[]
        deadLine_H=[]
        deadLine_M=[]
        deadLine_S=[]
        for l in user_all_tasks:
            user_last_time=l.EndTime
            user_last_date=l.EndDate
            user_last_date=user_last_date.replace("-","/")
            end_date = datetime.strptime(f"{user_last_date} {user_last_time}", "%Y/%m/%d %I:%M %p")
            time_difference = end_date - start_date
            total_day = int(((time_difference.total_seconds() / 60) / 60) / 24)
            total_hour = int((time_difference.total_seconds() / 60) / 60)
            total_minute = int(time_difference.total_seconds() / 60)
            total_second = int(time_difference.total_seconds())
            deadLine_D.append(total_day)
            deadLine_H.append(total_hour)
            deadLine_M.append(total_minute)
            deadLine_S.append(total_second)
            
        tasks_with_deadlines = zip(user_all_tasks, deadLine_D, deadLine_H, deadLine_M, deadLine_S)
        ele={
            "tasks":Task.objects.filter(task_user_name=Uname),
            "log":log,
            "Uname":Uname,
            "passw":passw,
            "num_of_C_task":Users.objects.get(username=Uname).C_task,
            "numtasks":Users.objects.get(username=Uname).T_task,
            "pintask":pintask,
            "tasks_with_deadlines":tasks_with_deadlines,
        
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
        User_last_date=request.POST.get("enddate")
        User_last_time=request.POST.get("endtime")
        uname=request.session.get("username")
        time_24 = datetime.strptime(User_last_time, "%H:%M")
        User_last_time = time_24.strftime("%I:%M %p")
        data=Task(
            task_user_name=uname,
            user_task=User_task,
            EndDate=User_last_date,
            EndTime=User_last_time,
            
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


def logresettask(request):
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
            request.session.flush()
            return redirect("/")
        elif no_buttom=="True":
            request.session.flush()
            return redirect("/")
    ele={
        "log":log,
        "Uname":Uname,
        "passw":passw,
    }
    return render(request,"logOutReset.html",ele)

def send_e_mail(self):
    tasks = Task.objects.filter(C_or_Not=False)
    user_l=[]
    for task in tasks:
        if task.task_user_name not in user_l:
            user_l.append(task.task_user_name)
            user = Users.objects.get(username=task.task_user_name)
            subject = 'Task Reminder'
            message = f'''
            <html>
            <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
                <h1>------------------------------------- R-TO-DO -----------------------------------</h1>
                <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);">
                    <h2 style="color: #4CAF50;">Task Reminder</h2>
                    <p>Hi <strong>{user.Fname}</strong>,</p>
                    <p>You have a pending task:</p>
                    <p style="background-color: #f3f3f3; padding: 10px; border-left: 4px solid #4CAF50;">
                        <strong>{task.user_task}</strong>
                    </p>
                    <p><strong>Deadline:</strong> {task.EndDate} at {task.EndTime}</p>
                    <p>Please complete it as soon as possible!</p>
                    
                    <div style="text-align: center; margin: 20px 0;">
                        <img src="/static/l1.png"alt="Reminder Image" style="width: 100%; max-width: 500px; border-radius: 8px;">
                    </div>
                    
                    <hr style="border-top: 1px solid #ddd; margin: 20px 0;">
                    <p style="text-align: center; font-size: 12px; color: #888;"><br>This is an automated reminder from your Task Manager</br></p>
                </div>
            </body>
            </html>
            
            '''
            email_from = 'therayhan009@gmail.com'
            recipient_list = [user.Email]
            send_mail(subject, strip_tags(message), email_from, recipient_list,fail_silently=False)
    return redirect("/about")
