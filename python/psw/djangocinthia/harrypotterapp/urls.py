from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="index"),
    path("visualizar/", views.listar, name="listar_personagens"),
    path("detalhes/<int:pk>/", views.details, name="details"),
    path("adicionar/", views.create, name="create"),
    path("atualizar/<int:pk>/", views.update, name="update"),
    path("deletar/<int:pk>/", views.delete, name="delete"),
]



