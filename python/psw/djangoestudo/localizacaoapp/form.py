from django import forms
from .models import Localizacao


class LocalizacaoForm(forms.ModelForm):
    class Meta:
        model = Localizacao
        fields = ["historico", "integracao_coleira", "alertas", "status"]
