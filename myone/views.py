from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


def products(request, id):
    return HttpResponse(f"Товар {id}")


def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")


def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")


def index(request):
    data = {"header":"Metanit", "message":"My first message to Django"}
    return TemplateResponse(request,  "index.html", context=data)


def user(request):
    age = request.GET.get("age")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")
