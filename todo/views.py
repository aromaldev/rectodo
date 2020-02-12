from django.shortcuts import render,redirect
from .models import User,Task
from django.http import HttpResponse,JsonResponse
from django.urls import reverse
from django.core import serializers
import json
# Create your views here.
def login(request):
    if request.session.has_key('id'):
        user=User.objects.get(id=request.session['id'])
        tasks=user.task_set.filter(headtask=0).order_by('-created_on')
        context={
            'username' : request.session['name'],
            'id': request.session['id'],
            'tasks':tasks
        }
        return render(request,'todo/home.html',context)
    else:
        return render(request,'todo/login.html')

def verifyCredentials(request):
    try:
        user=User.objects.get(username=request.POST['username'],password=request.POST['password'])
        request.session['name'] = user.username
        request.session['id'] = user.id
        return redirect(reverse('todo:login'))
    except User.DoesNotExist:
        return HttpResponse("Invalid")

def addTask(request):
    if(request.method=="POST"):
        newtask=Task(task=request.POST['task'],userId=User.objects.get(id=request.session['id']),headtask=request.POST['head'],tasktype=request.POST['tasktype'])
        newtask.save()
        return HttpResponse(newtask.id) 

    

def logout(request):
    del request.session['name']
    del request.session['id']
    return redirect(reverse('todo:login'))

def completeTask(request):
    if(request.method=="POST"):
        task=Task.objects.get(id=request.POST['id'])
        task.completed=request.POST['status']
        task.save()
        return HttpResponse("success")

def fetchtodo(request):
    tasks=Task.objects.filter(headtask=request.POST['id'])
    # return HttpResponse(dict(tasks),content_type='application/json')
    task_list = serializers.serialize('json', tasks)
    return HttpResponse(task_list, content_type="text/json-comment-filtered")