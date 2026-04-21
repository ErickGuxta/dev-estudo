from django.shortcuts import get_object_or_404, redirect, render
from .form import PartidaForm
from .models import Partida


def index(request):
    return listar(request)


def listar(request):
    partidas = Partida.objects.all()
    context = {"partidas": partidas}
    return render(request, "partidas/listar.html", context)


def details(request, id):
    partida = get_object_or_404(Partida, id=id)
    context = {"partida": partida}
    return render(request, "partidas/detalhes.html", context)
 

def create(request):
    form = PartidaForm()

    if request.method == "POST":
        form = PartidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_partidas")

    context = {"form": form}
    return render(request, "partidas/criar.html", context)


def update(request, id):
    partida = get_object_or_404(Partida, id=id)
    form = PartidaForm(request.POST or None, instance=partida)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_partidas")

    context = {"form": form, "partida": partida}
    return render(request, "partidas/atualizar.html", context)


def delete(request, id):
    partida = get_object_or_404(Partida, id=id)

    if request.method == "POST":
        partida.delete()
        return redirect("listar_partidas")

    context = {"partida": partida}
    return render(request, "partidas/deletar.html", context)
