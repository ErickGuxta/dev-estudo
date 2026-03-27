from django.db import models

# Create your models here.

## Aqui, cada modelo é representado por uma classe derivada da classe django.db.models.Model. 
class Pet(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    raca = models.CharField(max_length=100)


    def __str__(self):
        return self.nome

class Dono(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    pets = models.ManyToManyField(Pet, related_name='donos')


    def __str__(self):
        return self.nome