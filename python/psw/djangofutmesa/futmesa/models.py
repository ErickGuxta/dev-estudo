from django.db import models


class Partida(models.Model):
    dupla_um = models.CharField(max_length=120)
    dupla_dois = models.CharField(max_length=120)
    horario = models.DateTimeField()
    local = models.CharField(max_length=150)
    placar_dupla_um = models.PositiveIntegerField(blank=True, null=True)
    placar_dupla_dois = models.PositiveIntegerField(blank=True, null=True)
    observacao = models.TextField(blank=True)

    class Meta:
        ordering = ['horario']
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'

    def __str__(self):
        return f'{self.dupla_um} x {self.dupla_dois}'
