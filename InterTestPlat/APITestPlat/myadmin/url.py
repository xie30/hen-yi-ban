
from django.urls import path
from myadmin import views
urlpatterns = [

    path(r'', views.hello),
    path(r'login/', views.login),
    path(r'register/', views.register),

]