from assistencia.views import usuario_views
from django.urls import path


urlpatterns = [
    path('usuario/', usuario_views.lista_usuarios, name='usuarios'),
    path('cadastro/usuarios/',  usuario_views.cadastrar, name='usuario_cadastrar'),
    path('cadastro/usuarios/<int:id>/editar/', usuario_views.editar, name='editar_usuario'),
    path('cadastro/usuarios/<int:id>/excluir/', usuario_views.eliminar, name="excluir_usuario"),
]
