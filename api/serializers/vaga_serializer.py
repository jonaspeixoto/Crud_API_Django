from rest_framework import serializers
from ..models import Vagas

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vagas
        fields = ('titulo', 'descricao', 'salario', 'local', 'quantidade', 'contato',
                  'tipo_contratacao', 'tecnologia')