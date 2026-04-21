from mailbox import NotEmptyError
from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    idade = models.IntegerField()
    cor = models.CharField(max_length=100) 
    especie = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MaeDoPet(models.Model):
    nome = models.CharField(max_length=100) 
    idade = models.IntegerField()
    cpf = models.CharField(max_length=100)
    pets = models.ManyToManyField(Pet, related_name='maes')
 
    def __str__(self):
        return self.nome

