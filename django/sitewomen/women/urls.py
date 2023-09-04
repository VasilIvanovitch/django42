from django.urls import path, re_path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index),
    path('cats/', views.categoris),
    path('cats/<int:cat_id>/', views.categoris_id),
    path('cats/<slug:cat_slug>/', views.categoris_by_slug),
    path("archive/<year4:year>/", views.archive),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),

]


