from django import forms
from .models import Partida


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = [
            'dupla_um',
            'dupla_dois',
            'horario',
            'local',
            'placar_dupla_um',
            'placar_dupla_dois',
            'observacao',
        ]
        widgets = {
            'dupla_um': forms.TextInput(attrs={'class': 'form-control'}),
            'dupla_dois': forms.TextInput(attrs={'class': 'form-control'}),
            'horario': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
            'placar_dupla_um': forms.NumberInput(attrs={'class': 'form-control'}),
            'placar_dupla_dois': forms.NumberInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
        labels = {
            'dupla_um': 'Dupla 1',
            'dupla_dois': 'Dupla 2',
            'horario': 'Horário',
            'local': 'Local',
            'placar_dupla_um': 'Placar dupla 1',
            'placar_dupla_dois': 'Placar dupla 2',
            'observacao': 'Observações',
        }
