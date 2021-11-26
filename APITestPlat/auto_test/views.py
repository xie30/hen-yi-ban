# Create your views here.


import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from auto_test.models import RunEnv, Project
from auto_test import models
import json
from myadmin.views import login_check
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core import serializers


def deal_data(data):
    rep = {"msg": "success", "code": "200", "data": []}
    for i in range(len(data)):
        rep["data"].append(data[i])
    return rep


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
    :param request:
    :return:project.html
    """
    if not request.is_ajax():
        return render(request, './templates/project.html')
    return render(request, './templates/home.html')


@login_check
def projects(request):
    """
    访问项目 and 查询项目的所有数据 and 新增项目 and 删除项目
    :param requset:
    :return:
    """
    if request.method == "POST":
        req = json.loads(request.body)
        # print(req, "id" in req)
        if "id" in req:
            qn = models.Project.objects.filter(id=req["id"])
            qn.update(name=req["pro_name"], p_description=req["pro_description"],
                      p_creator=req["creator"], p_tester=req["tester"],
                      update_time=datetime.datetime.now())
            return JsonResponse(data={"msg": "update ok"}, status=200)
        else:
            models.Project.objects.create(name=req["pro_name"], p_description=req["pro_description"],
                                          p_creator=req["creator"], p_tester=req["tester"])
            return JsonResponse(data={"msg": req}, status=200)
    elif request.method == "GET" and request.is_ajax():
        pro = models.Project.objects.values()
        req = deal_data(pro)
        return JsonResponse(req)
    elif request.method == "DELETE":
        req = json.loads(request.body)
        models.Project.objects.filter(id=req["id"]).delete()
        msg = {"msg": "delete success", "code": "40010"}
        return JsonResponse(msg)
    else:
        if not request.is_ajax():
            return render(request, './templates/project.html')
        return render(request, './templates/home.html')


@login_check
def mokuai(request):
    """
    模块处理
    :param request:
    :return:
    """
    if not request.is_ajax():
        # 查询所有项目返回
        # 所有数据的QuerySet对象
        pro_list = models.Project.objects.all()
        # print(pro_list)
        # for p in pro_list:
        #     print(p.id)
        return render(request, "./templates/mokuai.html", {"pro": pro_list})
    elif request.method == "GET" and request.is_ajax():
        mo = models.MoKuai.objects.values()
        res = deal_data(mo)
        return JsonResponse(res)
    elif request.method == "POST":
        pass
        # 怎么整合一起？

    else:
        pass