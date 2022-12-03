from django.urls import path, include
from myone import views

urlpatterns = [
    path("", views.index),
    path("send", views.send),
    path("sendObject", views.sendObject)
]
