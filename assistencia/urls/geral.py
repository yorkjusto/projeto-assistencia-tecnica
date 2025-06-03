from assistencia.views.geral_views import home, contato, sobre
from django.urls import path


urlpatterns = [ 
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('sobre/', sobre, name='sobre'),
]