from django.shortcuts import get_object_or_404, redirect, render

from .forms import CasaForm
from .models import Casa


def listar(request):
    casas = Casa.objects.order_by("id")
    return render(request, "casas/listar.html", {"casas": casas})


index = listar


def details(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    return render(request, "casas/detalhes.html", {"casa": casa})


def create(request):
    form = CasaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("listar_casas")

    return render(request, "casas/criar.html", {"form": form})


def update(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    form = CasaForm(request.POST or None, instance=casa)

    if form.is_valid():
        form.save()
        return redirect("listar_casas")

    return render(request, "casas/atualizar.html", {"form": form, "casa": casa})


def delete(request, pk):
    casa = get_object_or_404(Casa, pk=pk)

    if request.method == "POST":
        casa.delete()
        return redirect("listar_casas")

    return render(request, "casas/deletar.html", {"casa": casa})
