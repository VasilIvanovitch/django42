from django.urls import path, re_path, register_converter

from . import views, converters

app_name = 'women'

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.ShowPost.as_view(), name='post'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.WomenTag.as_view(), name='tag'),
    # path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
    path("archive/<year4:year>/", views.archive, name='archive'),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),

]
