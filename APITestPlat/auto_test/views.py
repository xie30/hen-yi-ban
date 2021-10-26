from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def hello(request):
    return HttpResponse('hello')

def env_add(request):
    return HttpResponse('新增')

def env(requset):
    #查询env表并返回数据

    return render(requset, "./templates/home.html")