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

delete_msg = {"msg": "delete success", "code": "40010"}
update_msg = {"msg": "update success", "code": "20010"}


def deal_data(data):
    rep = {"msg": "success", "code": "200", "data": []}
    for i in range(len(data)):
        rep["data"].append(data[i])
    return rep


def delete(request):
    req = json.loads(request.body)
    models.MoKuai.objects.filter(id=req["id"]).delete()
    return JsonResponse(delete_msg)


def all_data(request):
    """用于查询所有数据并用json格式返回"""
    pass

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
        return JsonResponse(delete_msg)
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
    :param request:
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
        return delete(request)
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
    if request.method == "GET" and not request.is_ajax():
        # 查询所有项目返回
        # 所有数据的QuerySet对象
        pro_list = models.Project.objects.all()
        return render(request, "./templates/mokuai.html", {"pro": pro_list})
    elif request.method == "GET" and request.is_ajax():
        # mo循环了是字典，用all可以
        mo = models.MoKuai.objects.values()
        res = deal_data(mo)
        # 这里要根据项目的id，查询到项目的名字返回在页面上显示
        # moo = models.MoKuai.objects.all()
        # for i in moo:
        #     print(i.id, i.project.name)
        # m_pro = models.MoKuai.objects.values("project__name")
        # print(m_pro)
        for i in range(len(res["data"])):
            m_pro = models.Project.objects.filter(id=res["data"][i]["project_id"]).get()
            res["data"][i]["m_pro"] = m_pro.name
        return JsonResponse(res)
    elif request.method == "POST":
        req = json.loads(request.body)
        if "id" in req:
            # models ---> project多对一
            qm = models.MoKuai.objects.filter(id=req["id"])
            qm.update(name=req["m_name"], m_description=req["m_description"], m_creator=req["m_creator"],
                      m_tester=req["m_tester"], project_id=req["m_pro"], update_time=datetime.datetime.now())
            return JsonResponse(update_msg)
        else:
            # models ---> project多对一  \\\先实例化外键查询
            # ORM查询操作详解：https://www.cnblogs.com/hanbowen/p/9566787.html
            # print(type(req["m_proName"]))
            # pname = models.Project.objects.get(name=req["m_proName"]) 通过id匹配
            models.MoKuai.objects.create(name=req["m_name"], m_description=req["m_description"],
                                         m_creator=req["m_creator"], m_tester=req["m_tester"], project_id=req["m_pro"])
            return JsonResponse(data={"msg": req}, status=200)
    elif request.method == "DELETE":
        return delete(request)
    else:
        pass


@login_check
def case(request):
    """
    :param request:
    :return: 查询case表，并返回所有的数据
    """
    pass


@login_check
def edit_case(request):
    pass