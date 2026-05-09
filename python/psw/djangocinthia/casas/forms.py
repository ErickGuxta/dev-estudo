from django import forms

from .models import Casa


class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ["nome", "fundador", "data_fundacao", "animal_simbolo"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex.: Corvinal"}),
            "fundador": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex.: Rowena Ravenclaw"}),
            "data_fundacao": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "animal_simbolo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex.: Águia"}),
        }
