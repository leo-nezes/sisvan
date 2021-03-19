from django.db import models


class PesoIdade(models.Model):
    regiao = models.CharField(max_length=50)
    codigo_uf = models.IntegerField()
    uf = models.CharField(max_length=2)
    codigo_ibge = models.CharField(max_length=6)
    município = models.CharField(max_length=255)
    PMB_quantidade = models.IntegerField()
    PMB_porcentagem = models.FloatField()
    PB_quatidade = models.IntegerField()
    PB_porcentagem = models.FloatField()
    PAE_quantidade = models.IntegerField()
    PAE_porcentagem = models.FloatField()
    PE_quantidade = models.IntegerField()
    PE_porcentagem = models.FloatField()
    total = models.IntegerField()
    ano = models.IntegerField()

    def __str__(self):
        return self.município
