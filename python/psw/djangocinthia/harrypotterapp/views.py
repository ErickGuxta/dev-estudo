from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonagemHarryPotterForm
from .models import PersonagemHarryPotter


def listar(request):
    personagens = PersonagemHarryPotter.objects.order_by("id")
    return render(request, "personagens/listar.html", {"personagens": personagens})


index = listar


def details(request, pk):
    personagem = get_object_or_404(PersonagemHarryPotter, pk=pk)
    return render(request, "personagens/detalhes.html", {"personagem": personagem})


def create(request):
    form = PersonagemHarryPotterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("listar_personagens")

    return render(request, "personagens/criar.html", {"form": form})


def update(request, pk):
    personagem = get_object_or_404(PersonagemHarryPotter, pk=pk)
    form = PersonagemHarryPotterForm(request.POST or None, instance=personagem)

    if form.is_valid():
        form.save()
        return redirect("listar_personagens")

    return render(request, "personagens/atualizar.html", {"form": form, "personagem": personagem})


def delete(request, pk):
    personagem = get_object_or_404(PersonagemHarryPotter, pk=pk)

    if request.method == "POST":
        personagem.delete()
        return redirect("listar_personagens")

    return render(request, "personagens/deletar.html", {"personagem": personagem})
