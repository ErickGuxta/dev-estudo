from django.db import models


class Casa(models.Model):
    nome = models.CharField(max_length=100)
    fundador = models.CharField(max_length=100)
    data_fundacao = models.DateField()
    animal_simbolo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
