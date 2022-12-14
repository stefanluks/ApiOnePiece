# Generated by Django 4.0.4 on 2022-10-02 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_personagem_options_personagem_recompensa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abertura',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.base')),
                ('duracao', models.IntegerField(default=0, verbose_name='Duração em minutos')),
                ('letra', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Letra da Música')),
            ],
            options={
                'verbose_name': 'ABERTURA',
                'verbose_name_plural': 'ABERTURAS',
            },
            bases=('api.base',),
        ),
        migrations.AlterModelOptions(
            name='bando',
            options={'verbose_name': 'BANDO', 'verbose_name_plural': 'BANDOS'},
        ),
        migrations.AlterModelOptions(
            name='capitulo',
            options={'verbose_name': 'CAPÍTULO', 'verbose_name_plural': 'CAPÍTULOS'},
        ),
        migrations.AlterModelOptions(
            name='episodio',
            options={'verbose_name': 'EPISÓDIO', 'verbose_name_plural': 'EPISÓDIOS'},
        ),
        migrations.AlterModelOptions(
            name='habilidade',
            options={'verbose_name': 'HABILIDADE', 'verbose_name_plural': 'HABILIDADES'},
        ),
        migrations.AlterModelOptions(
            name='lugar',
            options={'verbose_name': 'LUGAR', 'verbose_name_plural': 'LUGAR'},
        ),
        migrations.AlterModelOptions(
            name='navio',
            options={'verbose_name': 'NAVIO', 'verbose_name_plural': 'NAVIOS'},
        ),
        migrations.AlterModelOptions(
            name='personagem',
            options={'verbose_name': 'PERSONAGEM', 'verbose_name_plural': 'PERSONAGENS'},
        ),
        migrations.RenameField(
            model_name='personagem',
            old_name='apricao_anime',
            new_name='aparicao_anime',
        ),
        migrations.RenameField(
            model_name='personagem',
            old_name='apricao_manga',
            new_name='aparicao_manga',
        ),
        migrations.RemoveField(
            model_name='personagem',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='personagem',
            name='resumo',
        ),
        migrations.AddField(
            model_name='bando',
            name='apricao_anime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Episodio_Bando', to='api.episodio'),
        ),
        migrations.AddField(
            model_name='bando',
            name='apricao_manga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Capitulo_Bando', to='api.capitulo'),
        ),
        migrations.AddField(
            model_name='bando',
            name='capitao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Capitão', to='api.personagem'),
        ),
        migrations.AddField(
            model_name='bando',
            name='integrantes',
            field=models.ManyToManyField(blank=True, to='api.personagem'),
        ),
        migrations.AddField(
            model_name='bando',
            name='jolly_roger',
            field=models.CharField(blank=True, max_length=2500, null=True, verbose_name='JOlly Roger (bandeira)'),
        ),
        migrations.AddField(
            model_name='bando',
            name='recompensa',
            field=models.IntegerField(default=0, verbose_name='Recompensa do bando'),
        ),
        migrations.AddField(
            model_name='bando',
            name='veiculo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.navio'),
        ),
        migrations.AddField(
            model_name='base',
            name='descricao',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Descrição / História'),
        ),
        migrations.AddField(
            model_name='base',
            name='resumo',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Resumo curto'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='capa',
            field=models.CharField(blank=True, max_length=2500, null=True, verbose_name='Capa do capitulo'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='data_lancamento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de lançamento'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='espisodio_relacionado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.episodio'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='numero',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Número do capitulo'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='qtd_paginas',
            field=models.IntegerField(default=0, verbose_name='Quantidade de paginas'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='volume',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Volume'),
        ),
        migrations.AddField(
            model_name='episodio',
            name='capitulo_relacionado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.capitulo'),
        ),
        migrations.AddField(
            model_name='episodio',
            name='data_lancamento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de lançamento'),
        ),
        migrations.AddField(
            model_name='episodio',
            name='duracao',
            field=models.IntegerField(default=0, verbose_name='Duração em minutos'),
        ),
        migrations.AddField(
            model_name='episodio',
            name='numero',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Número do episódio'),
        ),
        migrations.AddField(
            model_name='episodio',
            name='temporada',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Temporada / Arco'),
        ),
        migrations.AddField(
            model_name='habilidade',
            name='apricao_anime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ep', to='api.episodio'),
        ),
        migrations.AddField(
            model_name='habilidade',
            name='apricao_manga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cap', to='api.capitulo'),
        ),
        migrations.AddField(
            model_name='habilidade',
            name='tipo',
            field=models.CharField(blank=True, choices=[('0', 'Haki Do Armamento'), ('1', 'Haki Da Observação'), ('2', 'Haki Do Rei'), ('3', 'Akuma no Mi - Paramecia'), ('4', 'Akuma no Mi - Zoan'), ('5', 'Akuma no Mi - Logia'), ('6', 'Akuma no Mi - Paramecia Mítica'), ('7', 'Akuma no Mi - Zoan Mítica'), ('8', 'Akuma no Mi - Logia Mítica')], max_length=100, null=True, verbose_name='Tipo de Poder'),
        ),
        migrations.AddField(
            model_name='lugar',
            name='aparicao_anime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Episodio_Lugar', to='api.episodio'),
        ),
        migrations.AddField(
            model_name='lugar',
            name='aparicao_manga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Capitulo_Lugar', to='api.capitulo'),
        ),
        migrations.AddField(
            model_name='navio',
            name='afiliacao',
            field=models.ManyToManyField(blank=True, related_name='Afiliação', to='api.bando'),
        ),
        migrations.AddField(
            model_name='navio',
            name='aparencia',
            field=models.CharField(blank=True, max_length=2500, null=True, verbose_name='Aparencia'),
        ),
        migrations.AddField(
            model_name='navio',
            name='aparicao_anime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Episodio_Navio', to='api.episodio'),
        ),
        migrations.AddField(
            model_name='navio',
            name='aparicao_manga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Capitulo_Navio', to='api.capitulo'),
        ),
        migrations.AddField(
            model_name='navio',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'VIVO'), ('1', 'MORTO')], max_length=6, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='personagem',
            name='dubladores',
            field=models.ManyToManyField(blank=True, related_name='Dubladores', to='api.personagem'),
        ),
        migrations.AddField(
            model_name='episodio',
            name='opening',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.abertura'),
        ),
    ]
