from django.urls import path
from . import views


app_name = "localizacaoapp"

urlpatterns = [
    path("", views.listar, name="index"),
    path("visualizar/", views.listar, name="listar_localizacoes"),
    path("detalhes/<int:id>/", views.details, name="details"),
    path("adicionar/", views.create, name="create"),
    path("atualizar/<int:id>/", views.update, name="update"),
    path("deletar/<int:id>/", views.delete, name="delete"),
]
