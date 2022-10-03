from django.db import models

class Base(models.Model):
    UID = models.CharField("Codigo",max_length=200, null=True, blank=True)
    nome_portugues = models.CharField("Nome em português",max_length=150,null=True,blank=True)
    nome_japones = models.CharField("Nome em japonês",max_length=150,null=True,blank=True)
    nome_romanizado = models.CharField("Nome em romanizado",max_length=150)
    resumo = models.TextField("Resumo curto",max_length=500,blank=True,null=True)
    descricao = models.TextField("Descrição / História",max_length=5000,blank=True,null=True)

    def __str__(self):
        return "[ "+ self.nome_portugues + " ] - { " + self.nome_romanizado + " } - ( " + self.nome_japones+" )"

    def save(self, *args, **kwargs):
        nome = self.nome_portugues
        self.UID = nome.replace(" ", "-")
        super().save(*args, **kwargs)


class Personagem(Base):
    alcunha = models.CharField("Alcunha",max_length=150,blank=True,null=True)
    idade = models.IntegerField("Idade",default=0)
    recompensa = models.IntegerField("Recompensa",default=0)
    pai = models.ForeignKey("Personagem",on_delete=models.CASCADE,related_name="Mãe",blank=True,null=True)
    mae = models.ForeignKey("Personagem",on_delete=models.CASCADE,related_name="Pai",blank=True,null=True)
    afiliacao = models.ManyToManyField("Bando",blank=True)
    origem = models.ForeignKey("Lugar",on_delete=models.CASCADE,blank=True,null=True)
    status = models.CharField("Status",max_length=6,choices=(("0","VIVO"),("1","MORTO")),blank=True,null=True)
    aniversario = models.DateField("Data de aniversario",blank=True,null=True)
    altura_pre_timeskip = models.FloatField("Altura pré timeskip",default=0)
    altura_pos_timeskip = models.FloatField("Altura pós timeskip",default=0)
    tipo_sanguineo = models.CharField("Tipo sanguinéo",max_length=150,null=True,blank=True)
    habilidade = models.ManyToManyField("Habilidade",blank=True)
    aparicao_manga = models.ForeignKey("Capitulo",on_delete=models.CASCADE,related_name="Capitulo",null=True,blank=True)
    aparicao_anime = models.ForeignKey("Episodio",on_delete=models.CASCADE,related_name="Episodio",null=True,blank=True)
    risada = models.CharField("Risada Onomatopeia",max_length=150,null=True,blank=True)
    aparencia_crianca = models.CharField("Aparencia Criança",max_length=1500,null=True,blank=True)
    aparencia_pre_timeskip = models.CharField("Aparencia Pré TimeSkip",max_length=1500,null=True,blank=True)
    aparencia_pos_timeskip = models.CharField("Aparencia Pós TImeSkip",max_length=1500,null=True,blank=True)
    irmaos = models.ManyToManyField("Personagem",blank=True,related_name="Irmãos")
    dubladores = models.ManyToManyField("Personagem",blank=True,related_name="Dubladores")

    class Meta:
        verbose_name = "PERSONAGEM"
        verbose_name_plural = "PERSONAGENS"


class Bando(Base):
    jolly_roger = models.CharField("JOlly Roger (bandeira)",max_length=2500,blank=True, null=True)
    apricao_manga = models.ForeignKey("Capitulo",on_delete=models.CASCADE,related_name="Capitulo_Bando",null=True,blank=True)
    apricao_anime = models.ForeignKey("Episodio",on_delete=models.CASCADE,related_name="Episodio_Bando",null=True,blank=True)
    capitao = models.ForeignKey(Personagem,on_delete=models.CASCADE, blank=True, null=True, related_name="Capitão")
    veiculo = models.OneToOneField("Navio",on_delete=models.CASCADE, blank=True, null=True)
    integrantes = models.ManyToManyField(Personagem,blank=True)
    recompensa = models.IntegerField("Recompensa do bando",default=0)

    class Meta:
        verbose_name = "BANDO"
        verbose_name_plural = "BANDOS"

    def getRecompensa(self):
        soma = 0
        for p in self.integrantes:
            soma += p.recompensa
        self.recompensa = soma
        return self.recompensa


