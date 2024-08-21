from django.db import models

# Create your models here.

class Users(models.Model):
    Fname=models.CharField(max_length=100)
    Lname=models.CharField(max_length=100)
    username = models.CharField(max_length=255)
    password=models.CharField(max_length=200)
    C_task=models.IntegerField(default=0,null=True)
    T_task=models.IntegerField(default=0,null=True)
class Task(models.Model):
    task_user_name=models.CharField(max_length=255 ,null=True)
    user_task=models.TextField(max_length=5000)
    C_or_Not=models.BooleanField(default=False,null=True)
    