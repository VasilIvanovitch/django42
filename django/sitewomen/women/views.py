import uuid
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.db.models import Prefetch
from  django.views import View
from  django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.template.loader import render_to_string


from women.forms import AddPostForm, UploadFileForm
from women.models import Women, Category, TagPosts, UploadFiles
from women.utils import DataMixin

menu = [{'title': "О сайте", 'url_name': 'women:about'},
        {'title': "Добавить статью", 'url_name': 'women:add_page'},
        {'title': "Обратная связь", 'url_name': 'women:contact'},
        {'title': "Войти", 'url_name': 'women:login'}
]


# def handle_uploaded_file(f):
#     with open(f"uploads/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def handle_uploaded_file(f):
    name = f.name
    ext = ''

    if '.' in name:
        ext = name[name.rindex('.'):]
        name = name[:name.rindex('.')]

    suffix = str(uuid.uuid4())
    with open(f"uploads/{name}_{suffix}{ext}", "wb+") as destination:  #  файл не загружается, вероятно проблемма с правами доступа
        for chunk in f.chunks():
            destination.write(chunk)


# def index(request):
#     posts = Women.published.all().prefetch_related(Prefetch('cat', to_attr='category'))
#     # posts = Women.published.all().select_related('cat')
#     data = {'title': 'Главная страница',
#             'menu': menu,
#             'posts': posts,
#             'cat_selected': 0}
#     return render(request, 'women/index.html', context=data)
    # st = render_to_string('women/index.html')
    # return HttpResponse(st)

class WomenHome(DataMixin, ListView):
    # model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    title_page = 'Главная страница'
    cat_selected = 0
    # extra_context = {
    #         'title': 'Главная страница',
    #         'menu': menu,
    #         #  'posts': Women.published.all().prefetch_related(Prefetch('cat', to_attr='category')),
    #         'cat_selected': 0
    # }


    def get_queryset(self):
        return Women.published.all().prefetch_related(Prefetch('cat', to_attr='category'))


class WomenCategory(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context,
                                      title='Категория - ' + cat.name,
                                      cat_selected=cat.pk)
        # context['title'] = 'Категория - ' + cat.name
        # context['menu'] = menu
        # context['cat_selected'] = cat.id
        # return context

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).prefetch_related(Prefetch('cat', to_attr='category'))


class WomenTag(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = True

    def get_queryset(self):
        tag = TagPosts.objects.filter(slug=self.kwargs['tag_slug']).first()  # get_object_or_404(TagPosts, slug=tag_slug)
        self.kwargs['tag_name'] = tag.tag
        return tag.womens.filter(is_published=Women.Status.PUBLISHED).prefetch_related('cat')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Тег: ' + self.kwargs['tag_name'])
        # tag = self.kwargs['tag_slug']  # context['posts'][0].tags.all()[0]
        # context['title'] = 'Категория - ' + self.kwargs['tag_name']
        # context['menu'] = menu
        # context['cat_selected'] = None
        # return context


class ShowPost(DataMixin, DetailView):
    template_name = 'women/post.html'
    context_object_name = 'post'
    #  pk_url_kwarg = 'pk'
    slug_url_kwarg = 'post_slug'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = context['post'].title
        return self.get_mixin_context(context, title = context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(DataMixin, CreateView):
    template_name = 'women/addpage.html'
    model = Women
    fields = ['title', 'slug', 'photo', 'content', 'cat', 'is_published']
    success_url = reverse_lazy('women:home')
    title_page = 'Добавление страницы'
    # extra_context = {'title': 'Добавление страницы', 'menu': menu}



class UpdatePage(DataMixin, UpdateView):
    template_name = 'women/addpage.html'
    model = Women
    fields = ['title', 'slug', 'photo', 'content', 'cat', 'is_published', 'husband']
    title_page = 'Редактирование статьи'
    #  extra_context = {'title': 'Добавление страницы', 'menu': menu}
    #  success_url = reverse_lazy('women:home')

class DeletePage(DataMixin, DeleteView):
    template_name = 'women/deletepage.html'
    model = Women
    success_url = reverse_lazy('women:home')
    title_page = 'Удаление страницы'


def about(request):
    contact_list = Women.published.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'women/about.html',
                  {'title': 'О сайте', 'page_object':  page_object})
    # if request.method == 'POST':
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         # handle_uploaded_file(form.cleaned_data['file'])
    #         fr = UploadFiles(file=form.cleaned_data['file'])
    #         fr.save()
    # else:
    #     form = UploadFileForm()
    # return render(request, 'women/about.html', {'title': 'О сайте',
    #                                             'menu': menu, 'form': form})


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     data = {'title': post.title,
#             'menu': menu,
#             'post': post,
#             'cat_selected': None}
#     return render(request, 'women/post.html', context=data)

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('women:home')
            # try:
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect('women:home')
            # except:
            #     form.add_error(None, 'Ошибка добавления поста')
            # print(form.cleaned_data)

    # else:
    #     form = AddPostForm()
    # return render(request, 'women/addpage.html', context={'menu': menu,
    #                                             'title': 'Добавление страницы', 'form': form})


def login(request):
    return HttpResponse(f"<h2>Вход</h2>")


def contact(request):
    return HttpResponse(f"<h2>Обратная связь</h2>")


# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     data_db = Women.published.filter(cat_id=category.pk).select_related('cat')
#     data = {'title': f'Рубрика {category.name}',
#             'menu': menu,
#             'posts': data_db,
#             'cat_selected': category.pk}
#     return render(request, 'women/index.html', context=data)

# def show_tag_postlist(request, tag_slug):
#     tag = get_object_or_404(TagPosts, slug=tag_slug)
#     posts = tag.womens.filter(is_published=Women.Status.PUBLISHED).select_related('cat')
#     data = {
#         'title': f'Тег: {tag.tag}',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': None
#     }
#     return render(request, 'women/index.html', context=data)


def archive(request, year):
    if year > 2023:
        url1 = reverse('women:cats', args=('sport',))
        return redirect(url1)
    return HttpResponse(f"<h1>Архив по годам</h1><p>год: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")