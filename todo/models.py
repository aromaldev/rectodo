from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return "username : "+self.username

class Task(models.Model):
    task=models.TextField()
    headtask=models.IntegerField(default=0)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    completed=models.BooleanField(default=0)
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    task_choice=[('task','task'),('todo','todo')];
    tasktype=models.CharField(max_length=5,choices=task_choice,default='task')
    def __str__(self):
        return self.task
