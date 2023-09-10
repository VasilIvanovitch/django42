from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db,
            'url': slugify('Margot Robbie')}
    return render(request, 'women/index.html', context=data)
    # st = render_to_string('women/index.html')
    # return HttpResponse(st)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте',
                                                'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f"<h2>Отображение статьи с id = {post_id}</h2>")


def addpage(request):
    return HttpResponse(f"<h2>Добавление статьи</h2>")


def login(request):
    return HttpResponse(f"<h2>Вход</h2>")


def contact(request):
    return HttpResponse(f"<h2>Обратная связь</h2>")



def categoris_by_slug(request, cat_slug):
    if req_dict := request.GET:
        print(req_dict)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Категория slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        url1 = reverse('women:cats', args=('sport',))
        return redirect(url1)
    return HttpResponse(f"<h1>Архив по годам</h1><p>год: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
