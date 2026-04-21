from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="index"),
    path("partidas/", views.listar, name="listar_partidas"),
    path("detalhes/<int:id>/", views.details, name="details"),
    path("adicionar/", views.create, name="create"),
    path("atualizar/<int:id>/", views.update, name="update"),
    path("deletar/<int:id>/", views.delete, name="delete"),

]




