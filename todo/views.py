from django.shortcuts import render
from .models import User,Task
from django.http import HttpResponse
# Create your views here.
def login(request):
    if request.session.has_key('id'):
        context={
            'username' : request.session['name'],
            'id': request.session['id']
        }
        return render(request,'todo/home.html',context)
    else:
        return render(request,'todo/login.html')

def verifyCredentials(request):
    user=User.objects.get(username=request.POST['username'],password=request.POST['password'])
    request.session['name'] = user.username
    request.session['id'] = user.id
    return HttpResponse(user.id)