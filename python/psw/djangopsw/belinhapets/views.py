from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Olá, mundo! Esta é o App index")

def details(request):
    return HttpResponse(f"Rota de operação CRUD: mostrar detalhes ")
   
def create(request):
    return HttpResponse("Rota de operação CRUD: create")

def update(request):
    return HttpResponse(f"Rota de operação CRUD: update ")

def delete(request):
    return HttpResponse(f"Rota de operação CRUD: delete ")



