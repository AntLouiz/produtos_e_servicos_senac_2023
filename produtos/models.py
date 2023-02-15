from django.db import models

TIPO_PRODUTO = 'P'
TIPO_SERVICO = 'S'

class Produto(models.Model):
    TIPOS_CHOICES = [
        (TIPO_PRODUTO, 'Produto'),
        (TIPO_SERVICO, 'Serviço')
    ]

    nome = models.CharField(max_length=100)
    preco = models.FloatField(default=0)
    estoque = models.IntegerField(default=0)
    tipo = models.CharField(max_length=2, choices=TIPOS_CHOICES, default=TIPO_PRODUTO)
    excluido = models.BooleanField(default=False)
