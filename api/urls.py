from django.urls import include, path
from .views import tecnologia_views , vaga_views

urlpatterns = [
    path('tecnologias/', tecnologia_views.TecnologiaList.as_view(), name='tecnologia-list'),
    path('tecnologias/<int:id>', tecnologia_views.TecnologiaDetalhes.as_view(), name='tecnologia-detalhes'),
    path('vagas/', vaga_views.VagasList.as_view(), name='vaga-list'),
    path('vagas/<int:id>', vaga_views.VagaDetalhes.as_view(), name='vaga-detalhes'),


]