from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Olá, mundo! Esta é o App index")

def details(request, id):
    return HttpResponse(f"Rota de operação CRUD: mostrar detalhes {id}")
   
def create(request, id):
    return HttpResponse(f"Rota de operação CRUD: create {id}")

def update(request, id):
    return HttpResponse(f"Rota de operação CRUD: update {id}")

def delete(request, id):
    return HttpResponse(f"Rota de operação CRUD: delete {id}")

