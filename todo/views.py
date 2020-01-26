from django.shortcuts import render,redirect
from .models import User,Task
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def login(request):
    if request.session.has_key('id'):
        user=User.objects.get(id=request.session['id'])
        tasks=user.task_set.all().order_by('-updated_on')
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
        newtask=Task(task=request.POST['task'],userId=User.objects.get(id=request.session['id']),headtask=request.POST['head'])
        newtask.save()
        return HttpResponse(newtask.id) 

    

def logout(request):
    del request.session['name']
    del request.session['id']
    return redirect(reverse('todo:login'))