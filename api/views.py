from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from .forms import PersonagemForm, BandoForm, NavioForm, LugarForm, CapituloForm, EpisodioForm, AberturaForm, HabilidadeForm
from .models import Personagem, Bando, Navio, Lugar, Capitulo, Episodio, Abertura, Habilidade
from .series import PersonagemSerializer, BandoSerializer, NavioSerializer, LugarSerializer, CapituloSerializer, EpisodioSerializer, AberturaSerializer, HabilidadeSerializer

def Home(request):
    return render(request, "home.html", {
        "topPersonagens":list(Personagem.objects.all())[:9],
    })


def Sobre(request):
    return render(request, "sobre.html", {})


def Documentos(request):
    return render(request, "documentos.html", {})


def Administracao(request):
    if request.user.is_staff:
        return render(request, "administracao/administracao.html", {
            "personagens":list(Personagem.objects.all()),
            "bandos":list(Bando.objects.all()),
            "navios":list(Navio.objects.all()),
            "lugares":list(Lugar.objects.all()),
            "capitulos":list(Capitulo.objects.all()),
            "episodios":list(Episodio.objects.all()),
            "aberturas":list(Abertura.objects.all()),
            "habilidades":list(Habilidade.objects.all()),
        })
    else:
        return render(request, 'erro.html', {
            "msg_erro":"Está pagina é apenas para menbros da equipe!"
        })
    

def Bandos(request, id=None):
    if request.method == "GET":
        form = BandoForm()
        edicao = False
        bando = None
        if id and Bando.objects.filter(pk=id):
            edicao = True
            bando = Bando.objects.get(pk=id)
            form = BandoForm(instance=bando)
        return render(request, 'administracao/admin.html', { "form":form, "modelo":"Bandos", "edicao":edicao, "obj":bando})
    elif request.method == "POST":
        resposta = BandoForm(request.POST)
        if id and Bando.objects.filter(pk=id):
            bando = Bando.objects.get(pk=id)
            resposta = BandoForm(request.POST, instance=bando)
        if resposta.is_valid:
            resposta.save()
            return redirect("Administracao")
        return render(request, 'erro.html', {
            "msg_erro":"Formulario invalído!"
        })
    else:
        return render(request, 'erro.html', {
            "msg_erro":"Erro na requesição!"
        })


def Personagens(request, id=None):
    if request.method == "GET":
        form = PersonagemForm()
        edicao = False
        personagem = None
        if id and Personagem.objects.filter(pk=id):
            edicao = True
            personagem = Personagem.objects.get(pk=id)
            form = PersonagemForm(instance=personagem)
        return render(request, 'administracao/admin.html', { "form":form, "modelo":"Personagens" , "edicao":edicao, "obj":personagem })
    elif request.method == "POST":
        resposta = PersonagemForm(request.POST)
        if id and Personagem.objects.filter(pk=id):
            personagem = Personagem.objects.get(pk=id)
            resposta = PersonagemForm(request.POST, instance=personagem)
        if resposta.is_valid:
            resposta.save()
            return redirect("Administracao")
        return render(request, 'erro.html', {
            "msg_erro":"Formulario invalído!"
        })
    else:
        return render(request, 'erro.html', {
            "msg_erro":"Erro na requesição!"
        })    


def Navios(request, id=None):
    if request.method == "GET":
        form = NavioForm()
        edicao = False
        navio = None
        if id and Navio.objects.filter(pk=id):
            edicao = True
            navio = Navio.objects.get(pk=id)
            form = NavioForm(instance=navio)
        return render(request, 'administracao/admin.html', { "form":form, "modelo":"Navios", "edicao":edicao, "obj":navio  })
    elif request.method == "POST":
        resposta = NavioForm(request.POST)
        if id and Navio.objects.filter(pk=id):
            navio = Navio.objects.get(pk=id)
            resposta = NavioForm(request.POST, instance=navio)
        if resposta.is_valid:
            resposta.save()
            return redirect("Administracao")
        return render(request, 'erro.html', {
            "msg_erro":"Formulario invalído!"
        })
    else:
        return render(request, 'erro.html', {
            "msg_erro":"Erro na requesição!"
        })


