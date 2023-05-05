from rest_framework.views import APIView
from ..entidades import vagas
from ..services import vaga_service
from ..serializers import vaga_serializer
from rest_framework.response import Response
from rest_framework import status


class VagasList(APIView):
    def get(self, request, format=None):
        vagas = vaga_service.listas_vagas()
        serializer = vaga_serializer.VagaSerializer(vagas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = vaga_serializer.VagaSerializer(data=request.data)
        if serializer.is_valid():
            titulo = serializer.data["titulo"]
            descricao = serializer.data["descricao"]
            salario = serializer.data["salario"]
            local = serializer.data["local"]
            quantidade = serializer.data["quantidade"]
            tipo_contratacao = serializer.data["tipo_contratacao"]
            tecnologias = serializer.data["tecnologia"]
            contato = serializer.data["contato"]
            vaga = vagas.Vagas(titulo=titulo, descricao=descricao, salario=salario, local=local,
                               quantidade=quantidade, tipo_contratacao=tipo_contratacao, tecnologia=tecnologias,contato=contato)

            vaga_service.cadastrar_vagas(vaga)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



