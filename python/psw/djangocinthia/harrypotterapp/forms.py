from django import forms

from .models import PersonagemHarryPotter


class PersonagemHarryPotterForm(forms.ModelForm):
    class Meta:
        model = PersonagemHarryPotter
        fields = ["nome", "casa", "data_nascimento", "patrono"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex.: Harry Potter"}),
            "casa": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex.: Grifinória"}),
            "data_nascimento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "patrono": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex.: Cervo"}),
        }
