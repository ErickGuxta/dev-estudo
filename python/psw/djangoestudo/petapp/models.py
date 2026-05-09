from calendar import LocaleTextCalendar
from pyexpat import model
from django.db import models

# Create your models here.

## Aqui, cada modelo é representado por uma classe derivada da classe django.db.models.Model. 
class Pet(models.Model):
    nome            = models.CharField(max_length=100)
    cor             = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    raca            = models.CharField(max_length=100)


    def __str__(self):
        return self.nome

#relação (1,n)
class Dono(models.Model):

    nome     = models.CharField(max_length=100)
    cpf      = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email    = models.EmailField()
    endereco = models.CharField(max_length=100)

    pet = models.ForeignKey(Pet, on_delete= models.CASCADE)

    def __str__(self):
        return self.nome


#relação (n,n)
class Vacina(models.Model) :

    nome_vacina   = models.CharField(max_length=100)
    fabricante    = models.CharField(max_length=100)
    lote          = models.CharField(max_length=30)
    data_validade = models.DateField()
    descricao     = models.CharField(max_length=100)

    pet = models.ManyToManyField(Pet)