class Navio(Base):
    aparicao_manga = models.ForeignKey("Capitulo",on_delete=models.CASCADE,related_name="Capitulo_Navio",null=True,blank=True)
    aparicao_anime = models.ForeignKey("Episodio",on_delete=models.CASCADE,related_name="Episodio_Navio",null=True,blank=True)
    status = models.CharField("Status",max_length=6,choices=(("0","VIVO"),("1","MORTO")),blank=True,null=True)
    aparencia = models.CharField("Aparencia",max_length=2500,null=True,blank=True)
    afiliacao = models.ManyToManyField("Bando",blank=True,related_name="Afiliação")

    class Meta:
        verbose_name = "NAVIO"
        verbose_name_plural = "NAVIOS"


class Lugar(Base):
    aparicao_manga = models.ForeignKey("Capitulo",on_delete=models.CASCADE,related_name="Capitulo_Lugar",null=True,blank=True)
    aparicao_anime = models.ForeignKey("Episodio",on_delete=models.CASCADE,related_name="Episodio_Lugar",null=True,blank=True)

    class Meta:
        verbose_name = "LUGAR"
        verbose_name_plural = "LUGAR"


class Capitulo(Base):
    capa = models.CharField("Capa do capitulo",max_length=2500, null=True, blank=True)
    volume = models.IntegerField("Volume", default=0, null=True, blank=True)
    numero = models.IntegerField("Número do capitulo", default=0, null=True, blank=True)
    qtd_paginas = models.IntegerField("Quantidade de paginas", default=0)
    data_lancamento = models.DateField("Data de lançamento", null=True, blank=True)
    espisodio_relacionado = models.ForeignKey("Episodio",on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "CAPÍTULO"
        verbose_name_plural = "CAPÍTULOS"


class Abertura(Base):
    duracao = models.IntegerField("Duração em minutos", default=0)
    letra = models.TextField("Letra da Música",max_length=10000,blank=True, null=True)

    class Meta:
        verbose_name = "ABERTURA"
        verbose_name_plural = "ABERTURAS"


class Episodio(Base):
    opening = models.ForeignKey(Abertura,on_delete=models.CASCADE,null=True,blank=True)
    temporada = models.IntegerField("Temporada / Arco", default=0,null=True,blank=True)
    numero = models.IntegerField("Número do episódio", default=0,null=True,blank=True)
    duracao = models.IntegerField("Duração em minutos", default=0)
    data_lancamento = models.DateField("Data de lançamento",null=True, blank=True)
    capitulo_relacionado = models.ForeignKey("Capitulo",on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        verbose_name = "EPISÓDIO"
        verbose_name_plural = "EPISÓDIOS"


class Habilidade(Base):
    apricao_manga = models.ForeignKey("Capitulo",on_delete=models.CASCADE,related_name="Cap",null=True,blank=True)
    apricao_anime = models.ForeignKey("Episodio",on_delete=models.CASCADE,related_name="Ep",null=True,blank=True)
    tipo = models.CharField("Tipo de Poder",max_length=100,choices=(
        ("0","Haki Do Armamento"),
        ("1","Haki Da Observação"),
        ("2","Haki Do Rei"),
        ("3","Akuma no Mi - Paramecia"),
        ("4","Akuma no Mi - Zoan"),
        ("5","Akuma no Mi - Logia"),
        ("6","Akuma no Mi - Paramecia Mítica"),
        ("7","Akuma no Mi - Zoan Mítica"),
        ("8","Akuma no Mi - Logia Mítica")
    ),null=True, blank=True)

    class Meta:
        verbose_name = "HABILIDADE"
        verbose_name_plural = "HABILIDADES"