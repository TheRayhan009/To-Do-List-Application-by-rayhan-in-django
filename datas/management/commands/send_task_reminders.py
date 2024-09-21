from django.core.management.base import BaseCommand
from django.core.mail import send_mail ,EmailMultiAlternatives
from datetime import datetime
from datas.models import Task, Users
from django.utils.html import strip_tags
class Command(BaseCommand):
    def handle(self,*args, **options):
        self.e_mail_send()
    
    def e_mail_send(self):
        tasks = Task.objects.filter(C_or_Not=False)
        user_l=[]
        date_time_now=datetime.now()
        for task in tasks:
            task_end_date = datetime.strptime(str(task.EndDate+" "+task.EndTime), "%Y-%m-%d %I:%M %p")
            deff = task_end_date - date_time_now 
            sec=int(deff.total_seconds() / 3600)
            print(sec)
            if sec<=5:
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
                            <p>Hi <strong>{user.Fname} {user.Lname}</strong>,</p>
                            <p>You have a pending task:</p>
                            <p style="background-color: #f3f3f3; padding: 10px; border-left: 4px solid #4CAF50;">
                                <strong>{task.user_task}</strong>
                            </p>
                            <p><strong>Deadline:</strong> {task.EndDate} at {task.EndTime}</p>
                            <p>Please complete it as soon as possible!</p>
                            
                            <div style="text-align: center; margin: 20px 0;">
                                <img src="https://www.creativefabrica.com/wp-content/uploads/2021/07/06/Tasks-To-Do-icon-Graphics-14354205-1-1-580x387.jpg"alt="Reminder Image" style="width: 100%; max-width: 500px; border-radius: 8px;">
                            </div>
                            
                            <hr style="border-top: 1px solid #ddd; margin: 20px 0;">
                            <p style="text-align: center; font-size: 12px; color: #888;"><br>This is an automated reminder from your Task Manager</br></p>
                        </div>
                    </body>
                    </html>
                    
                    '''
                    email_from = 'therayhan009@gmail.com'
                    recipient_list = [user.Email]
                    email = EmailMultiAlternatives(subject, strip_tags(message), email_from, recipient_list)
                    email.attach_alternative(message, "text/html")
                    email.send(fail_silently=False)
                    

