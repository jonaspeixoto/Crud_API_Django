from ..models import Vagas

def listas_vagas():
    lista_vagas = Vagas.objects.all()
    return (lista_vagas)