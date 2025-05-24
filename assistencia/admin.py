from django.contrib import admin
from .models.cliente import Cliente
from .models.ordem import OrdemDeServico
from .models.usuario import Usuario

# Register your models here.
admin.site.register(Cliente)
admin.site.register(OrdemDeServico)
admin.site.register(Usuario)