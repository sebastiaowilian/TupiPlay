# Generated by Django 5.0.4 on 2024-05-16 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0007_partidas_resumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verbete',
            name='ds_verbete_idioma_1',
            field=models.CharField(max_length=200, verbose_name='Definição verbete idioma nativo'),
        ),
    ]
