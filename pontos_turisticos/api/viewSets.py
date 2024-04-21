from rest_framework import viewsets
from pontos_turisticos_app.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    queryset = PontoTuristico.objects.all() # Lista de dados que serão retornados nessa viewset
    serializer_class = PontoTuristicoSerializer