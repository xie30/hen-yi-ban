from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from auto_test.models import RunEnv
from auto_test import models
import json
from django.core import serializers

def hello(request):
    return HttpResponse('hello')

def env(requset):
    #查询env表并返回数据
    if requset.is_ajax():
        env = RunEnv.objects.values()
        rep = {}
        rep["msg"] = "success"
        rep["code"] = "200"
        rep["data"] = []
        for i in range(len(env)):
            rep["data"].append(env[i])
        return JsonResponse(rep)
    print("查询失败")
    return render(requset, "./templates/home.html")

def env_add(request):
    if request.is_ajax():
        reqs = request.body.decode()
        req = json.loads(reqs)
        env = models.RunEnv.objects.create(name=req["name"], host_url=req["host_url"], env_description=req["env_description"])
        return JsonResponse(data={"msg":"ok"},status=200)
    print ("新增失败")
    return render(request, "./templates/home.html")

def env_delete(request):
    if request.is_ajax():
        shan = request.body.decode()
        env = json.loads(shan)
        print (env)
        models.RunEnv.objects.filter(name=env["name"]).delete()
        msg = {"msg": "success", "code": "40010"}
        return JsonResponse(msg)
    # return render(requset, "./templates/home.html")