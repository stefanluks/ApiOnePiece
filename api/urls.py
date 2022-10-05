from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, Sobre, Documentos, Api, Personagens, Bandos, Navios, Aberturas, Lugares, Habilidades, Capitulos, Episodios, Administracao

urlpatterns = [
    path('', Home, name="Home"),
    
    path('Administracao/', Administracao, name="Administracao"),
    path('Sobre/', Sobre, name="Sobre"),
    path('Documentos/', Documentos, name="Documentos"),

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
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
