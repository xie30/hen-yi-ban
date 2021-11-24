# Create your views here.


import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from auto_test.models import RunEnv,Project
from auto_test import models
import json
from myadmin.views import login_check
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core import serializers


@login_check
def env(request):
    # 查询env表并返回数据
    # if requset.session.get("is_login"):
    if request.is_ajax():
        envs = RunEnv.objects.values()
        rep = {"msg": "success", "code": "200", "data": []}
        for i in range(len(envs)):
            rep["data"].append(envs[i])
        return JsonResponse(rep)
    else:
        print("查询失败")
        return render(request, "./templates/home.html")
    # else:
    #     #如果没有权限，怎么让用户直接跳转到登录页????怎样全局加上session，每个函数都加太麻烦了
    #     # 1.
    #     #2.login_required,或者自己写一个装饰器
    #     return redirect('/login/')


@login_check
def env_add(request):
    if request.is_ajax():
        req = json.loads(request.body)
        models.RunEnv.objects.create(name=req["name"], host_url=req["host_url"], env_description=req["env_description"])
        return JsonResponse(data={"msg": "ok"}, status=200)
    print("新增失败")
    return render(request, "./templates/home.html")


@login_check
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


@login_check
def env_delete(request):
    if request.is_ajax():
        envs = json.loads(request.body)
        # print (env)
        models.RunEnv.objects.filter(name=envs["name"]).delete()
        msg = {"msg": "success", "code": "40010"}
        return JsonResponse(msg)
    # return render(requset, "./templates/home.html")


@login_check
def project(request):
    """
    查询project数据
    :param request:
    :return:
    """

    return redirect(reverse("project_page"))
    # return render(request, './templates/project.html')


def project_page(request):
    if not request.is_ajax():
        print("不是ajax")
        return render(request, './templates/project.html')
    return render(request, './templates/home.html')


@login_check
def add_project(requset):
    """
    新增项目
    :param requset:
    :return:
    """
    pass


@login_check
def edit_project(request):
    """
    编辑项目信息
    :param request:
    :return:
    """
    pass


@login_check
def delte_project(request):
    """
    删除项目
    :param request:
    :return:
    """
    pass