from django.shortcuts import render
import datetime

# Create your views here.

from django.http import HttpResponse, JsonResponse
from auto_test.models import RunEnv
from auto_test import models
import json
from django.core import serializers


def env(requset):
    # 查询env表并返回数据
    if requset.is_ajax():
        envs = RunEnv.objects.values()
        rep = {"msg": "success", "code": "200", "data": []}
        for i in range(len(envs)):
            rep["data"].append(envs[i])
        return JsonResponse(rep)
    print("查询失败")
    return render(requset, "./templates/home.html")


def env_add(request):
    if request.is_ajax():
        req = json.loads(request.body)
        models.RunEnv.objects.create(name=req["name"], host_url=req["host_url"], env_description=req["env_description"])
        return JsonResponse(data={"msg": "ok"}, status=200)
    print("新增失败")
    return render(request, "./templates/home.html")


def env_modify(request):
    if request.is_ajax():
        req = json.loads(request.body)
        # run_env : RunEnv
        # run_env = models.RunEnv.objects.filter(id=req["id"]).get()
        # for field in ["name", "host_url", "env_description"]:
        #     setattr(run_env, field, req[field])
        # run_env.save()
        qs = models.RunEnv.objects.filter(id=req["id"])
        # qs : QuerySet
        qs.update(name=req["name"], host_url=req["host_url"], env_description=req["env_description"],
                  update_time=datetime.datetime.now())
        return JsonResponse(data={"msg": "ok"}, status=200)
    print("修改失败")
    return render(request, "./templates/home.html")


def env_delete(request):
    if request.is_ajax():
        envs = json.loads(request.body)
        # print (env)
        models.RunEnv.objects.filter(name=envs["name"]).delete()
        msg = {"msg": "success", "code": "40010"}
        return JsonResponse(msg)
    # return render(requset, "./templates/home.html")
