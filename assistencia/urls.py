from django.contrib import admin
from django.urls import path
from .views import usuario_views
from .views.geral_views import home, contato, sobre
from .views import cliente_views
from .views import ordem_servico_views

app_name = 'assistencia'
urlpatterns = [

    # Geral
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('sobre/', sobre, name='sobre'),

    # Usuários
    path('usuario/', usuario_views.lista_usuarios, name='usuarios'),
    path('cadastro/usuarios/',  usuario_views.cadastrar, name='usuario_cadastrar'),
    path('cadastro/usuarios/<int:id>/editar/', usuario_views.editar, name='editar_usuario'),
    path('cadastro/usuarios/<int:id>/excluir/', usuario_views.eliminar, name="excluir_usuario"),

    # Clientes
    path('cliente/', cliente_views.lista_clientes, name="clientes"),
    path('cadastro/clientes/', cliente_views.adicionar_cliente, name='cliente_cadastrar'),
    path('cadastro/clientes/<int:id>/editar/', cliente_views.editar_cliente, name='editar_cliente'),
    path('cadastro/clientes/<int:id>/excluir/', cliente_views.excluir_cliente, name="excluir_cliente"),

    # Ordens de serviços
    path('servicos/', ordem_servico_views.lista_servicos, name='servicos'),
    path('cadastro/servicos/', ordem_servico_views.cadastrar, name='cadastrar_servico'),
    path('cadastro/servicos/<int:id>/editar/', ordem_servico_views.editar, name='editar_servico'),
    path('cadastro/servicos/<int:id>/excluir/', ordem_servico_views.excluir, name='excluir_servico'),
]
