from django.db import models
from .geral import Geral

class Cliente(Geral):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=9)
    morada = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.nome