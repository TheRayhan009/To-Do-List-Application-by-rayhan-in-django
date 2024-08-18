from django.db import models

# Create your models here.

class Users(models.Model):
    Fname=models.CharField(max_length=100)
    Lname=models.CharField(max_length=100)
    username = models.CharField(max_length=255)
    password=models.CharField(max_length=200)
    
class Task(models.Model):
    task_user_name=models.CharField(max_length=255)
    user_task=models.TextField(max_length=5000)
    