def Lugares(request, id=None):
    if request.method == "GET":
        form = LugarForm()
        edicao = False
        lugar = None
        if id and Lugar.objects.filter(pk=id):
            edicao = True
            lugar = Lugar.objects.get(pk=id)
            form = LugarForm(instance=lugar)
        return render(request, 'administracao/admin.html', { "form":form, "modelo":"Lugares", "edicao":edicao, "obj":lugar  })
    elif request.method == "POST":
        resposta = LugarForm(request.POST)
        if id and Lugar.objects.filter(pk=id):
            lugar = Lugar.objects.get(pk=id)
            resposta = LugarForm(request.POST, instance=lugar)
        if resposta.is_valid:
            resposta.save()
            return redirect("Administracao")
        return render(request, 'erro.html', {
            "msg_erro":"Formulario invalído!"
        })
    else:
        return render(request, 'erro.html', {
            "msg_erro":"Erro na requesição!"
        })


def Capitulos(request, id=None):
    if request.method == "GET":
        form = CapituloForm()
        edicao = False
        capitulo = None
        if id and Capitulo.objects.filter(pk=id):
            edicao = True
            capitulo = Capitulo.objects.get(pk=id)
            form = CapituloForm(instance=capitulo)
        return render(request, 'administracao/admin.html', { "form":form, "modelo":"Capitulos", "edicao":edicao, "obj":capitulo  })
    elif request.method == "POST":
        resposta = CapituloForm(request.POST)
        if id and Capitulo.objects.filter(pk=id):
            capitulo = Capitulo.objects.get(pk=id)
            resposta = CapituloForm(request.POST, instance=capitulo)
        if resposta.is_valid:
            resposta.save()
            return redirect("Administracao")
        return render(request, 'erro.html', {
            "msg_erro":"Formulario invalído!"
        })
    else:
        return render(request, 'erro.html', {
            "msg_erro":"Erro na requesição!"
        })


def Episodios(request, id=None):
    if request.method == "GET":
        form = EpisodioForm()
        edicao = False
        episodio = None
        if id and Episodio.objects.filter(pk=id):
            edicao = True
            episodio = Episodio.objects.get(pk=id)
            form = EpisodioForm(instance=episodio)
        return render(request, 'administracao/admin.html', { "form":form, "modelo":"Episodios", "edicao":edicao, "obj":episodio  })
    elif request.method == "POST":
        resposta = EpisodioForm(request.POST)
        if id and Episodio.objects.filter(pk=id):
            episodio = Episodio.objects.get(pk=id)
            resposta = EpisodioForm(request.POST, instance=episodio)
        if resposta.is_valid:
            resposta.save()
            return redirect("Administracao")
        return render(request, 'erro.html', {
            "msg_erro":"Formulario invalído!"
        })
    else:
        return render(request, 'erro.html', {
            "msg_erro":"Erro na requesição!"
        })


def Aberturas(request, id=None):
    if request.method == "GET":
        form = AberturaForm()
        edicao = False
        abertura = None
        if id and Abertura.objects.filter(pk=id):
            edicao = True
            abertura = Abertura.objects.get(pk=id)
            form = AberturaForm(instance=abertura)
        return render(request, 'administracao/admin.html', { "form":form, "modelo":"Aberturas", "edicao":edicao, "obj":abertura })
    elif request.method == "POST":
        resposta = AberturaForm(request.POST)
        if id and Abertura.objects.filter(pk=id):
            abertura = Abertura.objects.get(pk=id)
            resposta = AberturaForm(request.POST, instance = abertura)
        if resposta.is_valid:
            resposta.save()
            return redirect("Administracao")
        return render(request, 'erro.html', {
            "msg_erro":"Formulario invalído!"
        })
    else:
        return render(request, 'erro.html', {
            "msg_erro":"Erro na requesição!"
        })


