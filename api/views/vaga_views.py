from rest_framework.views import APIView
from ..entidades import vagas
from ..services import vaga_service
from ..serializers import vaga_serializer
from rest_framework.response import Response
from rest_framework import status


class VagasList(APIView):
    def get(self, request, format=None):
        vagas = vaga_service.listas_vagas
        serializer = vaga_serializer.TecnologiaSerializer(vagas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
