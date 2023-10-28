from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.db.models import Prefetch
from django.template.loader import render_to_string

from women.forms import AddPostForm
from women.models import Women, Category, TagPosts

menu = [{'title': "О сайте", 'url_name': 'women:about'},
        {'title': "Добавить статью", 'url_name': 'women:add_page'},
        {'title': "Обратная связь", 'url_name': 'women:contact'},
        {'title': "Войти", 'url_name': 'women:login'}
]


# data_db = [
#     {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h3>Анджелина Джоли</h3> (англ. Angelina Jolie[7],
#     при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
#     Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
#      'is_published': True},
#     {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
#     {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
# ]


def index(request):
    posts = Women.published.all().prefetch_related(Prefetch('cat', to_attr='category'))
    # posts = Women.published.all().select_related('cat')
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': posts,
            'cat_selected': 0}
    return render(request, 'women/index.html', context=data)
    # st = render_to_string('women/index.html')
    # return HttpResponse(st)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте',
                                                'menu': menu})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {'title': post.title,
            'menu': menu,
            'post': post,
            'cat_selected': None}
    return render(request, 'women/post.html', context=data)

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('women:home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
            # print(form.cleaned_data)

    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', context={'menu': menu,
                                                'title': 'Добавление страницы', 'form': form})


def login(request):
    return HttpResponse(f"<h2>Вход</h2>")


def contact(request):
    return HttpResponse(f"<h2>Обратная связь</h2>")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    data_db = Women.published.filter(cat_id=category.pk).select_related('cat')
    data = {'title': f'Рубрика {category.name}',
            'menu': menu,
            'posts': data_db,
            'cat_selected': category.pk}
    return render(request, 'women/index.html', context=data)

def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPosts, slug=tag_slug)
    posts = tag.womens.filter(is_published=Women.Status.PUBLISHED).select_related('cat')
    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None
    }
    return render(request, 'women/index.html', context=data)


def archive(request, year):
    if year > 2023:
        url1 = reverse('women:cats', args=('sport',))
        return redirect(url1)
    return HttpResponse(f"<h1>Архив по годам</h1><p>год: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")