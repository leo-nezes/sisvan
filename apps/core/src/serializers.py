from rest_framework.serializers import ModelSerializer
from ..models import PesoIdade


class PesoIdadeSerializer(ModelSerializer):
    class Meta:
        model = PesoIdade
        fields = '__all__'
