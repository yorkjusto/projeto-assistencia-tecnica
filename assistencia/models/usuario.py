from django.db import models
from .geral import Geral

class Usuario(Geral):
    PERFIL = (
        ('U', 'User'),
        ('A', 'Admin')
    )

    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    login = models.CharField(max_length=50, unique=True, verbose_name="Login de acesso")
    senha = models.CharField(max_length=50)
    perfil = models.CharField(choices=PERFIL, max_length=1)

    def __str__(self):
        return self.nome
