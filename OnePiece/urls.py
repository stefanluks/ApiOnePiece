from django.contrib import admin
from django.urls import path, include
from api.views import GetPersonagens, GetBandos, GetNavios, GetLugares, GetCapitulos, GetEpisodios, GetAberturas, GetHabilidades
from api.views import GetPersonagens_detail, GetBandos_detail, GetNavios_detail, GetLugares_detail, GetCapitulos_detail, GetEpisodios_detail, GetAberturas_detail, GetHabilidades_detail

urlpatterns = [
    path('', include("api.urls")),
    
    path('api/personagens/', GetPersonagens),
    path('api/personagens/<str:uid>', GetPersonagens_detail),
    
    path('api/bandos/', GetBandos),
    path('api/bandos/<str:uid>', GetBandos_detail),
    
    path('api/navios/', GetNavios),
    path('api/navios/<str:uid>', GetNavios_detail),
    
    path('api/lugares/', GetLugares),
    path('api/lugares/<str:uid>', GetLugares_detail),
    
    path('api/capitulos/', GetCapitulos),
    path('api/capitulos/<int:num>', GetCapitulos_detail),
    
    path('api/episodios/', GetEpisodios),
    path('api/episodios/<int:num>', GetEpisodios_detail),
    
    path('api/aberturas/', GetAberturas),
    path('api/aberturas/<str:uid>', GetAberturas_detail),
    
    path('api/habilidades/', GetHabilidades),
    path('api/habilidades/<str:uid>', GetHabilidades_detail),
    
    path('admin/', admin.site.urls),
]
