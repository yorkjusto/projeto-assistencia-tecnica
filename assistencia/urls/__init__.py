from django.urls import include, path

app_name = "assistencia"
urlpatterns = [
    path('', include('assistencia.urls.geral')),          # URLs da página inicial, contato, sobre
    path('', include('assistencia.urls.cliente')),        # URLs de clientes
    path('', include('assistencia.urls.usuario')),        # URLs de usuários
    path('', include('assistencia.urls.ordem_servico')),  # URLs de ordens de serviço
]