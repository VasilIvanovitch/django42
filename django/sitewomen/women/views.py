from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse("Страница приложения Women")

def categoris(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")

def categoris_id(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Категория id: {cat_id}</p>")


def categoris_by_slug(request, cat_slug):
    if req_dict := request.GET:
        print(req_dict)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Категория slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        url = reverse('cats', args=('sport',))
        return redirect(url)
    return HttpResponse(f"<h1>Архив по годам</h1><p>год: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")