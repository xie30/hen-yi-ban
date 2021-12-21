
from django.urls import path, re_path
from auto_test import views

urlpatterns = [
    # path(r"", views.hello),
    #总的路由中 ---》/home/autotest/
    re_path(r"^env/$", views.env, name="env"),
    #路由前后结束正则要有
    re_path(r"env_add/$", views.env_add, name="env_add"),
    re_path(r"env_delete/$", views.env_delete, name="env_delete"),
    re_path(r"env_modify/$", views.env_modify, name="env_modify"),
    re_path(r"^project/$", views.project, name="project"),
    re_path(r"^projects/$", views.projects, name="projects"),
    re_path(r"^mokuai/$", views.mokuai, name="mokuai"),
    re_path(r"^case/$", views.case, name="case"),
    re_path(r"^edit_case/$", views.edit_case, name="edit_case"),
    re_path(r"^runcase/$", views.run_case, name="run_case"),

    #参数模式？
]