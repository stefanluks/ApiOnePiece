from django.contrib import admin
from django.urls import path
from .views import Home, Api, Personagens, Bandos, Navios, Aberturas, Lugares, Habilidades, Capitulos, Episodios, Administracao

urlpatterns = [
    path('', Home, name="Home"),
    
    path('Administracao/', Administracao, name="Administracao"),

    path('api/', Api, name="Api"),

    path('Personagens/', Personagens, name="Personagens"),
    path('Personagens/<int:id>', Personagens, name="Personagens"),

    path('Bandos/', Bandos, name="Bandos"),
    path('Bandos/<int:id>', Bandos, name="Bandos"),
    
    path('Navios/', Navios, name="Navios"),
    path('Navios/<int:id>', Navios, name="Navios"),

    path('Lugares/', Lugares, name="Lugares"),
    path('Lugares/<int:id>', Lugares, name="Lugares"),

    path('Capitulos/', Capitulos, name="Capitulos"),
    path('Capitulos/<int:id>', Capitulos, name="Capitulos"),

    path('Episodios/', Episodios, name="Episodios"),
    path('Episodios/<int:id>', Episodios, name="Episodios"),

    path('Aberturas/', Aberturas, name="Aberturas"),
    path('Aberturas/<int:id>', Aberturas, name="Aberturas"),

    path('Habilidades/', Habilidades, name="Habilidades"),
    path('Habilidades/<int:id>', Habilidades, name="Habilidades"),
]
