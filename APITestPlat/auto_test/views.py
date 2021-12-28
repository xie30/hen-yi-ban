# Create your views here.

import datetime
import json
import ast

from django.http import JsonResponse
from django.shortcuts import render

from auto_test import models
from auto_test.models import RunEnv, Project, MoKuai, CaseList
from myadmin.views import login_check
from auto_test.thread import CaseThread

new_msg = {"msg": "saved successfully", "code": "20010"}
update_msg = {"msg": "update completed", "code": "20020"}
query_msg = {"msg": "query successfully", "code": "20030", "data": []}
delete_msg = {"msg": "deleted successfully", "code": "20040"}
illegal_input_msg = {"error": "illegal input", "code": "40010"}
run_msg = {"msg": "running", "code": "30010"}


def all_data(request, mod):
    """用于查询所有数据并用json格式返回"""
    rep = mod.objects.values()
    data = deal_data(rep)
    return data


def deal_data(data):
    """查询到的数据转换成json格式"""
    query_msg["data"] = []
    for i in range(len(data)):
        query_msg["data"].append(data[i])
    return query_msg


def delete(request, mod):
    """通过唯一的id删除一条数据"""
    if request.is_ajax():
        req = json.loads(request.body)
        mod.objects.filter(id=req["id"]).delete()


def get_data(data, mos, **d_f_name):
    """
    通过id获取对应的模型中的name字段,整理出完整的数据给前端
    :param data:需要查询的模型的数据
    :param mos:根据id需要查询对应实例化name字段的模型
    :param d:mo中，多对一的实例化属性
    :param f_name:返回给前端显示对应的字段
    :return:根据id返回对应的实例化
    """
    if d_f_name:
        for d, j in d_f_name.items():
            for i in range(len(data["data"])):
                if data["data"][i][d] is None:
                    data["data"][i][j] = None
                else:
                    d_name = mos.objects.filter(id=data["data"][i][d]).get()
                    data["data"][i][j] = d_name.name
        return data


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
        data = all_data(request, RunEnv)
        return JsonResponse(data)
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
    delete(request, RunEnv)
    return JsonResponse(delete_msg)


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
            qn = Project.objects.filter(id=req["id"])
            qn.update(name=req["pro_name"], p_description=req["pro_description"],
                      p_creator=req["creator"], p_tester=req["tester"],
                      update_time=datetime.datetime.now())
            return JsonResponse(data=update_msg, status=200)
        else:
            Project.objects.create(name=req["pro_name"], p_description=req["pro_description"],
                                   p_creator=req["creator"], p_tester=req["tester"])
            return JsonResponse(data=new_msg, status=200)
    elif request.method == "GET" and request.is_ajax():
        data = all_data(request, Project)
        return JsonResponse(data)
    elif request.method == "DELETE" and request.is_ajax():
        delete(request, Project)
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
        pro_list = Project.objects.all()
        return render(request, "./templates/mokuai.html", {"pro": pro_list})
    elif request.method == "GET" and request.is_ajax():
        # mo循环了是字典，用all可以
        mo = MoKuai.objects.values()
        data = deal_data(mo)
        # # 这里要根据项目的id，查询到项目的名字返回在页面上显示
        # """
        # 如果前端没有校验必填，name字段可以="",而且project_id可以为none，导致会出现一些查询错误？？？？
        # --创建数据或者更新数据，后台需要校验错误的数据
        # --https://www.cnblogs.com/hello-wei/p/12504548.html
        # """
        # # models ---> project多对一, 项目一旦被删除，id就是none了，查询不到数据，需要处理？--
        # # print(res["data"][0]["project_id"])
        # for i in range(len(res["data"])):
        #     if res["data"][i]["project_id"] is None:
        #         res["data"][i]["m_pro"] = None
        #     else:
        #         m_pro = Project.objects.filter(id=res["data"][i]["project_id"]).get()
        #         res["data"][i]["m_pro"] = m_pro.name
        res = get_data(data, Project, project_id="m_pro")
        return JsonResponse(res)
    elif request.method == "POST":
        return write_mk(request)
    elif request.method == "DELETE":
        delete(request, MoKuai)
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
        illegal_input_msg.update({"msg": req})
        return JsonResponse(data=illegal_input_msg, status=400)


