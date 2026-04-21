from django.shortcuts import get_object_or_404, redirect, render

from .form import LocalizacaoForm
from .models import Localizacao


def index(request):
    return listar(request)


def listar(request):
    localizacoes = Localizacao.objects.all().order_by("id")
    context = {"localizacoes": localizacoes}

    return render(request, "localizacoes/listar.html", context)


def details(request, id):
    localizacao = get_object_or_404(Localizacao, id=id)
    context = {"localizacao": localizacao}

    return render(request, "localizacoes/detalhes.html", context)


def create(request):
    form = LocalizacaoForm()

    if request.method == "POST":
        form = LocalizacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("localizacaoapp:listar_localizacoes")
    else:
        context = {"form": form}
        return render(request, "localizacoes/criar.html", context)

    context = {"form": form}
    return render(request, "localizacoes/criar.html", context)


def update(request, id):
    localizacao = get_object_or_404(Localizacao, id=id)
    form = LocalizacaoForm(request.POST or None, instance=localizacao)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("localizacaoapp:listar_localizacoes")

    context = {"form": form, "localizacao": localizacao}
    return render(request, "localizacoes/atualizar.html", context)


def delete(request, id):
    localizacao = get_object_or_404(Localizacao, id=id)

    if request.method == "POST":
        localizacao.delete()
        return redirect("localizacaoapp:listar_localizacoes")

    context = {"localizacao": localizacao}
    return render(request, "localizacoes/deletar.html", context)
