from django.urls import path, re_path, register_converter
from django.views.decorators.cache import cache_page

from . import views, converters

app_name = 'women'

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    # path('', cache_page(30)(views.WomenHome.as_view()), name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.ShowPost.as_view(), name='post'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('edit/<int:pk>/', views.UpdatePage.as_view(), name='edit_page'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<slug:slug>/', views.DeletePage.as_view(), name='delete_page'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('login/', views.login, name='login'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.WomenTag.as_view(), name='tag'),
    # path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
    path("archive/<year4:year>/", views.archive, name='archive'),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),

]
