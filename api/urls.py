from django.urls import include, path
from .views import tecnologia_views

urlpatterns = [
    path('tecnologias/', tecnologia_views.TecnologiaList.as_view(), name='tecnologia-list'),
]