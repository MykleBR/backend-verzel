# meu_app/serializers.py

from rest_framework import serializers
from .models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ('id', 'nome', 'marca', 'modelo', 'foto')
