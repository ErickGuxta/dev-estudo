from .models import Pet
from django import forms

class PetForm(forms.ModelForm):
    #uma metaclasse é um dado sobre o dado
    class Meta:
        model = Pet
        fields = ["nome", "cor", "data_nascimento", "raca"]

