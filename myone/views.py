from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request, n):
    name = "Otabek"
    data = {"n" : n}
    return TemplateResponse(request, "index.html", context=data)
