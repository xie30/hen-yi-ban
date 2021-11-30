# Create your views here.

import datetime, json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from auto_test import models
from auto_test.models import RunEnv, Project
from myadmin.views import login_check
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core import serializers

new_msg = {"msg": "saved successfully", "code": "20010"}
update_msg = {"msg": "update completed", "code": "20020"}
query_msg = {"msg": "query successfully", "code": "20030", "data": []}
delete_msg = {"msg": "successfully deleted", "code": "20040"}
illegal_input_msg = {"error": "illegal input", "code": "40010"}


def deal_data(data):
    query_msg["data"] = []
    for i in range(len(data)):
        query_msg["data"].append(data[i])
    return query_msg


def delete(request):
    if request.is_ajax():
        req = json.loads(request.body)
        # 每个库都要实例化？怎么传？才能公用
        models.MoKuai.objects.filter(id=req["id"]).delete()


def all_data(request):
    """用于查询所有数据并用json格式返回"""
    pass


def check_data(s, *args, **kwargs):
    """
    用于校验字符串是否为空，列表是否为空，字典的value值是否为空!
    如果前端没有校验必填，name字段可以="",而且project_id可以为none，导致会出现一些查询错误
        --创建数据或者更新数据，后台需要校验错误的数据
        --https://www.cnblogs.com/hello-wei/p/12504548.html
    :param s:
    :param args:
    :param kwargs:
    :return: True OR False
    """
    if len(s) == 0 or s is None:
        return False
    return True


@login_check
def env(request):
    # 查询env表并返回数据
    # if requset.session.get("is_login"):
    if request.is_ajax():
        envs = RunEnv.objects.values()
        req = deal_data(envs)
        return JsonResponse(req)
    else:
        print("查询失败")
        return render(request, "./templates/home.html")


@login_check
def env_add(request):
    if request.is_ajax():
        req = json.loads(request.body)
        models.RunEnv.objects.create(name=req["name"], host_url=req["host_url"], env_description=req["env_description"])
        return JsonResponse(data=new_msg, status=200)
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
        return JsonResponse(data=update_msg, status=200)
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
    # return delete(request)


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
            return JsonResponse(data=update_msg, status=200)
        else:
            models.Project.objects.create(name=req["pro_name"], p_description=req["pro_description"],
                                          p_creator=req["creator"], p_tester=req["tester"])
            return JsonResponse(data=new_msg, status=200)
    elif request.method == "GET" and request.is_ajax():
        pro = models.Project.objects.values()
        req = deal_data(pro)
        return JsonResponse(req)
    elif request.method == "DELETE" and request.is_ajax():
        req = json.loads(request.body)
        models.Project.objects.filter(id=req["id"]).delete()
        return JsonResponse(delete_msg)
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
        """
        如果前端没有校验必填，name字段可以="",而且project_id可以为none，导致会出现一些查询错误？？？？
        --创建数据或者更新数据，后台需要校验错误的数据
        --https://www.cnblogs.com/hello-wei/p/12504548.html
        """
        # models ---> project多对一, 项目一旦被删除，id就是none了，查询不到数据，需要处理？--
        # print(res["data"][0]["project_id"])
        for i in range(len(res["data"])):
            if res["data"][i]["project_id"] is None:
                res["data"][i]["m_pro"] = None
            else:
                m_pro = models.Project.objects.filter(id=res["data"][i]["project_id"]).get()
                res["data"][i]["m_pro"] = m_pro.name
        return JsonResponse(res)
    elif request.method == "POST":
        return write_mk(request)
    elif request.method == "DELETE":
        req = json.loads(request.body)
        models.MoKuai.objects.filter(id=req["id"]).delete()
        return JsonResponse(delete_msg)
    else:
        return render(request, "./templates/mokuai.html")


def write_mk(request):
    req = json.loads(request.body)
    if check_data(req["m_name"]) and check_data(req["m_pro"]):
        # print("88888888888888888")
        if "id" in req:
            # models ---> project多对一
            qm = models.MoKuai.objects.filter(id=req["id"])
            try:
                qm.update(name=req["m_name"], m_description=req["m_description"], m_creator=req["m_creator"],
                          m_tester=req["m_tester"], project_id=req["m_pro"], update_time=datetime.datetime.now())
            except Exception as e:
                return JsonResponse(data={"msg": str(e)}, status=400)
            return JsonResponse(update_msg)
        else:
            # models ---> project多对一  \\\先实例化外键查询
            # ORM查询操作详解：https://www.cnblogs.com/hanbowen/p/9566787.html
            try:
                models.MoKuai.objects.create(name=req["m_name"], m_description=req["m_description"],
                                             m_creator=req["m_creator"], m_tester=req["m_tester"],
                                             project_id=req["m_pro"])
            except Exception as e:
                return JsonResponse(data={"msg": str(e)}, status=400)
            return JsonResponse(data=new_msg, status=200)
    else:
        return JsonResponse(data={"msg": req}.update(illegal_input_msg), status=400)


@login_check
def case(request):
    """
    :param request:
    :return: 查询case表，并返回所有的数据
    """
    if request.method == "GET" and not request.is_ajax():
        return render(request, "./templates/case_list.html")
    elif request.method == "GET" and request.is_ajax():
        pass
    else:
        pass


@login_check
def edit_case(request):
    pass
