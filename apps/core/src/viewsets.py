from rest_framework.viewsets import ModelViewSet
from ..models import EyeHealth
from .serializers import EyeHealthSerializer


class EyeHealthViewSet(ModelViewSet):
    queryset = EyeHealth.objects.all()
    serializer_class = EyeHealthSerializer
