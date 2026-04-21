from django.db import models

class PersonagemHarryPotter(models.Model):
    nome = models.CharField(max_length=100)
    casa = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    patrono = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
