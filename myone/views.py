from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    data = {"header": "Metanit", "message": "My first message to Django"}
    return TemplateResponse(request, "index.html", context=data)
def send(request):
    header = "Данные пользователя"  # обычная переменная
    langs = ["Python", "Java", "C#"]  # список
    user = {"name": "Tom", "age": 23}  # словарь
    address = ("Абрикосовая", 23, 45)  # кортеж

    data = {"header": header, "langs": langs, "user": user, "address": address}

    return TemplateResponse(request, "index_2.html", context=data)