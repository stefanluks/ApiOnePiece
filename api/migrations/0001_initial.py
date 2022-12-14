# Generated by Django 4.0.4 on 2022-09-23 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_portugues', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome em português')),
                ('nome_japones', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome em japonês')),
                ('nome_romanizado', models.CharField(max_length=150, verbose_name='Nome em romanizado')),
            ],
        ),
        migrations.CreateModel(
            name='Bando',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.base')),
            ],
            bases=('api.base',),
        ),
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.base')),
            ],
            bases=('api.base',),
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.base')),
            ],
            bases=('api.base',),
        ),
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.base')),
            ],
            bases=('api.base',),
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.base')),
            ],
            bases=('api.base',),
        ),
        migrations.CreateModel(
            name='Navio',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.base')),
            ],
            bases=('api.base',),
        ),
        migrations.CreateModel(
            name='Personagem',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.base')),
                ('alcunha', models.CharField(blank=True, max_length=150, null=True, verbose_name='Alcunha')),
                ('resumo', models.TextField(blank=True, max_length=500, null=True, verbose_name='Resumo curto')),
                ('descricao', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Descrição / História')),
                ('idade', models.IntegerField(default=0, verbose_name='Idade')),
                ('status', models.CharField(blank=True, choices=[('0', 'VIVO'), ('1', 'MORTO')], max_length=6, null=True, verbose_name='Status')),
                ('aniversario', models.DateField(blank=True, null=True, verbose_name='Data de aniversario')),
                ('altura_pre_timeskip', models.FloatField(default=0, verbose_name='Altura pré timeskip')),
                ('altura_pos_timeskip', models.FloatField(default=0, verbose_name='Altura pós timeskip')),
                ('tipo_sanguineo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Tipo sanguinéo')),
                ('risada', models.CharField(blank=True, max_length=150, null=True, verbose_name='Risada Onomatopeia')),
                ('aparencia_crianca', models.CharField(blank=True, max_length=1500, null=True, verbose_name='Aparencia Criança')),
                ('aparencia_pre_timeskip', models.CharField(blank=True, max_length=1500, null=True, verbose_name='Aparencia Pré TimeSkip')),
                ('aparencia_pos_timeskip', models.CharField(blank=True, max_length=1500, null=True, verbose_name='Aparencia Pós TImeSkip')),
                ('afiliacao', models.ManyToManyField(blank=True, to='api.bando')),
                ('apricao_anime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Episodio', to='api.episodio')),
                ('apricao_manga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Capitulo', to='api.capitulo')),
                ('habilidade', models.ManyToManyField(blank=True, to='api.habilidade')),
                ('irmaos', models.ManyToManyField(blank=True, related_name='Irmãos', to='api.personagem')),
                ('mae', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pai', to='api.personagem')),
                ('origem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.lugar')),
                ('pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mãe', to='api.personagem')),
            ],
            bases=('api.base',),
        ),
    ]
