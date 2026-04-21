from django.db import models

# Create your models here.


class Localizacao(models.Model):
    historico = models.TextField()
    integracao_coleira = models.CharField(max_length=100)
    alertas = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status
