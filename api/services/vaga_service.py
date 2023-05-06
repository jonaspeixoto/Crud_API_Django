from ..models import Vagas
from .tecnologia_service import listar_tecnologia_id
from django.http import Http404
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

def listar_vaga_id(id):
    try:
        return Vagas.objects.get(id=id)
    except Vagas.DoesNotExist:
        raise Http404
    
def editar_vaga(vaga_antiga, vaga_nova):
    vaga_antiga.titulo = vaga_nova.titulo
    vaga_antiga.descricao = vaga_nova.descricao
    vaga_antiga.salario = vaga_nova.salario
    vaga_antiga.local = vaga_nova.local
    vaga_antiga.contato = vaga_nova.contato
    vaga_antiga.tipo_contratacao = vaga_nova.tipo_contratacao
    vaga_antiga.quantidade = vaga_nova.quantidade 
    vaga_antiga.tecnologia.set(vaga_nova.tecnologia)
    vaga_antiga.save(force_update=True)

def remover_vaga(vaga):
    vaga.delete()