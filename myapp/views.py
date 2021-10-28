from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def myfunc1(request):
    return HttpResponse('Hello my dear friends')


def welcome(request,name):
    return HttpResponse(f'Hello my dear friend {name}')

def show(request):
    context={'title':'welcome'}
    return render(request,'index.htm',context)