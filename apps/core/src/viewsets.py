from rest_framework.viewsets import ModelViewSet
from ..models import PesoIdade
from .serializers import PesoIdadeSerializer


class PesoIdadeViewSet(ModelViewSet):
    queryset = PesoIdade.objects.all()
    serializer_class = PesoIdadeSerializer
