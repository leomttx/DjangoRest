from rest_framework import serializers
from pontos_turisticos_app.models import PontoTuristico

class PontoTuristicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao')