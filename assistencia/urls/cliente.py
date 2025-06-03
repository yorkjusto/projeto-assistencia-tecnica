from assistencia.views import cliente_views
from django.urls import path


urlpatterns = [
    path('cliente/', cliente_views.lista_clientes, name="clientes"),
    path('cadastro/clientes/', cliente_views.adicionar_cliente, name='cliente_cadastrar'),
    path('cadastro/clientes/<int:id>/editar/', cliente_views.editar_cliente, name='editar_cliente'),
    path('cadastro/clientes/<int:id>/excluir/', cliente_views.excluir_cliente, name="excluir_cliente"),
]
