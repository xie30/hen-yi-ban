from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render,redirect
from myadmin.models import UserFi
# from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def hello(request):
    return redirect(reverse("login")) #http://127.0.0.1:8000/访问直接跳转到登录页面

def home(request):
    return render(request, './templates/home.html')

def login(request):
    '''
    用户登录：
    1.用户输入账号密码，通过post的方式传给后台
    2.后台拿着用户的数据和数据库的账号密码比对
    3.重置密码功能/立即注册功能
    :param request:
    :return:
    '''
    if request.method == 'POST':
        #获取提交的数据https://docs.djangoproject.com/zh-hans/3.2/ref/request-response/
        user_form = request.POST
        print('提交:\n'+ str(user_form.dict()))
        # model对象
        login_user = UserFi()
        login_user.username = user_form['username']
        login_user.password = user_form['password']
        print(login_user.username)
        #查询数据，拿密码作比对，先查账号有没有，再查密码对不对
        print(UserFi.objects.all().values())
        user = UserFi.objects.filter(username=login_user.username).values()
        msg = "账号或密码不对,请输入正确的账号和密码"
        if user:
            print (user)
            passw = user[0]["password"]
            if passw == login_user.password:
                # print()
                return redirect(reverse("home")) #直接域名 @login_required,主页要限制只有登录才能访问
            else:
                # print("请输入正确的用户名/密码")
                return render(request,"templates/login.html",{"wrong_msg":msg,"info":user_form})
        else:
            return render(request, "templates/login.html", {"wrong_msg":msg,"info":user_form})
    else:
        print('打开登录页面')
        return render(request, './templates/login.html')


def register(request):
    '''
   用户注册，通过form表单提交数据
    1.数据格式
    2.校验数据
    3.写入库
    4.返回注册成功
    :param request:
    :return:
    '''
    if request.method == 'POST':
        #获取提交的数据https://docs.djangoproject.com/zh-hans/3.2/ref/request-response/
        user_form = request.POST
        # print('提交:\n'+ str(user_form.dict()))
        # model对象
        new_user = UserFi()
        new_user.username = user_form['username']
        new_user.password = user_form['password']
        new_user.email = user_form['email']
        #如果出现同名，返回告知用户注册失败
        if UserFi.objects.filter(username=new_user.username).values():
            msg = "用户已存在，请输入新的用户名注册"
            return render(request,"templates/register.html",{"user_register":user_form,"msg":msg})
        else:
            new_user.save()
            # print('查询数据：')
            # print(UserFi.objects.all().values())
            # 怎样提示注册成功后跳转登录页面？
            return HttpResponse("<h1>注册成功</h1> <a href='/login'>登录</a>")
            # return HttpResponse("<h1>注册成功</h1> <a href={{ login }}>登录</a>")
            # return redirect('/login') #页面跳转了

    else:
        # print('打开注册页面')
        return render(request, './templates/register.html')

