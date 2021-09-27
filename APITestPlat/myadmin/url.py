
from django.urls import path
from myadmin import views
urlpatterns = [
    path(r'', views.hello),
    path(r'login/', views.login, name="login"),
    path(r'register/', views.register, name='register'),
    path(r'home/', views.home, name="home"),
    # re_path(r'^home/$', views.home),^以什么开头，$以什么结尾，path中不需要，已自动处理
]