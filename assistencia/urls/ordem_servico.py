from assistencia.views import ordem_servico_views
from django.urls import path


urlpatterns = [
    path('servicos/', ordem_servico_views.lista_servicos, name='servicos'),
    path('cadastro/servicos/', ordem_servico_views.cadastrar, name='cadastrar_servico'),
    path('cadastro/servicos/<int:id>/editar/', ordem_servico_views.editar, name='editar_servico'),
    path('cadastro/servicos/<int:id>/excluir/', ordem_servico_views.excluir, name='excluir_servico'),
    path('cadastro/servicos/<int:id>/ver/', ordem_servico_views.ver_ordem, name='ver_ordem'),
]
