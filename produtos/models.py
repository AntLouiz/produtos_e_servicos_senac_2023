from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField(default=0)
    estoque = models.IntegerField(default=0)
    excluido = models.BooleanField(default=False)
