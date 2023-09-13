from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = [{'title': "О сайте", 'url_name': 'women:about'},
        {'title': "Добавить статью", 'url_name': 'women:add_page'},
        {'title': "Обратная связь", 'url_name': 'women:contact'},
        {'title': "Войти", 'url_name': 'women:login'}
]


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h3>Анджелина Джоли</h3> (англ. Angelina Jolie[7],
    при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db,
            'cat_selected': 0}
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


def show_category(request, cat_id):
    data = {'title': 'Отображение по рубрикам',
            'menu': menu,
            'posts': data_db,
            'cat_selected': cat_id}
    return render(request, 'women/index.html', context=data)


def archive(request, year):
    if year > 2023:
        url1 = reverse('women:cats', args=('sport',))
        return redirect(url1)
    return HttpResponse(f"<h1>Архив по годам</h1><p>год: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
