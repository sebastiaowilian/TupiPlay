# Generated by Django 5.0.4 on 2024-05-13 00:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores', '0004_alter_escolaridade_dt_alteracao_and_more'),
        ('jogos', '0002_frase_ds_frase_idioma_2_observacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='id_jogador',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='jogadores.jogador', verbose_name='Jogador(a)'),
        ),
        migrations.AddField(
            model_name='partidas_resumo',
            name='id_jogador',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='jogadores.jogador', verbose_name='Jogador(a)'),
        ),
    ]