@login_check
def case(request):
    """
    :param request:
    :return: 查询case表，并返回所有的数据
    """
    if request.method == "GET" and not request.is_ajax():
        env_list = RunEnv.objects.all()
        return render(request, "./templates/case_list.html", {"env_url": env_list})
    elif request.method == "GET" and request.is_ajax():
        data = all_data(request, CaseList)
        # print(data)
        # 模块和项目，在case表中，多对一，存的是id，需要根据id到对应的表查询到对应的数据返回给前端显示
        # get——data函数要怎么改，让下面调用两次变成一次？？？
        data = get_data(data, Project, project_id="pros")
        data = get_data(data, MoKuai, model_id="mokuais")
        return JsonResponse(data)
    elif request.method == "POST" and not request.is_ajax():
        req = json.loads(request.body)
        if "id" in req:
            ca = CaseList.objects.filter(id=req["id"])
            ca.update(include=req["include"], name=req["name"], url=req["url"], method=req["method"],
                      re_header=req["re_header"], param_type=req["param_type"], params=req["params"],
                      check_key=req["check_key"], check_value=req["check_value"],assert_type=req["assert_type"],
                      creator=req["creator"], project_id=req["pros"], model_id=req['mokuais'],
                      update_time=datetime.datetime.now())
            return JsonResponse(update_msg)
        else:
            CaseList.objects.create(include=req["include"], name=req["name"], url=req["url"], method=req["method"],
                                    re_header=req["re_header"], param_type=req["param_type"], params=req["params"],
                                    check_key=req["check_key"], check_value=req["check_value"],
                                    assert_type=req["assert_type"], creator=req["creator"],
                                    project_id=req["pros"], model_id=req['mokuais'])
            return JsonResponse(data=new_msg, status=200)
    elif request.method == "DELETE" and request.is_ajax():
        delete(request, CaseList)
        return JsonResponse(delete_msg)
    else:
        pass


@login_check
def edit_case(request):
    # 返回编辑用例页面
    if request.method == "GET":
        mo = all_data(request, MoKuai)
        d = {"mof": mo["data"]}
        po = all_data(request, Project)  # 这里用的是.value的方法，与all有区别
        # 连续调用两次，mo、po的值最后都是取了po？？？-暂时用字典赋值处理下
        d["pof"] = po["data"]
        # 获取前置用例
        ca = all_data(request, CaseList)
        # print(ca["data"])
        d["include"] = ca["data"]
        return render(request, "./templates/edit_case.html", {"mof": d["mof"], "pof": d["pof"], "include": d["include"]})
    if request.method == "POST":
        req = json.loads(request.body)
        case_info = CaseList.objects.values().filter(id=req["id"])
        print(case_info)
        case_info = deal_data(case_info)["data"][0]
        # https://www.cnblogs.com/xiao-xue-di/p/11414210.html --字符串转为字典
        re_header = ast.literal_eval(case_info["re_header"])
        # print(re_header, type(re_header))
        case_info["pros"] = Project.objects.get(id=case_info["project_id"]).name
        case_info["mokuais"] = MoKuai.objects.get(id=case_info["model_id"]).name
        case_info["include"] = CaseList.objects.get(id=case_info["include"]).name
        case_info["re_header"] = re_header
        # case_info["suite"] =
        print(case_info)
        return JsonResponse(case_info)


@login_check
def run_case(requset):
    """运行单个用例"""
    # 需要多线程运行。第一步要生成对应的测试用例json文件；第二步是调用unittest框架执行并生成测试报告
    if requset.method == "POST" and requset.is_ajax():
        req = json.loads(requset.body)
        # print(req)
        CaseThread(req["id"], req["env_url"]).run()
        return JsonResponse(run_msg)
