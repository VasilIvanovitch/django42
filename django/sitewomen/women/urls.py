from django.urls import path, re_path, register_converter

from . import views, converters

app_name = 'women'

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path("archive/<year4:year>/", views.archive, name='archive'),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),

]
