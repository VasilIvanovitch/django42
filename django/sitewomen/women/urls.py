from django.urls import path, re_path, register_converter

from . import views, converters


app_name = 'women'

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/', views.categoris),
    path('cats/<int:cat_id>/', views.categoris_id, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categoris_by_slug, name='cats'),
    path("archive/<year4:year>/", views.archive, name='archive'),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),

]


