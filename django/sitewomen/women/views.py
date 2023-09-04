from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница приложения Women")

def categoris(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")

def categoris_id(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Категория id: {cat_id}</p>")


def categoris_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Категория slug: {cat_slug}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>год: {year}</p>")