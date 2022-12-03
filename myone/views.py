from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    data = {"n": 5}
    return TemplateResponse(request, "index.html", context=data)
