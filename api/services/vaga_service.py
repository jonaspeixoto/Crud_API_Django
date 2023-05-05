from ..models import Vagas
from .tecnologia_service import listar_tecnologia_id
def listas_vagas():
    lista_vagas = Vagas.objects.all()
    return (lista_vagas)

def cadastrar_vagas(vagas):
    vaga_bd = Vagas.objects.create(titulo=vagas.titulo,descricao=vagas.descricao,salario=vagas.salario,tipo_contratacao=vagas.tipo_contratacao,
                                local=vagas.local, quantidade=vagas.quantidade,contato=vagas.contato)
    vaga_bd.save()
    for i in vagas.tecnologia:
        tecnologia = listar_tecnologia_id(i)
        vaga_bd.tecnologia.add(tecnologia)
    return vaga_bd