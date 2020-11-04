from rest_framework.serializers import ModelSerializer
from ..models import EyeHealth


class EyeHealthSerializer(ModelSerializer):
    class Meta:
        model = EyeHealth
        fields = '__all__'