def Habilidades(request, id=None):
    if request.method == "GET":
        form = HabilidadeForm()
        edicao = False
        habilidade = None
        if id and Habilidade.objects.filter(pk=id):
            edicao = True
            habilidade = Habilidade.objects.get(pk=id)
            form = HabilidadeForm(instance=habilidade)
        return render(request, 'administracao/admin.html', { "form":form, "modelo":"Habilidades", "edicao":edicao, "obj":habilidade  })
    elif request.method == "POST":
        resposta = HabilidadeForm(request.POST)
        if id and Habilidade.objects.filter(pk=id):
            habilidade = Habilidade.objects.get(pk=id)
            resposta = HabilidadeForm(request.POST, instance=habilidade)
        if resposta.is_valid:
            resposta.save()
            return redirect("Administracao")
        return render(request, 'erro.html', {
            "msg_erro":"Formulario invalído!"
        })
    else:
        return render(request, 'erro.html', {
            "msg_erro":"Erro na requesição!"
        })


def Api(request):
    return render(request, 'api.html', {})


@api_view(['GET'])
def GetPersonagens(request):
    if request.method == 'GET':
        personagens = Personagem.objects.all()
        serializer = PersonagemSerializer(personagens, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def GetPersonagens_detail(request, uid):
    try:
        personagem = Personagem.objects.get(UID=uid)
    except personagem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonagemSerializer(personagem)
        return Response(serializer.data)

@api_view(['GET'])
def GetBandos(request):
    if request.method == 'GET':
        bandos = Bando.objects.all()
        serializer = BandoSerializer(bandos, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def GetBandos_detail(request, uid):
    try:
        bando = Bando.objects.get(UID=uid)
    except bando.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BandoSerializer(bando)
        return Response(serializer.data)


@api_view(['GET'])
def GetNavios(request):
    if request.method == 'GET':
        navios = Navio.objects.all()
        serializer = NavioSerializer(navios, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def GetNavios_detail(request, uid):
    try:
        navio = Navio.objects.get(UID=uid)
    except navio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NavioSerializer(navio)
        return Response(serializer.data)

@api_view(['GET'])
def GetLugares(request):
    if request.method == 'GET':
        lugares = Lugar.objects.all()
        serializer = LugarSerializer(lugares, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def GetLugares_detail(request, id):
    try:
        lugar = Lugar.objects.get(UID=id)
    except lugar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LugarSerializer(lugar)
        return Response(serializer.data)


@api_view(['GET'])
def GetCapitulos(request):
    if request.method == 'GET':
        capitulos = Capitulo.objects.all()
        serializer = CapituloSerializer(capitulos, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def GetCapitulos_detail(request, num):
    try:
        capitulo = Capitulo.objects.get(numero=num)
    except capitulo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CapituloSerializer(capitulo)
        return Response(serializer.data)


@api_view(['GET'])
def GetEpisodios(request):
    if request.method == 'GET':
        episodios = Episodio.objects.all()
        serializer = EpisodioSerializer(episodios, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def GetEpisodios_detail(request, num):
    try:
        episodio = Episodio.objects.get(numero=num)
    except episodio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EpisodioSerializer(episodio)
        return Response(serializer.data)


@api_view(['GET'])
def GetAberturas(request):
    if request.method == 'GET':
        aberturas = Abertura.objects.all()
        serializer = AberturaSerializer(aberturas, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def GetAberturas_detail(request, id):
    try:
        abertura = Abertura.objects.get(UID=id)
    except abertura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AberturaSerializer(abertura)
        return Response(serializer.data)


@api_view(['GET'])
def GetHabilidades(request):
    if request.method == 'GET':
        habilidades = Habilidade.objects.all()
        serializer = HabilidadeSerializer(habilidades, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def GetHabilidades_detail(request, id):
    try:
        habilidade = Habilidade.objects.get(UID=id)
    except habilidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HabilidadeSerializer(habilidade)
        return Response(serializer.data)