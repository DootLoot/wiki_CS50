from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path('search', views.search, name="search"),
    path('newPage', views.newPage, name="newPage"),
    path('create', views.create, name="create"),
    path('wiki/edit/<str:title>', views.edit, name="edit"),
    path('wiki/edit/save/<str:title>', views.save, name="save"),
    path('random', views.randomPage, name="random")
]
