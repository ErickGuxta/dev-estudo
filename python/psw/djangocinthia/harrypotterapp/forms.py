from django import forms

from .models import PersonagemHarryPotter


class PersonagemHarryPotterForm(forms.ModelForm):
    class Meta:
        model = PersonagemHarryPotter
        fields = ["nome", "casa", "data_nascimento", "patrono"]
