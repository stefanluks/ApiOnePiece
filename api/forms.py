from django.forms import ModelForm
from .models import Personagem, Bando, Navio, Lugar, Capitulo, Episodio, Abertura, Habilidade

class PersonagemForm(ModelForm):
    class Meta:
        model = Personagem
        fields = "__all__"


class BandoForm(ModelForm):
    class Meta:
        model = Bando
        fields = "__all__"


class NavioForm(ModelForm):
    class Meta:
        model = Navio
        fields = "__all__"


class LugarForm(ModelForm):
    class Meta:
        model = Lugar
        fields = "__all__"


class CapituloForm(ModelForm):
    class Meta:
        model = Capitulo
        fields = "__all__"


class EpisodioForm(ModelForm):
    class Meta:
        model = Episodio
        fields = "__all__"


class AberturaForm(ModelForm):
    class Meta:
        model = Abertura
        fields = "__all__"


class HabilidadeForm(ModelForm):
    class Meta:
        model = Habilidade
        fields = "__all__"
