from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from auto_test.models import RunEnv
from auto_test import models
import json
from django.core import serializers

def hello(request):
    return HttpResponse('hello')

def env_add(request):
    if request.is_ajax():
        reqs = request.body.decode()
        req = json.loads(reqs)
        # env = RunEnv()
        # env.name = req["name"]
        # env.host_url = req["host_url"]
        # env.env_description = req["env_description"]
        # env.save()
        env = models.RunEnv.objects.create(name=req["name"], host_url=req["host_url"], env_description=req["env_description"])
        return HttpResponse('新增成功')
    print ("新增失败")
    return render(requset, "./templates/home.html")

def env(requset):
    #查询env表并返回数据
    if requset.is_ajax():
        env = RunEnv.objects.values()
        # env = RunEnv.objects.all()
        # result = serializers.serialize("json", env)
        # print(len(env))
        rep = {}
        rep["msg"] = "success"
        rep["code"] = "200"
        rep["data"] = []
        for i in range(len(env)):
            rep["data"].append(env[i])
        # print(rep["data"])
        return JsonResponse(rep)
    return render(requset, "./templates/home.html")