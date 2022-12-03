from django.urls import path, include
from myone import views

urlpatterns = [
    path("", views.index),
    path("info/<int:n>", views.info),
   ]
