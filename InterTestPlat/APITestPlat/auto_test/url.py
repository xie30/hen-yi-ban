
from django.urls import path
from auto_test import views

urlpatterns = [
    path(r"", views.hello)

]