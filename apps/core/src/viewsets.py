from rest_framework.viewsets import ModelViewSet
from ..models import PesoIdade
from .serializers import PesoIdadeSerializer


class PesoIdadeViewSet(ModelViewSet):
    serializer_class = PesoIdadeSerializer

    def get_queryset(self):
        queryset = PesoIdade.objects.all()
        code = self.request.query_params.get('code')

        if code:
            return queryset.filter(codigo_ibge=code)

        return queryset
