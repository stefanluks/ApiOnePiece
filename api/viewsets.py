from django.http import request
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from .models import Personagem, Bando, Navio, Lugar, Capitulo, Episodio, Abertura, Habilidade
from .series import PersonagemSerializer, BandoSerializer, NavioSerializer, LugarSerializer, CapituloSerializer, EpisodioSerializer, AberturaSerializer, HabilidadeSerializer


class PersonagemViewSet(viewsets.ModelViewSet):
    serializer_class = PersonagemSerializer
    queryset = Personagem.objects.all()

    def get_extra_actions(self):
        pass

    def list(self, request, *args, **kwargs):
        serializer = PersonagemSerializer(models.Personagem.objects.all())
        return Response(serializer.data)



class BandoViewSet(viewsets.ModelViewSet):
    serializer_class = BandoSerializer
    queryset = Bando.objects.all()

    def get_extra_actions(self):
        pass

    def list(self, request, *args, **kwargs):
        serializer = BandoSerializer(models.Bando.objects.all())
        return Response(serializer.data)
    

class NavioViewSet(viewsets.ModelViewSet):
    serializer_class = NavioSerializer
    queryset = Navio.objects.all()

    def get_extra_actions(self):
        pass
    
    def list(self, request, *args, **kwargs):
        serializer = NavioSerializer(models.Navio.objects.all())
        return Response(serializer.data)



class LugarViewSet(viewsets.ModelViewSet):
    serializer_class = LugarSerializer
    queryset = Lugar.objects.all()

    def get_extra_actions(self):
        pass
    
    def list(self, request, *args, **kwargs):
        serializer = LugarSerializer(models.Lugar.objects.all())
        return Response(serializer.data)



class CapituloViewSet(viewsets.ModelViewSet):
    serializer_class = CapituloSerializer
    queryset = Capitulo.objects.all()

    def get_extra_actions(self):
        pass
      
    def list(self, request, *args, **kwargs):
        serializer = CapituloSerializer(models.Capitulo.objects.all())
        return Response(serializer.data)



class EpisodioViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodioSerializer
    queryset = Episodio.objects.all()

    def get_extra_actions(self):
        pass
      
    def list(self, request, *args, **kwargs):
        serializer = EpisodioSerializer(models.Episodio.objects.all())
        return Response(serializer.data)



class AberturaViewSet(viewsets.ModelViewSet):
    serializer_class = AberturaSerializer
    queryset = Abertura.objects.all()

    def get_extra_actions(self):
        pass
  
    def list(self, request, *args, **kwargs):
        serializer = AberturaSerializer(models.Abertura.objects.all())
        return Response(serializer.data)



class HabilidadeViewSet(viewsets.ModelViewSet):
    serializer_class = HabilidadeSerializer
    queryset = Habilidade.objects.all()

    def get_extra_actions(self):
        pass
  
    def list(self, request, *args, **kwargs):
        serializer = HabilidadeSerializer(models.Habilidade.objects.all())
        return Response(serializer.data)
