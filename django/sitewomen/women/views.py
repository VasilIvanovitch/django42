from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница приложения Women")

def categoris(request):
    return HttpResponse("<h1>Статьи по категориям   </h1>")