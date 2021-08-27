

from django.urls import path
from manual_test import views

urlpatterns = [
    path(r"", views.hello)
]