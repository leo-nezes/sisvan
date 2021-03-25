from rest_framework.serializers import ModelSerializer
from ..models import PesoIdade


class PesoIdadeSerializer(ModelSerializer):
    class Meta:
        model = PesoIdade
        fields = ('municipio', 'uf', 'regiao', 'PAE_porcentagem', 'PAE_quantidade', 'PB_porcentagem', 'PB_quatidade', 'PE_porcentagem', 'PE_quantidade', 'PMB_porcentagem', 'PMB_quantidade', 'total')
