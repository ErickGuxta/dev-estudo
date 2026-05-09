from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="index_casas"),
    path("visualizar/", views.listar, name="listar_casas"),
    path("detalhes/<int:pk>/", views.details, name="details_casa"),
    path("adicionar/", views.create, name="create_casa"),
    path("atualizar/<int:pk>/", views.update, name="update_casa"),
    path("deletar/<int:pk>/", views.delete, name="delete_casa"),
]
