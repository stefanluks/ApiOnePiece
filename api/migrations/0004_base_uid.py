# Generated by Django 4.0.4 on 2022-10-03 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_abertura_alter_bando_options_alter_capitulo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='UID',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Codigo'),
        ),
    ]
