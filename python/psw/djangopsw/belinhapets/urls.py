from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("adicionar/", views.create, name="create"),
    path("visualizar/", views.details, name="details"),
    path("atualizar/", views.update, name="update"),
    path("deletar/", views.delete, name="delete"),


]