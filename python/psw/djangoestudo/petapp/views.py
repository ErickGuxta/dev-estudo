from django.shortcuts import get_object_or_404, redirect, render # impotando shortcuts para renderização 
from .form import PetForm

from .models import Pet

# criando views para o app pet
def index(request):
    return listar(request)

def listar(request):
    # retorna todos os pets em ordem alfabética
    pets = Pet.objects.all().order_by("id")
    #definindo contexto
    context = {"pets": pets}

    #retorno a request, o caminho template e o contexto
    return render(request, "pets/listar.html", context)

def details(request, id):
    #retorno cada pet por id
    pet = get_object_or_404(Pet, id=id)
    
    #definindo contexto
    context = {"pet": pet}

    #retorno a request, o caminho template e o contexto
    return render(request, "pets/detalhes.html", context)
 
def create(request):
    #instancio a ModelForm PetForm()
    form = PetForm()

    # fazendo verificação da request (ta um pouco diferente da do professor)
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_pets")
    else:
        # se n for válido ele renderiza na tela de criar novamente
        context = {"form": form}
        return render(request, "pets/criar.html", context)


def update(request, id):
    # pegando cada pet por id (Pet -> classe da model, na qual comunica com o BD)
    pet = get_object_or_404(Pet, id=id)

    #instancia o PetForm, tendo como parametro: request via POST e a instância do pet
    form = PetForm(request.POST or None, instance=pet)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_pets")

    context = {"form": form, "pet": pet}
    return render(request, "pets/atualizar.html", context)

def delete(request, id):
    pet = get_object_or_404(Pet, id=id)

    if request.method == "POST":
        pet.delete()
        return redirect("listar_pets")

    context = {"pet": pet}
    return render(request, "pets/deletar.html", context)

