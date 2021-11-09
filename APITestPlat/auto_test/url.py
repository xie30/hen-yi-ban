
from django.urls import path, re_path
from auto_test import views

urlpatterns = [
    # path(r"", views.hello),
    #总的路由中 ---》/home/autotest/
    re_path(r"^env/$", views.env, name="env"),
    #路由前后结束正则要有
    re_path(r"env_add/$", views.env_add, name="env_add"),
    #参数模式？
]