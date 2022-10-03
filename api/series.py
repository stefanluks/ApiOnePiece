from rest_framework import serializers
from .models import Personagem, Bando, Navio, Lugar, Capitulo, Episodio, Abertura, Habilidade

class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = "__all__"


class BandoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bando
        fields = "__all__"


class NavioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navio
        fields = "__all__"


class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = "__all__"


class CapituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capitulo
        fields = "__all__"


class EpisodioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodio
        fields = "__all__"


class AberturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abertura
        fields = "__all__"


class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = "__all__"


